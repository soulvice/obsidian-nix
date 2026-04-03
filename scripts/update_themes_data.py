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
        "repo":  "owner/repo",
        "rev":   "<tag or commit SHA>",
        "hash":  "sha256-..."    // hash of the unpacked repo archive
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
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DATA_FILE = REPO_ROOT / "themes-data.json"
COMMUNITY_THEMES_URL = (
    "https://raw.githubusercontent.com/obsidianmd/obsidian-releases"
    "/master/community-css-themes.json"
)
GH_TOKEN = os.environ.get("GH_TOKEN", "")
HASH_WORKERS = 8


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


def get_latest_rev(owner: str, repo: str) -> str | None:
    """
    Return the best available rev for a theme repo, in preference order:
      1. Latest release tag
      2. Latest git tag
      3. Latest commit SHA on the default branch
    """
    base = f"https://api.github.com/repos/{owner}/{repo}"

    # 1. Latest release
    try:
        release = _fetch(f"{base}/releases/latest", github_api=True)
        return release["tag_name"]
    except urllib.error.HTTPError as e:
        if e.code not in (404, 403):
            raise

    # 2. Latest tag
    try:
        tags = _fetch(f"{base}/tags?per_page=1", github_api=True)
        if tags:
            return tags[0]["name"]
    except urllib.error.HTTPError:
        pass

    # 3. Latest commit on default branch
    try:
        branch_info = _fetch(f"{base}", github_api=True)
        default_branch = branch_info.get("default_branch", "main")
        commit_info = _fetch(f"{base}/commits/{default_branch}?per_page=1", github_api=True)
        return commit_info["sha"]
    except urllib.error.HTTPError:
        return None


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

def process_theme(tid: str, owner_repo: str, cached: dict):
    """Return (tid, new_data, error_str). new_data is None if unchanged or on error."""
    owner, repo = owner_repo.split("/", 1)

    try:
        rev = get_latest_rev(owner, repo)
    except Exception as e:
        return tid, None, f"rev lookup failed: {e}"

    if not rev:
        return tid, None, "could not determine latest rev"

    # Cache hit: same rev and hash already present
    if cached.get("rev") == rev and cached.get("hash"):
        return tid, {**cached, "repo": owner_repo, "rev": rev}, None

    hash_val = nix_hash_archive(owner, repo, rev)
    if not hash_val:
        return tid, None, f"failed to hash archive @ {rev}"

    return tid, {"repo": owner_repo, "rev": rev, "hash": hash_val}, None


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    filter_ids = set(sys.argv[1:])

    print("Fetching community-css-themes.json ...")
    themes_list = _fetch(COMMUNITY_THEMES_URL)

    # Build id → entry mapping
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

    updated_data = dict(existing)

    # Phase 1: get latest rev for each theme (sequential, respects rate limits)
    print("Phase 1: fetching latest revs ...")
    needs_hash: list[tuple] = []  # (tid, owner_repo, rev, cached)

    for i, (tid, theme) in enumerate(themes.items(), 1):
        owner_repo = theme["repo"]
        cached = existing.get(tid, {})
        owner, repo = owner_repo.split("/", 1)
        print(f"  [{i}/{len(themes)}] {tid}", end="", flush=True)

        try:
            rev = get_latest_rev(owner, repo)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

        if not rev:
            print("  (no rev found)")
            continue

        if cached.get("rev") == rev and cached.get("hash"):
            print(f"  cached @ {rev}")
            updated_data[tid] = {**cached, "repo": owner_repo}
        else:
            print(f"  needs update -> {rev}")
            needs_hash.append((tid, owner_repo, rev))

    # Phase 2: hash archives in parallel
    errors = []
    if needs_hash:
        print(f"\nPhase 2: hashing {len(needs_hash)} archive(s) ...")

        def _hash_one(args):
            tid, owner_repo, rev = args
            owner, repo = owner_repo.split("/", 1)
            hash_val = nix_hash_archive(owner, repo, rev)
            if not hash_val:
                return tid, None, f"hash failed"
            return tid, {"repo": owner_repo, "rev": rev, "hash": hash_val}, None

        with ThreadPoolExecutor(max_workers=HASH_WORKERS) as pool:
            futures = {pool.submit(_hash_one, args): args[0] for args in needs_hash}
            done = 0
            for future in as_completed(futures):
                done += 1
                tid, data, error = future.result()
                if error:
                    print(f"  [{done}/{len(needs_hash)}] FAIL  {tid}: {error}")
                    errors.append((tid, error))
                else:
                    print(f"  [{done}/{len(needs_hash)}] OK    {tid} @ {data['rev']}")
                    updated_data[tid] = data

    changed = updated_data != existing
    if changed:
        sorted_data = dict(sorted(updated_data.items()))
        DATA_FILE.write_text(json.dumps(sorted_data, indent=2) + "\n")
        print(f"\nWrote {DATA_FILE}")
    else:
        print("\nAll themes up-to-date, no changes.")

    if errors:
        print(f"\n{len(errors)} theme(s) had errors:")
        for tid, msg in errors:
            print(f"  {tid}: {msg}")

    github_output = os.environ.get("GITHUB_OUTPUT", "/dev/null")
    with open(github_output, "a") as f:
        f.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
