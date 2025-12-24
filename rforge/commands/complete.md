---
name: rforge:complete
description: Mark tasks complete with automatic documentation cascade
argument-hint: Task ID or description
---

# /rforge:complete - Task Completion with Doc Cascade

Mark tasks complete and automatically trigger documentation cascade updates.

## What It Does

Uses the `rforge_complete` MCP tool to:
- Mark task as complete in .STATUS
- Detect documentation changes needed
- Auto-update NEWS.md if needed
- Update cross-references
- Archive completed tasks

## Usage

```bash
# Complete a task by ID
/rforge:complete T-2025-01-15-001

# Complete by description
/rforge:complete "Add bootstrap intervals"

# Complete without doc cascade
/rforge:complete T-2025-01-15-001 --no-cascade
```

## Output

Returns completion summary with:
- **Task Details**: What was completed
- **Documentation**: Auto-updates performed
- **Cascade**: Related packages affected
- **Archive**: Where task was moved
- **Next Task**: Suggestion for what's next

## Examples

### Simple Completion
```
✅ COMPLETED

Task: Add bootstrap confidence intervals
ID: T-2025-01-15-001
Package: medfit
Completion time: 2025-01-15 14:30

Documentation cascade:
  ✅ NEWS.md updated (auto)
  ✅ .STATUS archived
  ⏩ No dependent updates needed

Next suggested task: Fix bug #234 (HIGH priority)
```

### Completion with Cascade
```
✅ COMPLETED (with cascade)

Task: Refactor extract_mediation API
ID: T-2025-01-10-005
Package: medfit

Documentation cascade triggered:
  ✅ medfit NEWS.md updated
  ⚠️ probmed needs update (2 references)
  ⚠️ medsim needs update (1 vignette)

Cascade plan created:
  1. Update probmed function calls
  2. Update medsim vignette
  3. Re-run ecosystem tests

Estimated cascade work: 2-3 hours

Would you like to run /rforge:cascade to plan the updates?
```

### Completion with Release Note
```
✅ COMPLETED (release-worthy)

Task: Add new bootstrap method
ID: T-2025-01-08-003
Package: medfit

Documentation updates:
  ✅ NEWS.md entry added:
     "## New Features
      - Added accelerated bootstrap for faster confidence intervals"

  ✅ Function documentation updated
  ✅ Vignette example added

Release notes ready for next version (medfit 2.2.0)

Next: Consider running /rforge:release to plan CRAN submission
```

## Use When

- Finishing tasks/features
- After code review approval
- Before committing changes
- During release preparation

## Related Commands

- `/rforge:capture` - Capture new tasks
- `/rforge:next` - Get next task
- `/rforge:cascade` - Plan doc updates
- `/rforge:doc-check` - Verify documentation
