# /task-cancel - Cancel Background Task

Cancel a running background task.

## Purpose

Stop execution of background tasks from:
- `/workflow:brainstorm --background`
- `/workflow:refine` (option 2: background)
- Any command with background delegation

**Use when:**
- Task is taking too long
- Realized you asked the wrong question
- Want to try a different approach
- Made a mistake in the prompt

## Usage

```bash
/workflow:task-cancel <task_id>           # Cancel specific task
/workflow:task-cancel <task_id> --force   # Force cancel without confirmation
/workflow:task-cancel --all               # Cancel all running tasks
```

---

## When invoked:

### Cancel Specific Task

```bash
/workflow:task-cancel abc123
```

**Output:**
```
CANCEL BACKGROUND TASK
════════════════════════════════════════════════════════════

Task ID: abc123
Command: /workflow:brainstorm "improve test coverage"
Status: 🔄 Running
Started: 2 minutes ago
Estimated completion: ~1 minute remaining

────────────────────────────────────────────────────────────
⚠️  CONFIRM CANCELLATION

Are you sure you want to cancel this task?

Progress will be lost and the task cannot be resumed.

────────────────────────────────────────────────────────────

Confirm? (y/n)
>
```

**If user confirms (y):**
```
✅ Task cancelled: abc123

The task has been stopped and removed from the queue.

────────────────────────────────────────────────────────────
💡 NEXT STEPS:

Retry with different approach:
  /workflow:brainstorm "improve test coverage" --wait

Try interactive mode:
  /workflow:brainstorm

Check remaining tasks:
  /workflow:task-status
```

**If user declines (n):**
```
❌ Cancellation aborted

Task abc123 is still running.

Check status:
  /workflow:task-status abc123
```

**Implementation:**
1. Look up task by ID
2. Verify it's currently running
3. Show confirmation prompt
4. If confirmed, use KillShell or appropriate tool to stop task
5. Update task registry with "cancelled" status
6. Clean up any partial outputs
7. Show next steps

---

### Force Cancel (No Confirmation)

```bash
/workflow:task-cancel abc123 --force
```

**Output:**
```
✅ Task cancelled: abc123 (forced)

Task stopped immediately without confirmation.

────────────────────────────────────────────────────────────
Check remaining tasks:
  /workflow:task-status
```

**Use case:** Quickly cancel during scripting or when very certain.

---

### Cancel All Running Tasks

```bash
/workflow:task-cancel --all
```

**Output:**
```
CANCEL ALL BACKGROUND TASKS
════════════════════════════════════════════════════════════

Found 3 running tasks:

  abc123 - /workflow:brainstorm "improve test coverage"
  xyz789 - /workflow:refine "help with tests"
  def456 - /code:test-gen

────────────────────────────────────────────────────────────
⚠️  CONFIRM CANCELLATION

Cancel all 3 running tasks?

All progress will be lost.

────────────────────────────────────────────────────────────

Confirm? (y/n)
>
```

**If user confirms (y):**
```
✅ Cancelled 3 tasks:
  • abc123 - /workflow:brainstorm
  • xyz789 - /workflow:refine
  • def456 - /code:test-gen

All running tasks have been stopped.

────────────────────────────────────────────────────────────
💡 Task queue is now clear

Start new tasks:
  /workflow:brainstorm "..."
  /workflow:refine "..."
```

**If user declines (n):**
```
❌ Cancellation aborted

All tasks are still running.

Check status:
  /workflow:task-status
```

---

## Error Handling

### Task Not Found
```
❌ Task not found: abc123

Recent tasks:
  xyz789 - /workflow:brainstorm (completed 5m ago)
  def456 - /workflow:refine (running)

Cancel a running task:
  /workflow:task-cancel def456

List all tasks:
  /workflow:task-status
```

### Task Already Completed
```
❌ Cannot cancel: Task already completed

Task ID: abc123
Status: ✅ Completed
Finished: 3 minutes ago

────────────────────────────────────────────────────────────
View results:
  /workflow:task-output abc123
```

### Task Already Cancelled
```
❌ Task already cancelled: abc123

Cancelled: 2 minutes ago

────────────────────────────────────────────────────────────
Start a new task:
  /workflow:brainstorm "..."
  /workflow:task-status  - View all tasks
```

### Task Already Failed
```
❌ Cannot cancel: Task already failed

Task ID: abc123
Status: ❌ Failed
Failed: 5 minutes ago

────────────────────────────────────────────────────────────
View error:
  /workflow:task-output abc123

Retry:
  /workflow:brainstorm "..." --wait
```

### No Running Tasks
```
No running tasks to cancel.

────────────────────────────────────────────────────────────
Recent tasks:
  abc123 - Completed 3m ago
  xyz789 - Completed 10m ago

View results:
  /workflow:task-output abc123
```

---

## Cancellation Behavior

**What happens when task is cancelled:**

1. **Task execution stopped** - Agent process terminated
2. **Status updated** - Marked as "cancelled" in registry
3. **Partial output discarded** - No incomplete results saved
4. **Resources released** - Memory and compute freed
5. **Notifications cleared** - No completion notification sent

**Partial work:**
- Not saved to IDEAS.md or other files
- Not available via task-output
- Completely discarded

**Why:** Partial results could be misleading or incorrect.

---

## Safety Features

### Confirmation Required
- Default behavior asks for confirmation
- Prevents accidental cancellation
- Shows task details before confirming

### Force Flag Available
- `--force` skips confirmation
- Useful for scripting
- Quick cancellation when certain

### Granular Control
- Cancel specific task by ID
- Cancel all running tasks
- Cannot cancel completed/failed tasks (protects results)

---

## Use Cases

### Use Case 1: Wrong Topic
```bash
/workflow:brainstorm "improve performance" --background
> Task abc123 launched

[Realize you meant "improve test coverage"]

/workflow:task-cancel abc123
> Confirm? y
> ✅ Cancelled

/workflow:brainstorm "improve test coverage" --background
> Task xyz789 launched
```

### Use Case 2: Taking Too Long
```bash
/workflow:brainstorm "complex redesign" --background
> Task abc123 launched (estimated 5 min)

[After 10 minutes, still running]

/workflow:task-status abc123
> Running for 10m (way over estimate)

/workflow:task-cancel abc123
> Confirm? y
> ✅ Cancelled

/workflow:brainstorm "complex redesign" --wait
> [Try synchronously to see what's wrong]
```

### Use Case 3: Clear Queue Before Shutdown
```bash
/workflow:task-status
> 3 tasks running

[Need to shutdown computer]

/workflow:task-cancel --all
> Cancel 3 tasks? y
> ✅ All cancelled

[Safe to shutdown]
```

---

## Integration with Workflow

**Typical flow:**
```bash
# Launch background task
/workflow:brainstorm "ideas" --background
> Task abc123 launched

# Realize mistake
> Oh no, wrong topic!

# Quick cancel
/workflow:task-cancel abc123 --force
> ✅ Cancelled

# Retry correctly
/workflow:brainstorm "correct topic" --background
> Task xyz789 launched
```

---

## ADHD-Friendly Features

1. **Quick correction** - Easy to fix mistakes
2. **No guilt** - Cancel anytime, no judgment
3. **Clear confirmation** - Know exactly what you're stopping
4. **Force option** - Fast cancel when certain
5. **Next steps provided** - What to do after cancelling

---

## Advanced Usage

### Cancel and Retry
```bash
/workflow:task-cancel abc123 --force && \
  /workflow:brainstorm "better topic" --background
```

### Cancel All and Start Fresh
```bash
/workflow:task-cancel --all --force && \
  /workflow:task-status
```

### Cancel with Custom Message
```bash
/workflow:task-cancel abc123
# Add to IDEAS.md: "Cancelled brainstorm - topic was too broad"
```

---

## Related Commands

- `/workflow:task-status` - Check what's running
- `/workflow:task-output` - View completed results
- `/workflow:brainstorm --background` - Launch new task
- `/workflow:refine` - Optimize prompts

---

## Examples

### Example 1: Simple Cancel
```bash
/workflow:task-cancel abc123

AI: Confirm cancellation? (y/n)
User: y
AI: ✅ Cancelled

    Retry: /workflow:brainstorm "..."
```

### Example 2: Force Cancel
```bash
/workflow:task-cancel abc123 --force

AI: ✅ Task cancelled: abc123 (forced)
```

### Example 3: Cancel All
```bash
/workflow:task-cancel --all

AI: Cancel 3 tasks? (y/n)
User: y
AI: ✅ Cancelled 3 tasks
```

### Example 4: Can't Cancel Completed
```bash
/workflow:task-cancel abc123

AI: ❌ Cannot cancel: Task already completed

    View results: /workflow:task-output abc123
```

---

## Technical Implementation

**Cancellation mechanism:**
1. Identify running task process
2. Send termination signal (SIGTERM)
3. Wait for graceful shutdown (2 seconds)
4. Force kill if needed (SIGKILL)
5. Update task registry
6. Clean up resources

**Task registry update:**
```json
{
  "id": "abc123",
  "status": "cancelled",
  "cancelled": "2025-12-14T14:45:00Z",
  "cancelled_by": "user"
}
```

---

**Last Updated:** 2025-12-14
**Category:** Workflow
**Phase:** 1 (Foundation)
