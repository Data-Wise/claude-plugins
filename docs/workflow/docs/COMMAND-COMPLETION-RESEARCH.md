# Claude Code Command Completion - Official Documentation

**Generated:** 2025-12-29
**Source:** Claude Code official documentation

---

## Official Tab Completion Behavior

### How `argument-hint` Works

From the docs: Tab completion uses the **`argument-hint`** frontmatter field.

```markdown
---
argument-hint: [pr-number] [priority] [assignee]
description: Review pull request
---
```

When you type `/review-pr ` and pause or press Tab:
```
[pr-number] [priority] [assignee]
```

**This is a text hint, NOT a dropdown menu.**

---

## Hierarchical Commands: Two Systems

### A. Custom Slash Commands (Personal & Project)

Uses **folder structure** for organization, but **NOT colon notation**:

| File Path | Command Name | Description |
|-----------|--------------|-------------|
| `.claude/commands/optimize.md` | `/optimize` | (project) |
| `.claude/commands/frontend/component.md` | `/component` | (project:frontend) |
| `~/.claude/commands/security-review.md` | `/security-review` | (user) |

**Key point:** Subdirectory appears in description for disambiguation, NOT in command name.

### B. Plugin Commands (with Colon Notation)

Plugins use **actual colon syntax**:

```
/plugin-name:command-name
```

From docs:
> Commands can use the format `/plugin-name:command-name` to avoid conflicts
> (plugin prefix is optional unless there are name collisions)

**This is how `/workflow:brainstorm` works** - it's a plugin command.

---

## Supported Frontmatter Fields

| Field | Purpose | Example |
|-------|---------|---------|
| `description` | Brief description (shown in `/help`) | `"Review pull request"` |
| `argument-hint` | Tab completion hint | `"[message]"` or `"quick\|default\|thorough"` |
| `allowed-tools` | Restrict available tools | `Bash(git:*)` |
| `model` | Specific model to use | `"claude-3-5-haiku-20241022"` |
| `disable-model-invocation` | Prevent auto-invocation | `true` |

---

## What Creates a "Menu"?

### The `/help` Output

When you type `/` and pause, Claude Code shows available commands with:
- Command name
- Description (from frontmatter)
- Scope: `(project)`, `(user)`, `(project:frontend)`

**This is the "menu" behavior** - a list of available commands.

### Plugin Sub-Commands

For a plugin like `workflow`, the "menu" when typing `/workflow:` shows:
- All `.md` files in the plugin's `commands/` folder
- Each becomes `/workflow:command-name`

**Current structure:**
```
workflow/commands/
├── brainstorm.md      → /workflow:brainstorm
├── done.md            → /workflow:done
├── focus.md           → /workflow:focus
└── ...
```

---

## Implementing Sub-Options for Brainstorm

### Option 1: Folder-Based Sub-Commands

Create `brainstorm/` folder to get `/workflow:brainstorm:quick` etc:

```
commands/
├── brainstorm.md              # /workflow:brainstorm (main)
└── brainstorm/                # Creates sub-command menu
    ├── quick.md               # /workflow:brainstorm:quick
    ├── default.md             # /workflow:brainstorm:default
    ├── thorough.md            # /workflow:brainstorm:thorough
    ├── feature.md             # /workflow:brainstorm:feature
    ├── architecture.md        # /workflow:brainstorm:architecture
    ├── design.md              # /workflow:brainstorm:design
    ├── backend.md             # /workflow:brainstorm:backend
    ├── frontend.md            # /workflow:brainstorm:frontend
    └── devops.md              # /workflow:brainstorm:devops
```

**Result:** Typing `/workflow:brainstorm:` + Tab shows sub-commands.

### Option 2: Enhanced argument-hint

Use `argument-hint` to show options:

```yaml
---
argument-hint: quick|default|thorough|feature|architecture|design|backend|frontend|devops [topic]
description: ADHD-friendly brainstorming with modes
---
```

**Result:** After typing `/workflow:brainstorm `, hint shows available modes.

### Option 3: Hybrid

Main logic in `brainstorm.md` with argument-hint, sub-folders for complex modes:

```
commands/
├── brainstorm.md              # Main with argument-hint
└── brainstorm/
    └── thorough.md            # Only thorough needs separate (uses agents)
```

---

## Argument Placeholders

### `$ARGUMENTS` - All arguments

```markdown
Brainstorm about: $ARGUMENTS
```

Usage: `/workflow:brainstorm quick feature auth`
→ `$ARGUMENTS` = `"quick feature auth"`

### `$1`, `$2`, `$3` - Positional

```markdown
Mode: $1
Topic: $2
```

Usage: `/workflow:brainstorm quick auth`
→ `$1` = `"quick"`, `$2` = `"auth"`

---

## Recommended Implementation

### For `/workflow:brainstorm` Tab Menu

**Step 1:** Create sub-command folder:

```bash
mkdir -p ~/.claude/plugins/cache/local-plugins/workflow/2.1.0/commands/brainstorm
```

**Step 2:** Create sub-command files with descriptions:

```markdown
# brainstorm/quick.md
---
description: Fast ideation (< 1 min, no agents)
---

Run brainstorm in quick mode. $ARGUMENTS
```

```markdown
# brainstorm/feature.md
---
description: User stories, MVP scope, acceptance criteria
---

Run brainstorm in feature mode. $ARGUMENTS
```

**Step 3:** Keep main `brainstorm.md` as fallback/default.

**Result:**
- `/workflow:brainstorm` + Tab → shows sub-commands (quick, feature, etc.)
- Each sub-command shows its description
- User can type `/workflow:brainstorm:quick auth` directly

---

## References

- [Slash commands docs](https://code.claude.com/docs/en/slash-commands.md)
- [Plugins reference](https://code.claude.com/docs/en/plugins-reference.md)
- [Common workflows](https://code.claude.com/docs/en/common-workflows.md)
