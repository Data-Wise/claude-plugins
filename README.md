# ⚠️ ARCHIVED: Claude Code Plugins Monorepo

> **This repository has been archived** as of January 9, 2026.
> All plugins have been moved to independent repositories.

[![Archived](https://img.shields.io/badge/status-archived-red.svg)](https://github.com/Data-Wise/claude-plugins)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🔀 Migration Complete

The three active plugins from this monorepo have been extracted into standalone repositories for easier maintenance and independent development:

### ✅ Active Standalone Repositories

| Plugin | Repository | Status | Install |
|--------|------------|--------|---------|
| **Scholar** | [github.com/Data-Wise/scholar](https://github.com/Data-Wise/scholar) | ✅ Active | `brew install scholar` |
| **Craft** | [github.com/Data-Wise/craft](https://github.com/Data-Wise/craft) | ✅ Active | `brew install craft` |
| **RForge** | [github.com/Data-Wise/rforge](https://github.com/Data-Wise/rforge) | ✅ Active | `brew install rforge` |

---

## 📚 Scholar Plugin

**Academic workflows for research and teaching**

- **Repository:** https://github.com/Data-Wise/scholar
- **Documentation:** https://data-wise.github.io/scholar/
- **npm:** `@data-wise/scholar`
- **Commands:** 21 (14 research + 7 teaching)
- **Skills:** 17 A-grade skills

**Features:**
- Literature management (arXiv, DOI, BibTeX)
- Manuscript writing assistance
- Simulation study design
- Course material generation (syllabi, assignments, exams)

**Install:**
```bash
brew tap data-wise/tap
brew install scholar
```

---

## 🛠️ Craft Plugin

**Full-stack developer toolkit with workflow automation**

- **Repository:** https://github.com/Data-Wise/craft
- **Documentation:** https://data-wise.github.io/craft/
- **npm:** `@data-wise/claude-craft-plugin`
- **Commands:** 86 (74 craft + 12 workflow)
- **Agents:** 8 (including orchestrator-v2)
- **Skills:** 21

**Features:**
- Architecture & code generation
- Testing & CI/CD automation
- Documentation & site generation
- Git workflows & distribution
- ADHD-friendly task management
- Multi-agent orchestration

**Install:**
```bash
brew tap data-wise/tap
brew install craft
```

---

## 📊 RForge Plugin

**R package ecosystem orchestrator**

- **Repository:** https://github.com/Data-Wise/rforge
- **Documentation:** https://data-wise.github.io/rforge/
- **npm:** `@data-wise/rforge-plugin`
- **Commands:** 15
- **MCP Integration:** Requires `rforge-mcp` server

**Features:**
- Auto-detect R project structure (single package, ecosystem, hybrid)
- Dependency analysis and cascade planning
- Mode system (default, debug, optimize, release)
- Health checks and CRAN readiness

**Install:**
```bash
brew tap data-wise/tap
brew install rforge
npm install -g rforge-mcp  # MCP server dependency
```

---

## 🕰️ Archive Reason

This monorepo was originally created to share common tooling and standards across multiple Claude Code plugins. However, as each plugin evolved independently with different:
- Release cycles
- Dependencies (some with MCP, some pure plugins)
- Documentation needs
- User bases

It became clearer that standalone repositories would provide:
- ✅ Easier contribution and maintenance
- ✅ Independent version control
- ✅ Clearer ownership and focus
- ✅ Simpler CI/CD pipelines
- ✅ Better discoverability

All git history has been preserved in each standalone repository using `git filter-branch`.

---

## 📖 Historical Documentation

The original monorepo documentation is still available:
- **KNOWLEDGE.md** - Architecture and design patterns
- **CLAUDE.md** - Development guide
- **docs/** - Archived documentation

However, please refer to the individual plugin repositories for current documentation.

---

## 🚀 For Users

If you previously installed plugins from this monorepo:

### Migration Steps

1. **Uninstall old plugins:**
   ```bash
   rm -rf ~/.claude/plugins/statistical-research
   rm -rf ~/.claude/plugins/craft
   rm -rf ~/.claude/plugins/rforge-orchestrator
   ```

2. **Install new standalone versions:**
   ```bash
   brew tap data-wise/tap
   brew install scholar  # Replaces statistical-research
   brew install craft
   brew install rforge   # Replaces rforge-orchestrator
   ```

3. **No breaking changes** - All commands remain the same!

---

## 🤝 Contributing

Please contribute to the individual plugin repositories:
- Scholar issues: https://github.com/Data-Wise/scholar/issues
- Craft issues: https://github.com/Data-Wise/craft/issues
- RForge issues: https://github.com/Data-Wise/rforge/issues

---

## 📜 License

MIT License - see individual plugin repositories for details.

---

## 🙏 Acknowledgments

Thank you to all contributors who helped build this monorepo! Your work continues in the standalone repositories.

**Archive Date:** January 9, 2026
**Last Active Version:** See individual plugin repositories
**Maintained By:** Data-Wise
