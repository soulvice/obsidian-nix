#!/usr/bin/env python3
"""
Sync plugins-data.json with the latest releases for all Obsidian community plugins.

Usage:
    python3 scripts/update_plugins_data.py [plugin_id ...]

    With no arguments, processes every plugin in community-plugins.json.
    Pass one or more plugin IDs to only update those.

Environment:
    GH_TOKEN  GitHub token for API requests (avoids rate limiting)

Output (plugins-data.json schema):
    {
      "<plugin-id>": {
        "repo":        "owner/repo",
        "name":        "Display Name",
        "description": "What the plugin does.",
        "version":     "1.2.3",
        "mainJs":      "sha256-...",
        "manifest":    "sha256-...",
        "stylesCss":   "sha256-..."   // only present if styles.css exists in the release
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
from datetime import datetime, timezone
from pathlib import Path
from threading import Event, Lock, Thread

REPO_ROOT    = Path(__file__).parent.parent
DATA_FILE    = REPO_ROOT / "plugins-data.json"
BROKEN_FILE  = REPO_ROOT / "broken-plugins.json"
COMMUNITY_PLUGINS_URL = (
    "https://raw.githubusercontent.com/obsidianmd/obsidian-releases"
    "/master/community-plugins.json"
)
GH_TOKEN = os.environ.get("GH_TOKEN", "")
API_WORKERS  = 8
HASH_WORKERS = 16

# Max GitHub API requests per second (5000/hr = 1.4/s; stay well under secondary limits)
_API_INTERVAL = 0.25   # 4 req/s
_api_lock     = Lock()
_api_last     = [0.0]


# ── HTTP / GitHub API ─────────────────────────────────────────────────────────

def _fetch(url: str, github_api: bool = False) -> object:
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "obsidian-nix/update-plugins")
    if github_api:
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        if GH_TOKEN:
            req.add_header("Authorization", f"Bearer {GH_TOKEN}")
        # Global rate limiter — prevents concurrent burst triggering secondary limits
        with _api_lock:
            wait = _API_INTERVAL - (time.time() - _api_last[0])
            if wait > 0:
                time.sleep(wait)
            _api_last[0] = time.time()

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                if github_api:
                    remaining = int(r.headers.get("X-RateLimit-Remaining", 9999))
                    if remaining < 20:
                        reset_at = int(r.headers.get("X-RateLimit-Reset", time.time() + 60))
                        wait = max(1, reset_at - time.time()) + 5
                        print(f"  [rate limit] {remaining} requests left, sleeping {wait:.0f}s", flush=True)
                        time.sleep(wait)
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 403 and github_api:
                retry_after = int(e.headers.get("Retry-After", 60))
                print(f"  [secondary rate limit] sleeping {retry_after}s (attempt {attempt + 1}/3)", flush=True)
                time.sleep(retry_after)
                continue
            raise
    raise RuntimeError(f"Failed after 3 retries: {url}")


def fetch_manifest_content(url: str) -> dict:
    """Download and parse a manifest.json. Returns {} on any error."""
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "obsidian-nix/update-plugins")
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except Exception:
        return {}


def get_latest_release(owner_repo: str) -> dict | None:
    url = f"https://api.github.com/repos/{owner_repo}/releases/latest"
    try:
        return _fetch(url, github_api=True)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


# ── Nix hashing ───────────────────────────────────────────────────────────────

def nix_hash(url: str) -> str | None:
    result = subprocess.run(
        ["nix", "store", "prefetch-file", "--json", "--hash-type", "sha256", url],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)["hash"]


# ── Per-plugin processing ─────────────────────────────────────────────────────

def hash_release_files(owner_repo: str, version: str, asset_names: set) -> dict:
    """Fetch hashes and manifest metadata for a release. Raises on hash failure."""
    base = f"https://github.com/{owner_repo}/releases/download/{version}"

    # Fetch manifest content for name/description (cheap urllib call)
    manifest_content = fetch_manifest_content(f"{base}/manifest.json")

    main_js_hash = nix_hash(f"{base}/main.js")
    if not main_js_hash:
        raise RuntimeError("failed to hash main.js")

    manifest_hash = nix_hash(f"{base}/manifest.json")
    if not manifest_hash:
        raise RuntimeError("failed to hash manifest.json")

    data = {
        "repo":        owner_repo,
        "name":        manifest_content.get("name", ""),
        "description": manifest_content.get("description", ""),
        "version":     version,
        "mainJs":      main_js_hash,
        "manifest":    manifest_hash,
    }

    if "styles.css" in asset_names:
        styles_hash = nix_hash(f"{base}/styles.css")
        if styles_hash:
            data["stylesCss"] = styles_hash

    return data


def fetch_metadata_only(owner_repo: str, version: str) -> dict:
    """Download manifest.json content only — no nix hashing. Used to backfill metadata."""
    base = f"https://github.com/{owner_repo}/releases/download/{version}"
    manifest_content = fetch_manifest_content(f"{base}/manifest.json")
    return {
        "name":        manifest_content.get("name", ""),
        "description": manifest_content.get("description", ""),
    }


def process_plugin(plugin_id: str, owner_repo: str, cached: dict):
    """Return (plugin_id, new_data_or_None, error_str_or_None)."""
    try:
        release = get_latest_release(owner_repo)
    except Exception as e:
        return plugin_id, None, str(e)

    if not release:
        return plugin_id, None, "no releases found"

    version = release["tag_name"]
    asset_names = {a["name"] for a in release.get("assets", [])}
    has_styles = "styles.css" in asset_names

    hashes_current = (
        cached.get("version") == version
        and cached.get("mainJs")
        and cached.get("manifest")
        and (not has_styles or cached.get("stylesCss"))
    )
    metadata_current = "name" in cached

    if hashes_current and metadata_current:
        # Fully cached — just keep it with updated repo field
        return plugin_id, {**cached, "repo": owner_repo}, None

    if hashes_current and not metadata_current:
        # Hashes are fine but we're missing name/description (old schema)
        meta = fetch_metadata_only(owner_repo, version)
        return plugin_id, {**cached, "repo": owner_repo, **meta}, None

    # Version changed or hashes missing — full update
    try:
        data = hash_release_files(owner_repo, version, asset_names)
    except Exception as e:
        return plugin_id, None, str(e)

    return plugin_id, data, None


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    filter_ids = set(sys.argv[1:])

    print("Fetching community-plugins.json ...")
    plugins_list = _fetch(COMMUNITY_PLUGINS_URL)
    if filter_ids:
        plugins_list = [p for p in plugins_list if p["id"] in filter_ids]
        missing = filter_ids - {p["id"] for p in plugins_list}
        for m in missing:
            print(f"  WARNING: '{m}' not found in community-plugins.json", file=sys.stderr)

    print(f"Processing {len(plugins_list)} plugins ...\n")

    existing: dict = {}
    if DATA_FILE.exists():
        existing = json.loads(DATA_FILE.read_text())

    broken: dict = {}
    if BROKEN_FILE.exists():
        broken = json.loads(BROKEN_FILE.read_text())

    state_lock   = Lock()
    needs_hash:   list[tuple] = []
    updated_data: dict        = dict(existing)

    def mark_broken(plugin_id: str, owner_repo: str, error: str):
        broken[plugin_id] = {
            "repo":  owner_repo,
            "error": error,
            "since": broken.get(plugin_id, {}).get("since") or datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    def fetch_one(plugin):
        plugin_id  = plugin["id"]
        owner_repo = plugin["repo"]
        cached     = existing.get(plugin_id, {})

        try:
            release = get_latest_release(owner_repo)
        except Exception as e:
            with state_lock:
                mark_broken(plugin_id, owner_repo, str(e))
            return f"  {plugin_id}  ERROR: {e}"

        if not release:
            with state_lock:
                mark_broken(plugin_id, owner_repo, "no GitHub releases found")
            return f"  {plugin_id}  (no releases)"

        version     = release["tag_name"]
        asset_names = {a["name"] for a in release.get("assets", [])}
        has_styles  = "styles.css" in asset_names

        hashes_current = (
            cached.get("version") == version
            and cached.get("mainJs")
            and cached.get("manifest")
            and (not has_styles or cached.get("stylesCss"))
        )
        metadata_current = "name" in cached

        if hashes_current and not metadata_current:
            meta = fetch_metadata_only(owner_repo, version)
            with state_lock:
                broken.pop(plugin_id, None)
                updated_data[plugin_id] = {**cached, "repo": owner_repo, **meta}
            return f"  {plugin_id}  backfilled metadata @ {version}"

        with state_lock:
            broken.pop(plugin_id, None)
            if hashes_current:
                updated_data[plugin_id] = {**cached, "repo": owner_repo}
                return f"  {plugin_id}  cached @ {version}"
            else:
                needs_hash.append((plugin_id, owner_repo, version, asset_names))
                return f"  {plugin_id}  needs update -> {version}"

    # Phase 1: fetch release metadata in parallel
    total   = len(plugins_list)
    done_count = [0]
    stop_hb = Event()

    def heartbeat():
        while not stop_hb.wait(30):
            print(f"  [progress] {done_count[0]}/{total} checked ...", flush=True)

    print(f"Phase 1: fetching release metadata ({API_WORKERS} workers, {total} plugins) ...")
    hb = Thread(target=heartbeat, daemon=True)
    hb.start()

    with ThreadPoolExecutor(max_workers=API_WORKERS) as pool:
        futures = {pool.submit(fetch_one, p): p["id"] for p in plugins_list}
        for future in as_completed(futures):
            done_count[0] += 1
            print(f"  [{done_count[0]}/{total}]{future.result()}", flush=True)

    stop_hb.set()

    # Phase 2: hash files in parallel
    if needs_hash:
        print(f"\nPhase 2: hashing {len(needs_hash)} plugin(s) ...")

        def _hash_one(args):
            plugin_id, owner_repo, version, asset_names = args
            try:
                data = hash_release_files(owner_repo, version, asset_names)
                return plugin_id, owner_repo, data, None
            except Exception as e:
                return plugin_id, owner_repo, None, str(e)

        with ThreadPoolExecutor(max_workers=HASH_WORKERS) as pool:
            futures = {pool.submit(_hash_one, args): args[0] for args in needs_hash}
            done = 0
            for future in as_completed(futures):
                done += 1
                plugin_id, owner_repo, data, error = future.result()
                if error:
                    print(f"  [{done}/{len(needs_hash)}] FAIL  {plugin_id}: {error}")
                    mark_broken(plugin_id, owner_repo, error)
                else:
                    print(f"  [{done}/{len(needs_hash)}] OK    {plugin_id} @ {data['version']}")
                    updated_data[plugin_id] = data
                    broken.pop(plugin_id, None)

    changed = updated_data != existing
    if changed:
        DATA_FILE.write_text(json.dumps(dict(sorted(updated_data.items())), indent=2) + "\n")
        print(f"\nWrote {DATA_FILE}")
    else:
        print("\nAll plugins up-to-date, no changes.")

    BROKEN_FILE.write_text(json.dumps(dict(sorted(broken.items())), indent=2) + "\n")
    if broken:
        print(f"\n{len(broken)} broken plugin(s) recorded in {BROKEN_FILE.name}")

    github_output = os.environ.get("GITHUB_OUTPUT", "/dev/null")
    with open(github_output, "a") as f:
        f.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
