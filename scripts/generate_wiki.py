#!/usr/bin/env python3
"""
Generate GitHub Wiki pages for obsidian-nix.

Reads plugins-data.json and themes-data.json from the repo root, fetches
community-plugin-stats.json live, and writes markdown files to an output directory.

Usage:
    python3 scripts/generate_wiki.py [output_dir]

    output_dir defaults to wiki/ relative to the repo root.
    The output directory should be a clone of the GitHub wiki repo.

Pages generated:
    Home.md                    — stats summary + navigation
    All-Packages.md            — all plugins alphabetically with stats
    All-Themes.md              — all themes alphabetically
    Packages-by-Popularity.md  — plugins ranked by total downloads
    Packages-by-Last-Updated.md — plugins sorted by most recently updated
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT   = Path(__file__).parent.parent
PLUGINS_DATA = REPO_ROOT / "plugins-data.json"
THEMES_DATA  = REPO_ROOT / "themes-data.json"
STATS_URL = (
    "https://raw.githubusercontent.com/obsidianmd/obsidian-releases"
    "/master/community-plugin-stats.json"
)


# ── Formatting helpers ────────────────────────────────────────────────────────

def fmt_int(n: int) -> str:
    return f"{n:,}"


def fmt_downloads(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return fmt_int(n)


def fmt_date(ts: int) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%b %d, %Y")


# ── Row builders ──────────────────────────────────────────────────────────────

def _name_cell(entry: dict, nix_id: str) -> str:
    name = entry.get("name") or nix_id
    repo = entry.get("repo", "")
    url  = f"https://github.com/{repo}" if repo else ""
    return f"[{name}]({url})" if url else name


def _desc(entry: dict) -> str:
    return (entry.get("description") or "").replace("|", "\\|").replace("\n", " ").strip()


def plugin_row(nix_id: str, entry: dict, stats: dict) -> str:
    s        = stats.get(nix_id, {})
    dl       = fmt_downloads(s["downloads"]) if "downloads" in s else "—"
    updated  = fmt_date(s["updated"]) if "updated" in s else "—"
    return f"| {_name_cell(entry, nix_id)} | `{nix_id}` | {dl} | {updated} | {_desc(entry)} |"


def ranked_plugin_row(rank: int, nix_id: str, entry: dict, stats: dict) -> str:
    s   = stats.get(nix_id, {})
    dl  = fmt_downloads(s.get("downloads", 0))
    upd = fmt_date(s["updated"]) if "updated" in s else "—"
    return f"| {rank} | {_name_cell(entry, nix_id)} | `{nix_id}` | {dl} | {upd} | {_desc(entry)} |"


def theme_row(nix_id: str, entry: dict) -> str:
    return f"| {_name_cell(entry, nix_id)} | `{nix_id}` | {_desc(entry)} |"


# ── Table builders ────────────────────────────────────────────────────────────

PLUGIN_HEADER = (
    "| Name | Package ID | Downloads | Last Updated | Description |\n"
    "|------|-----------|-----------|--------------|-------------|"
)

RANKED_HEADER = (
    "| Rank | Name | Package ID | Downloads | Last Updated | Description |\n"
    "|------|------|-----------|-----------|--------------|-------------|"
)

THEME_HEADER = (
    "| Name | Package ID | Description |\n"
    "|------|-----------|-------------|"
)


def plugin_table(rows: list[str]) -> str:
    return PLUGIN_HEADER + "\n" + "\n".join(rows)


def ranked_table(rows: list[str]) -> str:
    return RANKED_HEADER + "\n" + "\n".join(rows)


def theme_table(rows: list[str]) -> str:
    return THEME_HEADER + "\n" + "\n".join(rows)


# ── Page generators ───────────────────────────────────────────────────────────

def gen_home(plugins: dict, themes: dict, stats: dict) -> str:
    today = datetime.now(tz=timezone.utc).strftime("%B %d, %Y")

    total_dl = sum(
        s.get("downloads", 0) for s in stats.values() if isinstance(s, dict)
    )

    plugins_with_stats = {k: stats[k] for k in plugins if k in stats and stats[k].get("downloads")}
    if plugins_with_stats:
        top_id = max(plugins_with_stats, key=lambda k: plugins_with_stats[k]["downloads"])
        top_name = plugins[top_id].get("name") or top_id
        top_dl = fmt_downloads(plugins_with_stats[top_id]["downloads"])
        top_cell = f"[{top_name}](https://github.com/{plugins[top_id].get('repo', '')}) — {top_dl}"

        recent_id = max(plugins_with_stats, key=lambda k: plugins_with_stats[k].get("updated", 0))
        recent_name = plugins[recent_id].get("name") or recent_id
        recent_date = fmt_date(plugins_with_stats[recent_id]["updated"])
        recent_cell = f"[{recent_name}](https://github.com/{plugins[recent_id].get('repo', '')}) — {recent_date}"
    else:
        top_cell = "—"
        recent_cell = "—"

    # Top 5 snapshot for the home page
    top5 = sorted(
        [(k, plugins[k], stats[k]) for k in plugins if k in stats and stats[k].get("downloads")],
        key=lambda x: x[2]["downloads"],
        reverse=True,
    )[:5]
    top5_rows = "\n".join(ranked_plugin_row(i + 1, nix_id, entry, stats) for i, (nix_id, entry, _) in enumerate(top5))

    return f"""\
# Obsidian Nix Packages

Nix derivations for every [Obsidian](https://obsidian.md) community plugin and theme,
automatically kept up-to-date from
[obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases).

_Last updated: {today}_

---

## Quick Start

```nix
# flake.nix
inputs.obsidian-nix.url = "github:soulvice/obsidian-nix";
nixpkgs.overlays = [ inputs.obsidian-nix.overlays.default ];
```

```nix
# anywhere pkgs is in scope — no ${{system}} needed
programs.obsidian.myVault.communityPlugins = with pkgs.obsidianPlugins; [
  dataview
  templater-obsidian
];
programs.obsidian.myVault.communityThemes = with pkgs.obsidianThemes; [
  catppuccin
];
```

Or via direct package reference:

```nix
inputs.obsidian-nix.packages.${{system}}.plugin.dataview
inputs.obsidian-nix.packages.${{system}}.theme.catppuccin
```

**Custom plugins/themes** (private repos, forks, unreleased):

```nix
nixpkgs.overlays = [
  inputs.obsidian-nix.overlays.default
  (final: prev: {{
    obsidianPlugins = prev.obsidianPlugins // {{
      my-plugin = inputs.obsidian-nix.lib.mkPlugin final {{
        id       = "my-plugin";
        repo     = "myorg/obsidian-my-plugin";
        version  = "1.0.0";
        mainJs   = "sha256-...";
        manifest = "sha256-...";
      }};
    }};
  }})
];
```

---

## Stats

| | |
|--|--|
| **Plugins packaged** | {fmt_int(len(plugins))} |
| **Themes packaged** | {fmt_int(len(themes))} |
| **Total plugin downloads** | {fmt_downloads(total_dl)} |
| **Most popular plugin** | {top_cell} |
| **Most recently updated** | {recent_cell} |

---

## Top 5 Most Popular Plugins

{ranked_table(top5_rows)}

---

## Pages

| Page | Description |
|------|-------------|
| [[All-Packages]] | All {fmt_int(len(plugins))} plugins — alphabetical, with download stats |
| [[All-Themes]] | All {fmt_int(len(themes))} themes — alphabetical |
| [[Packages-by-Popularity]] | Plugins ranked by total downloads |
| [[Packages-by-Last-Updated]] | Most recently updated plugins first |
"""


def gen_all_packages(plugins: dict, stats: dict) -> str:
    sorted_plugins = sorted(
        plugins.items(), key=lambda kv: (kv[1].get("name") or kv[0]).lower()
    )
    rows = [plugin_row(nix_id, entry, stats) for nix_id, entry in sorted_plugins]
    return f"""\
# All Packages ({fmt_int(len(plugins))})

{plugin_table(rows)}
"""


def gen_all_themes(themes: dict) -> str:
    sorted_themes = sorted(
        themes.items(), key=lambda kv: (kv[1].get("name") or kv[0]).lower()
    )
    rows = [theme_row(nix_id, entry) for nix_id, entry in sorted_themes]
    return f"""\
# All Themes ({fmt_int(len(themes))})

{theme_table(rows)}
"""


def gen_by_popularity(plugins: dict, stats: dict) -> str:
    ranked = sorted(
        [(k, plugins[k], stats[k]) for k in plugins if k in stats and stats[k].get("downloads")],
        key=lambda x: x[2]["downloads"],
        reverse=True,
    )
    rows = [
        ranked_plugin_row(i + 1, nix_id, entry, stats)
        for i, (nix_id, entry, _) in enumerate(ranked)
    ]
    return f"""\
# Packages by Popularity ({fmt_int(len(ranked))} with stats)

{ranked_table(rows)}
"""


def gen_by_last_updated(plugins: dict, stats: dict) -> str:
    ranked = sorted(
        [(k, plugins[k], stats[k]) for k in plugins if k in stats and stats[k].get("updated")],
        key=lambda x: x[2]["updated"],
        reverse=True,
    )
    rows = [
        ranked_plugin_row(i + 1, nix_id, entry, stats)
        for i, (nix_id, entry, _) in enumerate(ranked)
    ]
    return f"""\
# Packages by Last Updated ({fmt_int(len(ranked))} with stats)

{ranked_table(rows)}
"""


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "wiki"
    out_dir.mkdir(parents=True, exist_ok=True)

    plugins: dict = {}
    themes:  dict = {}
    if PLUGINS_DATA.exists():
        plugins = json.loads(PLUGINS_DATA.read_text())
    if THEMES_DATA.exists():
        themes = json.loads(THEMES_DATA.read_text())

    print("Fetching community-plugin-stats.json ...")
    with urllib.request.urlopen(STATS_URL, timeout=30) as r:
        stats: dict = json.loads(r.read())

    print(f"Generating wiki pages -> {out_dir}/")
    pages = {
        "Home.md":                     gen_home(plugins, themes, stats),
        "All-Packages.md":             gen_all_packages(plugins, stats),
        "All-Themes.md":               gen_all_themes(themes),
        "Packages-by-Popularity.md":   gen_by_popularity(plugins, stats),
        "Packages-by-Last-Updated.md": gen_by_last_updated(plugins, stats),
    }

    for filename, content in pages.items():
        (out_dir / filename).write_text(content)
        print(f"  {filename}")

    print(f"\nDone — {len(pages)} pages written.")


if __name__ == "__main__":
    main()
