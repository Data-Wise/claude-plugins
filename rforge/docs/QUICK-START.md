# RForge Orchestrator Plugin - Quick Start

> **Get up and running in 3 minutes**

---

## Install (1 minute)

```bash
brew install data-wise/tap/rforge-orchestrator
```

**Done!** The plugin is automatically installed to `~/.claude/plugins/rforge-orchestrator`.

---

## Prerequisites

**Required:**
1. ✅ Claude Code CLI installed
2. ✅ RForge MCP server configured in `~/.claude/settings.json`
3. ✅ Working in an R package directory (has `DESCRIPTION` file)

**Check RForge MCP:**
```json
// ~/.claude/settings.json
{
  "mcpServers": {
    "rforge-mcp": {
      "command": "node",
      "args": ["/path/to/rforge-mcp/dist/index.js"]
    }
  }
}
```

---

## First Commands (1 minute)

### 1. Quick Health Check

```
/rforge:quick
```

**What it does:** Runs a fast (~10 sec) health check of your R package.

**Use:** Pre-commit checks, daily development.

### 2. Analyze Recent Changes

```
/rforge:analyze "Updated bootstrap algorithm"
```

**What it does:** Analyzes impact of your changes, runs tests, checks docs (~30 sec).

**Use:** After making code changes.

### 3. Prepare for Release

```
/rforge:thorough "CRAN submission"
```

**What it does:** Comprehensive analysis with all tools (2-5 min).

**Use:** Before CRAN releases, major milestones.

---

## The 3 Commands

| Command | Speed | When to Use |
|---------|-------|-------------|
| `/rforge:quick` | ~10s | Pre-commit, quick status |
| `/rforge:analyze` | ~30s | After changes, understand impact |
| `/rforge:thorough` | 2-5m | Release prep, comprehensive check |

---

## How It Works

```
Your Request
    ↓
Pattern Recognition (CODE_CHANGE, BUG_FIX, RELEASE_PREP, etc.)
    ↓
Tool Selection (impact, tests, docs, health, rdoc)
    ↓
Parallel Execution (4 tools in 8 sec, not 32 sec!)
    ↓
Results Synthesis
    ↓
Actionable Summary
```

**Key Innovation:** Parallel execution makes it fast!

---

## Common Workflows

### Daily Development

```bash
# 1. Make code changes
vim R/function.R

# 2. Quick check
/rforge:quick

# 3. Fix any issues

# 4. Commit
git commit
```

### After Feature Development

```bash
# 1. Implement feature

# 2. Analyze impact
/rforge:analyze "Added new plotting function"

# 3. Review results:
#    - Impact on existing code
#    - Test coverage
#    - Documentation needs

# 4. Address recommendations

# 5. Quick verify
/rforge:quick
```

### Before CRAN Release

```bash
# 1. Comprehensive check
/rforge:thorough "Prepare v2.0.0 for CRAN"

# 2. Review all recommendations

# 3. Fix all issues

# 4. Run R CMD check

# 5. Submit to CRAN
```

---

## Pattern Recognition

The orchestrator automatically detects what you're doing:

**"update algorithm"** → CODE_CHANGE pattern → Calls: impact, tests, docs

**"fix bug"** → BUG_FIX pattern → Calls: impact, tests

**"CRAN release"** → RELEASE_PREP pattern → Calls: all tools

**"quick status"** → HEALTH_CHECK pattern → Calls: health (minimal)

---

## Tips for Best Results

1. **Describe tasks clearly**
   - Good: `/rforge:analyze "Updated bootstrap algorithm in mediate()"`
   - Less good: `/rforge:analyze "changed code"`

2. **Use right command for context**
   - Pre-commit → `/rforge:quick`
   - After changes → `/rforge:analyze`
   - Before release → `/rforge:thorough`

3. **Must be in R package directory**
   - Needs `DESCRIPTION` file
   - Run from package root

4. **Parallel execution is automatic**
   - No configuration needed
   - Much faster than sequential tool calls

---

## What's Next?

- **Full command reference:** See `docs/REFCARD.md`
- **Homebrew formula:** `brew info rforge-orchestrator`
- **Plugin source:** https://github.com/Data-Wise/claude-plugins
- **GitHub release:** https://github.com/Data-Wise/claude-plugins/releases/tag/rforge-orchestrator-v0.1.0

---

## Uninstall

```bash
brew uninstall rforge-orchestrator
```

---

## Troubleshooting

**Commands not showing?**
- Restart Claude Code
- Check: `ls ~/.claude/plugins/rforge-orchestrator`

**"RForge MCP not configured"?**
- Add `rforge-mcp` to `~/.claude/settings.json`
- Restart Claude Code

**Slow performance?**
- Check RForge MCP server is running: `ps aux | grep rforge-mcp`
- Test MCP directly: Use Claude Desktop to verify MCP works

**Not in R package?**
- Must have `DESCRIPTION` file
- Run from package root directory

---

## Example Session

```bash
# In your R package directory
cd ~/projects/r-packages/mypackage

# Quick check before starting work
/rforge:quick
# → ✅ Package healthy, 95% test coverage

# Make changes
vim R/bootstrap.R

# Analyze impact
/rforge:analyze "Updated bootstrap algorithm for better performance"
# → Impact: Modified 1 function, affects 3 others
# → Tests: All pass, coverage maintained
# → Docs: Update help file for bootstrap_se()

# Fix documentation
vim man/bootstrap_se.Rd

# Quick verify
/rforge:quick
# → ✅ All clear!

# Commit
git commit -m "feat: improve bootstrap algorithm performance"
```

---

**You're ready!** Try `/rforge:quick` in your R package directory to get started.
