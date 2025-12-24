---
name: rforge:analyze
description: Analyze R package ecosystem with mode-specific behavior depth
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
version: 2.0.0
---

# /rforge:analyze - Mode-Aware R Package Analysis

Analyze R package ecosystem with explicit control over analysis depth and performance.

## Mode System

**Current Mode:** {{mode | default: "default"}}

### Mode Selection

Parse the user's request to detect mode:
- If user explicitly provides "debug", "optimize", or "release" → use that mode
- Otherwise → use "default" mode (fast, balanced)

### Default Mode (< 10 seconds)

**Purpose:** Daily check-ins, quick status validation

**Behavior:**
- Focus on critical issues only
- Recent changes (last 7 days)
- High-priority dependencies
- Quick health metrics
- Balanced, actionable output

**Tools:** `rforge_detect`, `rforge_status`, `rforge_quick_health`

**Time Budget:** MUST complete in < 10 seconds

**Output:**
- Critical issues highlighted
- Health score
- Next recommended action
- Quick summary

### Debug Mode (30s - 2 minutes)

**Purpose:** Finding bugs, investigating issues, troubleshooting

**Behavior:**
- Deep inspection of all components
- All dependencies (recursive analysis)
- Complete file scans (R/, tests/, vignettes/)
- Detailed error traces with stack traces
- Hidden configuration checks
- Cache validation
- Environment inspection

**Tools:** All RForge MCP tools with detailed flags

**Time Budget:** SHOULD complete in < 2 minutes

**Output:**
- Detailed error traces
- Complete dependency tree
- Per-file analysis
- Hidden issues revealed
- Root cause identification

### Optimize Mode (1-3 minutes)

**Purpose:** Speed improvements, performance tuning, bottleneck detection

**Behavior:**
- Profile R code execution
- Package load time analysis
- Dependency bloat detection
- Function call hotspots
- Memory usage patterns
- Benchmark comparisons
- Test execution time analysis

**Tools:** `rforge_profile`, performance benchmarks, load time analysis

**Time Budget:** SHOULD complete in < 3 minutes

**Output:**
- Top 3-5 bottlenecks identified
- Concrete optimization suggestions
- Quantified performance impact
- Before/after projections

### Release Mode (2-5 minutes)

**Purpose:** Pre-release validation, CRAN preparation, major releases

**Behavior:**
- Comprehensive validation (R CMD check equivalent)
- All test suites (unit + integration)
- Documentation completeness check
- CRAN policy compliance validation
- Breaking change detection
- Reverse dependency checks
- NEWS.md and version validation

**Tools:** `rforge_validate`, `rforge_test_all`, CRAN checks

**Time Budget:** SHOULD complete in < 5 minutes

**Output:**
- CRAN submission confidence level
- Breaking changes documented
- Documentation completeness
- Test coverage validation
- Release readiness score

## Implementation Instructions

You are orchestrating the analysis using RForge MCP tools. Follow this workflow:

### Step 1: Detect Mode

```
If user provides --mode argument:
    mode = argument value
Else if user mentions "debug", "debugging", "investigate" in context:
    mode = "debug"
Else if user mentions "optimize", "performance", "slow" in context:
    mode = "optimize"
Else if user mentions "release", "CRAN", "submit" in context:
    mode = "release"
Else:
    mode = "default"
```

### Step 2: Set Time Budget

```
time_budgets = {
    "default": 10 seconds,
    "debug": 120 seconds,
    "optimize": 180 seconds,
    "release": 300 seconds
}

Start timer
```

### Step 3: Execute Mode-Specific Analysis

**For Default Mode:**
1. Call `rforge_detect` to find packages
2. Call `rforge_status` for quick health
3. Identify critical issues only
4. Return actionable summary

**For Debug Mode:**
1. Call all analysis tools with detailed flags
2. Recursive dependency analysis
3. Complete file scans
4. Detailed error traces
5. Environment diagnostics

**For Optimize Mode:**
1. Call `rforge_profile` for performance data
2. Analyze load times
3. Identify slow functions
4. Check memory usage
5. Benchmark critical paths

**For Release Mode:**
1. Call `rforge_validate` for CRAN checks
2. Run complete test suite
3. Check documentation completeness
4. Validate NEWS.md and version
5. Check reverse dependencies

### Step 4: Format Output

Use the {{format}} parameter (default: "terminal"):

- **terminal**: Rich formatted output with emojis, colors, structure
- **json**: Machine-readable JSON for scripting
- **markdown**: Documentation-friendly markdown

### Step 5: Verify Time Budget

If approaching time budget:
- Return partial results with warning
- Suggest running in background (for longer modes)
- Show what was checked and what was skipped

## Context

{{context | default: "General ecosystem analysis"}}

## Usage Examples

### Basic Usage (Default Mode)

```bash
/rforge:analyze "Updated bootstrap algorithm"
# Fast analysis in < 10s, focused on critical issues
```

### Explicit Mode

```bash
/rforge:analyze "Fix bootstrap NA handling" --mode debug
# Deep inspection in < 2m, detailed traces

/rforge:analyze --mode optimize
# Performance analysis in < 3m, find bottlenecks

/rforge:analyze "Prepare for CRAN" --mode release
# Comprehensive validation in < 5m, release readiness
```

### Mode + Format

```bash
/rforge:analyze --mode debug --format json
# Debug analysis with JSON output for scripting

/rforge:analyze --mode release --format markdown
# Release validation with markdown report
```

## Backward Compatibility

All existing usage patterns continue to work without changes:

```bash
/rforge:analyze "Update algorithm"  # Uses default mode
/rforge:analyze                     # Uses default mode
```

**No breaking changes** - default mode provides fast, balanced analysis.

## Performance Guarantees

- **Default mode**: MUST complete in < 10 seconds (hard requirement)
- **Debug mode**: SHOULD complete in < 2 minutes (target)
- **Optimize mode**: SHOULD complete in < 3 minutes (target)
- **Release mode**: SHOULD complete in < 5 minutes (target)

If a mode exceeds its time budget:
1. Return partial results
2. Show warning about timeout
3. Explain what was checked and what was skipped
4. Suggest optimization or breaking into smaller checks

## Quality Guarantees

- **Default**: Catches 80% of critical issues, always actionable
- **Debug**: Catches 95% of all issues, shows root causes
- **Optimize**: Identifies top 3-5 bottlenecks with quantified impact
- **Release**: Provides CRAN submission confidence

## Output Format

{{format | default: "terminal"}}

## ADHD-Friendly Features

✅ **Fast by default** - Results in < 10 seconds (default mode)
✅ **Explicit control** - Choose depth vs speed tradeoff
✅ **Predictable** - Know what to expect from each mode
✅ **Actionable** - Always suggests next steps
✅ **Interruptible** - Can cancel long-running modes

## Related Commands

- `/rforge:status` - Quick status check (also mode-aware)
- `/rforge:quick` - Ultra-fast analysis (always < 10s, ignores modes)
- `/rforge:plan` - Generate implementation plan from analysis
- `/rforge:cascade` - Cascade dependency updates

## Troubleshooting

**"Analysis too slow"**
- Default mode should be < 10s - if not, report as bug
- Use default mode for daily checks
- Reserve debug/optimize/release for specific needs

**"Not enough detail"**
- Use --mode debug for detailed inspection
- Default mode focuses on critical issues only

**"Mode not recognized"**
- Valid modes: default, debug, optimize, release
- Mode names are case-insensitive
- Check spelling

---

## Implementation Notes for Claude

When executing this command:

1. **Parse mode** from user request (explicit flag or context clues)
2. **Respect time budget** - default mode MUST be < 10s
3. **Use Task tool** for delegation to RForge MCP with mode parameter
4. **Format appropriately** based on format parameter
5. **Always verify** results are actionable
6. **Track timing** and warn if approaching budget
7. **Maintain backward compatibility** - no mode = default mode

**Remember:**
- Default mode is optimized for frequent use
- Mode names are VERBS describing intent
- NO automatic mode detection (explicit only, except context hints)
- Always provide next steps based on findings

**Example Task Delegation:**

```
Use Task tool to delegate to RForge MCP tools:
- Mode: {{mode}}
- Context: {{context}}
- Time Budget: {{time_budget}}
- Focus: [mode-specific focus areas]
- Output Format: {{format}}
```

---

**Version 2.0.0** - Mode System Implementation
**Updated:** 2024-12-24
**Status:** ✅ Ready for use
