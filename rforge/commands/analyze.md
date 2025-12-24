---
name: rforge:analyze
description: Quick R package analysis with auto-delegation to RForge MCP tools
argument-hint: Optional context (e.g., "Update bootstrap algorithm")
---

# /rforge:analyze - Auto-Delegating R Package Analysis

Automatically analyze R package changes with intelligent tool delegation and parallel execution.

## Usage

```bash
# Quick analysis (< 30 seconds)
/rforge:analyze "Update RMediation bootstrap algorithm"

# With explicit package path
/rforge:analyze "Fix bug in ci_mediation" --package /path/to/RMediation

# Thorough analysis (2-5 minutes)
/rforge:analyze "Prepare for CRAN release" --thorough
```

## What It Does

1. **Auto-detects package** from current directory or git context
2. **Recognizes pattern** (code change, bug fix, new function, etc.)
3. **Selects appropriate tools** based on pattern
4. **Calls tools in parallel** for speed
5. **Shows live progress** as tools execute
6. **Synthesizes results** into actionable summary
7. **Suggests next steps** based on findings

## Output Example

```
🔍 Analyzing RMediation changes...
Pattern recognized: CODE_CHANGE
Delegating to 4 tools...

Analyzing...
[████████░░] Impact Analysis    80%
[██████████] Test Coverage     100% ✓
[██████░░░░] Documentation      70%
[████░░░░░░] Health Check       40%

✅ Analysis complete! (10.2 seconds)

🎯 IMPACT: MEDIUM
  • 2 packages affected (mediate, sensitivity)
  • Estimated cascade: 4 hours over 2 days
  • No breaking changes detected

✅ QUALITY: EXCELLENT
  • Tests: 187/187 passing (94% coverage)
  • CRAN: Clean, no warnings
  • CI: All platforms passing

📝 MAINTENANCE: 2 items
  • NEWS.md needs entry (auto-fixable)
  • Vignette example outdated (auto-fixable)

📋 RECOMMENDED NEXT STEPS:
  1. Implement bootstrap algorithm changes (3 hours)
  2. Auto-fix documentation (run /rforge:autofix)
  3. Run cascade plan for dependent packages
  4. Estimated total: 5 hours over 2 days

What would you like to do next?
[1] Generate detailed implementation plan
[2] Auto-fix documentation
[3] Show cascade sequence
[4] Something else
```

## Pattern Recognition

The skill automatically detects what you're doing:

| Your Request | Pattern Detected | Tools Used |
|--------------|------------------|------------|
| "Update algorithm" | CODE_CHANGE | impact, tests, docs, health |
| "Add new function" | NEW_FUNCTION | detect, tests, docs |
| "Fix bug in..." | BUG_FIX | tests, impact |
| "Update vignette" | DOCUMENTATION | docs, detect |
| "Prepare for CRAN" | RELEASE | health, impact, tests, docs |

## Options

- `--package <path>` - Explicit package path (otherwise auto-detected)
- `--thorough` - Use background R analysis (slower but comprehensive)
- `--quick` - Fast mode only (< 30 sec, default)
- `--no-progress` - Skip progress display
- `--json` - Output raw JSON instead of formatted summary

## Requirements

- RForge MCP server must be installed and configured
- R environment with required packages (devtools, testthat, covr)
- Must be in or specify path to an R package

## Quick Setup

If RForge MCP not configured:

```bash
npx rforge-mcp configure
```

Then restart Claude Code.

## Tools Delegated To

**Quick Analysis (Default):**
- `rforge_quick_impact` - Dependency impact (5-8 sec)
- `rforge_quick_tests` - Test status (3-5 sec)
- `rforge_quick_docs` - Documentation check (2-3 sec)
- `rforge_quick_health` - Overall health (5-7 sec)

**Thorough Analysis (--thorough):**
- `rforge_launch_analysis` - Full R CMD check (2-5 min)
- Background coverage analysis
- Performance benchmarks

## ADHD-Friendly Features

✅ **Fast feedback** - Results in < 30 seconds
✅ **Live progress** - See what's happening
✅ **Clear structure** - Consistent output format
✅ **Actionable** - Always suggests next steps
✅ **Interruptible** - Can cancel anytime (Ctrl+C)
✅ **Scannable** - Emojis, headers, bullets

## Examples

### Example 1: Code Change

```bash
/rforge:analyze "Update mediation formula in RMediation"

# Output:
# CODE_CHANGE pattern detected
# Tools: impact (3 packages), tests (passing), docs (outdated)
# Next: Update formula, fix docs, cascade to dependents
```

### Example 2: Bug Fix

```bash
/rforge:analyze "Fix NA handling in ci_mediation"

# Output:
# BUG_FIX pattern detected
# Tools: tests (2 failures found!), impact (low)
# Next: Fix NA check, run failing tests, verify
```

### Example 3: Release Prep

```bash
/rforge:analyze "Ready to release RMediation 2.1.0" --thorough

# Output:
# RELEASE pattern detected
# Background R analysis running...
# Health: 95/100, Tests: all pass, Docs: complete
# Next: Version bump, NEWS update, CRAN submit
```

## Troubleshooting

**"Package not found"**
- Run from package directory, or use `--package /path`
- Verify DESCRIPTION file exists

**"RForge MCP not available"**
- Install: `npx rforge-mcp configure`
- Restart Claude Code

**"Analysis too slow"**
- Use `--quick` mode (skips background R)
- Or wait for background analysis to complete

## Related Skills

- `/rforge:quick` - Ultra-fast analysis only
- `/rforge:thorough` - Deep analysis with background R
- `/rforge:plan` - Generate implementation plan
- `/rforge:cascade` - Cascade dependency updates
- `/rforge:autofix` - Auto-fix documentation issues

## How It Works

1. **Pattern matching** - Analyzes your request text
2. **Context detection** - Finds package via git/filesystem
3. **Tool selection** - Picks relevant RForge MCP tools
4. **Parallel execution** - Calls all tools simultaneously
5. **Progress monitoring** - Updates display in real-time
6. **Result synthesis** - Combines outputs coherently
7. **Next steps** - Generates actionable recommendations

All orchestration happens in Claude - the MCP tools just provide fast analysis. This hybrid approach is fast, flexible, and ADHD-friendly.

---

**Pro tip:** After analysis, the orchestrator remembers context. You can follow up with:
- "Generate the plan"
- "Fix the documentation"
- "Show me the cascade sequence"
- "What should I do first?"
