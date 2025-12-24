# RForge Modes - Quick Reference

**Version:** 1.0 | **Print This Page** 📄

---

## Mode Comparison Table

| Mode | Time | Purpose | Quality | Use When |
|------|------|---------|---------|----------|
| **default** | < 10s | Daily checks | 80% issues | Just checking status |
| **debug** | 30s-2m | Troubleshooting | 95% issues | Finding bugs |
| **optimize** | 1-3m | Performance | Top bottlenecks | Speed problems |
| **release** | 2-5m | CRAN validation | Comprehensive | Before release |

---

## Quick Decision Tree

```
What do you need?
│
├─ Quick status check? ──────────────────> default (no flag)
│
├─ Something broken? ────────────────────> --mode debug
│
├─ Package too slow? ────────────────────> --mode optimize
│
└─ Releasing to CRAN? ───────────────────> --mode release
```

---

## Common Commands

### Default Mode (Fast)
```bash
/rforge:analyze                    # Balanced analysis (< 10s)
/rforge:status                     # Quick dashboard (2-5s)
```

### Debug Mode (Detailed)
```bash
/rforge:analyze --mode debug       # Deep inspection (30s-2m)
/rforge:status --mode debug        # Detailed status (15-30s)
```

### Optimize Mode (Performance)
```bash
/rforge:analyze --mode optimize    # Performance analysis (1-3m)
/rforge:status --mode optimize     # Performance metrics (30s-1m)
```

### Release Mode (Comprehensive)
```bash
/rforge:analyze --mode release     # CRAN validation (2-5m)
/rforge:status --mode release      # Release readiness (1-2m)
```

---

## Command + Format Combinations

```bash
# Terminal output (default)
/rforge:analyze
/rforge:status --mode debug

# JSON output (scripting)
/rforge:analyze --mode debug --format json
/rforge:status --format json

# Markdown output (reports)
/rforge:analyze --mode release --format markdown
/rforge:status --mode debug --format markdown
```

---

## Time Budgets

| Mode | Maximum | Typical | Progress Bar |
|------|---------|---------|--------------|
| default | 10s | 3-7s | No |
| debug | 2m | 30-90s | Yes |
| optimize | 3m | 60-180s | Yes |
| release | 5m | 2-4m | Yes |

---

## Mode-Specific Checks

### Default Mode
- ✅ Critical issues only
- ✅ Recent changes (7 days)
- ✅ High-priority deps
- ✅ Quick health metrics

### Debug Mode
- ✅ All dependencies (recursive)
- ✅ Complete file scans
- ✅ Detailed error traces
- ✅ Hidden config issues
- ✅ Cache validation
- ✅ Environment inspection

### Optimize Mode
- ✅ Profile R code
- ✅ Package load times
- ✅ Dependency bloat
- ✅ Function hotspots
- ✅ Memory usage
- ✅ Benchmarks

### Release Mode
- ✅ R CMD check
- ✅ All test suites
- ✅ Documentation check
- ✅ CRAN compliance
- ✅ Breaking changes
- ✅ Reverse deps

---

## Format Options

| Format | Best For | Output |
|--------|----------|--------|
| `terminal` | Interactive use | Colorful, readable |
| `json` | Automation, CI/CD | Machine-readable |
| `markdown` | Reports, sharing | Documentation |

**Examples:**
```bash
--format terminal    # Default (omit flag)
--format json        # For scripts
--format markdown    # For reports
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Too slow | Use default mode (no flag) |
| Not enough detail | Add `--mode debug` |
| Need performance data | Use `--mode optimize` |
| Invalid mode error | Check spelling (debug, optimize, release) |
| Mode ignored | `/rforge:quick` doesn't support modes |
| Timeout | Mode exceeded budget, partial results returned |

---

## Best Practices

### ✅ DO
- Use default mode for 90% of tasks
- Switch modes explicitly when needed
- Use `--format json` for automation
- Check time budget before running
- Use progress as feedback

### ❌ DON'T
- Don't use debug mode for quick checks
- Don't use release mode daily
- Don't expect auto mode detection
- Don't ignore time budgets
- Don't skip default mode

---

## Real-World Examples

### Morning Routine
```bash
/rforge:status                # Fast check (2s)
```

### Debugging
```bash
/rforge:analyze --mode debug  # Find root cause (45s)
```

### Performance Issue
```bash
/rforge:analyze --mode optimize  # Profile code (90s)
```

### Before CRAN
```bash
/rforge:analyze --mode release   # Full validation (3.5m)
```

### CI/CD Pipeline
```bash
/rforge:analyze --mode release --format json > results.json
```

---

## Performance Guarantees

### Quality Metrics
- **Default:** 80% of critical issues
- **Debug:** 95% of all issues
- **Optimize:** Top 3-5 bottlenecks
- **Release:** CRAN submission confidence

### Time Enforcement
- Hard timeout at budget + 10%
- Progress indicators for > 10s
- Early exit with partial results
- Warning if approaching timeout

---

## Quick Tips

💡 **Tip 1:** Default mode is usually enough
```bash
/rforge:analyze  # Catches 80% of issues in < 10s
```

💡 **Tip 2:** Modes are explicit, not automatic
```bash
/rforge:analyze --mode debug  # Must specify
```

💡 **Tip 3:** JSON format for automation
```bash
/rforge:status --format json | jq '.health_score'
```

💡 **Tip 4:** Markdown for reports
```bash
/rforge:analyze --mode release --format markdown > report.md
```

💡 **Tip 5:** Progress shown for slow modes
```bash
/rforge:analyze --mode release
# [▓▓▓▓▓▓▓▓░░] 80% - Running tests...
```

---

## Time Savings

### Without Modes
All commands take 3-5 minutes (slow default)
- 10 daily checks × 3 min = 30 min wasted

### With Modes
Smart defaults + explicit deep dives
- 10 daily checks × 5s = 50 seconds
- 1 debug session × 1 min = 1 minute
- **Total:** ~2 minutes (93% faster!)

---

## Mode vs. Format

**Remember:** Modes and formats are independent!

| What | Controls | Options |
|------|----------|---------|
| **Mode** | Analysis depth | default, debug, optimize, release |
| **Format** | Output display | terminal, json, markdown |

**Example:**
```bash
/rforge:analyze --mode debug --format json
#               └─ depth      └─ output
```

---

## Workflow Patterns

### Pattern 1: Fast Iteration
```bash
# Quick checks between commits
/rforge:analyze        # 5s
git commit -m "fix"
/rforge:analyze        # 5s
git commit -m "docs"
```

### Pattern 2: Deep Debugging
```bash
/rforge:status                    # 3s - Issue found
/rforge:analyze --mode debug      # 45s - Root cause
# Fix issue
/rforge:analyze                   # 5s - Verify
```

### Pattern 3: Release Prep
```bash
/rforge:analyze --mode release    # 3m - Full check
# Fix issues
/rforge:analyze --mode release    # 3m - Verify
devtools::submit_cran()
```

---

## Common Mistakes

❌ **Using debug mode for quick checks**
```bash
/rforge:analyze --mode debug  # Takes 45s unnecessarily
```
✅ **Use default mode instead**
```bash
/rforge:analyze              # Takes 5s, catches critical issues
```

---

❌ **Forgetting format for automation**
```bash
/rforge:status | grep "health"  # Terminal output is hard to parse
```
✅ **Use JSON format**
```bash
/rforge:status --format json | jq '.health_score'
```

---

❌ **Using release mode daily**
```bash
/rforge:analyze --mode release  # Takes 3m, overkill for daily use
```
✅ **Save for actual releases**
```bash
# Daily: use default
/rforge:analyze

# Release week: use release mode
/rforge:analyze --mode release
```

---

## Integration Examples

### Git Hook (pre-commit)
```bash
#!/bin/bash
/rforge:analyze || exit 1
```

### CI/CD (GitHub Actions)
```yaml
- name: Validate package
  run: /rforge:analyze --mode release --format json > results.json
```

### Cron Job (nightly health)
```bash
0 2 * * * /rforge:status --mode debug --format json >> /logs/health.jsonl
```

### Performance Monitoring
```bash
/rforge:analyze --mode optimize --format json | \
  jq '{date: now, load_time: .load_time}' >> perf.jsonl
```

---

## Keyboard Shortcuts (Terminal Aliases)

Add to your `.zshrc` or `.bashrc`:

```bash
# Quick aliases
alias rf='/rforge:analyze'
alias rfs='/rforge:status'

# Mode aliases
alias rfd='/rforge:analyze --mode debug'
alias rfo='/rforge:analyze --mode optimize'
alias rfr='/rforge:analyze --mode release'

# Format aliases
alias rfj='/rforge:analyze --format json'
alias rfm='/rforge:analyze --format markdown'
```

**Usage:**
```bash
rf          # Quick analyze
rfs         # Quick status
rfd         # Debug mode
rfr         # Release mode
rfj         # JSON output
```

---

## Cheat Sheet for Print

```
┌─────────────────────────────────────────────────────┐
│ RForge Mode Quick Reference                          │
├─────────────────────────────────────────────────────┤
│                                                      │
│ MODES                    TIME     WHEN TO USE       │
│ ────────────────────────────────────────────────    │
│ default (no flag)        < 10s   Daily checks       │
│ --mode debug             < 2m    Debugging          │
│ --mode optimize          < 3m    Performance        │
│ --mode release           < 5m    CRAN submission    │
│                                                      │
│ FORMATS                                             │
│ ────────────────────────────────────────────────    │
│ terminal (default)       Human-readable             │
│ --format json            Automation, scripting      │
│ --format markdown        Reports, documentation     │
│                                                      │
│ QUICK DECISION                                      │
│ ────────────────────────────────────────────────    │
│ Just checking?           /rforge:analyze            │
│ Something broken?        --mode debug               │
│ Too slow?                --mode optimize            │
│ Releasing?               --mode release             │
│                                                      │
│ EXAMPLES                                            │
│ ────────────────────────────────────────────────    │
│ /rforge:analyze                                     │
│ /rforge:analyze --mode debug                        │
│ /rforge:analyze --mode release --format json        │
│ /rforge:status --mode debug --format markdown       │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

**Print this page and keep it handy!** 📄

**Full documentation:** See MODE-USAGE-GUIDE.md for detailed explanations and examples.
