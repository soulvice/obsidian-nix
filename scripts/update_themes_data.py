#!/usr/bin/env python3
"""
Sync themes-data.json with the latest commits/releases for all Obsidian community themes.

Usage:
    python3 scripts/update_themes_data.py [theme_id ...]

    With no arguments, processes every theme in community-css-themes.json.
    Pass one or more theme IDs to only update those.

Theme IDs are derived from the theme name: lowercase, spaces/special-chars → hyphens.
e.g. "Catppuccin" → "catppuccin", "An Old Hope" → "an-old-hope"

Environment:
    GH_TOKEN  GitHub token for API requests (avoids rate limiting)

Output (themes-data.json schema):
    {
      "<theme-id>": {
        "repo":        "owner/repo",
        "name":        "Display Name",
        "description": "What the theme looks like.",
        "rev":         "<tag or commit SHA>",
        "hash":        "sha256-..."
      },
      ...
    }
"""

import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock

REPO_ROOT   = Path(__file__).parent.parent
DATA_FILE   = REPO_ROOT / "themes-data.json"
BROKEN_FILE = REPO_ROOT / "broken-themes.json"
COMMUNITY_THEMES_URL = (
    "https://raw.githubusercontent.com/obsidianmd/obsidian-releases"
    "/master/community-css-themes.json"
)
GH_TOKEN = os.environ.get("GH_TOKEN", "")
API_WORKERS  = 8
HASH_WORKERS = 16


# ── Helpers ───────────────────────────────────────────────────────────────────

def theme_id(name: str) -> str:
    """Derive a stable Nix-safe ID from a theme's display name."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _fetch(url: str, github_api: bool = False) -> object:
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "obsidian-nix/update-themes")
    if github_api:
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        if GH_TOKEN:
            req.add_header("Authorization", f"Bearer {GH_TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        if github_api:
            remaining = int(r.headers.get("X-RateLimit-Remaining", 9999))
            if remaining < 20:
                reset_at = int(r.headers.get("X-RateLimit-Reset", time.time() + 60))
                wait = max(1, reset_at - time.time()) + 5
                print(f"  [rate limit] {remaining} left, sleeping {wait:.0f}s")
                time.sleep(wait)
        return json.loads(r.read())


def fetch_manifest_content(owner: str, repo: str, rev: str) -> dict:
    """Download and parse manifest.json from the raw repo at a specific rev."""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{rev}/manifest.json"
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "obsidian-nix/update-themes")
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except Exception:
        return {}


def get_latest_rev(owner: str, repo: str) -> str | None:
    """
    Return the best available rev in preference order:
      1. Latest release tag
      2. Latest git tag
      3. Latest commit SHA on the default branch
    """
    base = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        release = _fetch(f"{base}/releases/latest", github_api=True)
        return release["tag_name"]
    except urllib.error.HTTPError as e:
        if e.code not in (404, 403):
            raise

    try:
        tags = _fetch(f"{base}/tags?per_page=1", github_api=True)
        if tags:
            return tags[0]["name"]
    except urllib.error.HTTPError:
        pass

    try:
        repo_info = _fetch(base, github_api=True)
        default_branch = repo_info.get("default_branch", "main")
        commit = _fetch(f"{base}/commits/{default_branch}?per_page=1", github_api=True)
        return commit["sha"]
    except urllib.error.HTTPError:
        return None


# ── Nix hashing ───────────────────────────────────────────────────────────────

def nix_hash_archive(owner: str, repo: str, rev: str) -> str | None:
    """Hash the unpacked GitHub archive — matches what fetchFromGitHub produces."""
    url = f"https://github.com/{owner}/{repo}/archive/{rev}.tar.gz"
    result = subprocess.run(
        [
            "nix", "store", "prefetch-file",
            "--json", "--hash-type", "sha256", "--unpack",
            url,
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)["hash"]


# ── Per-theme processing ──────────────────────────────────────────────────────

def full_update(owner: str, repo: str, owner_repo: str, rev: str) -> dict:
    """Hash the archive and fetch manifest metadata. Raises on hash failure."""
    hash_val = nix_hash_archive(owner, repo, rev)
    if not hash_val:
        raise RuntimeError(f"failed to hash archive @ {rev}")

    manifest = fetch_manifest_content(owner, repo, rev)

    return {
        "repo":        owner_repo,
        "name":        manifest.get("name", ""),
        "description": manifest.get("description", ""),
        "rev":         rev,
        "hash":        hash_val,
    }


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    filter_ids = set(sys.argv[1:])

    print("Fetching community-css-themes.json ...")
    themes_list = _fetch(COMMUNITY_THEMES_URL)
    themes = {theme_id(t["name"]): t for t in themes_list}

    if filter_ids:
        unknown = filter_ids - set(themes)
        for u in unknown:
            print(f"  WARNING: '{u}' not found in community-css-themes.json", file=sys.stderr)
        themes = {k: v for k, v in themes.items() if k in filter_ids}

    print(f"Processing {len(themes)} themes ...\n")

    existing: dict = {}
    if DATA_FILE.exists():
        existing = json.loads(DATA_FILE.read_text())

    broken: dict = {}
    if BROKEN_FILE.exists():
        broken = json.loads(BROKEN_FILE.read_text())

    state_lock   = Lock()
    needs_hash:   list[tuple] = []
    updated_data: dict        = dict(existing)

    def mark_broken(tid: str, owner_repo: str, error: str):
        broken[tid] = {
            "repo":  owner_repo,
            "error": error,
            "since": broken.get(tid, {}).get("since") or datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    def fetch_one(args):
        tid, theme = args
        owner_repo = theme["repo"]
        owner, repo = owner_repo.split("/", 1)
        cached = existing.get(tid, {})

        try:
            rev = get_latest_rev(owner, repo)
        except Exception as e:
            with state_lock:
                mark_broken(tid, owner_repo, str(e))
            return f"  {tid}  ERROR: {e}"

        if not rev:
            with state_lock:
                mark_broken(tid, owner_repo, "could not determine latest rev (no releases, tags, or commits)")
            return f"  {tid}  (no rev found)"

        hash_current     = cached.get("rev") == rev and cached.get("hash")
        metadata_current = "name" in cached

        if hash_current and not metadata_current:
            manifest = fetch_manifest_content(owner, repo, rev)
            with state_lock:
                broken.pop(tid, None)
                updated_data[tid] = {
                    **cached,
                    "repo":        owner_repo,
                    "name":        manifest.get("name", ""),
                    "description": manifest.get("description", ""),
                }
            return f"  {tid}  backfilled metadata @ {rev}"

        with state_lock:
            broken.pop(tid, None)
            if hash_current:
                updated_data[tid] = {**cached, "repo": owner_repo}
                return f"  {tid}  cached @ {rev}"
            else:
                needs_hash.append((tid, owner_repo, owner, repo, rev))
                return f"  {tid}  needs update -> {rev}"

    # Phase 1: fetch latest revs in parallel
    print(f"Phase 1: fetching latest revs ({API_WORKERS} workers) ...")
    with ThreadPoolExecutor(max_workers=API_WORKERS) as pool:
        futures = {pool.submit(fetch_one, item): item[0] for item in themes.items()}
        done = 0
        for future in as_completed(futures):
            done += 1
            print(f"[{done}/{len(themes)}]{future.result()}", flush=True)

    # Phase 2: hash archives in parallel
    if needs_hash:
        print(f"\nPhase 2: hashing {len(needs_hash)} archive(s) ...")

        def _hash_one(args):
            tid, owner_repo, owner, repo, rev = args
            try:
                data = full_update(owner, repo, owner_repo, rev)
                return tid, owner_repo, data, None
            except Exception as e:
                return tid, owner_repo, None, str(e)

        with ThreadPoolExecutor(max_workers=HASH_WORKERS) as pool:
            futures = {pool.submit(_hash_one, args): args[0] for args in needs_hash}
            done = 0
            for future in as_completed(futures):
                done += 1
                tid, owner_repo, data, error = future.result()
                if error:
                    print(f"  [{done}/{len(needs_hash)}] FAIL  {tid}: {error}")
                    mark_broken(tid, owner_repo, error)
                else:
                    print(f"  [{done}/{len(needs_hash)}] OK    {tid} @ {data['rev']}")
                    updated_data[tid] = data
                    broken.pop(tid, None)

    changed = updated_data != existing
    if changed:
        DATA_FILE.write_text(json.dumps(dict(sorted(updated_data.items())), indent=2) + "\n")
        print(f"\nWrote {DATA_FILE}")
    else:
        print("\nAll themes up-to-date, no changes.")

    BROKEN_FILE.write_text(json.dumps(dict(sorted(broken.items())), indent=2) + "\n")
    if broken:
        print(f"\n{len(broken)} broken theme(s) recorded in {BROKEN_FILE.name}")

    github_output = os.environ.get("GITHUB_OUTPUT", "/dev/null")
    with open(github_output, "a") as f:
        f.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
