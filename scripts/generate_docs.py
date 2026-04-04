#!/usr/bin/env python3
"""
Generate PACKAGES.md from plugins-data.json, themes-data.json, and community-plugin-stats.json.

Usage:
    python3 scripts/generate_docs.py
"""

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT    = Path(__file__).parent.parent
PLUGINS_DATA = REPO_ROOT / "plugins-data.json"
THEMES_DATA  = REPO_ROOT / "themes-data.json"
OUTPUT       = REPO_ROOT / "PACKAGES.md"
STATS_URL = (
    "https://raw.githubusercontent.com/obsidianmd/obsidian-releases"
    "/master/community-plugin-stats.json"
)


def fmt_downloads(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return f"{n:,}"


def fmt_date(ts: int) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%b %d, %Y")


def plugin_row(nix_id: str, entry: dict, stats: dict) -> str:
    name    = entry.get("name") or nix_id
    repo    = entry.get("repo", "")
    desc    = (entry.get("description") or "").replace("|", "\\|").replace("\n", " ").strip()
    url     = f"https://github.com/{repo}" if repo else ""
    name_md = f"[{name}]({url})" if url else name
    s       = stats.get(nix_id, {})
    dl      = fmt_downloads(s["downloads"]) if "downloads" in s else "—"
    updated = fmt_date(s["updated"]) if "updated" in s else "—"
    return f"| {name_md} | `{nix_id}` | {dl} | {updated} | {desc} |"


def theme_row(nix_id: str, entry: dict) -> str:
    name    = entry.get("name") or nix_id
    repo    = entry.get("repo", "")
    desc    = (entry.get("description") or "").replace("|", "\\|").replace("\n", " ").strip()
    url     = f"https://github.com/{repo}" if repo else ""
    name_md = f"[{name}]({url})" if url else name
    return f"| {name_md} | `{nix_id}` | {desc} |"


def main():
    plugins: dict = {}
    themes:  dict = {}
    if PLUGINS_DATA.exists():
        plugins = json.loads(PLUGINS_DATA.read_text())
    if THEMES_DATA.exists():
        themes = json.loads(THEMES_DATA.read_text())

    print("Fetching community-plugin-stats.json ...")
    try:
        with urllib.request.urlopen(STATS_URL, timeout=30) as r:
            stats: dict = json.loads(r.read())
    except Exception as e:
        print(f"  WARNING: could not fetch stats: {e}")
        stats = {}

    today = datetime.now(tz=timezone.utc).strftime("%B %d, %Y")
    total_dl = sum(s.get("downloads", 0) for s in stats.values() if isinstance(s, dict))

    # Top 20 by downloads for the summary table
    top20 = sorted(
        [(k, plugins[k], stats[k]) for k in plugins if k in stats and stats[k].get("downloads")],
        key=lambda x: x[2]["downloads"],
        reverse=True,
    )[:20]

    top20_rows = "\n".join(
        f"| {i+1} | {plugin_row(nix_id, entry, stats)} "
        .replace(f"| {i+1} | | ", f"| {i+1} | ")  # clean up double-pipe if row starts with |
        for i, (nix_id, entry, _) in enumerate(top20)
    )

    # Build top20 table properly
    top20_lines = []
    for i, (nix_id, entry, s) in enumerate(top20):
        name    = entry.get("name") or nix_id
        repo    = entry.get("repo", "")
        desc    = (entry.get("description") or "").replace("|", "\\|").replace("\n", " ").strip()
        url     = f"https://github.com/{repo}" if repo else ""
        name_md = f"[{name}]({url})" if url else name
        dl      = fmt_downloads(s.get("downloads", 0))
        updated = fmt_date(s["updated"]) if "updated" in s else "—"
        top20_lines.append(f"| {i+1} | {name_md} | `{nix_id}` | {dl} | {updated} | {desc} |")

    # Full plugin table
    sorted_plugins = sorted(plugins.items(), key=lambda kv: (kv[1].get("name") or kv[0]).lower())
    plugin_rows = "\n".join(plugin_row(nix_id, e, stats) for nix_id, e in sorted_plugins)

    # Full theme table
    sorted_themes = sorted(themes.items(), key=lambda kv: (kv[1].get("name") or kv[0]).lower())
    theme_rows = "\n".join(theme_row(nix_id, e) for nix_id, e in sorted_themes)

    content = f"""\
# Obsidian Nix Packages

Nix derivations for every [Obsidian](https://obsidian.md) community plugin and theme,
sourced from [obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases).

_Last updated: {today} — {len(plugins):,} plugins · {len(themes):,} themes · {fmt_downloads(total_dl)} total downloads_

> **Full stats and sorted views** are available in the [Wiki](../../wiki).

## Usage

**With the overlay** (recommended — no `${{system}}` required):

```nix
# flake.nix
inputs.obsidian-nix.url = "github:soulvice/obsidian-nix";
nixpkgs.overlays = [ inputs.obsidian-nix.overlays.default ];
```

```nix
# anywhere pkgs is in scope
programs.obsidian.myVault.communityPlugins = with pkgs.obsidianPlugins; [
  dataview
  templater-obsidian
];
programs.obsidian.myVault.communityThemes = with pkgs.obsidianThemes; [
  catppuccin
];
```

**Direct package reference** (when you need an explicit system):

```nix
inputs.obsidian-nix.packages.${{system}}.plugin.dataview
inputs.obsidian-nix.packages.${{system}}.theme.catppuccin
```

---

## Top 20 Most Popular Plugins

| # | Name | Package ID | Downloads | Last Updated | Description |
|---|------|-----------|-----------|--------------|-------------|
{chr(10).join(top20_lines)}

---

## All Plugins ({len(plugins):,})

| Name | Package ID | Downloads | Last Updated | Description |
|------|-----------|-----------|--------------|-------------|
{plugin_rows}

---

## All Themes ({len(themes):,})

| Name | Package ID | Description |
|------|-----------|-------------|
{theme_rows}
"""

    OUTPUT.write_text(content)
    print(f"Wrote {OUTPUT}  ({len(plugins)} plugins, {len(themes)} themes)")


if __name__ == "__main__":
    main()
