# Workflow - ADHD-Friendly Automation

> ADHD-friendly workflow automation with 12 commands and auto-activating skills

**Version:** 2.1.0 | **Status:** Production-Ready

ADHD-friendly workflow automation designed for focus, task management, and decision support. Features smart brainstorming, auto-activating skills, and background task delegation.

## Overview

Workflow is an ADHD-optimized productivity toolkit that reduces decision paralysis through intelligent automation, clear structure, and fast feedback. It provides 12 commands spanning brainstorming, focus management, task tracking, and context restoration.

**Key Innovation:** Auto-activating skills that provide just-in-time guidance when relevant topics are discussed, eliminating the need to remember when to invoke specific commands.

## Key Features

### 🎯 Smart Workflow Commands

- **`/brainstorm`** - Smart ideation with auto-delegation
- **`/focus`** - Single-task mode with distraction blocking
- **`/next`** - Decision support for what to work on next
- **`/done`** - Session completion with context capture
- **`/recap`** - Context restoration when returning to work
- **`/stuck`** - Unblock helper with guided problem solving
- **`/refine`** - Prompt optimizer for better AI interactions

### 🤖 Auto-Activating Skills (3 skills)

Skills automatically activate based on conversation context:

- **backend-designer** - Triggers on API/database/auth discussions
- **frontend-designer** - Triggers on UI/UX/component topics
- **devops-helper** - Triggers on CI/CD/deployment/infrastructure

### ⚡ Background Delegation

- Automatically delegates complex analysis to specialized agents
- Agents run in parallel while you continue working
- Results synthesized into unified, actionable recommendations

### 🧠 ADHD-Friendly Design

- **Scannable output** - Visual hierarchy with emojis and clear sections
- **Quick wins** - Always offers <15min tasks
- **Clear next steps** - Numbered, actionable items
- **Reduced decision paralysis** - One clear recommendation with alternatives

## Installation

### From Source

```bash
# Clone repository
git clone https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins/workflow

# Development mode (symlink)
./scripts/install.sh --dev

# Production mode (copy)
./scripts/install.sh
```

### From npm

```bash
npm install -g @data-wise/claude-workflow-plugin
```

### Verify Installation

```bash
# Restart Claude Code, then test
/workflow:next
```

## Quick Start

⏱️ **2 minutes** • 🟢 Beginner • ADHD-optimized

### Daily Workflow

```bash
# Morning: Get next task
/next

# Start focused work
/focus "Implement user authentication"

# Stuck? Get help
/stuck

# Done for the day
/done "Completed auth implementation"

# Tomorrow: Restore context
/recap
```

### Brainstorming Session

```bash
# Quick ideation (< 1 min)
/brainstorm quick "Feature ideas for user dashboard"

# Deep analysis with agents (< 30 min)
/brainstorm thorough "Architecture for real-time notifications"

# Mode-specific brainstorms
/brainstorm feature "User profiles"
/brainstorm architecture "Microservices vs monolith"
/brainstorm design "Mobile-first UI"
```

### Task Management

```bash
# Check background task status
/task-status

# View task output
/task-output task-id

# Cancel running task
/task-cancel task-id
```

## Essential Commands

| Command | Time Budget | What It Does |
|---------|-------------|--------------|
| `/next` | <5s | Recommends ONE task with reasoning |
| `/focus <task>` | N/A | Activates single-task mode |
| `/stuck` | <1min | Guided problem solving (5 Whys) |
| `/done [msg]` | <5s | Captures session achievements |
| `/recap` | <10s | Restores context from previous session |
| `/brainstorm quick` | <60s | Fast ideation without agents |
| `/brainstorm` | <5min | Balanced analysis with agents |
| `/brainstorm thorough` | <30min | Deep analysis with full delegation |

## Brainstorm Modes

### Quick Mode (<1 min)

```bash
/brainstorm quick "Feature ideas"
```

- Fast ideation without delegation
- 3-5 ideas with brief descriptions
- No agent overhead

### Default Mode (<5 min)

```bash
/brainstorm "Feature ideas"
```

- Balanced analysis with light delegation
- 5-7 ideas with trade-offs
- 1-2 agents for validation

### Thorough Mode (<30 min)

```bash
/brainstorm thorough "Architecture design"
```

- Deep analysis with full delegation
- Multiple perspectives (3-4 agents)
- Comprehensive trade-off analysis
- Implementation timeline

## ADHD-Friendly Features

### Scannable Output

```
┌─────────────────────────────────────────────────────────────┐
│ 🎯 SUGGESTED NEXT STEP                                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   [TASK TITLE]                                              │
│                                                             │
│   📁 File: [specific file]                                  │
│   ⏱️  Est. time: [X-Y min]                                   │
│                                                             │
│   Why this? [Brief reason]                                  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ 💡 ALTERNATIVES:                                            │
│    A) [Alternative 1] [time] - [reason]                     │
│    B) [Quick win option] [time] ⚡                          │
└─────────────────────────────────────────────────────────────┘
```

### Quick Wins

Always includes <15min tasks for fast momentum:

- Small improvements
- Documentation updates
- Test additions
- Refactoring opportunities

### Decision Support

Reduces paralysis with:

- ONE clear recommendation
- WHY this task (builds trust)
- 2-3 escape hatches (alternatives)
- Time estimates (planning)

## Use Cases

### Morning Planning

```bash
# What should I work on?
/next

# Clear output:
# 🎯 Suggested: Finish auth tests (30-45 min)
# Why? Unblocked yesterday, maintains momentum
# Alternatives: A) Quick win: Update README (10 min)
```

### Deep Work Session

```bash
# Start focused work
/focus "Implement OAuth flow"

# Output:
# 📍 Focus Mode Activated
# Objective: Implement OAuth flow
# Success: OAuth login working with Google
# Time: 2 hours budgeted
```

### Stuck? Get Unstuck

```bash
# Hit a blocker
/stuck

# Guided problem solving:
# 🤔 Let's debug this...
# 1. What's the immediate blocker?
# 2. What have you tried?
# 3. What's a simpler version?
# 4. Who could help?
# 5. What would success look like?
```

### End of Day

```bash
# Wrap up session
/done "OAuth flow working, tests passing"

# Captures:
# ✅ Achievements: OAuth implementation complete
# 📝 Context: Tests at 85% coverage
# 🔄 Next: Add error handling for edge cases
```

## Next Steps

- **[Commands](commands.md)** - All 12 ADHD-friendly commands
- **[Skills & Agents](skills-agents.md)** - Auto-activating skills and agent delegation
- **ADHD Guide** - Best practices via `/workflow:docs:adhd-guide`

---

**Last Updated:** 2026-01-09
**Document Version:** v2.1.0
**Status:** ✅ Production ready with 12 commands, auto-activating skills, and background delegation
