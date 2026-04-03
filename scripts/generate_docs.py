#!/usr/bin/env python3
"""
Generate PACKAGES.md from plugins-data.json and themes-data.json.

Usage:
    python3 scripts/generate_docs.py
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PLUGINS_DATA = REPO_ROOT / "plugins-data.json"
THEMES_DATA  = REPO_ROOT / "themes-data.json"
OUTPUT       = REPO_ROOT / "PACKAGES.md"


def table_row(nix_id: str, entry: dict) -> str:
    name    = entry.get("name") or nix_id
    repo    = entry.get("repo", "")
    desc    = (entry.get("description") or "").replace("|", "\\|").replace("\n", " ").strip()
    gh_url  = f"https://github.com/{repo}" if repo else ""
    name_md = f"[{name}]({gh_url})" if gh_url else name
    return f"| {name_md} | `{nix_id}` | {desc} |"


def build_table(data: dict) -> str:
    header = (
        "| Name | Package ID | Description |\n"
        "|------|-----------|-------------|"
    )
    rows = [
        table_row(nix_id, entry)
        for nix_id, entry in sorted(data.items(), key=lambda kv: (kv[1].get("name") or kv[0]).lower())
    ]
    return header + "\n" + "\n".join(rows)


def main():
    plugins: dict = {}
    themes:  dict = {}

    if PLUGINS_DATA.exists():
        plugins = json.loads(PLUGINS_DATA.read_text())
    if THEMES_DATA.exists():
        themes = json.loads(THEMES_DATA.read_text())

    content = f"""\
# Obsidian Nix Packages

All Obsidian community plugins and themes packaged as Nix derivations, sourced from
[obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases).

## Usage

Add this flake as an input and reference packages by their **Package ID**:

```nix
inputs.obsidian-nix.url = "github:soulvice/obsidian-nix";

# then inside your config:
inputs.obsidian-nix.packages.${{system}}.dataview
inputs.obsidian-nix.packages.${{system}}.catppuccin
```

---

## Plugins ({len(plugins)})

{build_table(plugins) if plugins else "_No plugins yet — run the update workflow._"}

---

## Themes ({len(themes)})

{build_table(themes) if themes else "_No themes yet — run the update workflow._"}
"""

    OUTPUT.write_text(content)
    print(f"Wrote {OUTPUT}  ({len(plugins)} plugins, {len(themes)} themes)")


if __name__ == "__main__":
    main()
