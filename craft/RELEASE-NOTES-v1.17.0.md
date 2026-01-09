# Craft v1.17.0 - Workflow Integration 🎉

**Release Date:** January 8, 2026
**Status:** Production Ready

## 🎯 Milestone: Workflow Integration Complete

This release marks the **integration of the workflow plugin** into craft, combining full-stack development tools with ADHD-friendly workflow automation for a unified developer experience.

---

## 📊 What's Included

| Category | Count | Change |
|----------|-------|--------|
| **Commands** | **86** | +12 workflow commands |
| **Skills** | **21** | Unchanged |
| **Agents** | **8** | Unchanged |
| **Workflow Features** | **12** | ✅ Integrated |

---

## ✨ Major Features (v1.17.0)

### 1. Workflow Commands Integration (12 commands)

All workflow plugin commands are now available in craft:

#### **Brainstorming & Planning:**
- `/brainstorm [depth] [focus] [action]` - Enhanced brainstorming with smart detection, modes, and agent delegation
  - **Depth modes:** `q|quick`, `d|deep`, `m|max` (2-4 questions, 4-6, 8+ with agents)
  - **Focus areas:** `f|feat`, `a|arch`, `x|ux`, `b|api`, `u|ui`, `o|ops`
  - **Actions:** `save` (auto-save as spec), `exec` (implement immediately)
- `/spec-review <file>` - Interactive spec review with validation and status updates
- `/refine <spec-file>` - Refine and improve existing specifications

#### **Task Management:**
- `/focus [task]` - Enter focus mode for deep work
- `/next` - Get next task recommendation
- `/done [message]` - Mark current task complete
- `/recap` - Generate session summary and progress report
- `/stuck [description]` - Get help when blocked

#### **Background Task Control:**
- `/task-status [task-id]` - Check status of background tasks
- `/task-output <task-id>` - Get output from completed task
- `/task-cancel <task-id>` - Cancel running background task

#### **Workflow Guide:**
- `/adhd-guide` - ADHD-friendly workflow guide and best practices

### 2. Enhanced Developer Experience

**Unified Workflow:**
- All craft development commands work seamlessly with workflow features
- Use `/brainstorm` to design features, then `/craft:do` to implement
- Use `/focus` during development, `/done` to complete tasks

**Example Workflow:**
```bash
# Design phase
/brainstorm d feat save "user authentication"

# Implementation phase
/focus "implement auth"
/craft:do "add JWT authentication"

# Task completion
/done "auth implemented and tested"
/recap
```

### 3. Command Organization

Workflow commands are organized in a new category:
```
craft/commands/
├── workflow/          # NEW (12 commands)
│   ├── brainstorm.md
│   ├── spec-review.md
│   ├── focus.md
│   └── ... (9 more)
├── arch/             # Existing (4 commands)
├── ci/               # Existing (7 commands)
├── code/             # Existing (12 commands)
├── docs/             # Existing (10 commands)
├── git/              # Existing (9 commands)
├── plan/             # Existing (3 commands)
├── site/             # Existing (9 commands)
└── test/             # Existing (6 commands)
```

---

## 🔄 Migration from Workflow Plugin

If you were using the standalone `workflow` plugin:

### Automatic Migration
The workflow commands now work identically in craft:
- ✅ Same command names (no namespace changes)
- ✅ Same arguments and options
- ✅ Same behavior and output

### Steps to Migrate
```bash
# 1. Uninstall old workflow plugin (if installed)
rm -rf ~/.claude/plugins/workflow

# 2. Install/update craft to v1.17.0
cd ~/projects/dev-tools/claude-plugins/craft
./install.sh

# 3. Restart Claude Code
# That's it! All workflow commands now available via craft
```

### Command Compatibility
| Old Command | New Command | Status |
|------------|-------------|--------|
| `/brainstorm` | `/brainstorm` | ✅ Identical |
| `/spec-review` | `/spec-review` | ✅ Identical |
| `/focus` | `/focus` | ✅ Identical |
| `/next` | `/next` | ✅ Identical |
| `/done` | `/done` | ✅ Identical |
| `/recap` | `/recap` | ✅ Identical |
| `/stuck` | `/stuck` | ✅ Identical |
| `/refine` | `/refine` | ✅ Identical |
| `/task-status` | `/task-status` | ✅ Identical |
| `/task-output` | `/task-output` | ✅ Identical |
| `/task-cancel` | `/task-cancel` | ✅ Identical |
| `/adhd-guide` | `/adhd-guide` | ✅ Identical |

---

## 📦 Installation

### Quick Install
```bash
curl -fsSL https://raw.githubusercontent.com/Data-Wise/claude-plugins/main/craft/install.sh | bash
```

### Manual Install
```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins && git sparse-checkout set craft
cp -r craft ~/.claude/plugins/
```

---

## 🚀 Getting Started with Workflow Features

### 1. Quick Brainstorm
```bash
/brainstorm q feat "add dark mode"
# Quick feature brainstorm (2-4 questions, ~2 min)
```

### 2. Deep Architecture Design
```bash
/brainstorm d arch save "microservices migration"
# Deep analysis with spec capture (4-6 questions, ~5 min)
```

### 3. Max Depth with Agents
```bash
/brainstorm max ux save "redesign dashboard"
# Full analysis with expert agents (8+ questions, 2 agents, ~10 min)
```

### 4. Focus Mode Development
```bash
/focus "implement payment gateway"
# Enter focus mode, work, then:
/done "payment integration complete"
```

---

## 📚 Documentation

- **Full Documentation:** https://data-wise.github.io/claude-plugins/craft/
- **Workflow Guide:** https://data-wise.github.io/claude-plugins/craft/guide/workflow/
- **Quick Start:** https://data-wise.github.io/claude-plugins/craft/QUICK-START/
- **ADHD Guide:** https://data-wise.github.io/claude-plugins/craft/ADHD-QUICK-START/

---

## 🔧 Technical Details

### Changes
- ✅ Added 12 workflow commands to `craft/commands/workflow/`
- ✅ Updated plugin.json: version 1.16.0 → 1.17.0
- ✅ Updated package.json: version 1.16.0 → 1.17.0
- ✅ Updated README.md: 74 → 86 commands
- ✅ Updated install.sh: version display and command count
- ✅ No namespace conflicts with existing craft commands

### Compatibility
- ✅ Backward compatible with all existing craft commands
- ✅ Workflow commands work identically to standalone plugin
- ✅ No breaking changes

---

## 🎁 What's Next

With workflow integration complete, craft now provides:
- **Complete development toolkit:** 74 commands for code, git, docs, testing, CI
- **Workflow automation:** 12 commands for planning, focus, task management
- **Unified experience:** Seamless integration between development and workflow

**Happy coding!** 🚀

---

**Full Changelog:** https://github.com/Data-Wise/claude-plugins/blob/main/craft/RELEASE-NOTES-v1.17.0.md
