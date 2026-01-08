# Claude Code Plugins

Specialized tools for Claude Code workflows developed by Data-Wise. Each plugin is independently versioned and published to npm while sharing common standards and infrastructure.

## Available Plugins

### RForge - R Package Ecosystem Management
**Version:** 1.1.0 | **Status:** Production-Ready

Complete R package ecosystem orchestrator with 15 commands for development, dependency analysis, and intelligent workflow management.

**Key Features:**
- Auto-detect project structure (single package, ecosystem, or hybrid)
- Dependency analysis and cascade updates across packages
- Mode system with 4 analysis levels (default, debug, optimize, release)
- 292 passing tests with 4ms average performance

[Learn More →](rforge.md)

---

### Craft - Full-Stack Developer Toolkit
**Version:** 1.10.0 | **Status:** Active Development

Comprehensive developer toolkit with 67 commands, 7 agents, and 17 skills spanning code, git, documentation, testing, architecture, CI, and distribution.

**Key Features:**
- 13 command categories (arch, ci, code, dist, docs, git, plan, site, test)
- Orchestrator v2 with subagent monitoring
- Python-based testing framework
- Advanced workflow automation

[Learn More →](craft.md)

---

### Workflow - ADHD-Friendly Tools
**Version:** 2.1.0 | **Status:** Production-Ready

ADHD-friendly workflow automation designed for focus, task management, and decision support.

**Key Features:**
- Brainstorm mode with structured proposals
- Focus and task tracking commands
- Decision support (next, done, recap, stuck)
- 3-layer argument system
- Spec capture functionality

[Learn More →](workflow.md)

---

### Statistical Research - Research Toolkit
**Version:** 1.1.0 | **Status:** Production-Ready

Statistical research workflows with literature management, manuscript tools, and 17 A-grade skills for research and writing.

**Key Features:**
- Pure plugin (no MCP dependencies)
- Shell-based APIs (arXiv, Crossref, BibTeX)
- 14 commands across 4 categories
- 17 domain-specific skills (mathematical, implementation, writing, research)

[Learn More →](statistical-research.md)

---

## Quick Start

### Installation

Install plugins via npm:

```bash
# Install all plugins
npm install -g @data-wise/rforge-plugin
npm install -g @data-wise/claude-craft-plugin
npm install -g @data-wise/claude-workflow-plugin
npm install -g @data-wise/statistical-research-plugin

# Install in development mode (symlink)
cd <plugin-name>
./scripts/install.sh --dev
```

### Usage

Plugins automatically register their commands with Claude Code. Use slash commands to invoke plugin functionality:

```bash
# RForge commands
/rforge:status          # Check ecosystem health
/rforge:analyze         # Deep analysis with mode system

# Craft commands
/craft:test:run         # Run test suites
/craft:git:worktree     # Git worktree management

# Workflow commands
/workflow:brainstorm    # Start brainstorming session
/workflow:next          # Get next task suggestion

# Statistical Research commands
/research:lit:arxiv     # Search arXiv literature
/research:manuscript:methods  # Write methods section
```

## Plugin Architecture

All plugins follow a consistent structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json       # Metadata and configuration
├── commands/             # Slash commands (optional)
├── skills/               # Auto-activating skills (optional)
├── agents/               # Autonomous agents (optional)
├── lib/                  # Utilities/APIs (optional)
├── scripts/
│   ├── install.sh        # Installation script
│   └── uninstall.sh      # Uninstallation script
├── tests/                # Test suite
├── package.json          # npm metadata
├── README.md
└── LICENSE               # MIT license
```

## Documentation

- **[Developer Guide](../CLAUDE.md)** - Contributing and development standards
- **[Plugin Development](../PLUGIN-DEVELOPMENT.md)** - Creating new plugins
- **[Publishing](../PUBLISHING.md)** - npm and GitHub release workflows
- **[Mode System](../MODE-SYSTEM.md)** - Shared mode system architecture
- **[CI/CD](../CICD.md)** - Continuous integration and deployment

## Support

- **GitHub Issues:** [https://github.com/Data-Wise/claude-plugins/issues](https://github.com/Data-Wise/claude-plugins/issues)
- **npm Organization:** [https://www.npmjs.com/org/data-wise](https://www.npmjs.com/org/data-wise)
- **Documentation Site:** [https://data-wise.github.io/claude-plugins](https://data-wise.github.io/claude-plugins)
