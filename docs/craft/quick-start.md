# Craft - Full-Stack Developer Toolkit

> Full-stack toolkit with 67 commands, 17 skills, and 7 agents

**Version:** 1.10.0 | **Status:** Active Development

Comprehensive production-ready toolkit for Claude Code featuring smart orchestration, ADHD-friendly workflows, multi-agent coordination, and complete documentation coverage.

**Components:** 67 commands | 17 skills | 7 agents

## Overview

Craft is a full-stack developer toolkit that provides intelligent orchestration across 13 command categories. It excels at automating complex development workflows through smart delegation, parallel execution, and mode-aware operations.

**Key Innovation:** Universal `/craft:do` command that uses AI to route tasks to appropriate workflows, eliminating the need to memorize specific commands.

## Key Features

### 🎯 Smart Commands

- **`/craft:do <task>`** - Universal command that routes to appropriate workflow
- **`/craft:orchestrate <task>`** - Multi-agent orchestrator with context tracking
- **`/craft:check`** - Pre-flight checks for commits, PRs, and releases
- **`/craft:help`** - Context-aware help and suggestions

### 🔧 13 Command Categories

1. **Architecture** (arch) - System design and analysis
2. **CI/CD** (ci) - GitHub Actions workflow generation
3. **Code** (code) - Linting and quality checks
4. **Distribution** (dist) - Homebrew and package publishing
5. **Documentation** (docs) - Mermaid diagrams and API docs
6. **Git** (git) - Worktree management and cleanup
7. **Plan** (plan) - Task planning and breakdowns
8. **Site** (site) - Static site generation
9. **Test** (test) - Test running and coverage

### ⚡ Mode System

Four execution modes for different use cases:

- **default** (<10s) - Quick checks and validation
- **debug** (<120s) - Verbose output with traces
- **optimize** (<180s) - Parallel execution for performance
- **release** (<300s) - Comprehensive audit and validation

### 🤖 Orchestrator v2

Enhanced multi-agent orchestration with:

- Mode-aware execution (optimize, release modes)
- Context tracking and budget monitoring
- Timeline view of agent execution
- Subagent monitoring and coordination

### 🧠 ADHD-Friendly Design

- Fast feedback with progress indicators
- Clear structure and visual hierarchy
- Reduced decision paralysis
- Context-aware suggestions

## Installation

⏱️ **30 seconds** • 🟢 Beginner • ✓ 4 steps

### Quick Install

```bash
# One-command installation
curl -fsSL https://raw.githubusercontent.com/Data-Wise/claude-plugins/main/craft/install.sh | bash
```

**Then restart Claude Code to load the plugin.**

### Alternative Methods

=== "npm (when published)"

    ```bash
    npm install -g @data-wise/claude-craft-plugin
    ```

=== "Development Mode"

    ```bash
    cd craft
    ./scripts/install.sh --dev
    ```

=== "Manual Installation"

    ```bash
    git clone https://github.com/Data-Wise/claude-plugins.git
    cp -r claude-plugins/craft ~/.claude/plugins/
    ```

### Verify Installation

```bash
/craft:hub
```

Expected output:

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:hub - Command Discovery                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 67 commands available across 13 categories                  │
│                                                             │
│ [Command listing...]                                        │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### Universal Command (Most Powerful)

```bash
# Let AI route to best workflow
/craft:do "add user authentication"
/craft:do "optimize database queries"
/craft:do "prepare for release"
```

The `/craft:do` command uses AI to understand your intent and automatically routes to the appropriate workflow. No need to memorize specific commands!

### Pre-Flight Checks

```bash
# Quick validation
/craft:check

# Release audit
/craft:check --for release
```

### Context-Aware Help

```bash
# Project-specific suggestions
/craft:help

# Deep dive into category
/craft:help testing
/craft:help architecture
```

### Orchestrated Workflows

```bash
# Multi-agent orchestration
/craft:orchestrate "add user authentication"

# With specific mode
/craft:orchestrate "prepare release" release

# Monitor progress
/craft:orchestrate status
/craft:orchestrate timeline
```

## Common Workflows

### Example 1: Pre-Commit Workflow

```bash
# Quick validation before commit
/craft:check

# Or use universal command
/craft:do "check if ready to commit"
```

### Example 2: Generate CI/CD Workflow

```bash
# Detect project and generate GitHub Actions
/craft:ci:generate

# Validate existing workflow
/craft:ci:validate
```

### Example 3: Prepare for Release

```bash
# Comprehensive release preparation
/craft:orchestrate "prepare for release" release

# Or use universal command
/craft:do "prepare for CRAN release"
```

### Example 4: Create Documentation

```bash
# Generate Mermaid diagrams
/craft:docs:mermaid

# Create API documentation
/craft:docs:api-documenter
```

## Essential Commands Cheatsheet

| Command | What It Does |
|---------|--------------|
| `/craft:do <task>` | Universal AI-routed task execution |
| `/craft:orchestrate <task>` | Multi-agent orchestration |
| `/craft:check` | Pre-flight validation |
| `/craft:help` | Context-aware help |
| `/craft:hub` | Discover all commands |

## ADHD-Friendly Tips

1. **Start with `/craft:do`** - Don't try to memorize all 67 commands
2. **Use `/craft:help`** when stuck - Get context-aware suggestions
3. **Try `/craft:check`** before commits - Catch issues early
4. **Explore `/craft:hub`** - Discover commands as needed

## Next Steps

- **[Commands](commands.md)** - Complete command reference (67 commands)
- **[Skills & Agents](skills-agents.md)** - Auto-activating skills and agents
- **[Orchestrator](orchestrator.md)** - Deep dive into multi-agent orchestration
- **[Architecture](architecture.md)** - Technical implementation details

---

**Last Updated:** 2026-01-09
**Document Version:** v1.10.0
**Status:** ✅ Active development with 67 commands, 17 skills, and 7 agents
