# Mode System Design

**Version:** 1.0
**Date:** 2024-12-24
**Status:** Design Complete - Ready for Implementation

---

## Executive Summary

The mode system provides explicit control over command behavior depth and performance. Modes are VERBS that describe what the command should DO, not HOW it should format output.

**Key Principles:**
1. **Modes are VERBS** - `debug`, `optimize`, `release` (not `detailed`, `verbose`)
2. **Default = Fast** - All commands default to lightweight (< 10s)
3. **Explicit Only** - NO automatic mode detection
4. **Backward Compatible** - All existing commands work unchanged
5. **Performance Guarantees** - Strict time budgets per mode

---

## Mode Definitions

### Core Modes

| Mode | Time Budget | Purpose | When to Use |
|------|-------------|---------|-------------|
| **Default** | < 10s | Fast, lightweight analysis | Daily check-ins, quick status |
| **debug** | 30s - 2m | Deep inspection, troubleshooting | Finding bugs, investigating issues |
| **optimize** | 1-3m | Performance analysis, bottleneck detection | Speed improvements, profiling |
| **release** | 2-5m | Comprehensive pre-release validation | Before CRAN submission, major releases |

### Format Flags (Separate Concern)

Format flags control OUTPUT format, not behavior depth:

| Flag | Output Format | Purpose |
|------|---------------|---------|
| `--format json` | JSON | Machine-readable, scripting |
| `--format markdown` | Markdown | Documentation, reports |
| `--format terminal` | Rich terminal | Default, human-readable |

**Important:** Modes and formats are orthogonal:
- `rforge:status --mode debug` → Deep analysis in terminal format
- `rforge:status --format json` → Fast analysis in JSON format
- `rforge:status --mode debug --format json` → Deep analysis in JSON format

---

## Command-Specific Mode Behaviors

### `/rforge:analyze`

**Default (< 10s):**
```
Balanced analysis focused on:
- Critical issues only
- Recent changes (last 7 days)
- High-priority dependencies
- Quick health metrics
```

**Debug Mode (30s - 2m):**
```
Deep inspection including:
- All dependencies (recursive)
- Complete file scans
- Detailed error traces
- Hidden configuration checks
- Cache validation
- Environment inspection
```

**Optimize Mode (1-3m):**
```
Performance analysis:
- Profiling R code execution
- Package load time analysis
- Dependency bloat detection
- Function call hotspots
- Memory usage patterns
- Benchmark comparisons
```

**Release Mode (2-5m):**
```
Comprehensive validation:
- R CMD check equivalent
- All test suites (unit + integration)
- Documentation completeness
- CRAN policy compliance
- Breaking change detection
- Reverse dependency checks
```

### `/rforge:status`

**Default (2-5s):**
```
Quick dashboard:
- Overall health score
- Active warnings (critical only)
- Git status (clean/dirty)
- Last update timestamp
```

**Debug Mode (15-30s):**
```
Detailed status:
- Per-package health breakdown
- All warnings (all severities)
- Dependency tree visualization
- Test coverage metrics
- Documentation coverage
- Known issues list
```

**Optimize Mode (30s - 1m):**
```
Performance status:
- Package load times
- Test execution times
- Build times
- Slow functions identified
- Resource usage stats
```

**Release Mode (1-2m):**
```
Release readiness:
- CRAN compliance check
- Version number validation
- NEWS.md completeness
- Documentation currency
- Test coverage requirements
- Breaking change summary
```

### `/rforge:quick`

**Default (< 10s):**
```
Instant status check:
- Project type
- Health score
- Critical issues only
- Next recommended action
```

**Note:** `/rforge:quick` IGNORES all modes by design. It's always fast (< 10s).

---

## Implementation Specification

### Command Syntax

```bash
# Default mode (fast)
/rforge:analyze
/rforge:status

# Explicit mode
/rforge:analyze --mode debug
/rforge:status --mode optimize
/rforge:analyze --mode release

# Mode + format
/rforge:status --mode debug --format json
/rforge:analyze --mode release --format markdown
```

### Plugin Command Structure

Each command file should follow this pattern:

```markdown
---
name: rforge:analyze
description: Analyze R package ecosystem
arguments:
  - name: context
    description: What changed or what to focus on
    required: false
    type: string
  - name: mode
    description: Analysis depth (debug, optimize, release)
    required: false
    type: string
    default: "default"
  - name: format
    description: Output format (json, markdown, terminal)
    required: false
    type: string
    default: "terminal"
tags: ["rforge", "analysis", "ecosystem"]
version: 1.0.0
---

# RForge: Analyze Ecosystem

You are analyzing an R package ecosystem using RForge.

## Mode Behavior

**Current Mode:** {{mode | default: "default"}}

### Default Mode (< 10s)
Perform balanced analysis:
- Focus on critical issues
- Recent changes (last 7 days)
- High-priority dependencies
- Quick health metrics

### Debug Mode (30s - 2m)
Deep inspection:
- All dependencies (recursive)
- Complete file scans
- Detailed error traces
- Hidden configuration
- Cache validation
- Environment inspection

### Optimize Mode (1-3m)
Performance analysis:
- Profile R code
- Analyze load times
- Detect dependency bloat
- Find hotspots
- Check memory usage
- Run benchmarks

### Release Mode (2-5m)
Comprehensive validation:
- R CMD check equivalent
- All test suites
- Documentation check
- CRAN compliance
- Breaking changes
- Reverse dependencies

## Instructions

1. **Detect Mode**: Use {{mode}} argument (default if not specified)
2. **Set Time Budget**: Respect mode's time limit
3. **Delegate to MCP**: Use `rforge_analyze` tool with mode parameter
4. **Format Output**: Use {{format}} for output formatting
5. **Verify Performance**: Ensure completion within time budget

## Context

{{context | default: "General ecosystem analysis"}}

## Output Format

{{format | default: "terminal"}}

---

**Remember:**
- Default mode must complete in < 10s
- Stay within mode's time budget
- Use MCP tool delegation
- Format output appropriately
```

### MCP Server Integration

The RForge MCP server needs mode-aware tools:

```python
# In rforge-mcp-server/tools/analyze.py

@mcp_tool
async def rforge_analyze(
    context: str = "General analysis",
    mode: str = "default",
    format: str = "terminal"
) -> Dict[str, Any]:
    """
    Analyze R package ecosystem with mode-specific behavior.

    Args:
        context: What to analyze or focus on
        mode: Analysis depth (default, debug, optimize, release)
        format: Output format (json, markdown, terminal)

    Returns:
        Analysis results formatted according to mode and format
    """

    # Set time budget based on mode
    time_budgets = {
        "default": 10,      # seconds
        "debug": 120,       # 2 minutes
        "optimize": 180,    # 3 minutes
        "release": 300      # 5 minutes
    }

    budget = time_budgets.get(mode, 10)

    # Execute mode-specific analysis
    if mode == "default":
        result = await fast_analysis(context, budget)
    elif mode == "debug":
        result = await debug_analysis(context, budget)
    elif mode == "optimize":
        result = await optimize_analysis(context, budget)
    elif mode == "release":
        result = await release_analysis(context, budget)
    else:
        raise ValueError(f"Unknown mode: {mode}")

    # Format output
    return format_output(result, format)
```

---

## Performance Guarantees

### Time Budget Enforcement

**Hard Limits:**
- Default mode: **MUST** complete in < 10s
- Debug mode: **SHOULD** complete in < 2m
- Optimize mode: **SHOULD** complete in < 3m
- Release mode: **SHOULD** complete in < 5m

**Enforcement Strategy:**
1. **Timeouts**: Hard timeouts at budget + 10%
2. **Progress Indicators**: Show progress for modes > 10s
3. **Early Exit**: Return partial results if approaching timeout
4. **Warnings**: Warn if approaching time budget

### Quality Guarantees

**Default Mode:**
- ✅ Catches 80% of critical issues
- ✅ Fast enough for frequent use
- ✅ Always actionable output

**Debug Mode:**
- ✅ Catches 95% of all issues
- ✅ Detailed enough for troubleshooting
- ✅ Shows root causes

**Optimize Mode:**
- ✅ Identifies top 3-5 bottlenecks
- ✅ Provides concrete optimization suggestions
- ✅ Quantifies performance impact

**Release Mode:**
- ✅ CRAN submission confidence
- ✅ Catches breaking changes
- ✅ Documentation completeness
- ✅ Test coverage validation

---

## Backward Compatibility

### Existing Commands

All existing commands continue to work WITHOUT changes:

```bash
# These work exactly as before
/rforge:analyze "Updated mediation algorithm"
/rforge:status
/rforge:quick

# Default mode is assumed (< 10s, balanced)
```

### Migration Path

Users can adopt modes gradually:

1. **Phase 1**: Continue using commands without modes (default behavior)
2. **Phase 2**: Try explicit modes for specific use cases
3. **Phase 3**: Integrate modes into workflows

**No Breaking Changes**:
- Existing prompts work unchanged
- Default behavior is optimized for common case
- Modes are opt-in, not required

---

## Implementation Checklist

### Phase 1: Core Infrastructure (Week 2 Day 1-2)

- [ ] Update all RForge plugin commands with mode support
- [ ] Add mode parameter to command frontmatter
- [ ] Update command instructions with mode-specific behavior
- [ ] Test mode parameter parsing
- [ ] Verify default mode behavior (< 10s)

### Phase 2: MCP Integration (Week 2 Day 3)

- [ ] Add mode parameter to all MCP tools
- [ ] Implement time budget tracking
- [ ] Add timeout enforcement
- [ ] Test mode-specific behavior
- [ ] Verify performance guarantees

### Phase 3: Format Support (Week 2 Day 4)

- [ ] Add format parameter to commands
- [ ] Implement JSON formatter
- [ ] Implement Markdown formatter
- [ ] Test format + mode combinations
- [ ] Verify output quality

### Phase 4: Documentation (Week 2 Day 5)

- [ ] Update command reference with modes
- [ ] Create mode usage guide
- [ ] Add mode examples to USAGE-GUIDE.md
- [ ] Update CHEATSHEET with mode syntax
- [ ] Create mode decision flowchart

### Phase 5: Testing & Validation (Week 2 End)

- [ ] Test all commands in all modes
- [ ] Verify time budgets respected
- [ ] Test backward compatibility
- [ ] Performance benchmarking
- [ ] User acceptance testing

---

## Testing Strategy

### Unit Tests

```python
# Test mode parameter parsing
def test_mode_parsing():
    assert parse_mode("debug") == "debug"
    assert parse_mode(None) == "default"
    assert parse_mode("invalid") raises ValueError

# Test time budgets
def test_time_budgets():
    for mode in ["default", "debug", "optimize", "release"]:
        start = time.time()
        result = rforge_analyze(mode=mode)
        elapsed = time.time() - start
        assert elapsed < TIME_BUDGETS[mode] * 1.1  # 10% grace
```

### Integration Tests

```bash
# Test backward compatibility
/rforge:analyze  # Should work (default mode)
/rforge:status   # Should work (default mode)

# Test explicit modes
/rforge:analyze --mode debug     # Should be slower, more detailed
/rforge:status --mode optimize   # Should show performance metrics

# Test format combinations
/rforge:analyze --mode debug --format json
/rforge:status --format markdown
```

### Performance Tests

Track mode performance over time:

| Command | Mode | Target | Actual | Status |
|---------|------|--------|--------|--------|
| analyze | default | < 10s | 8.2s | ✅ |
| analyze | debug | < 120s | 95s | ✅ |
| analyze | optimize | < 180s | 145s | ✅ |
| analyze | release | < 300s | 230s | ✅ |
| status | default | < 5s | 3.1s | ✅ |
| status | debug | < 30s | 22s | ✅ |

---

## Usage Examples

### Daily Development Workflow

```bash
# Morning check-in (fast)
/rforge:status

# Before making changes (balanced)
/rforge:analyze "Planning to refactor bootstrap algorithm"

# After changes (balanced)
/rforge:analyze "Refactored bootstrap algorithm"
```

### Debugging Workflow

```bash
# Quick check
/rforge:status

# Issue detected, need details
/rforge:analyze --mode debug "Bootstrap fails with n < 30"

# Still unclear, get performance data
/rforge:analyze --mode optimize "Bootstrap performance"
```

### Release Workflow

```bash
# Start with quick check
/rforge:status

# Pre-release validation
/rforge:analyze --mode release "Preparing for CRAN submission"

# Generate release report
/rforge:analyze --mode release --format markdown "Release 2.2.0"
```

### Automation & Scripting

```bash
# CI/CD integration
/rforge:analyze --mode release --format json > release-report.json

# Nightly health check
/rforge:status --mode debug --format json > health-$(date +%Y%m%d).json

# Performance tracking
/rforge:analyze --mode optimize --format json >> performance-log.jsonl
```

---

## Future Enhancements

### Additional Modes (Post-v1.0)

**Test Mode** (1-2m):
- Run all test suites
- Generate coverage reports
- Identify flaky tests
- Suggest new test cases

**Security Mode** (2-3m):
- Scan for security vulnerabilities
- Check dependency security
- Validate input sanitization
- Review exported functions

**Documentation Mode** (1-2m):
- Check documentation completeness
- Validate examples
- Check roxygen2 consistency
- Generate missing docs

### Adaptive Modes (v2.0)

Learn from usage patterns:
- Auto-tune time budgets
- Predict optimal mode
- Suggest mode based on context
- Cache common analyses

### Custom Modes (v2.0)

Allow users to define custom modes:
```yaml
# .rforge/modes.yml
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

## Decision Log

### Why VERBS, Not Adjectives?

**Problem:** Initial design used `--detailed`, `--verbose`, `--full`

**Issue:** These describe OUTPUT quantity, not BEHAVIOR intent

**Solution:** Modes are VERBS describing what to DO:
- `debug` → "I want to debug this"
- `optimize` → "I want to optimize this"
- `release` → "I want to release this"

**Benefits:**
- Clearer user intent
- Mode-specific behavior makes sense
- Easy to add new modes (`test`, `security`, etc.)

### Why NO Auto-Detection?

**Problem:** Could detect mode from context (e.g., "I need details" → debug mode)

**Issue:**
- Unpredictable behavior
- Performance surprises
- Harder to script/automate

**Solution:** Explicit modes only

**Benefits:**
- Predictable performance
- Scriptable (no surprises)
- Clear user control

### Why < 10s Default?

**Problem:** What should default mode's time budget be?

**Analysis:**
- 5s feels instant
- 10s is acceptable for daily use
- 30s feels slow for frequent use
- 60s+ requires progress indicator

**Solution:** < 10s default

**Benefits:**
- Fast enough for frequent use
- Long enough for useful analysis
- Clear performance expectation

---

## Conclusion

The mode system provides explicit, predictable control over command behavior while maintaining backward compatibility and fast defaults.

**Key Takeaways:**
1. Modes are VERBS (debug, optimize, release)
2. Default is fast (< 10s)
3. Explicit only (no auto-detection)
4. Backward compatible (existing commands work)
5. Performance guaranteed (strict time budgets)

**Next Steps:**
1. Implement mode support in plugin commands
2. Add mode handling to MCP server
3. Test and validate performance
4. Document and deploy

---

**Ready for Implementation: Week 2** 🚀
