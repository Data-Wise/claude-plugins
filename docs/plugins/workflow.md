# Workflow - ADHD-Friendly Automation

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

### 📊 Multiple Output Formats
- **terminal** - Rich colors and formatted output
- **json** - Machine-readable for automation
- **markdown** - Documentation-ready

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

## Core Commands

### Workflow Commands (7)

**`/brainstorm [mode] [topic]`**
- Smart ideation with auto-delegation
- Modes: quick (<1min), default (<5min), thorough (<30min)
- Auto-detects: feature, architecture, design

**`/focus <task>`**
- Single-task mode with distraction blocking
- Sets clear objective and success criteria
- Tracks time and provides milestone reminders

**`/next`**
- Decision support for what to work on next
- Analyzes .STATUS file and recent context
- Suggests ONE task with reasoning + alternatives

**`/done [message]`**
- Session completion with context capture
- Prompts for achievements and blockers
- Updates .STATUS file automatically

**`/recap`**
- Context restoration for returning to work
- Reviews recent commits and .STATUS
- Suggests where to resume

**`/stuck`**
- Unblock helper with guided problem solving
- 5 Why analysis
- Suggests alternative approaches

**`/refine <prompt>`**
- Prompt optimizer for better AI interactions
- Improves clarity and specificity
- Suggests better phrasing

### Task Management (3)

**`/task-status`**
- Check progress of background tasks
- View agent execution status
- Estimate completion time

**`/task-output <task-id>`**
- View results from completed background task
- Formatted synthesis of agent outputs
- Actionable recommendations

**`/task-cancel <task-id>`**
- Cancel running background task
- Clean up resources
- Report partial results if available

### Documentation (1)

**`/workflow:docs:adhd-guide`**
- Best practices for ADHD-friendly development
- Workflow optimization strategies
- Tool configuration tips

## Auto-Activating Skills

Skills trigger automatically based on conversation keywords:

### backend-designer

**Triggers:**
- API design, REST, GraphQL
- Database schema, SQL, migrations
- Authentication, authorization
- Caching, performance

**Provides:**
- Pragmatic backend patterns
- "Solid indie" architecture advice
- Scalability considerations

**Delegates to:**
- backend-architect agent
- database-architect agent
- security-specialist agent

### frontend-designer

**Triggers:**
- UI/UX design
- Component architecture
- React, Vue, Svelte
- Accessibility (a11y)
- Responsive design

**Provides:**
- ADHD-friendly design patterns
- Component structure recommendations
- Accessibility guidance

**Delegates to:**
- ux-ui-designer agent
- frontend-specialist agent

### devops-helper

**Triggers:**
- CI/CD, GitHub Actions
- Deployment, hosting
- Docker, containers
- Infrastructure, cloud

**Provides:**
- Platform recommendations
- Cost optimization
- Indie-friendly DevOps patterns

**Delegates to:**
- devops-engineer agent
- performance-engineer agent

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

## Time Budgets

All modes have explicit time guarantees:

| Mode | Time Budget | Use Case |
|------|-------------|----------|
| **quick** | <60s | Fast ideation, status checks |
| **default** | <5min | Balanced analysis |
| **thorough** | <30min | Deep analysis with agents |

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

### Clear Next Steps

Numbered, actionable items:
1. [ ] Immediate action (this session)
2. [ ] Follow-up (next session)
3. [ ] Future consideration (backlog)

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

## Documentation

- **Commands Reference:** [workflow/docs/commands.md](../../workflow/docs/commands.md) *(coming soon)*
- **ADHD Guide:** Available via `/workflow:docs:adhd-guide`
- **Skills & Agents:** [workflow/docs/skills-agents.md](../../workflow/docs/skills-agents.md) *(coming soon)*

## Related

- **[Craft Plugin](craft.md)** - Full-stack developer toolkit
- **[Plugin Development](../PLUGIN-DEVELOPMENT.md)** - Creating workflow plugins

## Support

- **GitHub Issues:** [https://github.com/Data-Wise/claude-plugins/issues](https://github.com/Data-Wise/claude-plugins/issues)
- **npm Package:** [https://www.npmjs.com/package/@data-wise/claude-workflow-plugin](https://www.npmjs.com/package/@data-wise/claude-workflow-plugin)
- **Documentation Site:** [https://data-wise.github.io/claude-plugins](https://data-wise.github.io/claude-plugins)

## Status

### Production-Ready Features
- ✅ 12 workflow commands fully functional
- ✅ 3 auto-activating skills implemented
- ✅ Background task delegation working
- ✅ Multiple output formats supported
- ✅ ADHD-optimized design patterns
- ✅ Comprehensive test coverage

### Recent Updates (v2.1.0)
- ✅ Performance guarantees (<60s quick, <5m default, <30m thorough)
- ✅ Shell automation helpers
- ✅ ADHD guide documentation
- ✅ Backward compatibility with v0.1.0

### Future Enhancements
- 🔄 Integration with calendar/time blocking
- 🔄 Pomodoro timer integration
- 🔄 Team collaboration features
- 🔄 Analytics and productivity insights
