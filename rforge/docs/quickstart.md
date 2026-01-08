# RForge Quick Start Guide

Get started with RForge in 5 minutes. This guide walks you through installation, basic usage, and your first analysis.

## Prerequisites

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

## Installation

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

## Basic Usage

### Quick Status Check (<10 seconds)

```bash
/rforge:status
```

**Example output:**
```
╭──────────────────────────────────────────╮
│ 📊 RForge Status - mypackage             │
├──────────────────────────────────────────┤
│                                          │
│ Health Score: 85/100 ✅                  │
│                                          │
│ 📦 Package: mypackage v0.1.0             │
│ 📂 Path: /path/to/mypackage              │
│ 🌿 Git: main (clean)                     │
│                                          │
│ ✅ Dependencies: 5 packages, all current │
│ ✅ Tests: 42 passing                     │
│ ⚠️  Coverage: 78% (target: 80%)          │
│                                          │
╰──────────────────────────────────────────╯
```

### Analyze Package (<30 seconds)

```bash
/rforge:analyze "Check package health before CRAN submission"
```

This performs:
- Dependency analysis
- Test execution status
- Documentation completeness
- NAMESPACE validation
- Git status check

### Mode System

RForge supports 4 analysis modes with different time budgets:

| Mode | Command | Time | Use Case |
|------|---------|------|----------|
| **default** | `/rforge:status` | <10s | Quick daily checks |
| **debug** | `/rforge:analyze --mode debug` | <120s | Detailed diagnostics |
| **optimize** | `/rforge:analyze --mode optimize` | <180s | Performance analysis |
| **release** | `/rforge:analyze --mode release` | <300s | CRAN preparation |

**Example:**
```bash
# Debug mode for investigating test failures
/rforge:analyze --mode debug "Why are tests failing on CI?"

# Release mode for comprehensive CRAN check
/rforge:analyze --mode release "Prepare for CRAN submission"
```

## Common Workflows

### 1. Daily Development Check

```bash
# Morning check-in
/rforge:status

# If issues found
/rforge:analyze --mode debug "Investigate warnings"
```

### 2. Before Committing Code

```bash
# Quick pre-commit validation
/rforge:status

# Check impact of your changes
/rforge:cascade "Updated base dependency version"
```

### 3. CRAN Preparation

```bash
# Comprehensive release check
/rforge:analyze --mode release "CRAN submission checklist"

# Plan release sequence (for ecosystems)
/rforge:release

# Generate dependency graph
/rforge:deps
```

### 4. Ecosystem Management

```bash
# Detect project structure
/rforge:detect

# Analyze cross-package impact
/rforge:impact "Changed API in base package"

# Plan coordinated updates
/rforge:cascade "Major version bump in dependency"
```

## Output Formats

RForge supports 3 output formats:

### Terminal (Default)
Rich colors, emojis, and formatted tables for human readability.

```bash
/rforge:status
```

### JSON
Machine-readable with metadata envelope for automation.

```bash
/rforge:status --format json > status.json
```

### Markdown
Documentation-ready for reports and READMEs.

```bash
/rforge:status --format markdown > STATUS.md
```

## Project Structure Detection

RForge automatically detects three project types:

### Single Package
```
mypackage/
├── DESCRIPTION
├── NAMESPACE
├── R/
├── man/
└── tests/
```

### Ecosystem (Multiple Packages)
```
my-ecosystem/
├── base-package/
│   └── DESCRIPTION
├── extension-1/
│   └── DESCRIPTION
└── extension-2/
    └── DESCRIPTION
```

### Hybrid (Mixed Content)
```
my-project/
├── packages/
│   ├── pkg-1/DESCRIPTION
│   └── pkg-2/DESCRIPTION
├── analysis/
└── docs/
```

Use `/rforge:detect` to see how RForge categorizes your project.

## Troubleshooting

### "RForge MCP server not found"

**Solution:**
```bash
# Check MCP server status
claude mcp list

# Reconfigure if needed
npx rforge-mcp configure
```

### "Not an R package directory"

**Solution:**
```bash
# Ensure you're in a directory with DESCRIPTION file
ls -la DESCRIPTION

# Or specify package path explicitly
cd /path/to/your-package
```

### "R CMD not found"

**Solution:**
```bash
# Check R is in PATH
which R

# Add R to PATH if needed (macOS/Linux)
export PATH="/usr/local/bin:$PATH"

# Restart Claude Code after updating PATH
```

### Performance Issues

If analysis is slow:

1. **Use faster modes:**

   ```bash
   /rforge:status  # Instead of /rforge:analyze
   ```

2. **Check for large .Rcheck directories:**

   ```bash
   find . -name "*.Rcheck" -type d
   # Remove if found
   rm -rf *.Rcheck
   ```

3. **Limit scope for ecosystems:**

   ```bash
   /rforge:status mypackage  # Specify single package
   ```

## Next Steps

Now that you're set up, explore:

- **[Commands Reference](commands.md)** - All 15 RForge commands
- **[Architecture Guide](architecture.md)** - How RForge works internally
- **[Mode System Guide](../../docs/MODE-USAGE-GUIDE.md)** - Deep dive into modes

## Common Commands Cheat Sheet

```bash
# Status and analysis
/rforge:status                    # Quick health check
/rforge:analyze                   # Balanced analysis
/rforge:quick                     # Ultra-fast (<10s)
/rforge:thorough                  # Comprehensive (2-5min)

# Ecosystem management
/rforge:detect                    # Detect project structure
/rforge:cascade                   # Plan coordinated updates
/rforge:impact                    # Analyze change impact
/rforge:release                   # Plan CRAN release sequence
/rforge:deps                      # Visualize dependencies

# Documentation
/rforge:doc-check                 # Check documentation drift
/rforge:complete                  # Mark tasks complete
/rforge:capture                   # Quick capture ideas
/rforge:next                      # Get next task suggestion

# Health checks
/rforge:ecosystem-health          # Ecosystem health metrics
/rforge:rpkg-check                # R CMD check integration
```

## Getting Help

- **GitHub Issues:** [claude-plugins/issues](https://github.com/Data-Wise/claude-plugins/issues)
- **Documentation Site:** [data-wise.github.io/claude-plugins](https://data-wise.github.io/claude-plugins)
- **npm Package:** [@data-wise/rforge-plugin](https://www.npmjs.com/package/@data-wise/rforge-plugin)
