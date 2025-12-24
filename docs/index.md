# Claude Code Plugins

**Professional plugins for Claude Code CLI** - Enhance your AI-assisted development workflow with specialized tools for R packages, statistical research, and ADHD-friendly workflows.

---

## 🎯 Available Plugins

### [RForge Orchestrator](https://github.com/Data-Wise/claude-plugins/tree/main/rforge-orchestrator)

**Auto-delegation orchestrator for R package development**

- **3 commands** - Quick, balanced, and comprehensive analysis modes
- **Intelligent delegation** - Automatically selects appropriate RForge MCP tools
- **Fast feedback** - Results in 10 seconds to 5 minutes depending on mode
- **ADHD-friendly** - Clear progress, actionable results

**Key Commands:**
- `/rforge:quick` - Ultra-fast analysis (< 10 seconds)
- `/rforge:analyze` - Balanced analysis with auto-delegation (< 30 seconds)
- `/rforge:thorough` - Comprehensive analysis with background R processes (2-5 minutes)

---

### [Statistical Research](https://github.com/Data-Wise/claude-plugins/tree/main/statistical-research)

**Research workflow automation for statistical methods development**

- **13 commands** - Literature search, manuscript writing, simulation design
- **17 A-grade skills** - Mathematical foundations, implementation, writing, research
- **MCP integration** - Connects to arXiv, Zotero, R environment
- **Publication-ready** - Methods papers, proofs, reviewer responses

**Command Categories:**
- **Literature** - arXiv search, DOI lookup, BibTeX management
- **Manuscript** - Methods sections, results, reviewer responses, proofs
- **Simulation** - Study design, analysis planning
- **Research** - Literature gaps, hypothesis formulation, analysis plans

---

### [Workflow](https://github.com/Data-Wise/claude-plugins/tree/main/workflow)

**ADHD-friendly workflow automation with intelligent delegation**

- **Enhanced brainstorming** - Smart context detection and mode selection
- **Auto-delegation** - Automatically delegates to specialized agents
- **Structured output** - Clear options, next steps, trade-offs
- **Design modes** - Technical, creative, user-focused, system-wide

**Key Features:**
- Context-aware brainstorming
- Automatic agent delegation (backend, frontend, DevOps, etc.)
- ADHD-friendly output formatting
- Interactive decision support

---

## 📚 Documentation

### Quick Links

- **[Command Reference](COMMAND-REFERENCE.md)** - Complete reference of all 17 commands
- **[Architecture](diagrams/ECOSYSTEM.md)** - System architecture and diagrams
- **[Development](https://github.com/Data-Wise/claude-plugins/tree/main/scripts)** - Scripts for plugin development

### Getting Started

1. **Installation**
   ```bash
   # Clone repository
   git clone https://github.com/Data-Wise/claude-plugins.git
   cd claude-plugins

   # Install a plugin
   ./scripts/install-plugin.sh rforge-orchestrator
   ```

2. **Restart Claude Code**
   - Commands won't appear until you restart

3. **Use Commands**
   ```bash
   /rforge:quick
   /research:arxiv "mediation analysis"
   /brainstorm "API design"
   ```

### Architecture

- **[Ecosystem Diagram](diagrams/ECOSYSTEM.md)** - How plugins interact
- **[Dependencies](diagrams/DEPENDENCIES.md)** - Plugin requirements
- **Plugin Structures** - [RForge](diagrams/rforge-orchestrator-structure.md) | [Research](diagrams/statistical-research-structure.md) | [Workflow](diagrams/workflow-structure.md)
- **Command Flows** - [RForge](diagrams/rforge-orchestrator-flow.md) | [Research](diagrams/statistical-research-flow.md) | [Workflow](diagrams/workflow-flow.md)

---

## 🚀 Features

### Automated Quality Assurance

- ✅ **CI/CD validation** - GitHub Actions validate every commit
- ✅ **Pre-commit hooks** - Catch issues before commit
- ✅ **Comprehensive tests** - Structure, JSON, frontmatter validation
- ✅ **Auto-generated docs** - Documentation always up-to-date

### Developer Experience

- ✅ **One-command installation** - `./scripts/install-plugin.sh <name>`
- ✅ **Fast validation** - `python3 scripts/validate-all-plugins.py` (< 5 sec)
- ✅ **Auto-backups** - Existing installations backed up before reinstall
- ✅ **Clear errors** - Actionable error messages with solutions

### Documentation

- ✅ **Auto-generated** - Command reference from frontmatter
- ✅ **Architecture diagrams** - Mermaid diagrams from structure
- ✅ **Always current** - Regenerates in 5 seconds
- ✅ **Professional** - Material theme, search, navigation

---

## 📊 Stats

| Metric | Count |
|--------|-------|
| **Plugins** | 3 |
| **Commands** | 17 |
| **Skills** | 17 (research only) |
| **MCP Servers** | 2 |
| **Architecture Diagrams** | 8 |
| **Validation Time** | < 5 seconds |
| **Doc Generation Time** | ~5 seconds |

---

## 🛠️ Development

### For Plugin Developers

```bash
# Validate all plugins
python3 scripts/validate-all-plugins.py

# Generate documentation
./scripts/generate-docs.sh

# Install locally for testing
./scripts/install-plugin.sh <plugin-name> --force
```

### For Contributors

1. Fork the repository
2. Install pre-commit hooks: `pre-commit install`
3. Make changes
4. Run validation: `python3 scripts/validate-all-plugins.py`
5. Submit PR (CI/CD will validate)

### Documentation

- **[Scripts Guide](https://github.com/Data-Wise/claude-plugins/tree/main/scripts)** - Development tools documentation
- **[Validation Report](https://github.com/Data-Wise/claude-plugins/blob/main/PLUGIN-VALIDATION-REPORT.md)** - Plugin validation results
- **[DevOps Guide](https://github.com/Data-Wise/claude-plugins/blob/main/DEVOPS-IMPLEMENTATION-COMPLETE.md)** - CI/CD infrastructure
- **[Docs Automation](https://github.com/Data-Wise/claude-plugins/blob/main/DOCS-AUTOMATION-COMPLETE.md)** - Documentation system

---

## 🔗 Links

- **GitHub Repository:** [Data-Wise/claude-plugins](https://github.com/Data-Wise/claude-plugins)
- **Documentation:** [data-wise.github.io/claude-plugins](https://data-wise.github.io/claude-plugins/)
- **Issues:** [GitHub Issues](https://github.com/Data-Wise/claude-plugins/issues)

---

## 📝 License

MIT License - See [LICENSE](https://github.com/Data-Wise/claude-plugins/blob/main/LICENSE) for details

---

## 🙏 Credits

**Author:** Data-Wise
**Maintained by:** DT
**Built for:** Claude Code CLI users

---

**Last updated:** Auto-generated from repository code
**Documentation version:** Synchronized with main branch
