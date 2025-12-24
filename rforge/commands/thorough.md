---
name: rforge:thorough
description: Comprehensive analysis with background R processes (2-5 minutes)
argument-hint: Optional context (e.g., "Prepare for CRAN release")
---

# /rforge:thorough - Comprehensive R Package Analysis

Deep, comprehensive analysis using background R processes. Takes 2-5 minutes but provides publication-quality insights.

## Usage

```bash
# Thorough analysis
/rforge:thorough

# With context
/rforge:thorough "Prepare RMediation for CRAN"

# Specific analysis type
/rforge:thorough --type full_check
/rforge:thorough --type coverage
/rforge:thorough --type performance
```

## What It Does

Runs comprehensive R analysis in background:

1. **Launch Phase** (5 sec)
   - Start background R process
   - Return task ID immediately
   - Show estimated duration

2. **Monitoring Phase** (2-5 min)
   - Poll task every 10 seconds
   - Show progress updates
   - Display intermediate results

3. **Results Phase** (5 sec)
   - Retrieve complete results
   - Synthesize comprehensive report
   - Provide detailed recommendations

## Output Example

```
🔬 Launching thorough analysis...

Background R analysis started (task: abc123)
Estimated duration: 3-5 minutes

You can:
- Wait here (I'll show progress)
- Do other work (run /rforge:results abc123 later)
- Cancel anytime (Ctrl+C)

[10s] 📊 Running R CMD check...
[20s] 📊 Still running checks (platform: ubuntu)...
[30s] 📊 Checking examples...
[45s] ✅ R CMD check complete: 0 errors, 0 warnings, 0 notes
[60s] 📊 Running test suite...
[75s] 📊 Calculating coverage...
[90s] ✅ Coverage analysis complete: 94.2%
[120s] 📊 Running performance benchmarks...
[150s] ✅ Performance analysis complete

✅ Thorough analysis complete! (2m 35s)

═══════════════════════════════════════════════════

🎯 COMPREHENSIVE ANALYSIS: RMediation

📦 PACKAGE INFO:
  • Version: 2.0.1
  • R dependency: >= 3.5.0
  • Imports: 3 packages
  • Suggests: 5 packages

🔍 R CMD CHECK: ✅ PASS
  • Errors: 0
  • Warnings: 0
  • Notes: 0
  • Platforms tested: ubuntu-latest, macos-latest, windows-latest
  • Time: 45 seconds

🧪 TEST RESULTS: ✅ EXCELLENT
  • Tests: 187/187 passing
  • Coverage: 94.2%
  • Test files: 12
  • Assertions: 1,245
  • Performance: 2.3 seconds

📊 COVERAGE BREAKDOWN:
  • R/: 96.1% (138/143 lines)
  • R/ci_mediation.R: 98.5%
  • R/bootstrap.R: 92.3% ⚠️ (needs 2 more tests)
  • R/utils.R: 100%

⚡ PERFORMANCE:
  • ci_mediation(): 2.3ms (fast)
  • bootstrap_ci(): 145ms (acceptable)
  • Benchmarked: 1000 iterations
  • No regressions detected

🎯 DEPENDENCY IMPACT:
  • Reverse dependencies: 5 packages
  • All passing with current version
  • 2 packages would be affected by API change

📝 DOCUMENTATION:
  • Roxygen: ✅ Up to date
  • Vignettes: 3 found, all build successfully
  • Examples: All run without errors
  • NEWS.md: Last entry 2.0.0 (needs update for 2.0.1)
  • README badges: All current

🌐 CRAN STATUS:
  • Current CRAN version: 2.0.0
  • Check results: All OK (last check: 2 days ago)
  • Incoming: No submissions pending
  • Reverse check results: All passing

💯 OVERALL HEALTH SCORE: 95/100 (A)

Grade breakdown:
  • Code quality: 96/100 (excellent test coverage)
  • Documentation: 92/100 (minor NEWS update needed)
  • CRAN compliance: 100/100 (perfect)
  • Performance: 94/100 (good)
  • Maintenance: 91/100 (active development)

═══════════════════════════════════════════════════

📋 DETAILED RECOMMENDATIONS:

🔥 BEFORE RELEASE:
  1. Update NEWS.md with 2.0.1 changes
  2. Add 2 tests to R/bootstrap.R (coverage < 95%)
  3. Update version badge in README
  4. Run final check: R CMD check --as-cran

🎯 FOR THIS CHANGE:
  1. Implement bootstrap algorithm update (3 hours)
  2. Update algorithm vignette
  3. Benchmark new vs old performance
  4. Update 2 affected packages (mediate, sensitivity)

⭐ OPTIONAL IMPROVEMENTS:
  1. Add performance benchmarks to vignettes
  2. Create pkgdown site
  3. Add code coverage badge

═══════════════════════════════════════════════════

Next steps:
[1] Generate release checklist
[2] Create cascade plan for dependents
[3] Export report to markdown
[4] Something else
```

## Analysis Types

### full_check (Default)
- R CMD check --as-cran
- Full test suite
- Coverage analysis
- Basic performance
- **Time:** 3-5 minutes

### coverage
- Detailed coverage by file
- Identify untested code
- Generate coverage report
- **Time:** 2-3 minutes

### performance
- Benchmark key functions
- Compare to baseline
- Memory profiling
- **Time:** 2-4 minutes

## Background Task Management

### Check Task Status
```bash
# While analysis running in background
/rforge:status abc123
```

### Get Results Later
```bash
# If you closed Claude or interrupted
/rforge:results abc123
```

### Cancel Task
```bash
# Stop background R process
/rforge:cancel abc123
```

## When to Use

Use `/rforge:thorough` when:
- ✅ Preparing for CRAN submission
- ✅ Need comprehensive coverage report
- ✅ Want performance benchmarks
- ✅ Release readiness check
- ✅ Detailed dependency analysis
- ✅ Can wait 2-5 minutes

**Don't use** when:
- ❌ Just need quick status (use `/rforge:quick`)
- ❌ Iterating rapidly (use `/rforge:analyze`)
- ❌ In a hurry

## Options

- `--type <type>` - Analysis type (full_check, coverage, performance)
- `--package <path>` - Explicit package path
- `--platforms <list>` - Test platforms (ubuntu, macos, windows)
- `--wait` - Wait for completion (default: true)
- `--background` - Return immediately, check later
- `--json` - Raw JSON output

## Output to File

```bash
# Export comprehensive report
/rforge:thorough --export report.md

# Or JSON for CI/CD
/rforge:thorough --export report.json --json
```

## CI/CD Integration

Perfect for automated checks:

```yaml
# .github/workflows/rforge-check.yml
- name: Thorough RForge Check
  run: |
    npx rforge-mcp
    claude-code "/rforge:thorough --json --export results.json"
    # Parse results.json for pass/fail
```

## ADHD Considerations

**Challenges:**
- ⏰ Takes 2-5 minutes (long wait)
- 🎯 Risk of distraction during wait

**Mitigations:**
- 📊 Live progress updates every 10s
- 🔔 Can do other work, come back later
- ⏱️ Clear time estimates upfront
- ✅ Incremental result streaming
- 💾 Results saved if interrupted

## Comparison

| Feature | Quick | Analyze | Thorough |
|---------|-------|---------|----------|
| Time | 10s | 30s | 2-5min |
| R CMD check | ❌ | ❌ | ✅ |
| Test suite | Status only | ✅ | ✅ Full |
| Coverage | Last run | ✅ | ✅ Detailed |
| Performance | ❌ | ❌ | ✅ |
| CRAN check | ❌ | Status | ✅ Full |
| Depth | Surface | Medium | Deep |
| Use case | Quick check | Daily dev | Pre-release |

## Related Skills

- `/rforge:quick` - Ultra-fast (10s)
- `/rforge:analyze` - Balanced (30s)
- `/rforge:status <task>` - Check background task
- `/rforge:results <task>` - Get background results

---

**Perfect for:** Pre-release validation, comprehensive audits, CRAN preparation
**Trade-off:** Depth over speed (worth the wait for releases!)

**Pro tip:** Run `/rforge:thorough` at end of day, review results in morning. Or run in background while you work on something else.
