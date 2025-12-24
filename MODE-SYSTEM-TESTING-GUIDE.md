# Mode System Testing Guide

**Date:** 2024-12-24
**Purpose:** Verify mode system implementation
**Status:** Ready for testing

---

## Quick Test Checklist

### Phase 1: Command Syntax (Immediate)

Test that commands accept mode and format parameters:

```bash
# Test analyze command
/rforge:analyze --mode default
/rforge:analyze --mode debug
/rforge:analyze --mode optimize
/rforge:analyze --mode release

# Test status command
/rforge:status --mode default
/rforge:status --mode debug
/rforge:status --mode optimize
/rforge:status --mode release

# Test format options
/rforge:analyze --format json
/rforge:analyze --format markdown
/rforge:analyze --format terminal

# Test mode + format combos
/rforge:analyze --mode debug --format json
/rforge:status --mode release --format markdown
```

**Expected:** Commands should accept parameters without error

---

### Phase 2: Backward Compatibility (Critical)

Test that existing usage patterns still work:

```bash
# Original syntax (no mode specified)
/rforge:analyze "Update algorithm"
/rforge:analyze
/rforge:status
/rforge:status medfit

# Should default to "default" mode
# Should complete in < 10s (analyze) or < 5s (status)
```

**Expected:** All commands work exactly as before

---

### Phase 3: Mode Behavior (Next)

Test that different modes produce different outputs:

#### `/rforge:analyze` Mode Tests

```bash
# 1. Default mode test
/rforge:analyze "Test default mode"
# Expected: < 10s, critical issues only, balanced output

# 2. Debug mode test
/rforge:analyze "Test debug mode" --mode debug
# Expected: < 2m, detailed traces, all issues

# 3. Optimize mode test
/rforge:analyze --mode optimize
# Expected: < 3m, performance metrics, bottlenecks

# 4. Release mode test
/rforge:analyze --mode release
# Expected: < 5m, CRAN validation, comprehensive
```

#### `/rforge:status` Mode Tests

```bash
# 1. Default mode test
/rforge:status
# Expected: < 5s, quick dashboard, critical only

# 2. Debug mode test
/rforge:status --mode debug
# Expected: < 30s, detailed breakdown, all warnings

# 3. Optimize mode test
/rforge:status --mode optimize
# Expected: < 1m, performance metrics, slow functions

# 4. Release mode test
/rforge:status --mode release
# Expected: < 2m, CRAN readiness, release checklist
```

---

### Phase 4: Performance Validation (Important)

Track execution times for each mode:

#### Timing Template

```markdown
## `/rforge:analyze` Performance

| Run | Mode | Time | Within Budget? | Notes |
|-----|------|------|----------------|-------|
| 1 | default | X.Xs | ✅/❌ (< 10s) | |
| 2 | debug | X.Xs | ✅/❌ (< 2m) | |
| 3 | optimize | X.Xs | ✅/❌ (< 3m) | |
| 4 | release | X.Xs | ✅/❌ (< 5m) | |

## `/rforge:status` Performance

| Run | Mode | Time | Within Budget? | Notes |
|-----|------|------|----------------|-------|
| 1 | default | X.Xs | ✅/❌ (< 5s) | |
| 2 | debug | X.Xs | ✅/❌ (< 30s) | |
| 3 | optimize | X.Xs | ✅/❌ (< 1m) | |
| 4 | release | X.Xs | ✅/❌ (< 2m) | |
```

**Critical:** Default modes MUST meet time budgets

---

### Phase 5: Format Testing (Day 2)

Test each format with each mode:

```bash
# Terminal format (default)
/rforge:analyze --mode debug --format terminal
# Expected: Rich formatted output, colors, emojis

# JSON format
/rforge:analyze --mode debug --format json
# Expected: Valid JSON, machine-readable

# Markdown format
/rforge:analyze --mode debug --format markdown
# Expected: Valid markdown, documentation-friendly
```

**Validate:**
- Terminal: Readable, scannable, uses Rich formatting
- JSON: Valid JSON syntax, parseable
- Markdown: Valid markdown, renders correctly

---

## Detailed Test Scenarios

### Scenario 1: Daily Developer Workflow

**User:** Developer doing morning check-in

**Commands:**
```bash
# Quick status (should be < 5s)
/rforge:status

# Quick analysis after changes (should be < 10s)
/rforge:analyze "Updated bootstrap algorithm"
```

**Expected:**
- Both commands fast enough for frequent use
- Output is actionable (clear next steps)
- Critical issues highlighted
- No overwhelming detail

**Success Criteria:**
- ✅ Combined time < 15 seconds
- ✅ Shows critical issues only
- ✅ Suggests next action
- ✅ Not overwhelming

---

### Scenario 2: Bug Investigation

**User:** Developer debugging a specific issue

**Commands:**
```bash
# Quick check first
/rforge:status

# Found issue, need details
/rforge:analyze "Bootstrap fails with n < 30" --mode debug
```

**Expected:**
- Default status is fast (< 5s)
- Debug mode provides detailed traces (< 2m)
- Shows root cause
- Provides detailed error information

**Success Criteria:**
- ✅ Debug mode shows more detail than default
- ✅ Includes error traces
- ✅ Shows root cause
- ✅ Complete in < 2m

---

### Scenario 3: Performance Tuning

**User:** Developer optimizing package performance

**Commands:**
```bash
# Check performance status
/rforge:status --mode optimize

# Get detailed performance analysis
/rforge:analyze --mode optimize

# Export for tracking
/rforge:analyze --mode optimize --format json > perf-baseline.json
```

**Expected:**
- Shows performance metrics
- Identifies slow functions
- Quantifies impact
- Suggests optimizations

**Success Criteria:**
- ✅ Shows load times
- ✅ Identifies bottlenecks (top 3-5)
- ✅ Provides concrete suggestions
- ✅ JSON output is valid

---

### Scenario 4: Release Preparation

**User:** Preparing package for CRAN submission

**Commands:**
```bash
# Quick check
/rforge:status

# Full release validation
/rforge:analyze --mode release

# Get release report
/rforge:analyze --mode release --format markdown > RELEASE-CHECKLIST.md
```

**Expected:**
- Comprehensive validation
- CRAN policy compliance check
- Breaking change detection
- Release readiness score

**Success Criteria:**
- ✅ R CMD check equivalent
- ✅ Shows breaking changes
- ✅ CRAN compliance verified
- ✅ Markdown report generated
- ✅ Complete in < 5m

---

## Edge Case Testing

### Invalid Mode Names

```bash
/rforge:analyze --mode invalid
/rforge:analyze --mode VERBOSE
/rforge:analyze --mode detailed
```

**Expected:**
- Error message or fallback to default
- Clear guidance on valid modes
- No crash

---

### Invalid Format Names

```bash
/rforge:analyze --format invalid
/rforge:analyze --format html
/rforge:analyze --format pdf
```

**Expected:**
- Error message or fallback to terminal
- Clear guidance on valid formats
- No crash

---

### Mode Case Sensitivity

```bash
/rforge:analyze --mode DEBUG
/rforge:analyze --mode Debug
/rforge:analyze --mode DeBuG
```

**Expected:**
- Should work (case-insensitive)
- Or clear error if case-sensitive

---

### Empty/Missing Arguments

```bash
/rforge:analyze --mode
/rforge:analyze --format
/rforge:status --mode
```

**Expected:**
- Fallback to defaults
- Or clear error message

---

### Combination Edge Cases

```bash
# Multiple modes (invalid)
/rforge:analyze --mode debug --mode release

# Multiple formats (invalid)
/rforge:analyze --format json --format markdown

# Mode without dashes
/rforge:analyze mode debug

# Format without dashes
/rforge:analyze format json
```

**Expected:**
- Clear error messages
- Guidance on correct syntax

---

## Performance Benchmarking

### Setup

Run each mode 3 times and record:
- Minimum time
- Maximum time
- Average time
- Standard deviation

### Default Mode Requirements (CRITICAL)

**MUST meet these budgets:**

```
/rforge:analyze (default):  < 10 seconds (hard requirement)
/rforge:status (default):   < 5 seconds (hard requirement)
```

**If these fail:** Mode system needs optimization before release

### Other Modes (SHOULD meet)

```
/rforge:analyze --mode debug:     < 2 minutes (target)
/rforge:analyze --mode optimize:  < 3 minutes (target)
/rforge:analyze --mode release:   < 5 minutes (target)

/rforge:status --mode debug:      < 30 seconds (target)
/rforge:status --mode optimize:   < 1 minute (target)
/rforge:status --mode release:    < 2 minutes (target)
```

**If these fail:** Document actual times, may need optimization

---

## Quality Validation

### Default Mode Quality

**Test:** Introduce known issues and verify detection

```r
# Introduce issues
- Missing dependency in DESCRIPTION
- Outdated documentation
- Failing test
```

**Run:**
```bash
/rforge:analyze --mode default
```

**Expected:**
- Catches missing dependency (critical)
- May/may not catch doc issue (not critical)
- Catches failing test (critical)

**Guarantee:** Should catch 80% of critical issues

---

### Debug Mode Quality

**Test:** Same issues as above

**Run:**
```bash
/rforge:analyze --mode debug
```

**Expected:**
- Catches ALL issues
- Provides detailed traces
- Shows root causes

**Guarantee:** Should catch 95% of all issues

---

### Optimize Mode Quality

**Test:** Identify known slow function

```r
# Known slow function
slow_bootstrap <- function(n = 1000) {
  for (i in 1:n) {
    # Intentionally slow
  }
}
```

**Run:**
```bash
/rforge:analyze --mode optimize
```

**Expected:**
- Identifies slow_bootstrap in top 3-5
- Quantifies impact (e.g., "2.3 seconds")
- Suggests optimization

**Guarantee:** Should identify top bottlenecks

---

### Release Mode Quality

**Test:** Run on package ready for CRAN

**Run:**
```bash
/rforge:analyze --mode release
```

**Expected:**
- R CMD check equivalent
- All test suites run
- Documentation validated
- Breaking changes detected
- Release readiness score

**Guarantee:** Should provide CRAN submission confidence

---

## Documentation Testing

### Command Help Text

```bash
# Test help text (if supported)
/rforge:analyze --help
/rforge:status --help
```

**Expected:**
- Shows available modes
- Shows available formats
- Shows example usage

---

### Error Messages

Test error message quality:

```bash
# Invalid mode
/rforge:analyze --mode invalid

# Invalid format
/rforge:analyze --format invalid
```

**Expected:**
- Clear error message
- Lists valid options
- Shows example usage

---

## User Acceptance Testing

### Test with Real Users

1. **Developer A** (daily development)
   - Use default modes for 1 week
   - Track: frequency of use, satisfaction, issues

2. **Developer B** (debugging)
   - Use debug mode when issues arise
   - Track: usefulness, time saved, issues found

3. **Developer C** (release prep)
   - Use release mode for CRAN submission
   - Track: confidence level, issues caught, time saved

### Feedback Questions

1. Are time budgets appropriate?
2. Is mode selection intuitive?
3. Is output quality sufficient for each mode?
4. Are there missing modes/features?
5. Is backward compatibility seamless?

---

## Regression Testing

### Ensure No Breaking Changes

**Test:** Run all existing workflows

```bash
# These should work EXACTLY as before
/rforge:analyze "Update algorithm"
/rforge:status
/rforge:status medfit
```

**Expected:**
- No changes in behavior
- Same output format
- Same performance

**Critical:** Zero breaking changes

---

## Test Results Template

```markdown
# Mode System Test Results

**Date:** YYYY-MM-DD
**Tester:** [Name]
**Environment:** [RForge MCP version, R version, etc.]

## Phase 1: Command Syntax ✅/❌

- [ ] Commands accept --mode parameter
- [ ] Commands accept --format parameter
- [ ] All 4 modes recognized (default, debug, optimize, release)
- [ ] All 3 formats recognized (json, markdown, terminal)

**Issues:**
- [List any issues]

## Phase 2: Backward Compatibility ✅/❌

- [ ] `/rforge:analyze` works without mode
- [ ] `/rforge:status` works without mode
- [ ] Default behavior unchanged
- [ ] No breaking changes

**Issues:**
- [List any issues]

## Phase 3: Performance ✅/❌

| Command | Mode | Time | Budget | Status |
|---------|------|------|--------|--------|
| analyze | default | X.Xs | < 10s | ✅/❌ |
| analyze | debug | X.Xs | < 2m | ✅/❌ |
| analyze | optimize | X.Xs | < 3m | ✅/❌ |
| analyze | release | X.Xs | < 5m | ✅/❌ |
| status | default | X.Xs | < 5s | ✅/❌ |
| status | debug | X.Xs | < 30s | ✅/❌ |
| status | optimize | X.Xs | < 1m | ✅/❌ |
| status | release | X.Xs | < 2m | ✅/❌ |

**Critical Issues:**
- [Any default mode over budget - MUST FIX]

**Other Issues:**
- [Document actual times if over budget]

## Phase 4: Quality ✅/❌

- [ ] Default mode catches critical issues
- [ ] Debug mode provides detailed traces
- [ ] Optimize mode identifies bottlenecks
- [ ] Release mode validates CRAN readiness

**Issues:**
- [List any quality issues]

## Phase 5: Format Output ✅/❌

- [ ] Terminal format is readable
- [ ] JSON format is valid JSON
- [ ] Markdown format is valid markdown

**Issues:**
- [List any format issues]

## Overall Assessment

**Status:** ✅ Pass / ⚠️ Pass with issues / ❌ Fail

**Summary:**
[Overall assessment of mode system]

**Next Steps:**
[What needs to be done before release]
```

---

## Success Criteria

### Must Pass (Required for Day 1 Completion)

- [x] Commands accept mode parameter
- [x] Commands accept format parameter
- [x] Mode behaviors documented
- [x] Time budgets documented
- [x] Backward compatibility maintained
- [x] Implementation instructions clear

### Should Pass (Required for Week 2 Completion)

- [ ] Default modes meet time budgets (< 10s / < 5s)
- [ ] All modes produce distinct outputs
- [ ] Format options work correctly
- [ ] Quality guarantees met
- [ ] No breaking changes
- [ ] User documentation complete

### Could Pass (Nice to Have)

- [ ] Other modes meet time budgets
- [ ] Edge cases handled gracefully
- [ ] Error messages helpful
- [ ] Help text comprehensive

---

## Notes for Testers

1. **Start with backward compatibility** - Most important
2. **Test default modes first** - Most frequently used
3. **Performance is critical** - Default modes must be fast
4. **Document all issues** - Even minor ones
5. **Real-world scenarios** - Use actual packages when possible

---

**Status:** ✅ Ready for testing
**Updated:** 2024-12-24
**Next:** Run tests and document results
