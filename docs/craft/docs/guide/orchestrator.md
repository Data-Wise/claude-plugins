# Orchestrator Mode

⏱️ **8 minutes** • 🔴 Advanced • ✓ Power user features

> **TL;DR** (30 seconds)
> - **What:** Advanced task orchestrator coordinating multiple agents with 4 execution modes (10s, 2min, 3min, 5min)
> - **Why:** Handle complex multi-step tasks with proper delegation, monitoring, and ADHD-friendly tracking
> - **How:** `/craft:orchestrate "task" [mode]` where mode = default/debug/optimize/release
> - **Next:** Try `/craft:orchestrate "add auth" debug` for verbose execution tracking

## Overview

The orchestrator coordinates multiple agents and tools for complex, multi-step tasks.

!!! warning "Advanced Feature"
    The orchestrator is powerful but complex. Start with simple commands like `/craft:do` and `/craft:check` first. Come back here when you need parallel agent execution.

**Key Features:**
- Mode-aware execution (default/debug/optimize/release)
- Subagent delegation and monitoring
- Chat compression for long sessions
- ADHD-optimized status tracking
- Timeline view of execution

## Basic Usage

```bash
/craft:orchestrate "implement user authentication"
```

The orchestrator will:
1. Analyze the task
2. Create an execution plan
3. Delegate to appropriate agents/commands
4. Monitor progress
5. Report results

## Modes

### Default Mode (<10s)

Quick orchestration for simple tasks:

```bash
/craft:orchestrate "add validation"
```

### Debug Mode (<120s)

Verbose output with detailed logging:

```bash
/craft:orchestrate "fix the bug" debug
```

### Optimize Mode (<180s)

Parallel execution for speed:

```bash
/craft:orchestrate "implement auth" optimize
```

**Benefits:**
- Runs up to 4 agents in parallel
- Faster completion
- Resource-efficient

### Release Mode (<300s)

Comprehensive audit for releases:

```bash
/craft:orchestrate "prep for v2.0 release" release
```

**Includes:**
- Full test suite
- Documentation validation
- Security checks
- Build verification

## Monitoring

### Status Dashboard

```bash
/craft:orchestrate status
```

Shows:
- Active agents
- Completed tasks
- Pending work
- Resource usage

### Timeline View

```bash
/craft:orchestrate timeline
```

Visual timeline of execution steps.

### Budget Tracking

```bash
/craft:orchestrate budget
```

Context usage and remaining capacity.

## Resuming Sessions

If interrupted, resume with:

```bash
/craft:orchestrate continue
```

The orchestrator maintains state and continues from where it left off.

## ADHD-Optimized Features

- **Clear status indicators** - Always know what's happening
- **Progress tracking** - See completion percentage
- **Time estimates** - Know how long tasks will take
- **Session state** - Resume interrupted work easily
- **Compressed chat** - Reduces cognitive load in long sessions

## Next Steps

- [Skills & Agents](skills-agents.md) - Understanding the system
- [Getting Started](getting-started.md) - Basic usage
