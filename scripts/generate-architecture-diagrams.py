#!/usr/bin/env python3
"""
Auto-generate Mermaid architecture diagrams from plugin structure.

Generates:
- Plugin structure diagrams (directories and files)
- Command flow diagrams
- Plugin ecosystem diagram
- Dependency diagrams

Usage:
    python3 generate-architecture-diagrams.py [--output DIR]

Output:
    docs/diagrams/ (or specified directory)
"""

import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime

class ArchitectureDiagramGenerator:
    """Generates Mermaid architecture diagrams."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.plugins = ['rforge-orchestrator', 'statistical-research', 'workflow']

    def generate_plugin_structure(self, plugin_name: str) -> str:
        """Generate directory structure diagram for a plugin."""
        plugin_path = self.repo_root / plugin_name

        lines = []
        lines.append("```mermaid")
        lines.append("graph TD")
        lines.append(f"    ROOT[{plugin_name}]")

        # Add main directories
        if (plugin_path / 'commands').exists():
            lines.append("    ROOT --> COMMANDS[commands/]")
            cmd_files = list((plugin_path / 'commands').rglob('*.md'))
            for i, cmd_file in enumerate(cmd_files[:5]):  # Show first 5
                rel_path = cmd_file.relative_to(plugin_path / 'commands')
                lines.append(f"    COMMANDS --> CMD{i}[\"{rel_path}\"]")
            if len(cmd_files) > 5:
                lines.append(f"    COMMANDS --> MORE[\"... {len(cmd_files) - 5} more\"]")

        if (plugin_path / 'skills').exists():
            lines.append("    ROOT --> SKILLS[skills/]")
            skill_files = list((plugin_path / 'skills').rglob('*.md'))
            lines.append(f"    SKILLS --> SKILL_COUNT[\"{len(skill_files)} skill files\"]")

        if (plugin_path / '.claude-plugin').exists():
            lines.append("    ROOT --> PLUGIN[.claude-plugin/]")
            lines.append("    PLUGIN --> PLUGIN_JSON[plugin.json]")

        if (plugin_path / 'package.json').exists():
            lines.append("    ROOT --> PKG[package.json]")

        if (plugin_path / 'README.md').exists():
            lines.append("    ROOT --> README[README.md]")

        # Style nodes
        lines.append("")
        lines.append("    style ROOT fill:#e1f5ff")
        lines.append("    style COMMANDS fill:#fff4e6")
        lines.append("    style SKILLS fill:#f3e5f5")
        lines.append("    style PLUGIN fill:#e8f5e9")

        lines.append("```")
        return '\n'.join(lines)

    def generate_command_flow(self, plugin_name: str) -> str:
        """Generate command flow diagram."""
        lines = []
        lines.append("```mermaid")
        lines.append("sequenceDiagram")
        lines.append("    participant User")
        lines.append("    participant Claude as Claude Code")
        lines.append(f"    participant Plugin as {plugin_name}")

        if plugin_name == 'rforge-orchestrator':
            lines.append("    participant MCP as RForge MCP Server")
            lines.append("")
            lines.append("    User->>Claude: /rforge:analyze \"Update code\"")
            lines.append("    Claude->>Plugin: Execute command")
            lines.append("    Plugin->>Plugin: Detect pattern (CODE_CHANGE)")
            lines.append("    Plugin->>MCP: Call rforge_quick_impact")
            lines.append("    MCP-->>Plugin: Impact results")
            lines.append("    Plugin->>MCP: Call rforge_quick_tests")
            lines.append("    MCP-->>Plugin: Test results")
            lines.append("    Plugin->>Plugin: Synthesize results")
            lines.append("    Plugin-->>Claude: Analysis complete")
            lines.append("    Claude-->>User: Display results + recommendations")
        elif plugin_name == 'statistical-research':
            lines.append("    participant Tools as Research Tools")
            lines.append("")
            lines.append("    User->>Claude: /research:arxiv \"mediation\"")
            lines.append("    Claude->>Plugin: Execute command")
            lines.append("    Plugin->>Tools: Search arXiv API")
            lines.append("    Tools-->>Plugin: Paper results")
            lines.append("    Plugin->>Plugin: Format results")
            lines.append("    Plugin-->>Claude: Formatted papers")
            lines.append("    Claude-->>User: Display papers with metadata")
        else:  # workflow
            lines.append("    participant Agent as Specialized Agent")
            lines.append("")
            lines.append("    User->>Claude: /brainstorm \"API design\"")
            lines.append("    Claude->>Plugin: Execute command")
            lines.append("    Plugin->>Plugin: Detect context")
            lines.append("    Plugin->>Plugin: Select mode (TECHNICAL)")
            lines.append("    Plugin->>Agent: Delegate to backend-architect")
            lines.append("    Agent-->>Plugin: Design proposals")
            lines.append("    Plugin->>Plugin: Format output")
            lines.append("    Plugin-->>Claude: Structured brainstorm")
            lines.append("    Claude-->>User: Display options + next steps")

        lines.append("```")
        return '\n'.join(lines)

    def generate_ecosystem_diagram(self) -> str:
        """Generate overall plugin ecosystem diagram."""
        lines = []
        lines.append("```mermaid")
        lines.append("graph TB")
        lines.append("    subgraph \"Claude Code Environment\"")
        lines.append("        USER[User]")
        lines.append("        CLAUDE[Claude Code CLI]")
        lines.append("    end")
        lines.append("")
        lines.append("    subgraph \"Plugins\"")
        lines.append("        RFORGE[rforge-orchestrator]")
        lines.append("        RESEARCH[statistical-research]")
        lines.append("        WORKFLOW[workflow]")
        lines.append("    end")
        lines.append("")
        lines.append("    subgraph \"MCP Servers\"")
        lines.append("        RFORGE_MCP[RForge MCP]")
        lines.append("        STAT_MCP[Statistical Research MCP]")
        lines.append("    end")
        lines.append("")
        lines.append("    subgraph \"External Services\"")
        lines.append("        ARXIV[arXiv API]")
        lines.append("        ZOTERO[Zotero]")
        lines.append("        R[R Environment]")
        lines.append("    end")
        lines.append("")
        lines.append("    USER -->|Commands| CLAUDE")
        lines.append("    CLAUDE -->|/rforge:*| RFORGE")
        lines.append("    CLAUDE -->|/research:*| RESEARCH")
        lines.append("    CLAUDE -->|/brainstorm| WORKFLOW")
        lines.append("")
        lines.append("    RFORGE -->|MCP Protocol| RFORGE_MCP")
        lines.append("    RESEARCH -->|MCP Protocol| STAT_MCP")
        lines.append("")
        lines.append("    RFORGE_MCP -->|R CMD check| R")
        lines.append("    STAT_MCP -->|Search| ARXIV")
        lines.append("    STAT_MCP -->|Citations| ZOTERO")
        lines.append("")
        lines.append("    style USER fill:#e3f2fd")
        lines.append("    style CLAUDE fill:#fff3e0")
        lines.append("    style RFORGE fill:#f3e5f5")
        lines.append("    style RESEARCH fill:#e8f5e9")
        lines.append("    style WORKFLOW fill:#fce4ec")
        lines.append("    style RFORGE_MCP fill:#fff9c4")
        lines.append("    style STAT_MCP fill:#fff9c4")
        lines.append("```")
        return '\n'.join(lines)

    def generate_dependency_diagram(self) -> str:
        """Generate plugin dependency diagram."""
        lines = []
        lines.append("```mermaid")
        lines.append("graph LR")
        lines.append("    subgraph \"Required for All Plugins\"")
        lines.append("        CLAUDE[Claude Code CLI]")
        lines.append("        NODE[Node.js >= 18]")
        lines.append("    end")
        lines.append("")
        lines.append("    subgraph \"Plugin: rforge-orchestrator\"")
        lines.append("        RFORGE[rforge-orchestrator]")
        lines.append("        RFORGE_MCP[rforge-mcp >= 0.1.0]")
        lines.append("        R_ENV[R >= 4.0]")
        lines.append("    end")
        lines.append("")
        lines.append("    subgraph \"Plugin: statistical-research\"")
        lines.append("        RESEARCH[statistical-research]")
        lines.append("        STAT_MCP[statistical-research-mcp]")
        lines.append("    end")
        lines.append("")
        lines.append("    subgraph \"Plugin: workflow\"")
        lines.append("        WORKFLOW[workflow]")
        lines.append("    end")
        lines.append("")
        lines.append("    RFORGE -.->|requires| CLAUDE")
        lines.append("    RFORGE -->|peerDependency| RFORGE_MCP")
        lines.append("    RFORGE_MCP -->|requires| R_ENV")
        lines.append("")
        lines.append("    RESEARCH -.->|requires| CLAUDE")
        lines.append("    RESEARCH -->|uses| STAT_MCP")
        lines.append("")
        lines.append("    WORKFLOW -.->|requires| CLAUDE")
        lines.append("")
        lines.append("    CLAUDE -->|requires| NODE")
        lines.append("")
        lines.append("    style CLAUDE fill:#fff3e0")
        lines.append("    style RFORGE fill:#f3e5f5")
        lines.append("    style RESEARCH fill:#e8f5e9")
        lines.append("    style WORKFLOW fill:#fce4ec")
        lines.append("```")
        return '\n'.join(lines)

    def generate_all_diagrams(self, output_dir: Path):
        """Generate all architecture diagrams."""
        output_dir.mkdir(parents=True, exist_ok=True)

        print(f"Generating architecture diagrams in {output_dir}...")

        # Ecosystem diagram
        print("  - Ecosystem diagram...")
        ecosystem_file = output_dir / 'ECOSYSTEM.md'
        content = [
            "# Plugin Ecosystem",
            "",
            f"**Auto-generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Overview",
            "",
            self.generate_ecosystem_diagram(),
            ""
        ]
        ecosystem_file.write_text('\n'.join(content))

        # Dependency diagram
        print("  - Dependency diagram...")
        dep_file = output_dir / 'DEPENDENCIES.md'
        content = [
            "# Plugin Dependencies",
            "",
            f"**Auto-generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Dependency Graph",
            "",
            self.generate_dependency_diagram(),
            ""
        ]
        dep_file.write_text('\n'.join(content))

        # Per-plugin diagrams
        for plugin in self.plugins:
            plugin_path = self.repo_root / plugin
            if not plugin_path.exists():
                continue

            print(f"  - {plugin} diagrams...")

            # Structure diagram
            struct_file = output_dir / f'{plugin}-structure.md'
            content = [
                f"# {plugin.replace('-', ' ').title()} Structure",
                "",
                f"**Auto-generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "",
                "## Directory Structure",
                "",
                self.generate_plugin_structure(plugin),
                ""
            ]
            struct_file.write_text('\n'.join(content))

            # Command flow diagram
            flow_file = output_dir / f'{plugin}-flow.md'
            content = [
                f"# {plugin.replace('-', ' ').title()} Command Flow",
                "",
                f"**Auto-generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "",
                "## Example Command Execution",
                "",
                self.generate_command_flow(plugin),
                ""
            ]
            flow_file.write_text('\n'.join(content))

        print(f"✅ Generated {len(list(output_dir.glob('*.md')))} diagram files")

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate architecture diagrams')
    parser.add_argument('--output', '-o',
                       default='docs/diagrams',
                       help='Output directory (default: docs/diagrams)')
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    output_dir = repo_root / args.output

    generator = ArchitectureDiagramGenerator(repo_root)
    generator.generate_all_diagrams(output_dir)

if __name__ == '__main__':
    main()
