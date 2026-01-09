# Workflow Integration Documentation

**craft v1.17.0** - Integrated workflow automation features

This directory contains documentation for the workflow automation features integrated into craft v1.17.0. These features were originally part of the standalone `workflow` plugin and are now fully integrated into craft.

---

## Documentation Files

### Quick Start
**[QUICK-START.md](QUICK-START.md)** - Get started with workflow commands in 5 minutes
- Brainstorming basics
- Task management workflow
- Focus mode and productivity features
- Common use cases

### Command Reference
**[REFCARD.md](REFCARD.md)** - Complete reference for all 12 workflow commands
- `/brainstorm` - Enhanced brainstorming with modes and agents
- `/spec-review` - Interactive spec review
- `/focus`, `/next`, `/done` - Task management
- `/recap`, `/stuck` - Session management
- `/task-*` - Background task control
- `/adhd-guide` - ADHD-friendly workflow guide

### Command Details
**[commands.md](commands.md)** - Detailed explanation of each workflow command
- Command syntax and arguments
- Usage examples
- Integration with craft features

### Skills & Agents
**[skills-agents.md](skills-agents.md)** - Workflow skills and agent integration
- Orchestrator patterns
- Agent delegation
- Background task management

---

## Workflow Commands Overview

### Brainstorming & Planning (3 commands)
- `/brainstorm [depth] [focus] [action]` - Enhanced brainstorming
- `/spec-review <file>` - Review specifications
- `/refine <spec-file>` - Refine existing specs

### Task Management (5 commands)
- `/focus [task]` - Enter focus mode
- `/next` - Get next task
- `/done [message]` - Complete current task
- `/recap` - Session summary
- `/stuck [description]` - Get unstuck

### Background Tasks (3 commands)
- `/task-status [task-id]` - Check task status
- `/task-output <task-id>` - Get task output
- `/task-cancel <task-id>` - Cancel task

### Workflow Guide (1 command)
- `/adhd-guide` - ADHD-friendly workflow best practices

---

## Integration with craft

Workflow commands integrate seamlessly with craft's existing features:

**Example Development Workflow:**
```bash
# 1. Brainstorm feature
/brainstorm d feat save "user authentication"

# 2. Enter focus mode
/focus "implement auth"

# 3. Use craft commands for development
/craft:do "add JWT authentication"
/craft:test:run

# 4. Complete and recap
/done "auth feature complete with tests"
/recap
```

**Workflow + craft Orchestrator:**
```bash
# Brainstorm with orchestrator
/brainstorm max arch save "microservices migration"

# Implement with orchestrator
/craft:orchestrate "migrate to microservices" optimize

# Monitor background tasks
/task-status
/task-output <task-id>
```

---

## Migration from Standalone Workflow Plugin

If you were using the standalone `workflow` plugin:

1. **Commands work identically** - Same names, same arguments
2. **No breaking changes** - All features preserved
3. **Migration script available** - `craft/scripts/migrate-from-workflow.sh`

See [craft v1.17.0 Release Notes](../../RELEASE-NOTES-v1.17.0.md) for full migration guide.

---

## Additional Resources

- **craft Documentation:** https://data-wise.github.io/claude-plugins/craft/
- **Main README:** [../../README.md](../../README.md)
- **Release Notes:** [../../RELEASE-NOTES-v1.17.0.md](../../RELEASE-NOTES-v1.17.0.md)
- **ADHD Guide:** [../../docs/ADHD-QUICK-START.md](../ADHD-QUICK-START.md)

---

## Quick Links

- [Commands Reference](REFCARD.md)
- [Quick Start Guide](QUICK-START.md)
- [Detailed Command Docs](commands.md)
- [Skills & Agents](skills-agents.md)

---

**Integration Date:** January 8, 2026
**Version:** craft v1.17.0
**Status:** Production-ready
