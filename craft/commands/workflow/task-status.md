# /task-status - Background Task Status

Check status of background tasks launched by workflow commands.

## Purpose

Monitor background tasks from:
- `/workflow:brainstorm --background`
- `/workflow:refine` (option 2: background)
- Any other command with background delegation

## Usage

```bash
/workflow:task-status              # List all tasks
/workflow:task-status <task_id>    # Check specific task
/workflow:task-status --wait <task_id>  # Wait for completion
```

---

## When invoked:

### Without Arguments: List All Tasks

```
BACKGROUND TASKS
════════════════════════════════════════════════════════════

🔄 ACTIVE ({count}):

  {task_id} - {command} "{topic}"
    Started: {time_ago}
    Estimated: {estimated_duration}
    Status: Running...

  {task_id2} - {command2} "{topic2}"
    Started: {time_ago2}
    Estimated: {estimated_duration2}
    Status: Running...

────────────────────────────────────────────────────────────
✅ COMPLETED ({count}):

  {task_id3} - {command3} "{topic3}" ✓
    Completed: {time_ago3}
    Duration: {actual_duration3}

────────────────────────────────────────────────────────────
❌ FAILED ({count}):

  {task_id4} - {command4} "{topic4}" ✗
    Failed: {time_ago4}
    Error: {error_summary}

────────────────────────────────────────────────────────────
💡 COMMANDS:

  /workflow:task-output <id>  - View results
  /workflow:task-cancel <id>  - Cancel running task
  /workflow:task-status <id>  - Check specific task
```

**Implementation:**
1. Check for `.claude/tasks.json` file
2. If doesn't exist, check Claude Code's internal task tracking via `/tasks` command
3. Parse task list and categorize by status
4. Format output with clear sections
5. Show time estimates and actual durations

---

### With Task ID: Check Specific Task

```bash
/workflow:task-status abc123
```

**Output for RUNNING task:**
```
TASK STATUS: abc123
════════════════════════════════════════════════════════════

Command: /workflow:brainstorm "improve test coverage"
Status: 🔄 Running
Started: 2 minutes ago
Estimated: 2-3 minutes
Progress: ~66% (2 of 3 min)

────────────────────────────────────────────────────────────
💡 NEXT STEPS:

  • Wait a bit longer (~1 minute remaining)
  • Continue working, I'll notify when done
  • Check again: /workflow:task-status abc123
  • Cancel: /workflow:task-cancel abc123

Or wait for completion:
  /workflow:task-status abc123 --wait
```

**Output for COMPLETED task:**
```
TASK STATUS: abc123
════════════════════════════════════════════════════────════

Command: /workflow:brainstorm "improve test coverage"
Status: ✅ Completed
Started: 5 minutes ago
Completed: 2 minutes ago
Duration: 2m 45s

────────────────────────────────────────────────────────────
💡 NEXT STEPS:

View results:
  /workflow:task-output abc123
```

**Output for FAILED task:**
```
TASK STATUS: abc123
════════════════════════════════════════════════════════════

Command: /workflow:brainstorm "improve test coverage"
Status: ❌ Failed
Started: 5 minutes ago
Failed: 3 minutes ago
Duration: 2m 10s

Error: Agent encountered an error during execution

────────────────────────────────────────────────────────────
💡 NEXT STEPS:

View error details:
  /workflow:task-output abc123

Retry with different approach:
  /workflow:brainstorm "improve test coverage" --wait
```

**Implementation:**
1. Look up task by ID in task registry
2. Check current status using TaskOutput tool with `block: false`
3. Calculate time elapsed and estimate remaining
4. Format status with appropriate emoji and color
5. Provide relevant next steps

---

### With --wait Flag: Wait for Completion

```bash
/workflow:task-status abc123 --wait
```

**Output:**
```
TASK STATUS: abc123
════════════════════════════════════════════════════════════

Command: /workflow:brainstorm "improve test coverage"
Status: 🔄 Running
Started: 2 minutes ago

⏳ Waiting for completion...

[Progress dots appear every 5 seconds]
.....

✅ Task completed! (2m 45s total)

────────────────────────────────────────────────────────────
View results now? (y/n)
> y

[Automatically calls /workflow:task-output abc123]
```

**Implementation:**
1. Use TaskOutput tool with `block: true`
2. Show waiting indicator
3. When complete, offer to show results
4. If user says yes, retrieve and display output

---

## Task Registry Format

**Location:** `.claude/tasks.json`

```json
{
  "tasks": [
    {
      "id": "abc123",
      "command": "/workflow:brainstorm",
      "args": "improve test coverage",
      "status": "running",
      "started": "2025-12-14T14:30:00Z",
      "estimated_duration": "2-3 minutes",
      "type": "general-purpose"
    },
    {
      "id": "xyz789",
      "command": "/workflow:refine",
      "args": "help me with tests",
      "status": "completed",
      "started": "2025-12-14T14:35:00Z",
      "completed": "2025-12-14T14:37:15Z",
      "duration": "2m 15s"
    }
  ]
}
```

**Note:** If `.claude/tasks.json` doesn't exist, fall back to Claude Code's built-in `/tasks` command and parse output.

---

## Status Indicators

| Status | Icon | Meaning |
|--------|------|---------|
| Running | 🔄 | Task is currently executing |
| Completed | ✅ | Task finished successfully |
| Failed | ❌ | Task encountered an error |
| Cancelled | ⛔ | Task was cancelled by user |

---

## Time Display

**Relative time formatting:**
- < 1 minute: "30 seconds ago"
- < 60 minutes: "5 minutes ago"
- < 24 hours: "2 hours ago"
- >= 24 hours: "2 days ago"

**Duration formatting:**
- < 60s: "45s"
- < 60m: "2m 30s"
- >= 60m: "1h 15m"

---

## Error Handling

**If task ID not found:**
```
❌ Task not found: abc123

Available tasks:
  xyz789 - /workflow:brainstorm (completed)
  def456 - /workflow:refine (running)

List all tasks:
  /workflow:task-status
```

**If no tasks exist:**
```
No background tasks found.

Background tasks are created when you use:
  • /workflow:brainstorm <topic> --background
  • /workflow:refine (choose option 2)
  • Other commands with --background flag

────────────────────────────────────────────────────────────
💡 TIP: Try launching a brainstorm in background:
   /workflow:brainstorm "your topic" --background
```

---

## Integration with Other Commands

**After launching background task:**
```
/workflow:brainstorm "ideas" --background

AI: ✅ Task launched (abc123)
    Check status: /workflow:task-status abc123
```

**Check status anytime:**
```
/workflow:task-status abc123

AI: Running... 66% complete
```

**When task completes:**
```
AI: 🎉 Task abc123 complete!

    /workflow:task-status abc123  # Shows completed status
    /workflow:task-output abc123  # View results
```

---

## ADHD-Friendly Features

1. **Visual status indicators** - Quick scan with emojis
2. **Clear next steps** - No guessing what to do
3. **Time estimates** - Know how long to wait
4. **Progress indicators** - Reduces anxiety about stuck tasks
5. **Simple commands** - Easy to remember and use

---

## Related Commands

- `/workflow:task-output <id>` - View task results
- `/workflow:task-cancel <id>` - Cancel running task
- `/workflow:brainstorm --background` - Launch background brainstorm
- `/workflow:refine` (option 2) - Launch background execution

---

**Last Updated:** 2025-12-14
**Category:** Workflow
**Phase:** 1 (Foundation)
