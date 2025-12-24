---
name: rforge:quick
description: Ultra-fast analysis using only quick tools (< 10 seconds)
---

# /rforge:quick - Ultra-Fast R Package Analysis

Lightning-fast analysis using only quick MCP tools. Results in < 10 seconds guaranteed.

## Usage

```bash
# Ultra-fast analysis
/rforge:quick

# With context
/rforge:quick "Update bootstrap code"

# Specific package
/rforge:quick --package /path/to/RMediation
```

## What It Does

Runs 4 fast MCP tools in parallel:
1. **Quick Impact** - Dependency check (5-8 sec)
2. **Quick Tests** - Test status (3-5 sec)
3. **Quick Docs** - Documentation check (2-3 sec)
4. **Quick Health** - Overall score (5-7 sec)

**Total time:** ~10 seconds (parallel execution)

## Output Example

```
⚡ Quick analysis running...

[████████░░] Impact      80%
[██████████] Tests      100% ✓
[██████████] Docs       100% ✓
[████░░░░░░] Health      40%

✅ Done! (8.2 seconds)

📊 QUICK SUMMARY:
✅ Impact: 2 packages (MEDIUM)
✅ Tests: 187/187 passing
⚠️ Docs: NEWS.md needs update
✅ Health: 87/100 (B+)

Next: Run /rforge:analyze for detailed recommendations
```

## When to Use

Use `/rforge:quick` when:
- ✅ You want instant feedback
- ✅ You're just checking status
- ✅ You don't need deep analysis
- ✅ You're in a hurry
- ✅ You're doing quick iterations

**Don't use** when:
- ❌ Preparing for CRAN release (use `/rforge:thorough`)
- ❌ Need detailed cascade plan (use `/rforge:analyze`)
- ❌ Want comprehensive coverage report (use `/rforge:thorough`)

## Tools Used

| Tool | What It Checks | Time |
|------|----------------|------|
| `rforge_quick_impact` | Dependency graph | 5-8s |
| `rforge_quick_tests` | Test files & last results | 3-5s |
| `rforge_quick_docs` | NEWS, vignettes, README | 2-3s |
| `rforge_quick_health` | Overall package health | 5-7s |

All run in **parallel** → total ~10 seconds

## Options

- `--package <path>` - Explicit package path
- `--json` - Raw JSON output
- `--no-progress` - Skip progress bars

## Example Output

```json
{
  "mode": "quick",
  "duration_seconds": 8.2,
  "results": {
    "impact": {
      "affected_packages": 2,
      "severity": "MEDIUM"
    },
    "tests": {
      "passing": 187,
      "total": 187,
      "coverage": 94
    },
    "docs": {
      "has_news": true,
      "needs_update": true
    },
    "health": {
      "score": 87,
      "grade": "B+"
    }
  }
}
```

## ADHD Benefits

- ⚡ **Instant gratification** - Results in seconds
- 📊 **Clear status** - Simple yes/no answers
- 🎯 **Focus on essentials** - Only critical info
- 🔄 **Quick iterations** - Check → fix → check again

## Related Skills

- `/rforge:analyze` - Balanced analysis with recommendations
- `/rforge:thorough` - Deep analysis (2-5 min)
- `/rforge:plan` - Implementation planning

---

**Perfect for:** Quick status checks during development
**Trade-off:** Speed over depth (but usually good enough!)
