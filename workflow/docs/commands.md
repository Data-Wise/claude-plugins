# Workflow Commands Reference

Complete reference for all 12 ADHD-friendly workflow commands. Designed to reduce decision paralysis and maintain focus.

## Command Categories

- [Core Workflow](#core-workflow) (7 commands)
- [Task Management](#task-management) (3 commands)
- [Documentation](#documentation) (1 command)
- [Aliases](#command-aliases) (1 command)

## Core Workflow

### /brainstorm
Smart ideation with auto-delegation and mode detection.

```bash
# Auto-detect mode from context
/brainstorm

# Specific modes
/brainstorm quick "Feature ideas"           # <1 min, no delegation
/brainstorm "Architecture design"           # <5 min, balanced
/brainstorm thorough "Production strategy"  # <30 min, deep analysis

# Specific topics
/brainstorm feature "User profiles"
/brainstorm architecture "Real-time system"
/brainstorm design "Mobile-first UI"

# Output formats
/brainstorm --format json
/brainstorm --format markdown > brainstorm.md
```

**Features:**
- Auto-activating skills (backend/frontend/devops)
- Background agent delegation
- Multiple output formats
- Time budgets enforced

### /focus
Single-task mode with distraction blocking.

```bash
/focus "Implement OAuth authentication"
/focus "Fix memory leak in worker process"
```

**Sets:**
- Clear objective
- Success criteria
- Time budget (default: 2 hours)
- Milestone reminders

**Output:**
```
📍 Focus Mode Activated
Objective: Implement OAuth authentication
Success: OAuth login working with Google + GitHub
Time: 2 hours budgeted
Milestones: Setup (30min), Implementation (60min), Testing (30min)
```

### /next
Decision support for what to work on next.

```bash
/next
```

**Analyzes:**
- .STATUS file (Next Action section)
- Recent commits
- Current context
- Blockers

**Provides:**
- ONE recommended task
- WHY this task (reasoning)
- Time estimate
- 2-3 alternatives with quick wins

**Output format:**
```
┌─────────────────────────────────────────────┐
│ 🎯 SUGGESTED NEXT STEP                      │
├─────────────────────────────────────────────┤
│ [Task Title]                                │
│ 📁 File: [specific location]                │
│ ⏱️  Est: 30-45 min                           │
│ Why? [Clear reasoning]                       │
├─────────────────────────────────────────────┤
│ 💡 ALTERNATIVES:                            │
│ A) [Alternative 1] (1hr)                     │
│ B) [Quick win] (10min) ⚡                   │
└─────────────────────────────────────────────┘
```

### /done
Session completion with context capture.

```bash
/done
/done "Completed OAuth implementation, tests passing"
```

**Captures:**
- Achievements
- Blockers encountered
- Context for next session
- Updates .STATUS automatically

**Prompts for:**
- What did you complete?
- Any blockers?
- What's next?

### /recap
Context restoration when returning to work.

```bash
/recap
```

**Reviews:**
- Recent commits (last session)
- .STATUS file
- Open TODO items
- Suggests where to resume

**Output:**
```
📋 Context Recap

Last session (2 hours ago):
✅ Implemented OAuth with Google
✅ Added unit tests (15 tests passing)
🔄 In progress: GitHub OAuth provider

Current status:
📦 Branch: feature/oauth
🌿 Git: 3 commits ahead, clean working tree

🎯 Suggested: Continue with GitHub OAuth integration
📝 Context: Google OAuth working, follow same pattern
⏱️  Est: 45-60 minutes
```

### /stuck
Unblock helper with guided problem solving.

```bash
/stuck
/stuck "Can't figure out why tests are failing"
```

**5 Why Analysis:**
1. What's the immediate blocker?
2. What have you tried?
3. What's a simpler version?
4. Who/what could help?
5. What would success look like?

**Provides:**
- Alternative approaches
- Simplification strategies
- Resource suggestions
- Success definition

### /refine
Prompt optimizer for better AI interactions.

```bash
/refine "make the app faster"
```

**Improves:**
- Clarity and specificity
- Actionable language
- Context inclusion
- Expected outcomes

**Example:**
```
Original: "make the app faster"

Refined: "Profile the React application to identify rendering bottlenecks. Focus on the UserDashboard component which users report as sluggish. Generate a performance report with specific optimization recommendations."
```

## Task Management

### /task-status
Check progress of background tasks.

```bash
/task-status
```

**Shows:**
- Active agents
- Execution time
- Estimated completion
- Current status

### /task-output
View results from completed background task.

```bash
/task-output <task-id>
```

**Returns:**
- Formatted synthesis
- Agent outputs
- Actionable recommendations

### /task-cancel
Cancel running background task.

```bash
/task-cancel <task-id>
```

**Actions:**
- Stops agent execution
- Cleans up resources
- Reports partial results if available

## Documentation

### /workflow:docs:adhd-guide
ADHD-friendly development best practices.

```bash
/workflow:docs:adhd-guide
```

**Topics:**
- Reducing decision paralysis
- Managing context switching
- Time budgeting strategies
- Focus techniques
- Tool configuration

## Command Aliases

### /workflow:next
Alias for `/next` command.

```bash
/workflow:next
```

Same functionality as `/next` but with explicit namespace.

## Time Budgets

All commands respect explicit time guarantees:

| Command | Mode | Time Budget |
|---------|------|-------------|
| `/brainstorm` | quick | <60s |
| `/brainstorm` | default | <5min |
| `/brainstorm` | thorough | <30min |
| `/focus` | - | User-defined (default: 2hr) |
| `/next` | - | <10s |
| `/done` | - | <30s |
| `/recap` | - | <30s |
| `/stuck` | - | <2min |
| `/refine` | - | <30s |

## ADHD-Friendly Features

### Scannable Output

All commands use visual hierarchy:
- Emojis for quick scanning
- Clear sections with boxes
- Numbered action items
- Time estimates visible

### Reduced Decisions

Commands make decisions FOR you:
- `/next` → ONE recommendation (not a list)
- `/focus` → Clear objective set
- `/done` → Auto-updates status

### Quick Wins

Always included:
- `/next` → Includes <15min alternative
- `/brainstorm` → Quick mode available
- `/stuck` → Simpler version suggested

### Context Preservation

Commands help maintain context:
- `/done` → Captures session context
- `/recap` → Restores context quickly
- `/focus` → Sets clear boundaries

## See Also

- **[Skills & Agents Guide](skills-agents.md)** - Auto-activating skills
- **ADHD Guide:** `/workflow:docs:adhd-guide`
