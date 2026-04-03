#!/usr/bin/env python3
"""
Generate or update Nix package files for Obsidian community plugins.

Usage:
    python3 scripts/generate_packages.py [plugin_id ...]

    With no arguments, reads plugin IDs from plugins.txt in the repo root.
    Pass one or more plugin IDs to only process those.

Requires: nix (for hashing), network access, optionally GH_TOKEN env var.
"""
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PACKAGES_DIR = REPO_ROOT / "packages"
PLUGINS_FILE = REPO_ROOT / "plugins.txt"
FLAKE_NIX = REPO_ROOT / "flake.nix"
COMMUNITY_PLUGINS_URL = (
    "https://raw.githubusercontent.com/obsidianmd/obsidian-releases"
    "/master/community-plugins.json"
)
GH_TOKEN = os.environ.get("GH_TOKEN", "")


# ── HTTP helpers ──────────────────────────────────────────────────────────────

def _request(url, accept="application/json"):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "obsidian-nix/generate-packages")
    req.add_header("Accept", accept)
    if GH_TOKEN and "api.github.com" in url:
        req.add_header("Authorization", f"Bearer {GH_TOKEN}")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def fetch_latest_release(owner_repo):
    url = f"https://api.github.com/repos/{owner_repo}/releases/latest"
    try:
        return _request(url, accept="application/vnd.github+json")
    except urllib.error.HTTPError as e:
        print(f"  ERROR: GitHub API {e.code} for {owner_repo}", file=sys.stderr)
        return None


# ── Nix hashing ───────────────────────────────────────────────────────────────

def get_sri_hash(url):
    result = subprocess.run(
        ["nix", "store", "prefetch-file", "--json", "--hash-type", "sha256", url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  ERROR hashing {url}:\n    {result.stderr.strip()}", file=sys.stderr)
        return None
    return json.loads(result.stdout)["hash"]


# ── Nix file generation ───────────────────────────────────────────────────────

def _styles_block(styles_hash):
    if not styles_hash:
        return ""
    return f"""
  stylesCss = pkgs.fetchurl {{
    url = "${{repo}}/releases/download/${{version}}/styles.css";
    sha256 = "{styles_hash}";
  }};
"""


def _styles_install(styles_hash):
    return "    cp $stylesCss $out/styles.css\n" if styles_hash else ""


def render_nix(plugin_id, owner_repo, version, main_js_hash, manifest_hash, styles_hash):
    return f"""\
{{
  lib,
  pkgs,
  ...
}}:

pkgs.stdenv.mkDerivation rec {{
  pname = "obsidian.plugins.{plugin_id}";
  version = "{version}";
  repo = "https://github.com/{owner_repo}";

  mainJs = pkgs.fetchurl {{
    url = "${{repo}}/releases/download/${{version}}/main.js";
    sha256 = "{main_js_hash}";
  }};

  manifest = pkgs.fetchurl {{
    url = "${{repo}}/releases/download/${{version}}/manifest.json";
    sha256 = "{manifest_hash}";
  }};
{_styles_block(styles_hash)}  phases = [ "installPhase" ];

  installPhase = ''
    mkdir -p $out
    cp $mainJs $out/main.js
    cp $manifest $out/manifest.json
{_styles_install(styles_hash)}  '';
}}
"""


# ── flake.nix update ──────────────────────────────────────────────────────────

def ensure_in_flake(plugin_id, nix_filename):
    """Add the package to flake.nix if it isn't already referenced."""
    content = FLAKE_NIX.read_text()
    if f"./{nix_filename}" in content:
        return  # already present

    new_line = f"        {plugin_id} = pkgs.callPackage ./{nix_filename} {{ }};\n"
    # Insert before the closing }; of the packages.${system} block
    updated = re.sub(
        r'(packages\.\$\{system\}\s*=\s*\{[^}]*?)(\s*\};)',
        lambda m: m.group(1) + "\n" + new_line + m.group(2),
        content,
        count=1,
        flags=re.DOTALL,
    )
    if updated == content:
        print(f"  WARNING: could not auto-update flake.nix for {plugin_id}", file=sys.stderr)
        return
    FLAKE_NIX.write_text(updated)
    print(f"  added to flake.nix: {plugin_id}")


# ── Per-plugin logic ──────────────────────────────────────────────────────────

def find_existing_nix(owner_repo):
    """Return the first .nix file in packages/ that references this repo, or None."""
    repo_url = f"https://github.com/{owner_repo}"
    for f in PACKAGES_DIR.glob("*.nix"):
        if repo_url in f.read_text():
            return f
    return None


def process_plugin(plugin_id, plugin_info):
    owner_repo = plugin_info["repo"]  # e.g. "Vinzent03/obsidian-git"

    release = fetch_latest_release(owner_repo)
    if not release:
        return False

    version = release["tag_name"]
    asset_names = {a["name"] for a in release.get("assets", [])}
    base_url = f"https://github.com/{owner_repo}/releases/download/{version}"

    print(f"  {owner_repo} @ {version}")

    main_js_hash = get_sri_hash(f"{base_url}/main.js")
    if not main_js_hash:
        return False

    manifest_hash = get_sri_hash(f"{base_url}/manifest.json")
    if not manifest_hash:
        return False

    styles_hash = None
    if "styles.css" in asset_names:
        styles_hash = get_sri_hash(f"{base_url}/styles.css")

    content = render_nix(plugin_id, owner_repo, version, main_js_hash, manifest_hash, styles_hash)

    # Prefer updating an existing file that already tracks this repo
    existing = find_existing_nix(owner_repo)
    out_file = existing if existing else PACKAGES_DIR / f"{plugin_id}.nix"

    if out_file.exists() and out_file.read_text() == content:
        print(f"  up-to-date ({out_file.name})")
        return False

    out_file.write_text(content)
    print(f"  written -> packages/{out_file.name}")

    ensure_in_flake(plugin_id, out_file.name)
    return True


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    # Fetch community plugin index
    print("Fetching community-plugins.json ...")
    plugins_list = _request(COMMUNITY_PLUGINS_URL)
    plugin_lookup = {p["id"]: p for p in plugins_list}
    print(f"Loaded {len(plugin_lookup)} plugins.\n")

    # Determine which plugins to process
    if len(sys.argv) > 1:
        plugin_ids = sys.argv[1:]
    elif PLUGINS_FILE.exists():
        plugin_ids = [
            line.strip()
            for line in PLUGINS_FILE.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]
    else:
        print("No plugins specified. Create plugins.txt or pass IDs as arguments.", file=sys.stderr)
        sys.exit(1)

    changed = False
    for plugin_id in plugin_ids:
        print(f"{plugin_id}:")
        if plugin_id not in plugin_lookup:
            print(f"  ERROR: not found in community-plugins.json", file=sys.stderr)
            continue
        if process_plugin(plugin_id, plugin_lookup[plugin_id]):
            changed = True
        print()

    # Signal to GitHub Actions whether anything changed
    github_output = os.environ.get("GITHUB_OUTPUT", "/dev/null")
    with open(github_output, "a") as f:
        f.write(f"changed={'true' if changed else 'false'}\n")

    print("All done." if not changed else "Packages updated.")


if __name__ == "__main__":
    main()
