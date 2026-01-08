# RForge Commands Reference

Complete reference for all 15 RForge commands. Commands are organized by category with usage examples and parameter details.

## Command Categories

- [Status & Analysis](#status--analysis) (4 commands)
- [Ecosystem Management](#ecosystem-management) (5 commands)
- [Documentation & Tasks](#documentation--tasks) (4 commands)
- [Health Checks](#health-checks) (2 commands)

---

## Status & Analysis

### /rforge:status

Quick ecosystem-wide status dashboard with mode-specific detail levels.

**Usage:**
```bash
/rforge:status [package] [--mode MODE] [--format FORMAT]
```

**Parameters:**
- `package` (optional) - Package name (defaults to current or ecosystem)
- `--mode` (optional) - Status detail level: `default`, `debug`, `optimize`, `release`
- `--format` (optional) - Output format: `terminal`, `json`, `markdown`

**Examples:**
```bash
# Quick health check (default mode)
/rforge:status

# Debug mode for detailed diagnostics
/rforge:status --mode debug

# JSON output for automation
/rforge:status --format json

# Specific package status
/rforge:status mypackage --mode release
```

**Output includes:**
- Health score (0-100)
- Package version and path
- Git status
- Dependencies status
- Test results
- Coverage metrics

**Time budget:** <10s (default), up to 300s (release mode)

---

### /rforge:analyze

Deep analysis with mode system support and intelligent recommendations.

**Usage:**
```bash
/rforge:analyze [description] [--mode MODE] [--format FORMAT]
```

**Parameters:**
- `description` (optional) - What to analyze or focus on
- `--mode` (optional) - Analysis depth: `default`, `debug`, `optimize`, `release`
- `--format` (optional) - Output format: `terminal`, `json`, `markdown`

**Examples:**
```bash
# Balanced analysis
/rforge:analyze "Check package health"

# Debug mode for investigating issues
/rforge:analyze --mode debug "Why are tests failing?"

# Release mode for CRAN preparation
/rforge:analyze --mode release "Prepare for CRAN submission"

# Performance analysis
/rforge:analyze --mode optimize "Identify bottlenecks"
```

**Performs:**
- Pattern recognition (CODE_CHANGE, BUG_FIX, CRAN_RELEASE, etc.)
- Tool selection based on context
- Parallel MCP execution
- Results synthesis with actionable recommendations

**Time budget:** <30s (default), up to 300s (release mode)

---

### /rforge:quick

Ultra-fast status check using only quick tools (<10 seconds).

**Usage:**
```bash
/rforge:quick [description]
```

**Parameters:**
- `description` (optional) - Brief context for the check

**Examples:**
```bash
# Morning stand-up check
/rforge:quick

# Pre-commit validation
/rforge:quick "Before committing changes"
```

**Provides:**
- Basic package info
- Git status
- Critical issues only
- No deep analysis

**Time budget:** <10s (guaranteed)

---

### /rforge:thorough

Comprehensive analysis with R CMD check integration (2-5 minutes).

**Usage:**
```bash
/rforge:thorough [description]
```

**Parameters:**
- `description` (optional) - Analysis context

**Examples:**
```bash
# Full CRAN preparation
/rforge:thorough "Prepare for CRAN submission"

# Deep quality audit
/rforge:thorough "Pre-release audit"
```

**Includes:**
- R CMD check execution
- Full dependency tree analysis
- Complete test suite with coverage
- Documentation completeness check
- All quality metrics

**Time budget:** 2-5 minutes

---

## Ecosystem Management

### /rforge:detect

Auto-detect project structure (single package, ecosystem, or hybrid).

**Usage:**
```bash
/rforge:detect
```

**No parameters**

**Examples:**
```bash
# Detect current directory structure
/rforge:detect
```

**Output:**
- Project type: single, ecosystem, or hybrid
- Package count and names
- Directory structure summary
- Dependency relationships

---

### /rforge:cascade

Plan coordinated updates across dependent packages.

**Usage:**
```bash
/rforge:cascade [description]
```

**Parameters:**
- `description` (optional) - What's changing and why

**Examples:**
```bash
# Plan update cascade
/rforge:cascade "Update base package dependency from v1 to v2"

# Version bump cascade
/rforge:cascade "Major version bump in core package"
```

**Analyzes:**
- Dependency graph
- Update order (respecting dependencies)
- Breaking changes impact
- Test coverage for affected packages

---

### /rforge:impact

Analyze change impact across ecosystem packages.

**Usage:**
```bash
/rforge:impact [description]
```

**Parameters:**
- `description` (optional) - What changed

**Examples:**
```bash
# API change impact
/rforge:impact "Changed function signature in base package"

# Dependency update impact
/rforge:impact "Updated ggplot2 to v3.5.0"
```

**Reports:**
- Affected packages
- Breaking vs non-breaking changes
- Required updates
- Test implications

---

### /rforge:release

Plan CRAN submission sequence based on dependencies.

**Usage:**
```bash
/rforge:release
```

**No parameters**

**Examples:**
```bash
# Generate release plan
/rforge:release
```

**Provides:**
- Submission order (base packages first)
- Pre-submission checklist per package
- Version compatibility check
- Timeline estimate

---

### /rforge:deps

Build and visualize dependency graph across R package ecosystem.

**Usage:**
```bash
/rforge:deps [--format FORMAT]
```

**Parameters:**
- `--format` (optional) - Output format: `terminal`, `json`, `mermaid`

**Examples:**
```bash
# Terminal visualization
/rforge:deps

# Mermaid diagram for documentation
/rforge:deps --format mermaid > deps.mmd

# JSON for programmatic use
/rforge:deps --format json
```

**Output:**
- Dependency graph (directed acyclic graph)
- Import vs Suggest relationships
- Circular dependency detection
- External dependencies

---

## Documentation & Tasks

### /rforge:doc-check

Check for documentation drift and inconsistencies across packages.

**Usage:**
```bash
/rforge:doc-check
```

**No parameters**

**Examples:**
```bash
# Check documentation status
/rforge:doc-check
```

**Validates:**
- Exported functions have documentation
- Examples are runnable
- NAMESPACE consistency with documentation
- Version numbers match across files

---

### /rforge:complete

Mark tasks complete with automatic documentation cascade.

**Usage:**
```bash
/rforge:complete [task_description]
```

**Parameters:**
- `task_description` (optional) - What was completed

**Examples:**
```bash
# Mark task complete
/rforge:complete "Implemented bootstrap CI method"

# Trigger doc cascade
/rforge:complete "Fixed critical bug in mediation function"
```

**Actions:**
- Updates task tracking
- Triggers documentation updates
- Updates CHANGELOG if configured
- Git commit prompt (optional)

---

### /rforge:capture

Quick capture ideas and tasks for later (with automatic doc cascade detection).

**Usage:**
```bash
/rforge:capture [idea]
```

**Parameters:**
- `idea` (required) - What to capture

**Examples:**
```bash
# Capture feature idea
/rforge:capture "Add support for weighted mediation"

# Capture bug note
/rforge:capture "Edge case: NA handling in bootstrap"
```

**Stores:**
- Idea with timestamp
- Context (current package, branch)
- Suggested next actions

---

### /rforge:next

Get ecosystem-aware next task recommendation.

**Usage:**
```bash
/rforge:next
```

**No parameters**

**Examples:**
```bash
# Get next task suggestion
/rforge:next
```

**Considers:**
- Unfinished tasks
- Blocking issues
- Dependency order
- Quick wins
- Priority indicators

**Output:**
- ONE recommended task
- WHY this task (reasoning)
- Time estimate
- 2-3 alternatives

---

## Health Checks

### /rforge:ecosystem-health

Comprehensive ecosystem health metrics with visual dashboard.

**Usage:**
```bash
/rforge:ecosystem-health [--format FORMAT]
```

**Parameters:**
- `--format` (optional) - Output format: `terminal`, `json`, `markdown`

**Examples:**
```bash
# Visual health dashboard
/rforge:ecosystem-health

# JSON metrics
/rforge:ecosystem-health --format json
```

**Metrics:**
- Overall health score (0-100)
- Per-package scores
- Test coverage distribution
- Dependency freshness
- Documentation completeness

---

### /rforge:rpkg-check

R CMD check integration with detailed error reporting.

**Usage:**
```bash
/rforge:rpkg-check [package]
```

**Parameters:**
- `package` (optional) - Package to check (defaults to current)

**Examples:**
```bash
# Check current package
/rforge:rpkg-check

# Check specific package
/rforge:rpkg-check mypackage
```

**Executes:**
- R CMD check with standard flags
- Parses output for errors/warnings/notes
- Categorizes issues
- Suggests fixes

**Note:** This can take 1-5 minutes depending on package size.

---

## Command Categories Summary

### By Time Budget

| Time | Commands |
|------|----------|
| <10s | `status`, `quick`, `detect`, `deps` (visual), `next` |
| <30s | `analyze` (default), `cascade`, `impact`, `doc-check` |
| <2min | `analyze` (debug/optimize) |
| <5min | `thorough`, `analyze` (release), `rpkg-check` |

### By Use Case

**Daily Development:**
- `/rforge:status` - Morning check-in
- `/rforge:next` - What to work on
- `/rforge:quick` - Pre-commit validation

**Feature Development:**
- `/rforge:analyze` - Check implementation impact
- `/rforge:impact` - Assess ecosystem effects
- `/rforge:complete` - Mark features done

**Release Preparation:**
- `/rforge:analyze --mode release` - Full audit
- `/rforge:thorough` - Comprehensive checks
- `/rforge:release` - Plan submission order
- `/rforge:rpkg-check` - R CMD check execution

**Ecosystem Management:**
- `/rforge:detect` - Understand structure
- `/rforge:deps` - Visualize dependencies
- `/rforge:cascade` - Plan coordinated updates
- `/rforge:ecosystem-health` - Overall metrics

## Global Flags

All analysis commands support:

**Mode flags:**
- `--mode default` - Quick analysis (<10s)
- `--mode debug` - Detailed diagnostics (<120s)
- `--mode optimize` - Performance focus (<180s)
- `--mode release` - Comprehensive audit (<300s)

**Format flags:**
- `--format terminal` - Rich colors and emojis (default)
- `--format json` - Machine-readable with metadata
- `--format markdown` - Documentation-ready

**Example:**
```bash
/rforge:analyze --mode release --format markdown > analysis.md
```

## See Also

- **[Quick Start Guide](quickstart.md)** - Getting started with RForge
- **[Architecture Guide](architecture.md)** - How RForge works
- **[Mode System Guide](../../docs/MODE-USAGE-GUIDE.md)** - Deep dive into modes
- **[Format Examples](../../docs/FORMAT-EXAMPLES.md)** - Output format samples
