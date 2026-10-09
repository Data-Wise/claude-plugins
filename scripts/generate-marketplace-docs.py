#!/usr/bin/env python3
"""Generate the public plugin catalog and command-source index from marketplace.json."""

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".claude-plugin" / "marketplace.json"
DOCS = ROOT / "docs"


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def load_plugins() -> list[dict[str, Any]]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    plugins = manifest.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        raise ValueError(f"{MANIFEST} must contain a non-empty plugins array")

    names = [plugin.get("name") for plugin in plugins]
    if any(not isinstance(name, str) or not name.strip() for name in names):
        raise ValueError("Each marketplace plugin must have a non-empty name")
    if len(names) != len(set(names)):
        raise ValueError("Marketplace plugin names must be unique")

    for plugin in plugins:
        repository = plugin.get("repository")
        if not repository and isinstance(plugin.get("source"), dict):
            repo = plugin["source"].get("repo")
            if repo:
                repository = f"https://github.com/{repo}"
                plugin["repository"] = repository
        if not repository:
            raise ValueError(f"Plugin {plugin['name']} has no repository URL")
    return plugins


def display_name(name: str) -> str:
    return "RForge" if name.lower() == "rforge" else name.replace("-", " ").title()


def generate_catalog(plugins: list[dict[str, Any]]) -> str:
    lines = [
        "# Active Plugin Catalog",
        "",
        f"**{len(plugins)} plugins** listed from the Data-Wise Marketplace manifest.",
        "",
        "This catalog reflects plugins registered in the marketplace. Versions and source links come from the same manifest.",
        "",
        "| Plugin | Version | Description | Plugin site | Repository |",
        "|---|---:|---|---|---|",
    ]
    for plugin in plugins:
        name = display_name(plugin["name"])
        version = markdown_cell(str(plugin.get("version", "not specified")))
        description = markdown_cell(plugin.get("description", ""))
        repository = plugin["repository"].rstrip("/")
        homepage = plugin.get("homepage")
        site = f"[Website]({homepage})" if homepage else "—"
        lines.append(
            f"| {name} | {version} | {description} | {site} | [Repository]({repository}) |"
        )
    lines.extend([
        "",
        "---",
        "",
        "Generated from .claude-plugin/marketplace.json. Do not edit by hand; run python3 scripts/generate-marketplace-docs.py.",
        "",
    ])
    return "\n".join(lines)


def generate_command_sources(plugins: list[dict[str, Any]]) -> str:
    lines = [
        "# Command Documentation Sources",
        "",
        "The active plugins are maintained in standalone repositories. This aggregator does not contain the canonical command files for every marketplace plugin, so it does not publish a combined slash-command list or total.",
        "",
        "| Plugin | Plugin site | Command source |",
        "|---|---|---|",
    ]
    for plugin in plugins:
        name = display_name(plugin["name"])
        repository = plugin["repository"].rstrip("/")
        homepage = plugin.get("homepage")
        site = f"[Website]({homepage})" if homepage else "—"
        lines.append(
            f"| {name} | {site} | [Repository]({repository}) |"
        )
    lines.extend([
        "",
        "This index is generated from .claude-plugin/marketplace.json. Run python3 scripts/generate-marketplace-docs.py to refresh it.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    plugins = load_plugins()
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "PLUGIN-CATALOG.md").write_text(generate_catalog(plugins), encoding="utf-8")
    (DOCS / "COMMAND-REFERENCE.md").write_text(generate_command_sources(plugins), encoding="utf-8")
    print(f"Generated catalog and command-source index for {len(plugins)} marketplace plugins.")


if __name__ == "__main__":
    main()
