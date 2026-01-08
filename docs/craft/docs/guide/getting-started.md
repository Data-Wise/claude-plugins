# Getting Started with Craft

⏱️ **10 minutes** • 🟡 Intermediate • ✓ Complete guide

> **TL;DR** (30 seconds)
> - **What:** Complete guide to installing and using craft's 69 commands, 17 skills, and 7 agents
> - **Why:** Master the full-stack toolkit to automate your entire development workflow
> - **How:** Install plugin → verify with `/craft:hub` → start with `/craft:do "task"`
> - **Next:** Read about [Skills & Agents](skills-agents.md) to understand AI automation

Complete guide to using the craft plugin for Claude Code.

## Installation

!!! abstract "Progress: Step 1/5"
    Installing craft - choose your method

### Method 1: Claude Code Plugin System

```bash
claude plugin install craft@local-plugins
```

### Method 2: Symlink

```bash
ln -s ~/projects/dev-tools/claude-plugins/craft ~/.claude/plugins/craft
```

## Verify Installation

!!! abstract "Progress: Step 2/5"
    Verify everything works

```bash
/craft:hub
```

You should see all 69 commands listed.

## Your First Commands

!!! abstract "Progress: Step 3/5"
    Try these 4 essential commands

### 1. Universal Task Execution

```bash
/craft:do "add user authentication"
```

The AI routes your task automatically.

### 2. Pre-Flight Checks

Before committing code:

```bash
/craft:check
```

Before creating a PR:

```bash
/craft:check --for pr
```

Before releasing:

```bash
/craft:check --for release
```

### 3. Documentation

Update all documentation:

```bash
/craft:docs:update
```

Check for stale docs:

```bash
/craft:docs:sync
```

### 4. Create a Documentation Site

```bash
/craft:site:create --preset data-wise --quick
```

## Understanding the System

!!! abstract "Progress: Step 4/5"
    Learn the 3-layer architecture

Craft has three levels of automation:

1. **Commands** (69 total) - Direct actions
2. **Skills** (17 total) - Auto-triggered expertise
3. **Agents** (7 specialized) - Long-running tasks

When you use `/craft:do`, the system determines which combination to use.

## Next Steps

!!! abstract "Progress: Step 5/5 - Complete! 🎉"
    Continue your journey

- [Skills & Agents](skills-agents.md) - Understanding the AI system
- [Orchestrator](orchestrator.md) - Advanced mode-aware execution
- [Commands Overview](../commands/overview.md) - Explore all commands
