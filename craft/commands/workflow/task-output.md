# /task-output - View Background Task Results

Retrieve and display results from completed (or running) background tasks.

## Purpose

View output from background tasks launched by:
- `/workflow:brainstorm --background`
- `/workflow:refine` (option 2: background)
- Any command with background delegation

## Usage

```bash
/workflow:task-output <task_id>        # View results
/workflow:task-output <task_id> --raw  # Show raw output
/workflow:task-output --latest         # View most recent completed task
```

---

## When invoked:

### View Completed Task Output

```bash
/workflow:task-output abc123
```

**Output:**
```
TASK OUTPUT
════════════════════════════════════════════════════════════

Task ID: abc123
Command: /workflow:brainstorm "improve test coverage"
Status: ✅ Completed
Duration: 2m 45s
Completed: 2 minutes ago

────────────────────────────────────────────────────────────
RESULTS:
────────────────────────────────────────────────────────────

💡 IDEAS: improve test coverage

⚡ Quick (< 1hr)
  1. Add edge case tests for user input validation
  2. Fix flaky test_auth() timeout issue
  3. Add assertion messages to existing tests

🔧 Medium (1-3hrs)
  4. Refactor test helpers into test_utils.R
  5. Add integration tests for API endpoints
  6. Set up coverage reporting with covr package

🚀 Big (1+ days)
  7. Implement CI/CD with automated testing
  8. Add property-based testing with hedgehog

💡 Start with #1 or #2

────────────────────────────────────────────────────────────
📋 Ideas saved to IDEAS.md

────────────────────────────────────────────────────────────
💡 NEXT STEPS:

Work on an idea:
  /workflow:next  - Pick from IDEAS.md and start

Check other tasks:
  /workflow:task-status  - List all tasks
```

**Implementation:**
1. Look up task by ID
2. Check if task is completed
3. Use TaskOutput tool to retrieve results
4. Parse and format output
5. Display in clean, readable format
6. Show relevant next steps

---

### View Running Task Output (Partial)

```bash
/workflow:task-output abc123
```

**If task is still running:**
```
TASK OUTPUT
════════════════════════════════════════════════════════════

Task ID: abc123
Command: /workflow:brainstorm "improve test coverage"
Status: 🔄 Running (1m 30s elapsed)
Estimated completion: ~1 minute

────────────────────────────────────────────────────────────
⚠️  Task not yet complete

Current status: Generating ideas...

────────────────────────────────────────────────────────────
💡 OPTIONS:

1. Wait for completion ⏳
   /workflow:task-output abc123 --wait

2. Check status
   /workflow:task-status abc123

3. Cancel task
   /workflow:task-cancel abc123

4. Continue working
   I'll notify you when complete!

>
```

**Implementation:**
1. Check task status with TaskOutput `block: false`
2. If not complete, show current status
3. Offer to wait or check later
4. Don't block unless user explicitly chooses to wait

---

### View with --wait Flag

```bash
/workflow:task-output abc123 --wait
```

**Output:**
```
TASK OUTPUT
════════════════════════════════════════════════════════════

Task ID: abc123
Status: 🔄 Running

⏳ Waiting for completion...

[Progress dots]
.....

✅ Task completed!

────────────────────────────────────────────────────────────
RESULTS:
────────────────────────────────────────────────────────────

[Full output displayed here]

[Rest of standard output format]
```

**Implementation:**
1. Use TaskOutput with `block: true`
2. Show waiting indicator
3. When complete, display full results
4. Format normally

---

### View Latest Completed Task

```bash
/workflow:task-output --latest
```

**Output:**
```
TASK OUTPUT (Latest)
════════════════════════════════════════════════════════════

Task ID: abc123
Command: /workflow:brainstorm "improve test coverage"
Completed: 2 minutes ago

────────────────────────────────────────────────────────────
RESULTS:
────────────────────────────────────────────────────────────

[Results displayed here]
```

**Implementation:**
1. List all tasks from registry
2. Find most recent completed task
3. Display its output
4. If no completed tasks, show error

---

### View Raw Output

```bash
/workflow:task-output abc123 --raw
```

**Output:**
```
TASK OUTPUT (Raw)
════════════════════════════════════════════════════════════

[Unformatted agent output exactly as returned]

[No additional formatting or parsing]

────────────────────────────────────────────────────────────
💡 View formatted version:
   /workflow:task-output abc123
```

**Useful for:**
- Debugging
- Copying output to other tools
- Seeing exactly what agent produced

---

## Output Formatting

**By command type:**

### Brainstorm Output
- Parse ideas structure
- Display with proper emoji and formatting
- Extract and highlight recommendations
- Show IDEAS.md save confirmation

### Refine Output
- Show original prompt
- Show optimized prompt
- Display execution results if applicable
- Highlight improvements made

### Generic Task Output
- Display as-is with minimal formatting
- Add clear section headers
- Show task metadata
- Provide context

---

## Error Handling

### Task Not Found
```
❌ Task not found: abc123

Recent tasks:
  xyz789 - /workflow:brainstorm (completed 5m ago)
  def456 - /workflow:refine (running)

List all tasks:
  /workflow:task-status
```

### Task Failed
```
TASK OUTPUT
════════════════════════════════════════════════════════════

Task ID: abc123
Command: /workflow:brainstorm "improve test coverage"
Status: ❌ Failed
Duration: 1m 30s
Failed: 3 minutes ago

────────────────────────────────────────────────────────────
ERROR:
────────────────────────────────────────────────────────────

Agent encountered an error during execution:

[Error message from agent]

[Stack trace if available]

────────────────────────────────────────────────────────────
💡 TROUBLESHOOTING:

Retry the command:
  /workflow:brainstorm "improve test coverage" --wait

Try a different approach:
  • Simplify the topic
  • Be more specific
  • Use interactive mode: /workflow:brainstorm

Get help:
  /workflow:stuck
```

### No Tasks Available
```
No background tasks found.

Launch a background task:
  /workflow:brainstorm "your topic" --background
  /workflow:refine "your prompt" (choose option 2)

Check task status:
  /workflow:task-status
```

---

## Output Persistence

**Where results are stored:**

1. **Primary:** Claude Code's TaskOutput API
2. **Backup:** `.claude/task-outputs/{task_id}.md`
3. **References:** IDEAS.md, PROMPTS.md (depending on command)

**Retention:**
- Active tasks: Until completed or cancelled
- Completed tasks: 7 days (configurable)
- Failed tasks: 7 days (for debugging)

---

## Integration with Workflow

**Typical flow:**
```bash
# Launch background task
/workflow:brainstorm "ideas" --background
> Task abc123 launched

# Continue working
[do other things]

# Notification appears
> 🎉 Task abc123 complete!

# View results
/workflow:task-output abc123
> [Shows brainstormed ideas]

# Act on results
/workflow:next
> Pick an idea to work on
```

---

## ADHD-Friendly Features

1. **Clear task identification** - Easy to see what output is from
2. **Formatted output** - Not overwhelming walls of text
3. **Next steps always shown** - No "now what?" moment
4. **Quick access to latest** - `--latest` flag for recent work
5. **Raw mode available** - For when you need unprocessed output

---

## Advanced Usage

### Chain with other commands
```bash
# View output and immediately work on it
/workflow:task-output abc123 && /workflow:next
```

### Save to file
```bash
/workflow:task-output abc123 --raw > my-output.md
```

### Check multiple tasks
```bash
/workflow:task-status              # List all
/workflow:task-output abc123       # View first
/workflow:task-output xyz789       # View second
```

---

## Related Commands

- `/workflow:task-status` - Check task status
- `/workflow:task-cancel` - Cancel running task
- `/workflow:brainstorm --background` - Launch background brainstorm
- `/workflow:refine` - Optimize and execute prompts
- `/workflow:next` - Work on brainstormed ideas

---

## Examples

### Example 1: View Brainstorm Results
```bash
/workflow:task-output abc123

AI: [Shows 8 brainstormed ideas]
    📋 Saved to IDEAS.md

User: /workflow:next

AI: [Lets user pick an idea to work on]
```

### Example 2: Check Failed Task
```bash
/workflow:task-output xyz789

AI: ❌ Task failed
    Error: [details]

    Try again with: /workflow:brainstorm "..." --wait
```

### Example 3: Wait for Running Task
```bash
/workflow:task-output abc123 --wait

AI: ⏳ Waiting...
    ✅ Complete!
    [Shows results]
```

---

**Last Updated:** 2025-12-14
**Category:** Workflow
**Phase:** 1 (Foundation)
