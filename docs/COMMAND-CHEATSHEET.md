# Command Cheatsheet with Mode System

**Quick reference for all RForge commands with mode and format options**

---

## Mode System Quick Start

### Mode Syntax

```bash
/command                          # Default mode (fast, < 10s)
/command --mode debug             # Debug mode (detailed, < 2m)
/command --mode optimize          # Optimize mode (performance, < 3m)
/command --mode release           # Release mode (comprehensive, < 5m)
```

### Format Syntax

```bash
/command                          # Terminal format (default)
/command --format json            # JSON output (automation)
/command --format markdown        # Markdown output (reports)
```

### Combined Syntax

```bash
/command --mode debug --format json
/command --mode release --format markdown
```

---

## Mode Comparison Table

| Mode | Time | Purpose | Commands Supporting Modes |
|------|------|---------|----------------------------|
| **default** | < 10s | Daily checks, quick status | All commands |
| **debug** | < 2m | Troubleshooting, investigation | `/rforge:analyze`, `/rforge:status` |
| **optimize** | < 3m | Performance analysis | `/rforge:analyze`, `/rforge:status` |
| **release** | < 5m | CRAN validation, pre-release | `/rforge:analyze`, `/rforge:status` |

**Note:** Most commands use default mode. Only `/rforge:analyze` and `/rforge:status` support all four modes.

---

## RForge Commands (13 total)

### Analysis Commands

| Command | Default Time | Modes | Description |
|---------|--------------|-------|-------------|
| `/rforge:quick` | < 10s | None | Ultra-fast analysis (always fast, no modes) |
| `/rforge:analyze` | < 10s | All 4 | Balanced analysis with auto-delegation |
| `/rforge:status` | 2-5s | All 4 | Ecosystem status dashboard |
| `/rforge:thorough` | 2-5m | None | Comprehensive analysis (deprecated - use `/rforge:analyze --mode release`) |

**Mode Support Details:**

#### `/rforge:quick` ⚡
```bash
/rforge:quick                     # Always < 10s, no mode support
```
- **Purpose:** Instant status check
- **Time:** < 10 seconds (fixed)
- **Modes:** None (ignores --mode flag)

#### `/rforge:analyze` 🔍
```bash
/rforge:analyze                   # Default: < 10s
/rforge:analyze --mode debug      # Debug: < 2m
/rforge:analyze --mode optimize   # Optimize: < 3m
/rforge:analyze --mode release    # Release: < 5m
```
- **Purpose:** Main analysis command
- **Modes:** All 4 supported
- **Formats:** terminal, json, markdown

#### `/rforge:status` 📊
```bash
/rforge:status                    # Default: 2-5s
/rforge:status --mode debug       # Debug: 15-30s
/rforge:status --mode optimize    # Optimize: 30s-1m
/rforge:status --mode release     # Release: 1-2m
```
- **Purpose:** Status dashboard
- **Modes:** All 4 supported
- **Formats:** terminal, json, markdown

#### `/rforge:thorough` 🏗️
```bash
/rforge:thorough                  # Always 2-5m (deprecated)
```
- **Purpose:** Comprehensive analysis
- **Time:** 2-5 minutes (fixed)
- **Modes:** None (deprecated - use `/rforge:analyze --mode release` instead)

---

### Ecosystem Commands

| Command | Time | Modes | Description |
|---------|------|-------|-------------|
| `/rforge:detect` | < 5s | Default only | Auto-detect project structure |
| `/rforge:deps` | 5-10s | Default only | Build dependency graph |
| `/rforge:impact` | 10-30s | Default only | Analyze change impact |
| `/rforge:cascade` | 15-45s | Default only | Plan coordinated updates |

**Examples:**
```bash
/rforge:detect                    # Auto-detect ecosystem
/rforge:deps                      # Visualize dependencies
/rforge:impact "API change"       # Analyze impact
/rforge:cascade "v2.1.0"          # Plan cascade updates
```

---

### Task Management Commands

| Command | Time | Modes | Description |
|---------|------|-------|-------------|
| `/rforge:capture` | < 2s | Default only | Quick capture ideas |
| `/rforge:next` | 2-5s | Default only | Get next task |
| `/rforge:complete` | 2-10s | Default only | Mark task complete |

**Examples:**
```bash
/rforge:capture "Add sensitivity analysis"
/rforge:next
/rforge:complete "Fix bootstrap bug"
```

---

### Release Commands

| Command | Time | Modes | Description |
|---------|------|-------|-------------|
| `/rforge:release` | 30s-2m | Default only | Plan CRAN submission |
| `/rforge:doc-check` | 10-20s | Default only | Check documentation |

**Examples:**
```bash
/rforge:release "v2.1.0"
/rforge:doc-check
```

---

## Mode-Specific Examples

### Default Mode (< 10s) - Daily Use

```bash
# Morning check-in
/rforge:status

# Before making changes
/rforge:analyze "Planning refactor"

# After commit
/rforge:analyze

# Quick dependency check
/rforge:deps
```

### Debug Mode (< 2m) - Troubleshooting

```bash
# Investigate test failures
/rforge:analyze --mode debug "Test failures"

# Detailed status with traces
/rforge:status --mode debug

# Debug with JSON output for logging
/rforge:analyze --mode debug --format json > debug.json
```

### Optimize Mode (< 3m) - Performance

```bash
# Analyze package performance
/rforge:analyze --mode optimize

# Get performance metrics
/rforge:status --mode optimize

# Export performance report
/rforge:analyze --mode optimize --format markdown > perf-report.md
```

### Release Mode (< 5m) - CRAN Submission

```bash
# Pre-release validation
/rforge:analyze --mode release

# Release readiness check
/rforge:status --mode release

# Generate release report
/rforge:analyze --mode release --format markdown > release-checklist.md

# CI/CD validation
/rforge:analyze --mode release --format json > validation.json
```

---

## Format Examples

### Terminal Format (Default)

```bash
/rforge:analyze
/rforge:status --mode debug
```

**Output:** Colorful, human-readable terminal output

---

### JSON Format (Automation)

```bash
# CI/CD pipeline
/rforge:analyze --mode release --format json > results.json

# Check health score
/rforge:status --format json | jq '.health_score'

# Nightly health log
/rforge:status --mode debug --format json >> health-log.jsonl

# Performance tracking
/rforge:analyze --mode optimize --format json | \
  jq '{date: now, load_time: .performance.load_time}' \
  >> performance.jsonl
```

---

### Markdown Format (Reports)

```bash
# Weekly status report
/rforge:status --mode debug --format markdown > weekly-report.md

# Release notes
/rforge:analyze --mode release --format markdown > RELEASE-NOTES.md

# Performance audit
/rforge:analyze --mode optimize --format markdown > performance-audit.md
```

---

## Workflow Patterns

### Pattern 1: Quick Iteration

```bash
# Fast checks between commits (5-10 seconds each)
/rforge:analyze
git commit -m "fix: bootstrap algorithm"
/rforge:analyze
git commit -m "docs: update README"
```

### Pattern 2: Deep Debugging

```bash
# Progressive investigation (total: ~2 minutes)
/rforge:status                         # 3s - Quick check
/rforge:analyze --mode debug           # 45s - Deep dive
# Fix issue
/rforge:analyze                        # 5s - Verify fix
```

### Pattern 3: Performance Work

```bash
# Performance optimization (total: ~4 minutes)
/rforge:status --mode optimize         # 45s - Baseline
# Optimize code
/rforge:analyze --mode optimize        # 90s - Re-analyze
# Compare results
/rforge:analyze --mode optimize --format json > after.json
```

### Pattern 4: Release Preparation

```bash
# Release workflow (total: ~10 minutes)
/rforge:analyze --mode release         # 3m - Initial check
# Fix issues
/rforge:analyze --mode release         # 3m - Verify
# Generate documentation
/rforge:analyze --mode release --format markdown > RELEASE.md
devtools::submit_cran()
```

---

## Statistical Research Commands (13 total)

### Literature Commands

| Command | Time | Description |
|---------|------|-------------|
| `/research:arxiv` | 5-15s | Search arXiv for papers |
| `/research:doi` | 2-5s | Look up paper by DOI |
| `/research:bib:search` | < 2s | Search BibTeX files |
| `/research:bib:add` | < 2s | Add BibTeX entry |

### Manuscript Commands

| Command | Time | Description |
|---------|------|-------------|
| `/research:manuscript:methods` | Variable | Write methods section |
| `/research:manuscript:results` | Variable | Write results section |
| `/research:manuscript:proof` | Variable | Review proofs |
| `/research:manuscript:reviewer` | Variable | Generate reviewer responses |

### Research Commands

| Command | Time | Description |
|---------|------|-------------|
| `/research:analysis-plan` | Variable | Create analysis plan |
| `/research:hypothesis` | Variable | Generate hypotheses |
| `/research:lit-gap` | Variable | Identify research gaps |

### Simulation Commands

| Command | Time | Description |
|---------|------|-------------|
| `/research:simulation:design` | Variable | Design simulation study |
| `/research:simulation:analysis` | Variable | Analyze simulation results |

**Note:** Statistical research commands don't support modes. They adapt based on context and user input.

---

## Workflow Commands (1 total)

| Command | Time | Description |
|---------|------|-------------|
| `/brainstorm` | Variable | Enhanced brainstorming with auto-delegation |

---

## Time Budget Summary

| Category | Range | Commands |
|----------|-------|----------|
| Instant | < 2s | `/rforge:capture` |
| Very Fast | 2-5s | `/rforge:status` (default), `/rforge:next`, `/rforge:detect` |
| Fast | 5-10s | `/rforge:analyze` (default), `/rforge:quick`, `/rforge:deps` |
| Medium | 10-30s | `/rforge:impact`, `/rforge:doc-check`, `/rforge:status` (debug) |
| Slow | 30s-2m | `/rforge:analyze` (debug), `/rforge:cascade`, `/rforge:release` |
| Very Slow | 2-5m | `/rforge:analyze` (release), `/rforge:thorough` |

---

## Mode Decision Tree

```
What do you need?
│
├─ Instant status? ──────────────────> /rforge:quick
│
├─ Quick check? ─────────────────────> /rforge:analyze
│
├─ Something broken? ────────────────> /rforge:analyze --mode debug
│
├─ Performance issue? ───────────────> /rforge:analyze --mode optimize
│
└─ CRAN submission? ─────────────────> /rforge:analyze --mode release
```

---

## Common Shortcuts (Aliases)

Add to your `.zshrc` or `.bashrc`:

```bash
# Quick commands
alias rf='/rforge:analyze'
alias rfs='/rforge:status'
alias rfq='/rforge:quick'

# Mode shortcuts
alias rfd='/rforge:analyze --mode debug'
alias rfo='/rforge:analyze --mode optimize'
alias rfr='/rforge:analyze --mode release'

# Format shortcuts
alias rfj='/rforge:analyze --format json'
alias rfm='/rforge:analyze --format markdown'

# Combined
alias rfrj='/rforge:analyze --mode release --format json'
alias rfrm='/rforge:analyze --mode release --format markdown'
```

**Usage:**
```bash
rf                  # Quick analyze
rfs                 # Quick status
rfd                 # Debug mode
rfr                 # Release mode
rfrj                # Release mode + JSON
```

---

## Best Practices

### ✅ DO

- Use default mode for 90% of daily work
- Switch to debug mode when troubleshooting
- Use release mode before CRAN submission
- Use JSON format for automation
- Use markdown format for reports
- Check time budgets before running

### ❌ DON'T

- Don't use debug mode for quick checks (too slow)
- Don't use release mode daily (overkill)
- Don't expect auto mode detection (be explicit)
- Don't ignore time budgets (plan accordingly)
- Don't use `/rforge:thorough` (deprecated - use `--mode release` instead)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Command too slow | Use default mode (no --mode flag) |
| Need more details | Add `--mode debug` |
| Invalid mode error | Check spelling (debug, optimize, release) |
| Mode ignored | Command doesn't support modes (check table above) |
| Need JSON output | Add `--format json` |
| Timeout occurred | Mode exceeded budget, partial results returned |

---

## See Also

- **[MODE-USAGE-GUIDE.md](MODE-USAGE-GUIDE.md)** - Comprehensive mode system guide with real-world examples
- **[MODE-QUICK-REFERENCE.md](MODE-QUICK-REFERENCE.md)** - One-page quick reference card
- **[COMMAND-REFERENCE.md](COMMAND-REFERENCE.md)** - Complete command reference with descriptions

---

**Last Updated:** 2024-12-24
**Mode System Version:** 1.0
