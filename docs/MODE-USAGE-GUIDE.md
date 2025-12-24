# RForge Mode System - Usage Guide

**Version:** 1.0
**Last Updated:** 2024-12-24
**Audience:** All RForge users

---

## Table of Contents

1. [What Are Modes?](#what-are-modes)
2. [Why Use Modes?](#why-use-modes)
3. [The Four Modes](#the-four-modes)
4. [When to Use Each Mode](#when-to-use-each-mode)
5. [Real-World Examples](#real-world-examples)
6. [Performance Expectations](#performance-expectations)
7. [Mode + Format Combinations](#mode-format-combinations)
8. [Common Workflows](#common-workflows)
9. [FAQ](#faq)

---

## What Are Modes?

Modes give you explicit control over **how deeply** RForge analyzes your R package. Think of modes as different "depth settings" for your analysis.

**Key Insight:** Modes are VERBS describing what you want to DO:
- `debug` → "I want to debug this"
- `optimize` → "I want to optimize performance"
- `release` → "I want to validate for release"

**Modes control:**
- ✅ How much time the analysis takes
- ✅ How detailed the results are
- ✅ Which checks are performed
- ✅ What actionable insights you get

**Modes do NOT control:**
- ❌ Output format (use `--format` for that)
- ❌ What gets displayed (that's automatic)
- ❌ Where results are saved (always shown in terminal)

---

## Why Use Modes?

### The Problem

Without modes, every command runs the same way:
- Quick checks take too long (waiting for deep analysis you don't need)
- Deep debugging is too shallow (missing critical details)
- Pre-release validation is incomplete (CRAN submission anxiety)

### The Solution

Modes let you choose the right analysis for your situation:

```bash
# Morning coffee - just checking in (2 seconds)
/rforge:status

# Found a bug - need details (30 seconds)
/rforge:analyze --mode debug "Bootstrap fails with small N"

# Preparing CRAN submission - need everything (3 minutes)
/rforge:analyze --mode release
```

### ADHD-Friendly Benefits

- **Fast feedback**: Default mode completes in < 10 seconds
- **No decision fatigue**: Modes auto-select appropriate checks
- **Clear expectations**: You know how long it will take
- **Actionable results**: Every mode gives next steps
- **Interruptible**: Long modes show progress, can be stopped

---

## The Four Modes

### 1. Default Mode (No Flag Needed)

**Time:** < 10 seconds
**Purpose:** Daily development, quick check-ins
**Quality:** Catches 80% of critical issues

```bash
# Just use the command without --mode
/rforge:analyze
/rforge:status
```

**What it checks:**
- Critical issues only
- Recent changes (last 7 days)
- High-priority dependencies
- Quick health metrics
- Active warnings

**Perfect for:**
- Morning check-in ("Is everything OK?")
- Before making changes ("What's the current state?")
- After quick edits ("Did I break anything obvious?")
- Frequent status checks

**Skip this mode if:**
- You're debugging a specific issue (use `debug`)
- You need performance analysis (use `optimize`)
- You're preparing a release (use `release`)

---

### 2. Debug Mode

**Time:** 30 seconds - 2 minutes
**Purpose:** Troubleshooting, investigating issues
**Quality:** Catches 95% of all issues

```bash
/rforge:analyze --mode debug
/rforge:status --mode debug
```

**What it checks:**
- All dependencies (recursive)
- Complete file scans
- Detailed error traces
- Hidden configuration issues
- Cache validation
- Environment inspection
- Root cause analysis

**Perfect for:**
- Tracking down a bug
- "Why isn't this working?"
- Investigating test failures
- Understanding unexpected behavior
- Finding dependency conflicts

**Skip this mode if:**
- Everything is working fine (use default)
- You need speed (use default)
- You're checking performance (use `optimize`)

**Example scenario:**
```bash
# Quick check shows a warning
/rforge:status
# Warning: 3 test failures detected

# Get details
/rforge:analyze --mode debug "Test failures in bootstrap tests"
# Output shows:
#   - Exact test file and line number
#   - Error trace
#   - Dependency versions
#   - Environment variables
#   - Suggests: Check bootstrap sample size handling
```

---

### 3. Optimize Mode

**Time:** 1-3 minutes
**Purpose:** Performance analysis, speed improvements
**Quality:** Identifies top 3-5 bottlenecks

```bash
/rforge:analyze --mode optimize
/rforge:status --mode optimize
```

**What it checks:**
- Profile R code execution
- Package load time analysis
- Dependency bloat detection
- Function call hotspots
- Memory usage patterns
- Benchmark comparisons
- Slowest operations

**Perfect for:**
- Package feels slow
- Optimizing before release
- Understanding performance
- Reducing dependencies
- Improving test speed

**Skip this mode if:**
- Performance is fine (use default)
- You're debugging errors (use `debug`)
- You just want status (use default)

**Example scenario:**
```bash
# Package loads slowly
/rforge:status
# Load time: 3.2s (slow)

# Analyze performance
/rforge:analyze --mode optimize "Package load time"
# Output shows:
#   - Top 5 slowest imports (ggplot2: 1.8s)
#   - Unused dependencies (3 detected)
#   - Lazy load opportunities
#   - Suggests: Remove ggplot2 from Imports, move to Suggests
```

---

### 4. Release Mode

**Time:** 2-5 minutes
**Purpose:** Pre-release validation, CRAN submission
**Quality:** CRAN submission confidence

```bash
/rforge:analyze --mode release
/rforge:status --mode release
```

**What it checks:**
- R CMD check equivalent
- All test suites (unit + integration)
- Documentation completeness
- CRAN policy compliance
- Breaking change detection
- Reverse dependency checks
- NEWS.md completeness
- Version number validation

**Perfect for:**
- Before CRAN submission
- Major version releases
- Publication-ready package
- "Is this ready to ship?"

**Skip this mode if:**
- Early development (use default)
- Between releases (use default)
- Debugging (use `debug`)

**Example scenario:**
```bash
# Ready to submit to CRAN
/rforge:analyze --mode release "Release 2.1.0"
# Output shows:
#   - R CMD check: PASS (0 errors, 0 warnings, 0 notes)
#   - Tests: 156/156 passing (100% coverage)
#   - Documentation: Complete
#   - CRAN policies: Compliant
#   - Breaking changes: None detected
#   - NEWS.md: Up to date
#   ✅ READY FOR CRAN SUBMISSION
```

---

## When to Use Each Mode

### Decision Flowchart

```
START: What do you need?
│
├─ Just checking if things are OK?
│  └─> Use DEFAULT MODE (/rforge:analyze)
│
├─ Something is broken and you need to find out why?
│  └─> Use DEBUG MODE (--mode debug)
│
├─ Package is slow and you want to speed it up?
│  └─> Use OPTIMIZE MODE (--mode optimize)
│
└─ About to release to CRAN?
   └─> Use RELEASE MODE (--mode release)
```

### Quick Decision Table

| Situation | Mode | Why |
|-----------|------|-----|
| Morning check-in | `default` | Fast, catch critical issues |
| Tests are failing | `debug` | Need error details and traces |
| Package loads slowly | `optimize` | Find performance bottlenecks |
| Before git commit | `default` | Quick validation |
| Bug in production | `debug` | Root cause analysis |
| Reducing dependencies | `optimize` | Find unused imports |
| CRAN submission tomorrow | `release` | Comprehensive validation |
| New feature working? | `default` | Quick check is enough |
| Memory issues suspected | `optimize` | Memory profiling |
| Major version bump | `release` | Check breaking changes |

---

## Real-World Examples

### Scenario 1: Morning Development Workflow

**Context:** Starting work on your R package

```bash
# 8:00 AM - Coffee in hand, opening project
/rforge:status

# Output (2 seconds):
# ✅ RMediation (v2.0.5)
# ✅ Health: 92/100
# ⚠️  1 warning: Documentation drift in mediation.Rd
# 💡 Next: Update documentation

# Quick and actionable - ready to work!
```

**Why default mode?** You just need to know if anything is broken. Default mode is fast and catches the important stuff.

---

### Scenario 2: Debugging Test Failures

**Context:** Your tests started failing after refactoring

```bash
# Quick check
/rforge:status
# ⚠️ 5 tests failing

# Need details - switch to debug mode
/rforge:analyze --mode debug "Bootstrap test failures"

# Output (45 seconds):
# ❌ Test: test_bootstrap_ci.R:23
#    Error: bootstrap samples contain NA values
#
# Root Cause Analysis:
#    - Function: ci_mediation()
#    - Line: bootstrap.R:156
#    - Issue: No NA handling for small sample sizes
#    - Introduced: commit abc123 (yesterday)
#
# Dependencies:
#    ✅ boot: 1.3-30 (OK)
#    ✅ MASS: 7.3-60 (OK)
#
# Environment:
#    ✅ R version: 4.3.2 (OK)
#    ⚠️  RNG seed not set in test
#
# Suggested Fix:
#    1. Add na.omit() in bootstrap.R:156
#    2. Set seed in test for reproducibility
#    3. Add test case for N < 30
```

**Why debug mode?** You need detailed traces, root causes, and specific line numbers. Default mode would just say "tests failing" - not enough info to fix it.

---

### Scenario 3: Performance Investigation

**Context:** Users complaining package is slow

```bash
# Check if performance is actually an issue
/rforge:status
# ⚠️ Load time: 4.2s (slow)

# Analyze performance
/rforge:analyze --mode optimize "Package load performance"

# Output (90 seconds):
# Performance Analysis: RMediation
#
# Load Time Breakdown:
#    Total: 4.2s
#    ├─ ggplot2 import: 2.1s (50%) ← BOTTLENECK
#    ├─ dplyr import: 0.8s (19%)
#    ├─ boot import: 0.6s (14%)
#    └─ Other: 0.7s (17%)
#
# Dependency Analysis:
#    ⚠️  ggplot2 only used in 1 function (plot_mediation)
#    💡 Move ggplot2 to Suggests (saves 2.1s)
#    ✅ dplyr and boot are core dependencies (keep)
#
# Function Hotspots:
#    1. bootstrap_ci(): 85% of runtime (expected)
#    2. calculate_se(): 12% of runtime
#    3. Other: 3%
#
# Memory Usage:
#    ✅ Peak: 24 MB (reasonable)
#    ✅ No memory leaks detected
#
# Suggestions:
#    1. Move ggplot2 to Suggests → Load time: 2.1s (50% faster)
#    2. Consider Rcpp for bootstrap_ci() → 3-5x speedup
#    3. Cache calculate_se() results → 10-15% speedup
```

**Why optimize mode?** You need profiling data, bottleneck analysis, and performance benchmarks. Debug mode focuses on errors, not speed.

---

### Scenario 4: CRAN Release Preparation

**Context:** Ready to submit new version to CRAN

```bash
# Final validation before submission
/rforge:analyze --mode release "Release v2.1.0"

# Output (3.5 minutes):
# CRAN Release Validation: RMediation v2.1.0
#
# R CMD check: ✅ PASS
#    Errors: 0
#    Warnings: 0
#    Notes: 0
#
# Test Suite: ✅ PASS
#    Unit tests: 145/145 passing
#    Integration tests: 11/11 passing
#    Coverage: 94% (target: 80%)
#    Runtime: 23s (acceptable)
#
# Documentation: ✅ COMPLETE
#    Functions documented: 23/23
#    Examples working: 23/23
#    Vignettes: 3 (all building)
#    README: Up to date
#
# CRAN Policies: ✅ COMPLIANT
#    Package size: 2.1 MB (limit: 5 MB)
#    Dependencies: 4 (all on CRAN)
#    License: MIT (CRAN-compatible)
#    Authors@R: Valid
#
# Version Control: ✅ READY
#    NEWS.md: Updated for 2.1.0
#    DESCRIPTION version: 2.1.0
#    Git tag: v2.1.0 created
#    Uncommitted changes: None
#
# Breaking Changes: ✅ NONE
#    API compatibility: 100%
#    Parameter changes: None
#    Deprecations: 1 (properly documented)
#
# Reverse Dependencies: ✅ ALL PASS
#    mediation: Tests pass
#    causalverse: Tests pass
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ READY FOR CRAN SUBMISSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Next Steps:
#    1. devtools::submit_cran()
#    2. Monitor CRAN incoming
#    3. Respond to any reviewer comments
```

**Why release mode?** You need comprehensive validation and CRAN compliance checks. This is the only mode that checks EVERYTHING.

---

### Scenario 5: Rapid Iteration

**Context:** Making quick fixes, committing frequently

```bash
# Fix a typo in documentation
# (edit file)

# Quick check before commit
/rforge:analyze
# Output (4 seconds):
# ✅ No issues detected
# 💡 Ready to commit

git add . && git commit -m "docs: fix typo in mediation.Rd"

# Make another quick change
# (edit file)

# Check again
/rforge:analyze
# Output (3 seconds):
# ✅ No issues detected
# 💡 Ready to commit

# Fast feedback loop = productivity!
```

**Why default mode?** You're making small changes and just need to catch obvious errors. Debug mode would be overkill and slow you down.

---

## Performance Expectations

### Time Budgets

All modes have guaranteed maximum times:

| Mode | Time Budget | Typical Time | Progress Bar |
|------|-------------|--------------|--------------|
| **Default** | < 10s | 3-7s | No (too fast) |
| **Debug** | < 2 min | 30-90s | Yes |
| **Optimize** | < 3 min | 60-180s | Yes |
| **Release** | < 5 min | 120-300s | Yes |

**Progress indicators:** Modes longer than 10 seconds show progress:

```bash
/rforge:analyze --mode release

# You'll see:
Comprehensive validation (release mode)...
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░] 75% - Running test suite...
```

---

### Quality vs. Speed Trade-off

```
High Quality │                           ● release
            │                     ● debug
            │              ● optimize
            │       ● default
            │
            └─────────────────────────────────> Fast
              10s    30s   1m    2m    5m
```

**Key insight:** Default mode catches 80% of issues in < 10 seconds. Only use slower modes when you need that extra 20%.

---

### Performance Guarantees

#### Default Mode
- **Must** complete in < 10 seconds (hard limit)
- **Typical** completion: 3-7 seconds
- **Catches:** 80% of critical issues
- **Use frequency:** Daily, multiple times

#### Debug Mode
- **Should** complete in < 2 minutes
- **Typical** completion: 30-90 seconds
- **Catches:** 95% of all issues
- **Use frequency:** When debugging (as needed)

#### Optimize Mode
- **Should** complete in < 3 minutes
- **Typical** completion: 60-180 seconds
- **Finds:** Top 3-5 bottlenecks
- **Use frequency:** Occasional (performance work)

#### Release Mode
- **Should** complete in < 5 minutes
- **Typical** completion: 2-4 minutes
- **Validates:** CRAN submission readiness
- **Use frequency:** Rare (before releases)

---

## Mode + Format Combinations

### Understanding Formats

Formats control **how results are displayed**, not **what analysis is done**.

Available formats:
- `terminal` (default) - Rich, colorful, human-readable
- `json` - Machine-readable, for scripting
- `markdown` - For reports and documentation

### Combining Modes and Formats

```bash
# Debug analysis in JSON (for logging)
/rforge:analyze --mode debug --format json > debug-log.json

# Release validation as Markdown report
/rforge:analyze --mode release --format markdown > release-report.md

# Quick status for CI/CD
/rforge:status --format json
```

### Use Cases for Each Combination

#### Terminal Format (Default)

**Best for:** Interactive use, daily development

```bash
/rforge:analyze
/rforge:status --mode debug
```

**Output:** Colorful, formatted, easy to read in terminal

---

#### JSON Format

**Best for:** Automation, CI/CD, logging, scripting

```bash
# CI/CD pipeline
/rforge:analyze --mode release --format json > results.json
cat results.json | jq '.health_score'

# Nightly health check
/rforge:status --mode debug --format json >> health-log.jsonl

# Performance tracking over time
/rforge:analyze --mode optimize --format json | \
  jq '{date: now, load_time: .performance.load_time}' \
  >> performance-history.jsonl
```

**Output:** Machine-readable JSON:
```json
{
  "package": "RMediation",
  "version": "2.0.5",
  "health_score": 92,
  "mode": "default",
  "timestamp": "2024-12-24T10:30:00Z",
  "issues": [
    {
      "severity": "warning",
      "type": "documentation",
      "message": "Documentation drift in mediation.Rd"
    }
  ],
  "next_action": "Update documentation"
}
```

---

#### Markdown Format

**Best for:** Reports, documentation, sharing with team

```bash
# Weekly status report
/rforge:status --mode debug --format markdown > weekly-report.md

# Release notes generation
/rforge:analyze --mode release --format markdown > RELEASE-NOTES.md

# Performance audit
/rforge:analyze --mode optimize --format markdown > performance-audit.md
```

**Output:** Formatted Markdown:
```markdown
# RMediation Package Status

**Date:** 2024-12-24
**Version:** 2.0.5
**Health Score:** 92/100

## Issues

### Warnings (1)
- Documentation drift in mediation.Rd

## Recommendations

1. Update documentation to match current API
2. Run tests before next commit

## Next Action
Update documentation
```

---

### Example: Full Workflow with Formats

```bash
# Morning: Quick terminal check
/rforge:status
# ✅ Health: 92/100 (terminal output)

# Found issue: Debug with details
/rforge:analyze --mode debug
# (terminal output with colors)

# Fixed issue: Document fix for team
/rforge:analyze --format markdown > bugfix-analysis.md
# (markdown report saved)

# End of day: Log status
/rforge:status --format json >> daily-status.jsonl
# (JSON logged for tracking)

# Release prep: Comprehensive report
/rforge:analyze --mode release --format markdown > v2.1.0-validation.md
# (full report for CRAN submission notes)
```

---

## Common Workflows

### Workflow 1: Daily Development

**Morning routine:**
```bash
# Check if anything broke overnight
/rforge:status

# If issues: investigate
/rforge:analyze --mode debug
```

**During development:**
```bash
# Before making changes
/rforge:analyze "Planning to refactor bootstrap"

# After changes
/rforge:analyze "Refactored bootstrap algorithm"
```

**Before committing:**
```bash
# Final check
/rforge:analyze

# If clean, commit
git add . && git commit -m "refactor: improve bootstrap algorithm"
```

---

### Workflow 2: Debugging

**Initial investigation:**
```bash
# Quick check shows issues
/rforge:status
# ⚠️ 3 test failures

# Get details
/rforge:analyze --mode debug "Test failures"
```

**Deep dive:**
```bash
# Still unclear? Check performance
/rforge:analyze --mode optimize "Bootstrap performance"
```

**Verification:**
```bash
# After fix, verify
/rforge:analyze
# ✅ No issues detected
```

---

### Workflow 3: Release Preparation

**1 week before release:**
```bash
# Early validation
/rforge:analyze --mode release

# Generate report
/rforge:analyze --mode release --format markdown > release-checklist.md
```

**Fix issues, then:**
```bash
# Daily progress checks
/rforge:status --mode release
```

**Release day:**
```bash
# Final validation
/rforge:analyze --mode release
# ✅ READY FOR CRAN SUBMISSION

# Submit to CRAN
devtools::submit_cran()
```

---

### Workflow 4: CI/CD Integration

**In `.github/workflows/R-CMD-check.yml`:**
```yaml
- name: Run RForge validation
  run: |
    /rforge:analyze --mode release --format json > validation.json

- name: Check if passed
  run: |
    if jq -e '.issues | length == 0' validation.json; then
      echo "✅ Validation passed"
    else
      echo "❌ Validation failed"
      exit 1
    fi
```

---

## FAQ

### Q: What mode should I use most often?

**A:** Default mode (no flag). It's designed for daily use - fast (< 10s) and catches 80% of issues. Only switch modes when you need something specific:
- Debugging? Use `debug`
- Performance? Use `optimize`
- Release? Use `release`

---

### Q: Can modes auto-detect based on context?

**A:** No, and this is intentional. Auto-detection leads to:
- Unpredictable performance (sometimes fast, sometimes slow)
- Surprising behavior (why did it take 3 minutes this time?)
- Harder to script (can't guarantee time budget)

Explicit modes give you control and predictable performance.

---

### Q: Why is default mode < 10 seconds?

**A:** Research shows:
- 5s feels instant
- 10s is acceptable for frequent use
- 30s feels slow for daily use
- 60s+ requires progress indicator and breaks flow

< 10s is fast enough for frequent use while allowing useful analysis.

---

### Q: What if I need something between debug and release?

**A:** Try debug mode first. It catches 95% of issues in < 2 minutes. Release mode is specifically for CRAN validation and includes checks most developers don't need daily (like reverse dependency validation).

---

### Q: Can I make modes faster?

**A:** Time budgets are maximums - modes often finish faster:
- Default: typically 3-7s (budget: 10s)
- Debug: typically 30-90s (budget: 120s)
- Optimize: typically 60-180s (budget: 180s)
- Release: typically 120-300s (budget: 300s)

Performance improves with caching and optimizations over time.

---

### Q: Does `/rforge:quick` support modes?

**A:** No. `/rforge:quick` is **always** fast (< 10 seconds) by design. It ignores `--mode` flags. If you want deeper analysis, use `/rforge:analyze --mode debug`.

---

### Q: Can I customize what each mode checks?

**A:** Not in v1.0, but planned for v2.0. Future versions will support custom modes:

```yaml
# .rforge/modes.yml (future)
modes:
  my-custom-mode:
    budget: 60s
    checks:
      - dependencies
      - tests
      - documentation
    format: markdown
```

---

### Q: What if a mode exceeds its time budget?

**A:** Modes have built-in safety:
1. **Hard timeout** at budget + 10%
2. **Early exit** with partial results if approaching timeout
3. **Warning** shown if taking longer than expected

You'll always get results, even if incomplete.

---

### Q: How do formats interact with modes?

**A:** Independently! Mode controls depth/behavior, format controls output:
- Mode: **What** analysis to run (default/debug/optimize/release)
- Format: **How** to display results (terminal/json/markdown)

All combinations work:
```bash
/rforge:analyze --mode debug --format json
/rforge:status --mode release --format markdown
```

---

### Q: Should I use modes in scripts/automation?

**A:** Yes! Especially with JSON format:

```bash
# CI/CD: Release validation
/rforge:analyze --mode release --format json > results.json

# Nightly: Performance tracking
/rforge:analyze --mode optimize --format json >> perf-log.jsonl

# Monitoring: Health checks
/rforge:status --format json | \
  jq -r 'select(.health_score < 80) | "Alert: Health score low"'
```

---

## Summary

**Modes = Depth control**
- Default: Fast daily checks (< 10s)
- Debug: Deep troubleshooting (< 2m)
- Optimize: Performance analysis (< 3m)
- Release: CRAN validation (< 5m)

**Formats = Output control**
- Terminal: Human-readable (default)
- JSON: Machine-readable (automation)
- Markdown: Reports (sharing)

**Key principles:**
1. Default mode for 90% of use cases
2. Explicit modes only (no auto-detection)
3. Modes are VERBS (debug, optimize, release)
4. Fast feedback = productivity
5. Every mode gives actionable next steps

**Start simple:** Use default mode. Switch to other modes only when you specifically need deep debugging, performance analysis, or release validation.

---

**Happy RForging!** 🔨
