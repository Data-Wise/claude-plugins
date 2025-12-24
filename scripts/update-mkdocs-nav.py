#!/usr/bin/env python3
"""
Auto-update mkdocs.yml navigation from generated documentation.

Updates:
- Command reference section
- Architecture diagrams section
- Plugin documentation links

Usage:
    python3 update-mkdocs-nav.py [--config FILE]

Output:
    Updates mkdocs.yml (or specified file) in place
"""

import yaml
from pathlib import Path
from datetime import datetime

class MkDocsNavigationUpdater:
    """Updates mkdocs.yml navigation automatically."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.plugins = ['rforge-orchestrator', 'statistical-research', 'workflow']

    def get_generated_docs(self) -> dict:
        """Find all generated documentation files."""
        docs = {
            'command_reference': None,
            'diagrams': [],
            'plugins': []
        }

        # Command reference
        cmd_ref = self.repo_root / 'docs' / 'COMMAND-REFERENCE.md'
        if cmd_ref.exists():
            docs['command_reference'] = 'COMMAND-REFERENCE.md'

        # Architecture diagrams
        diagrams_dir = self.repo_root / 'docs' / 'diagrams'
        if diagrams_dir.exists():
            for diagram_file in sorted(diagrams_dir.glob('*.md')):
                docs['diagrams'].append(f'diagrams/{diagram_file.name}')

        # Plugin READMEs
        for plugin in self.plugins:
            readme = self.repo_root / plugin / 'README.md'
            if readme.exists():
                docs['plugins'].append({
                    'name': plugin.replace('-', ' ').title(),
                    'path': f'../{plugin}/README.md'
                })

        return docs

    def create_navigation_structure(self, docs: dict) -> list:
        """Create navigation structure for mkdocs."""
        nav = []

        # Home
        nav.append({'Home': 'index.md'})

        # Getting Started
        nav.append({
            'Getting Started': [
                {'Installation': 'installation.md'},
                {'Quick Start': 'quick-start.md'}
            ]
        })

        # Plugins
        plugin_nav = []
        for plugin_info in docs['plugins']:
            plugin_nav.append({plugin_info['name']: plugin_info['path']})

        if plugin_nav:
            nav.append({'Plugins': plugin_nav})

        # Command Reference
        if docs['command_reference']:
            nav.append({'Command Reference': docs['command_reference']})

        # Architecture
        if docs['diagrams']:
            arch_nav = []
            for diagram in docs['diagrams']:
                # Generate nice name from filename
                name = diagram.split('/')[-1].replace('.md', '').replace('-', ' ').title()
                arch_nav.append({name: diagram})

            nav.append({'Architecture': arch_nav})

        # Development
        nav.append({
            'Development': [
                {'Scripts': 'scripts/README.md'},
                {'Validation': 'PLUGIN-VALIDATION-REPORT.md'},
                {'DevOps': 'DEVOPS-IMPLEMENTATION-COMPLETE.md'}
            ]
        })

        return nav

    def update_mkdocs_yaml(self, mkdocs_file: Path):
        """Update mkdocs.yml file with new navigation."""
        print(f"Reading {mkdocs_file}...")

        # Read existing config
        if mkdocs_file.exists():
            with open(mkdocs_file, 'r') as f:
                config = yaml.safe_load(f) or {}
        else:
            config = {}

        # Get generated docs
        print("Discovering generated documentation...")
        docs = self.get_generated_docs()

        print(f"  - Command reference: {'✅' if docs['command_reference'] else '❌'}")
        print(f"  - Architecture diagrams: {len(docs['diagrams'])} files")
        print(f"  - Plugin docs: {len(docs['plugins'])} plugins")

        # Create navigation
        print("Generating navigation structure...")
        nav = self.create_navigation_structure(docs)

        # Update config
        config['nav'] = nav

        # Ensure other required fields
        if 'site_name' not in config:
            config['site_name'] = 'Claude Code Plugins'

        if 'repo_url' not in config:
            config['repo_url'] = 'https://github.com/Data-Wise/claude-plugins'

        if 'theme' not in config:
            config['theme'] = {
                'name': 'material',
                'features': [
                    'navigation.tabs',
                    'navigation.sections',
                    'navigation.expand',
                    'search.suggest',
                    'search.highlight',
                    'content.code.copy'
                ]
            }

        if 'markdown_extensions' not in config:
            config['markdown_extensions'] = [
                'pymdownx.highlight',
                'pymdownx.superfences',
                'pymdownx.tabbed',
                'pymdownx.details',
                'admonition',
                'tables',
                'attr_list',
                'def_list'
            ]

        # Write updated config
        print(f"Writing updated configuration...")
        with open(mkdocs_file, 'w') as f:
            # Add header comment
            f.write(f"# MkDocs configuration for Claude Code Plugins\n")
            f.write(f"# Auto-updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Do not edit navigation manually - regenerate with scripts/update-mkdocs-nav.py\n\n")
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)

        print(f"✅ Updated {mkdocs_file}")
        print(f"   Navigation sections: {len(nav)}")

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Update mkdocs.yml navigation')
    parser.add_argument('--config', '-c',
                       default='mkdocs.yml',
                       help='MkDocs config file (default: mkdocs.yml)')
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    mkdocs_file = repo_root / args.config

    updater = MkDocsNavigationUpdater(repo_root)
    updater.update_mkdocs_yaml(mkdocs_file)

if __name__ == '__main__':
    main()
