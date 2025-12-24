# RForge Orchestrator Plugin - Reference Card

> **Version:** 0.1.0 | **Last Updated:** 2025-12-23

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  RFORGE ORCHESTRATOR REFERENCE                                     v0.1.0  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  COMMANDS (3)                                                               │
│  ─────────                                                                  │
│                                                                             │
│  /rforge:analyze [task]           Balanced analysis (~30 sec)              │
│    Auto-detects patterns, delegates to RForge MCP, synthesizes results     │
│    Example: /rforge:analyze "Update bootstrap algorithm"                   │
│                                                                             │
│  /rforge:quick                    Ultra-fast check (~10 sec)               │
│    Quick health check with minimal tool calls                              │
│    Use: Pre-commit checks, quick status                                    │
│                                                                             │
│  /rforge:thorough [milestone]     Comprehensive review (2-5 min)           │
│    Full analysis with all tools, detailed recommendations                  │
│    Example: /rforge:thorough "Prepare for CRAN release"                    │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  HOW IT WORKS                                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Pattern Recognition → Analyzes your task description                   │
│     • CODE_CHANGE - Code modifications                                     │
│     • BUG_FIX - Bug fixes                                                  │
│     • RELEASE_PREP - Release preparation                                   │
│     • HEALTH_CHECK - Quick status check                                    │
│     • FEATURE_ADD - New features                                           │
│                                                                             │
│  2. Tool Selection → Picks appropriate RForge MCP tools                     │
│     • impact - Code change impact analysis                                 │
│     • tests - Test coverage and execution                                  │
│     • docs - Documentation completeness                                    │
│     • health - Package health check                                        │
│     • rdoc - R documentation check                                         │
│                                                                             │
│  3. Parallel Execution → Calls multiple tools simultaneously               │
│     ⚡ 4 tools × 8 sec each = 8 sec total (not 32 sec!)                     │
│                                                                             │
│  4. Results Synthesis → Combines into actionable summary                   │
│     • Impact assessment                                                    │
│     • Quality metrics                                                      │
│     • Maintenance concerns                                                 │
│     • Next steps                                                           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  COMMON WORKFLOWS                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  After Code Changes              │  Before Commit                          │
│  1. Make changes                 │  1. /rforge:quick                       │
│  2. /rforge:analyze "what changed"│  2. Fix any issues                      │
│  3. Review impact + next steps   │  3. git commit                          │
│  4. Run suggested checks         │                                         │
│                                  │  Release Preparation                    │
│  Feature Development             │  1. /rforge:thorough "CRAN release"     │
│  1. /rforge:analyze "add feature"│  2. Address all recommendations         │
│  2. Check impact on tests/docs   │  3. Run R CMD check                     │
│  3. Update based on suggestions  │  4. Submit to CRAN                      │
│  4. /rforge:quick (verify)       │                                         │
│                                  │                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  REQUIREMENTS                                                               │
│  • Claude Code CLI installed                                               │
│  • RForge MCP server configured in ~/.claude/settings.json                 │
│  • R package project (DESCRIPTION file required)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  TIPS                                                                       │
│  • Use /rforge:quick for pre-commit checks - it's fast!                     │
│  • /rforge:analyze is best for understanding impact of changes              │
│  • /rforge:thorough before CRAN submission finds issues early               │
│  • Orchestrator runs tools in parallel - much faster than sequential        │
│  • Pattern recognition improves - describe tasks clearly for best results   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Quick Command Reference

| Command | Speed | When to Use | Output |
|---------|-------|-------------|--------|
| `/rforge:quick` | ~10s | Pre-commit, quick status | Basic health check |
| `/rforge:analyze` | ~30s | After changes, understand impact | Impact + recommendations |
| `/rforge:thorough` | 2-5m | Release prep, major changes | Comprehensive analysis |

---

## Pattern Recognition

The orchestrator automatically detects task types:

| Pattern | Triggers When... | Tools Called |
|---------|------------------|--------------|
| **CODE_CHANGE** | "update", "modify", "change code" | impact, tests, docs |
| **BUG_FIX** | "fix", "bug", "error" | impact, tests |
| **RELEASE_PREP** | "release", "CRAN", "publish" | health, tests, docs, rdoc |
| **HEALTH_CHECK** | "check", "status", "quick" | health |
| **FEATURE_ADD** | "add feature", "new function" | impact, tests, docs |

---

## RForge MCP Tools

Tools the orchestrator can delegate to:

| Tool | Purpose | Speed |
|------|---------|-------|
| `impact` | Analyze code change impact | ~8s |
| `tests` | Run and analyze tests | ~10s |
| `docs` | Check documentation completeness | ~8s |
| `health` | Package health metrics | ~8s |
| `rdoc` | R documentation validation | ~8s |

---

## Installation

**Homebrew (Recommended):**

```bash
brew install data-wise/tap/rforge-orchestrator
```

**Manual:**

```bash
cd ~/.claude/plugins
git clone https://github.com/Data-Wise/claude-plugins.git temp
mv temp/rforge-orchestrator .
rm -rf temp
```

**Uninstall:**

```bash
brew uninstall rforge-orchestrator
# or manually: rm -rf ~/.claude/plugins/rforge-orchestrator
```

---

## Configuration

RForge MCP server must be configured in `~/.claude/settings.json`:

```json
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

## File Structure

```
rforge-orchestrator/
├── commands/              # 3 slash commands
│   ├── analyze.md
│   ├── quick.md
│   └── thorough.md
├── agents/                # 1 orchestrator agent
│   └── orchestrator.md
├── scripts/               # Installation scripts
│   ├── install.sh
│   └── uninstall.sh
└── docs/                  # Documentation
    └── REFCARD.md (this file)
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Commands not showing | Restart Claude Code, check `~/.claude/plugins/` |
| "RForge MCP not configured" | Add rforge-mcp to settings.json |
| Slow performance | Check RForge MCP server is running |
| Pattern not recognized | Use clearer task description |
| No R package found | Must be in R package directory (has DESCRIPTION) |

---

## Examples

### After Code Changes
```
/rforge:analyze "Updated bootstrap algorithm in mediate() function"

→ Pattern: CODE_CHANGE
→ Tools: impact, tests, docs
→ Result: Impact assessment + test status + doc updates needed
```

### Quick Pre-commit Check
```
/rforge:quick

→ Pattern: HEALTH_CHECK
→ Tools: health (minimal)
→ Result: Quick health status + blocking issues
```

### Before CRAN Release
```
/rforge:thorough "Prepare v2.0.0 for CRAN submission"

→ Pattern: RELEASE_PREP
→ Tools: health, tests, docs, rdoc (all tools)
→ Result: Comprehensive checklist + recommendations
```

---

## More Documentation

- **Main README:** `README.md`
- **Installation Guide:** Homebrew formula includes full guide
- **Plugin Repository:** https://github.com/Data-Wise/claude-plugins
- **GitHub Release:** https://github.com/Data-Wise/claude-plugins/releases/tag/rforge-orchestrator-v0.1.0

---

## Comparison: When to Use Each Command

| Situation | Use | Why |
|-----------|-----|-----|
| Made small code change | `/rforge:analyze` | Understand impact |
| About to commit | `/rforge:quick` | Fast sanity check |
| Preparing release | `/rforge:thorough` | Catch everything |
| Testing new feature | `/rforge:analyze` | Check tests/docs |
| Fixing bug | `/rforge:analyze` | Verify fix, check tests |
| Daily development | `/rforge:quick` | Regular health checks |

---

**Quick Start:** `/rforge:quick` → Get instant health check of your R package!
