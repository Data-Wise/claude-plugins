# Claude Code Plugins

> **Official Claude Code plugins developed by Data-Wise** - Professional tools for statistical research, R package development, and AI-assisted workflows

A monorepo containing high-quality Claude Code plugins. Each plugin is independently published to npm but shares common standards, tooling, and documentation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Monorepo](https://img.shields.io/badge/repo-monorepo-blue.svg)](https://github.com/Data-Wise/claude-plugins)
[![Documentation](https://img.shields.io/badge/docs-online-brightgreen.svg)](https://data-wise.github.io/claude-plugins/)

📖 **[Complete Documentation](https://data-wise.github.io/claude-plugins/)** | 🚀 **[Quick Start](https://data-wise.github.io/claude-plugins/quick-start/)** | 📚 **[Command Reference](https://data-wise.github.io/claude-plugins/COMMAND-REFERENCE/)** | 🛠️ **[Developer Guide](CLAUDE.md)**

---

> Current marketplace entries and versions are maintained in [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json). See the [generated plugin catalog](docs/PLUGIN-CATALOG.md) for current links; details below are historical monorepo snapshots.

## Historical Monorepo Plugin Snapshot

### 📊 Statistical Research Plugin

**Status:** ✅ Released v1.0.0
**Location:** [`statistical-research/`](statistical-research/)
**npm:** `@data-wise/statistical-research-plugin`

Statistical research workflows for Claude Code - literature management, manuscript writing, simulation studies, and 17 A-grade research skills.

**Features:**
- 13 slash commands (literature, manuscript, simulation, research)
- 17 A-grade skills (mathematical, implementation, writing, research)
- Shell API wrappers (arXiv, Crossref, BibTeX)
- Pure plugin architecture (no MCP dependencies)

**Install:**
```bash
npm install -g @data-wise/statistical-research-plugin
# OR
cd statistical-research && ./scripts/install.sh --dev
```

[📖 Documentation](statistical-research/README.md) | [🚀 Quick Start](statistical-research/README.md#quick-start)

---

### 🔧 RForge Orchestrator Plugin (Coming Soon)

**Status:** 🚧 Planned
**Location:** `rforge-orchestrator/` (to be moved)
**npm:** `@data-wise/rforge-orchestrator-plugin`

Auto-delegation orchestrator for RForge MCP tools - intelligent analysis of R package changes.

**Features:**
- Pattern recognition (CODE_CHANGE, BUG_FIX, RELEASE)
- Parallel MCP tool execution
- 3 analysis modes (quick, balanced, thorough)

---

## 🚀 Quick Start

### Install All Plugins

```bash
# Clone repository
git clone https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins

# Install specific plugin
cd statistical-research
./scripts/install.sh --dev  # Development mode (symlink)
# OR
./scripts/install.sh        # Production mode (copy)
```

### Install from npm

```bash
# Install specific plugins
npm install -g @data-wise/statistical-research-plugin

# Future plugins
npm install -g @data-wise/rforge-orchestrator-plugin
```

### Verify Installation

```bash
# Check installed plugins
ls -la ~/.claude/plugins/

# Try a command
# (In Claude Code)
/research:arxiv "your research topic"
```

---

## 📚 Documentation

### For Plugin Users

- **[Getting Started Guide](docs/GETTING-STARTED.md)** - Install and use plugins
- **[Command Reference](docs/COMMAND-REFERENCE.md)** - All available commands
- **[Skills Guide](docs/SKILLS-GUIDE.md)** - How skills activate
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues

### For Plugin Developers

- **[Knowledge Base](KNOWLEDGE.md)** - Architecture, patterns, best practices
- **[Plugin Development Guide](docs/PLUGIN-DEVELOPMENT.md)** - Create new plugins
- **[Publishing Guide](docs/PUBLISHING.md)** - Publish to npm and GitHub
- **[Testing Guide](docs/TESTING.md)** - Test plugins thoroughly

---

## 🏗️ Repository Structure

```
claude-plugins/                    # Monorepo root
├── .github/
│   └── workflows/
│       ├── test-all.yml          # Test all plugins
│       └── publish-plugin.yml    # Publish individual plugin
├── statistical-research/          # Plugin 1
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── commands/                 # 13 slash commands
│   ├── skills/                   # 17 A-grade skills
│   ├── lib/                      # Shell API wrappers
│   ├── scripts/                  # Install/uninstall
│   ├── package.json
│   └── README.md
├── rforge-orchestrator/           # Plugin 2 (future)
├── shared/                        # Shared utilities
│   ├── test-utils/
│   ├── lint-config/
│   └── templates/
│       ├── plugin-template/      # Template for new plugins
│       ├── command-template.md
│       └── skill-template.md
├── docs/                          # Repository documentation
│   ├── GETTING-STARTED.md
│   ├── PLUGIN-DEVELOPMENT.md
│   ├── PUBLISHING.md
│   └── TESTING.md
├── scripts/                       # Repository-level scripts
│   ├── create-plugin.sh          # Scaffold new plugin
│   ├── validate-plugin.sh        # Validate plugin structure
│   └── publish-plugin.sh         # Publish to npm
├── KNOWLEDGE.md                   # Architecture knowledge base
├── README.md                      # This file
├── LICENSE                        # MIT License
├── .gitignore
└── package.json                   # Root package (workspaces)
```

---

## 🔧 Development

### Prerequisites

- Claude Code (latest version)
- Node.js 18+
- Git

### Clone and Setup

```bash
# Clone repository
git clone https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins

# Install dependencies (if using workspaces)
npm install

# Install a plugin in development mode
cd statistical-research
./scripts/install.sh --dev
```

### Create New Plugin

```bash
# Use plugin template
./scripts/create-plugin.sh my-plugin

# Creates:
# my-plugin/
# ├── commands/
# ├── skills/
# ├── lib/
# ├── scripts/
# ├── package.json
# └── README.md
```

### Test Changes

```bash
# Test specific plugin
cd statistical-research
npm test

# Validate plugin structure
./scripts/validate-plugin.sh statistical-research

# Test all plugins (from root)
npm test
```

---

## 📖 Plugin Standards

All plugins in this monorepo follow consistent standards:

### Naming Convention

- **Directory:** `kebab-case` (e.g., `statistical-research`)
- **npm package:** `@data-wise/<plugin-name>-plugin`
- **Commands:** `/namespace:command` (e.g., `/research:arxiv`)

### Required Files

Each plugin must have:
- ✅ `package.json` - npm configuration
- ✅ `README.md` - Plugin documentation
- ✅ `.claude-plugin/plugin.json` - Plugin metadata
- ✅ `scripts/install.sh` - Installation script
- ✅ `scripts/uninstall.sh` - Uninstallation script
- ✅ `LICENSE` - MIT license

### Directory Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required
├── commands/                  # Slash commands (optional)
├── skills/                    # Skills (optional)
├── lib/                       # Utilities (optional)
├── scripts/
│   ├── install.sh            # Required
│   └── uninstall.sh          # Required
├── tests/                     # Tests (recommended)
├── package.json              # Required
├── README.md                 # Required
└── LICENSE                   # Required (MIT)
```

### Quality Standards

- **Documentation:** Comprehensive README with examples
- **Installation:** Works in both dev (symlink) and prod (copy) mode
- **Testing:** Automated tests for critical functionality
- **Licensing:** MIT license for all plugins
- **Versioning:** Semantic versioning (semver)

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Follow plugin standards (see [PLUGIN-DEVELOPMENT.md](docs/PLUGIN-DEVELOPMENT.md))
4. Add tests for new functionality
5. Update documentation
6. Commit changes (`git commit -m 'feat: add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Open Pull Request

### Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(plugin-name): add new feature
fix(plugin-name): fix bug
docs(plugin-name): update documentation
test(plugin-name): add tests
chore: update dependencies
```

---

## 📜 License

MIT License - see [LICENSE](LICENSE) file

All plugins in this monorepo are licensed under MIT unless otherwise specified.

---

## 🏆 Plugin Quality Badges

Plugins that meet quality standards earn badges:

- 🥇 **A-Grade** - Comprehensive documentation, tests, and examples
- 🥈 **B-Grade** - Good documentation and basic tests
- 🥉 **C-Grade** - Functional with minimal documentation

**Current Plugins:**
- 📊 Statistical Research: 🥇 A-Grade

---

## 📊 Statistics

- **Total Plugins:** 1 (more coming soon)
- **Total Commands:** 13
- **Total Skills:** 17
- **Contributors:** 1
- **License:** MIT

---

## 🔗 Links

- **GitHub:** https://github.com/Data-Wise/claude-plugins
- **npm Organization:** https://www.npmjs.com/org/data-wise
- **Issues:** https://github.com/Data-Wise/claude-plugins/issues
- **Discussions:** https://github.com/Data-Wise/claude-plugins/discussions

---

## 🗺️ Roadmap

### Short-term (Next Release)

- [ ] Publish `statistical-research` to npm
- [ ] Add GitHub Actions for testing
- [ ] Create plugin template
- [ ] Add automated validation

### Medium-term (Next Quarter)

- [ ] Add `rforge-orchestrator` plugin
- [ ] Create shared test utilities
- [ ] Add comprehensive examples
- [ ] Improve documentation

### Long-term (Next Year)

- [ ] 5+ plugins in monorepo
- [ ] Plugin marketplace/catalog
- [ ] Community contributions
- [ ] Plugin CLI tool

---

## 💡 Philosophy

This monorepo follows these principles:

1. **Quality over Quantity** - Each plugin is thoroughly documented and tested
2. **Consistency** - All plugins follow same standards and patterns
3. **Independence** - Plugins can be installed and used independently
4. **Discoverability** - One repo makes it easy to find all plugins
5. **Maintainability** - Shared tooling reduces duplication
6. **Community** - Open to contributions and feedback

---

## 🙏 Acknowledgments

Built with:
- [Claude Code](https://code.claude.com/) - AI-powered development
- [npm](https://www.npmjs.com/) - Package distribution
- [GitHub Actions](https://github.com/features/actions) - CI/CD

Inspired by the needs of statistical researchers, R developers, and AI-assisted workflow enthusiasts.

---

**Ready to explore?** Check out the [Statistical Research Plugin](statistical-research/) to get started!
