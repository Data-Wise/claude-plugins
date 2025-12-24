#!/usr/bin/env python3
"""
Auto-generate command reference documentation from plugin command frontmatter.

Parses all command .md files and generates:
- Complete command reference with descriptions
- Usage examples
- Organized by plugin
- Markdown tables for easy reading

Usage:
    python3 generate-command-reference.py [--output FILE]

Output:
    docs/COMMAND-REFERENCE.md (or specified file)
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Command:
    """Represents a parsed command."""
    name: str
    description: str
    argument_hint: Optional[str] = None
    file_path: Path = None
    plugin: str = None
    content_preview: str = None

class CommandReferenceGenerator:
    """Generates command reference documentation."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.plugins = ['rforge-orchestrator', 'statistical-research', 'workflow']
        self.commands_by_plugin: Dict[str, List[Command]] = {}

    def parse_frontmatter(self, file_path: Path) -> Optional[Command]:
        """Parse YAML frontmatter from a command file."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()

            # Extract frontmatter
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.+)', content, re.DOTALL)
            if not match:
                return None

            frontmatter = match.group(1)
            body = match.group(2)

            # Parse fields
            name_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
            desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
            arg_match = re.search(r'^argument-hint:\s*(.+)$', frontmatter, re.MULTILINE)

            if not name_match:
                return None

            # Extract first paragraph of content as preview
            paragraphs = body.strip().split('\n\n')
            preview = None
            for para in paragraphs[1:3]:  # Skip first (usually # header)
                if para and not para.startswith('#'):
                    preview = para.strip()[:200]
                    break

            return Command(
                name=name_match.group(1).strip(),
                description=desc_match.group(1).strip() if desc_match else "No description",
                argument_hint=arg_match.group(1).strip() if arg_match else None,
                file_path=file_path,
                content_preview=preview
            )

        except Exception as e:
            print(f"Error parsing {file_path}: {e}", file=sys.stderr)
            return None

    def collect_commands(self):
        """Collect all commands from all plugins."""
        for plugin in self.plugins:
            plugin_path = self.repo_root / plugin
            commands_dir = plugin_path / 'commands'

            if not commands_dir.exists():
                continue

            commands = []
            for cmd_file in sorted(commands_dir.rglob('*.md')):
                cmd = self.parse_frontmatter(cmd_file)
                if cmd:
                    cmd.plugin = plugin
                    commands.append(cmd)

            if commands:
                self.commands_by_plugin[plugin] = sorted(commands, key=lambda c: c.name)

    def generate_markdown(self) -> str:
        """Generate markdown documentation."""
        lines = []

        # Header
        lines.append("# Command Reference")
        lines.append("")
        lines.append(f"**Auto-generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        lines.append("Complete reference of all commands across all plugins.")
        lines.append("")

        # Table of contents
        lines.append("## Table of Contents")
        lines.append("")
        for plugin in self.plugins:
            if plugin in self.commands_by_plugin:
                count = len(self.commands_by_plugin[plugin])
                plugin_title = plugin.replace('-', ' ').title()
                lines.append(f"- [{plugin_title}](#{plugin}) ({count} commands)")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Commands by plugin
        for plugin in self.plugins:
            if plugin not in self.commands_by_plugin:
                continue

            commands = self.commands_by_plugin[plugin]
            plugin_title = plugin.replace('-', ' ').title()

            lines.append(f"## {plugin_title}")
            lines.append("")
            lines.append(f"**Plugin:** `{plugin}`")
            lines.append(f"**Commands:** {len(commands)}")
            lines.append("")

            # Command table
            lines.append("| Command | Description | Arguments |")
            lines.append("|---------|-------------|-----------|")

            for cmd in commands:
                name = cmd.name
                desc = cmd.description.replace('|', '\\|')
                args = cmd.argument_hint.replace('|', '\\|') if cmd.argument_hint else "—"
                lines.append(f"| `/{name}` | {desc} | {args} |")

            lines.append("")

            # Detailed descriptions
            lines.append("### Detailed Descriptions")
            lines.append("")

            for cmd in commands:
                lines.append(f"#### `/{cmd.name}`")
                lines.append("")
                lines.append(f"**Description:** {cmd.description}")
                lines.append("")

                if cmd.argument_hint:
                    lines.append(f"**Arguments:** {cmd.argument_hint}")
                    lines.append("")

                if cmd.content_preview:
                    lines.append(f"**Usage:**")
                    lines.append("")
                    lines.append(f"{cmd.content_preview}")
                    lines.append("")

                # Link to source
                rel_path = cmd.file_path.relative_to(self.repo_root)
                lines.append(f"**Source:** [`{rel_path}`](../{rel_path})")
                lines.append("")

            lines.append("---")
            lines.append("")

        # Footer
        lines.append("## How to Use Commands")
        lines.append("")
        lines.append("Commands are invoked in Claude Code using the `/` prefix:")
        lines.append("")
        lines.append("```")
        lines.append("/command-name [arguments]")
        lines.append("```")
        lines.append("")
        lines.append("**Examples:**")
        lines.append("```")
        lines.append("/rforge:quick")
        lines.append("/rforge:analyze \"Update bootstrap algorithm\"")
        lines.append("/research:arxiv mediation analysis")
        lines.append("/brainstorm")
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("**Note:** This document is auto-generated from command frontmatter.")
        lines.append("Do not edit manually - regenerate with `scripts/generate-command-reference.py`")
        lines.append("")

        return '\n'.join(lines)

    def generate(self, output_file: Path):
        """Generate the command reference."""
        print(f"Collecting commands from {len(self.plugins)} plugins...")
        self.collect_commands()

        total_commands = sum(len(cmds) for cmds in self.commands_by_plugin.values())
        print(f"Found {total_commands} commands across {len(self.commands_by_plugin)} plugins")

        print(f"Generating markdown...")
        markdown = self.generate_markdown()

        print(f"Writing to {output_file}...")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(markdown)

        print(f"✅ Command reference generated: {output_file}")
        print(f"   Total commands: {total_commands}")

        # Print summary
        for plugin, commands in self.commands_by_plugin.items():
            print(f"   - {plugin}: {len(commands)} commands")

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate command reference documentation')
    parser.add_argument('--output', '-o',
                       default='docs/COMMAND-REFERENCE.md',
                       help='Output file path (default: docs/COMMAND-REFERENCE.md)')
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    output_file = repo_root / args.output

    generator = CommandReferenceGenerator(repo_root)
    generator.generate(output_file)

if __name__ == '__main__':
    main()
