# RForge - R Package Ecosystem Management

> Complete R package ecosystem orchestrator with 15 commands

**Version:** 1.1.0 | **Status:** Production-Ready | **Tests:** 292 passing

Complete R package ecosystem orchestrator with intelligent auto-delegation, parallel execution, and comprehensive analysis capabilities.

## Overview

RForge is a comprehensive R package development toolkit that automatically analyzes R packages and ecosystems by intelligently delegating to MCP tools and synthesizing results. It provides 15 commands spanning ecosystem management, dependency analysis, release planning, and health monitoring.

**Key Innovation:** Auto-delegation orchestrator that recognizes task patterns, selects appropriate tools, executes them in parallel, and synthesizes actionable summaries.

## Key Features

### 🎯 Intelligent Orchestration

- **Auto-delegation** - Recognizes task patterns (CODE_CHANGE, BUG_FIX, CRAN_RELEASE, etc.)
- **Parallel execution** - Calls multiple MCP tools simultaneously (4 tools × 8 sec = 8 sec total, not 32 sec!)
- **Smart synthesis** - Combines results into actionable summary with next steps

### ⚡ Mode System

Four analysis modes with time budgets:

- **default** (<10s) - Quick status checks and basic validation
- **debug** (<120s) - Detailed diagnostics and issue investigation
- **optimize** (<180s) - Performance profiling and optimization analysis
- **release** (<300s) - Full CRAN preparation with comprehensive checks

### 📊 Output Formats

- **terminal** - Rich colors, emojis, and formatted tables
- **json** - Machine-readable with ISO 8601 timestamps
- **markdown** - Documentation-ready with code blocks

### 🔧 Ecosystem Management

- Auto-detect project structure (single package, ecosystem, or hybrid)
- Dependency analysis and cascade updates
- Cross-package impact assessment
- Release sequencing based on dependencies

## Installation

### Prerequisites

Before installing RForge, ensure you have:

1. **Claude Code** - RForge is a Claude Code plugin

   ```bash
   # Check Claude Code version
   claude --version
   ```

2. **R Environment** (>= 4.0.0)

   ```bash
   # Check R version
   R --version
   ```

3. **Required R Packages**

   ```r
   # Install in R
   install.packages(c("devtools", "testthat"))

   # Optional (for coverage)
   install.packages("covr")
   ```

### Step 1: Install RForge MCP Server

The RForge plugin delegates to an MCP server for R package analysis:

```bash
npx rforge-mcp configure
```

This will:

- Install the RForge MCP server
- Configure Claude Code to use it
- Set up necessary R environment variables

### Step 2: Install RForge Plugin

```bash
# Via npm (recommended)
npm install -g @data-wise/rforge-plugin

# Or from source (development)
git clone https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins/rforge
./scripts/install.sh --dev
```

### Step 3: Restart Claude Code

```bash
# Exit and restart Claude Code
# The plugin will be automatically loaded
```

### Step 4: Verify Installation

```bash
# Navigate to any R package directory
cd ~/path/to/your-r-package

# Run a quick status check
/rforge:status
```

You should see output showing your package health status. If you get an error, check that:

- The RForge MCP server is configured (`claude mcp list`)
- You're in an R package directory (has `DESCRIPTION` file)
- R is accessible in your PATH

## Quick Start Examples

### Example 1: Check Package Health

```bash
# Navigate to your R package
cd ~/my-r-package

# Quick health check (default mode, <10s)
/rforge:status

# Output:
# 📦 Package: mypackage (v0.1.0)
# ✅ Health Score: 85/100
# 📊 15 functions, 12 tests, 92% coverage
# ⚠️  2 warnings, 0 errors
```

### Example 2: Analyze with Debug Mode

```bash
# Detailed diagnostics (debug mode, <120s)
/rforge:analyze debug

# Output includes:
# - Detailed dependency analysis
# - Code quality metrics
# - Test coverage breakdown
# - Performance profiling
```

### Example 3: Prepare for CRAN Release

```bash
# Comprehensive CRAN preparation (release mode, <300s)
/rforge:analyze release

# Output includes:
# - Full R CMD check results
# - Documentation completeness
# - CRAN policy compliance
# - Release checklist
```

### Example 4: Ecosystem Analysis

```bash
# Detect and analyze ecosystem structure
/rforge:detect

# For multi-package repos:
/rforge:cascade "update dependency"

# Analyze impact across packages
/rforge:impact --format json
```

## Common Workflows

### New Package Setup

1. Create R package structure
2. Run `/rforge:detect` to confirm structure
3. Run `/rforge:status` for initial health check
4. Address any issues flagged

### Pre-Commit Workflow

1. Run `/rforge:analyze default` for quick validation (<10s)
2. Review health score and warnings
3. Fix any critical issues
4. Commit changes

### CRAN Submission Workflow

1. Run `/rforge:analyze release` for comprehensive checks
2. Review all CRAN policy compliance items
3. Run `/rforge:release` to plan submission sequence (for ecosystems)
4. Address all warnings and notes
5. Submit to CRAN

## Next Steps

- **[Commands](commands.md)** - Complete command reference
- **[Architecture](architecture.md)** - Technical implementation details
- **[Mode System](../MODE-USAGE-GUIDE.md)** - Deep dive into analysis modes

---

**Last Updated:** 2026-01-09
**Document Version:** v1.1.0
**Status:** ✅ Production ready with Mode System and 292 passing tests
