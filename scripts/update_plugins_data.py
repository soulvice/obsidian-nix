#!/usr/bin/env python3
"""
Sync plugins-data.json with the latest releases for all Obsidian community plugins.

Usage:
    python3 scripts/update_plugins_data.py [plugin_id ...]

    With no arguments, processes every plugin in community-plugins.json.
    Pass one or more plugin IDs to only update those (useful for adding a single plugin).

Environment:
    GH_TOKEN  GitHub token for API requests (avoids rate limiting)

Output (plugins-data.json schema):
    {
      "<plugin-id>": {
        "repo":      "owner/repo",
        "version":   "1.2.3",
        "mainJs":    "sha256-...",
        "manifest":  "sha256-...",
        "stylesCss": "sha256-..."   // only present if styles.css exists in the release
      },
      ...
    }
"""

import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DATA_FILE = REPO_ROOT / "plugins-data.json"
COMMUNITY_PLUGINS_URL = (
    "https://raw.githubusercontent.com/obsidianmd/obsidian-releases"
    "/master/community-plugins.json"
)
GH_TOKEN = os.environ.get("GH_TOKEN", "")
# Parallel workers for nix prefetch (GitHub API calls stay sequential)
HASH_WORKERS = 8


# ── HTTP / GitHub API ─────────────────────────────────────────────────────────

def _fetch(url, github_api=False):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "obsidian-nix/update-plugins")
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
                print(f"  [rate limit] {remaining} requests left, sleeping {wait:.0f}s")
                time.sleep(wait)
        return json.loads(r.read())


def get_latest_release(owner_repo):
    url = f"https://api.github.com/repos/{owner_repo}/releases/latest"
    try:
        return _fetch(url, github_api=True)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None  # no releases yet
        raise


# ── Nix hashing ───────────────────────────────────────────────────────────────

def nix_hash(url):
    """Return the SRI sha256 hash of a URL using nix store prefetch-file."""
    result = subprocess.run(
        ["nix", "store", "prefetch-file", "--json", "--hash-type", "sha256", url],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)["hash"]


def hash_release_files(owner_repo, version, asset_names):
    """Download and hash all release files for a plugin. Returns a partial data dict."""
    base = f"https://github.com/{owner_repo}/releases/download/{version}"

    main_js_hash = nix_hash(f"{base}/main.js")
    if not main_js_hash:
        raise RuntimeError("failed to hash main.js")

    manifest_hash = nix_hash(f"{base}/manifest.json")
    if not manifest_hash:
        raise RuntimeError("failed to hash manifest.json")

    data = {
        "repo": owner_repo,
        "version": version,
        "mainJs": main_js_hash,
        "manifest": manifest_hash,
    }

    if "styles.css" in asset_names:
        styles_hash = nix_hash(f"{base}/styles.css")
        if styles_hash:
            data["stylesCss"] = styles_hash

    return data


# ── Per-plugin processing ─────────────────────────────────────────────────────

def process_plugin(plugin_id, owner_repo, cached):
    """
    Return (plugin_id, new_data, error_str).
    new_data is None on error or if nothing changed.
    """
    try:
        release = get_latest_release(owner_repo)
    except Exception as e:
        return plugin_id, None, str(e)

    if not release:
        return plugin_id, None, "no releases found"

    version = release["tag_name"]
    asset_names = {a["name"] for a in release.get("assets", [])}

    # Skip re-hashing if version and all expected files are unchanged
    if cached.get("version") == version:
        has_styles = "styles.css" in asset_names
        cache_complete = (
            cached.get("mainJs")
            and cached.get("manifest")
            and (not has_styles or cached.get("stylesCss"))
        )
        if cache_complete:
            # Ensure repo field is current
            return plugin_id, {**cached, "repo": owner_repo}, None

    try:
        data = hash_release_files(owner_repo, version, asset_names)
    except Exception as e:
        return plugin_id, None, str(e)

    return plugin_id, data, None


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    filter_ids = set(sys.argv[1:])

    # Fetch the full plugin index
    print("Fetching community-plugins.json ...")
    plugins_list = _fetch(COMMUNITY_PLUGINS_URL)
    if filter_ids:
        plugins_list = [p for p in plugins_list if p["id"] in filter_ids]
        missing = filter_ids - {p["id"] for p in plugins_list}
        for m in missing:
            print(f"  WARNING: '{m}' not found in community-plugins.json", file=sys.stderr)

    print(f"Processing {len(plugins_list)} plugins ...\n")

    # Load cached data
    existing: dict = {}
    if DATA_FILE.exists():
        existing = json.loads(DATA_FILE.read_text())

    # Phase 1: fetch latest release metadata sequentially (respects rate limits)
    print("Phase 1: fetching release metadata ...")
    release_info: list[tuple] = []  # (plugin_id, owner_repo, version, asset_names, cached)
    skipped = []

    for i, plugin in enumerate(plugins_list, 1):
        plugin_id = plugin["id"]
        owner_repo = plugin["repo"]
        cached = existing.get(plugin_id, {})
        print(f"  [{i}/{len(plugins_list)}] {plugin_id}", end="", flush=True)

        try:
            release = get_latest_release(owner_repo)
        except Exception as e:
            print(f"  ERROR: {e}")
            skipped.append((plugin_id, str(e)))
            continue

        if not release:
            print("  (no releases)")
            skipped.append((plugin_id, "no releases"))
            continue

        version = release["tag_name"]
        asset_names = {a["name"] for a in release.get("assets", [])}
        has_styles = "styles.css" in asset_names
        cache_hit = (
            cached.get("version") == version
            and cached.get("mainJs")
            and cached.get("manifest")
            and (not has_styles or cached.get("stylesCss"))
        )

        if cache_hit:
            print(f"  cached @ {version}")
            # Ensure repo is up-to-date even on cache hits
            existing[plugin_id] = {**cached, "repo": owner_repo}
        else:
            print(f"  needs update -> {version}")
            release_info.append((plugin_id, owner_repo, version, asset_names))

    # Phase 2: hash files in parallel
    updated_data = dict(existing)
    errors = list(skipped)

    if release_info:
        print(f"\nPhase 2: hashing {len(release_info)} updated plugin(s) ...")

        def _hash_one(args):
            plugin_id, owner_repo, version, asset_names = args
            try:
                data = hash_release_files(owner_repo, version, asset_names)
                return plugin_id, data, None
            except Exception as e:
                return plugin_id, None, str(e)

        with ThreadPoolExecutor(max_workers=HASH_WORKERS) as pool:
            futures = {pool.submit(_hash_one, args): args[0] for args in release_info}
            done = 0
            for future in as_completed(futures):
                done += 1
                plugin_id, data, error = future.result()
                if error:
                    print(f"  [{done}/{len(release_info)}] FAIL  {plugin_id}: {error}")
                    errors.append((plugin_id, error))
                else:
                    print(f"  [{done}/{len(release_info)}] OK    {plugin_id} @ {data['version']}")
                    updated_data[plugin_id] = data

    # Write output
    changed = updated_data != existing
    if changed:
        sorted_data = dict(sorted(updated_data.items()))
        DATA_FILE.write_text(json.dumps(sorted_data, indent=2) + "\n")
        print(f"\nWrote {DATA_FILE}")
    else:
        print("\nAll plugins up-to-date, no changes.")

    if errors:
        print(f"\n{len(errors)} plugin(s) had errors:")
        for plugin_id, msg in errors:
            print(f"  {plugin_id}: {msg}")

    github_output = os.environ.get("GITHUB_OUTPUT", "/dev/null")
    with open(github_output, "a") as f:
        f.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
