# Brainstorm: Sub-Command Menu UX

**Topic:** Interactive sub-menu behavior when commands have options
**Context:** Craft plugin command design

---

## The Vision

```
User types: /craft:site:nav

┌─────────────────────────────────────────────────────────────┐
│ /craft:site:nav                                             │
├─────────────────────────────────────────────────────────────┤
│ ⭐ [default]     Analyze nav structure & propose changes    │
│    --adhd       Enforce ADHD-friendly limits (max 7 sections│
│    --apply      Apply proposed changes to mkdocs.yml        │
│    --preview    Show diff without applying                  │
│    --help       Show detailed help                          │
└─────────────────────────────────────────────────────────────┘
         ↑ tip appears next to highlighted option
```

---

## Technical Perspectives

### How Claude Code Currently Works

| Feature | Current Behavior |
|---------|------------------|
| Tab completion | Shows available commands |
| Arguments | Typed manually or from help |
| Sub-options | Not interactive |
| Defaults | Implicit in command logic |

### What We Can Control

1. **Command frontmatter** - YAML at top of command files
2. **Command content** - Prompt that runs
3. **Output format** - What user sees after running
4. **AskUserQuestion tool** - Interactive prompts during execution

### What We Can't Control (Claude Code limitations)

- Tab completion behavior (built into Claude Code)
- Pre-execution menus (commands run immediately)
- Shell-level autocomplete

---

## Approach Ideas

### ⭐ Approach 1: Post-Invocation Menu (Recommended)

**How it works:** Command runs, immediately shows interactive menu

```markdown
# /craft:site:nav

You are a navigation reorganization assistant.

## When Invoked (No Arguments)

Show this menu using AskUserQuestion:

┌─────────────────────────────────────────────────────────────┐
│ /craft:site:nav - What would you like to do?                │
├─────────────────────────────────────────────────────────────┤
│ ○ Analyze & Propose     → Review current nav, suggest changes│
│ ○ ADHD Mode            → Enforce max 7 sections              │
│ ○ Apply Changes        → Apply previous proposal             │
│ ○ Preview Diff         → Show changes without applying       │
└─────────────────────────────────────────────────────────────┘
```

**Pros:**
- Works with current Claude Code
- Interactive and discoverable
- User sees all options

**Cons:**
- Extra step vs direct command
- Can't bypass menu with arguments

---

### ⭐ Approach 2: Smart Default with Bypass

**How it works:** Default action runs unless argument provided

```bash
/craft:site:nav              # Runs default (analyze & propose)
/craft:site:nav adhd         # Skips menu, runs ADHD mode
/craft:site:nav apply        # Skips menu, applies changes
```

**Command logic:**
```markdown
## When Invoked

Check for arguments:
- No args → Run default action (analyze & propose)
- `adhd` → Run with ADHD constraints
- `apply` → Apply previous proposal
- `help` → Show all options

Default behavior tip:
"Running in default mode (analyze & propose).
 For other modes: /craft:site:nav [adhd|apply|preview|help]"
```

**Pros:**
- Fast for power users
- Discoverable via help
- No extra menu step

**Cons:**
- Must remember arguments
- Less discoverable for new users

---

### ⭐ Approach 3: Hybrid (Best of Both)

**How it works:**
- First run: Show menu with tip
- Subsequent runs: Remember preference
- Arguments always bypass menu

```bash
# First time
/craft:site:nav
→ Shows menu, user selects "Analyze & Propose"
→ Tip: "Next time, use /craft:site:nav or /craft:site:nav adhd to skip this menu"

# After first run
/craft:site:nav
→ Runs last used mode
→ Shows: "Running: Analyze & Propose (use --menu to change)"

# Explicit mode
/craft:site:nav adhd
→ Runs ADHD mode directly
```

**Pros:**
- Best UX for both new and power users
- Progressive disclosure
- ADHD-friendly (reduces decisions over time)

**Cons:**
- More complex to implement
- Needs state management

---

### Approach 4: Tiered Commands

**How it works:** Separate commands for each mode

```bash
/craft:site:nav           # Main command (default)
/craft:site:nav:adhd      # ADHD mode
/craft:site:nav:apply     # Apply mode
/craft:site:nav:preview   # Preview mode
```

**Pros:**
- Very explicit
- Full tab completion
- No ambiguity

**Cons:**
- Proliferates commands
- Harder to discover all variants
- Not scalable

---

### Approach 5: Frontmatter Arguments

**How it works:** Define options in YAML frontmatter

```yaml
---
name: site:nav
description: Reorganize navigation structure
arguments:
  - name: mode
    type: choice
    default: analyze
    choices:
      - value: analyze
        label: Analyze & Propose
        tip: Review current nav, suggest changes
      - value: adhd
        label: ADHD Mode
        tip: Enforce max 7 sections
      - value: apply
        label: Apply Changes
        tip: Apply previous proposal
      - value: preview
        label: Preview Diff
        tip: Show changes without applying
---
```

**Pros:**
- Declarative
- Could enable future Claude Code features
- Self-documenting

**Cons:**
- Claude Code doesn't read frontmatter for menus (yet)
- Extra processing needed

---

## UX Perspectives

### ADHD-Friendly Analysis

| Pattern | ADHD Score | Why |
|---------|------------|-----|
| Always show menu | ⭐⭐⭐ | Clear options, no memorization |
| Smart default | ⭐⭐⭐⭐ | Fast, reduces decisions |
| Hybrid | ⭐⭐⭐⭐⭐ | Best of both |
| Tiered commands | ⭐⭐ | Too many to remember |

**ADHD-Friendly Requirements:**
1. **Reduce decisions** - Default should "just work"
2. **Discoverable** - Can find options when needed
3. **Memorable** - Consistent patterns across commands
4. **Forgiving** - Wrong choice easy to undo

### Power User Analysis

| Pattern | Power Score | Why |
|---------|-------------|-----|
| Always show menu | ⭐⭐ | Extra clicks |
| Smart default | ⭐⭐⭐⭐⭐ | Fast, predictable |
| Hybrid | ⭐⭐⭐⭐ | Good after learning |
| Tiered commands | ⭐⭐⭐ | Explicit but verbose |

---

## Menu Design Patterns

### Pattern A: Radio Selection (Single Choice)

```
┌─────────────────────────────────────────────────────────────┐
│ How should I reorganize the navigation?                     │
├─────────────────────────────────────────────────────────────┤
│ ● Analyze & Propose (Recommended)                           │
│   Review current structure, suggest ADHD-friendly changes   │
│                                                             │
│ ○ ADHD Mode                                                 │
│   Enforce max 7 sections, progressive disclosure            │
│                                                             │
│ ○ Apply Previous                                            │
│   Apply the proposal from last analysis                     │
│                                                             │
│ ○ Preview Only                                              │
│   Show what would change, don't modify files                │
└─────────────────────────────────────────────────────────────┘
```

### Pattern B: Quick Chips

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:nav                                             │
├─────────────────────────────────────────────────────────────┤
│ [Analyze ⭐] [ADHD] [Apply] [Preview]                        │
│                                                             │
│ ⭐ Default: Analyze current nav, propose improvements       │
└─────────────────────────────────────────────────────────────┘
```

### Pattern C: Compact List with Tips

```
Mode?
  ⭐ default     Analyze & propose changes
     adhd       Max 7 sections, ADHD-friendly
     apply      Apply previous proposal
     preview    Show diff only
```

### ⭐ Pattern D: AskUserQuestion Format (Actual Implementation)

```python
# Using Claude Code's AskUserQuestion tool
questions=[{
    "question": "How should I reorganize the navigation?",
    "header": "Mode",
    "options": [
        {"label": "Analyze & Propose (Recommended)",
         "description": "Review current nav, suggest ADHD-friendly changes"},
        {"label": "ADHD Mode",
         "description": "Enforce max 7 sections, progressive disclosure"},
        {"label": "Apply Previous",
         "description": "Apply the proposal from last analysis"},
        {"label": "Preview Only",
         "description": "Show changes without modifying files"}
    ],
    "multiSelect": false
}]
```

---

## ⭐ Keyboard Controls Specification

### Navigation & Selection

| Key | Action |
|-----|--------|
| `↑` / `↓` | Navigate between options |
| `Enter` / `Return` | Select highlighted option |
| `Esc` | Cancel / Exit menu |
| `Ctrl+C` | Force cancel (fallback) |
| `q` | Quick cancel (optional) |

### Visual Feedback

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:nav                                             │
├─────────────────────────────────────────────────────────────┤
│ ▸ Analyze & Propose    Review current nav, suggest changes  │  ← highlighted
│   ADHD Mode            Enforce max 7 sections               │
│   Apply Previous       Apply the proposal from last run     │
│   Preview Only         Show diff without applying           │
├─────────────────────────────────────────────────────────────┤
│ ↑↓ Navigate  ⏎ Select  Esc Cancel                           │
└─────────────────────────────────────────────────────────────┘
```

### Cancel Behavior

When user presses `Esc`:

```
┌─────────────────────────────────────────────────────────────┐
│ Cancelled. No changes made.                                 │
│                                                             │
│ To run directly: /craft:site:nav [mode]                     │
│ Available modes: adhd, apply, preview                       │
└─────────────────────────────────────────────────────────────┘
```

### AskUserQuestion Note

The AskUserQuestion tool in Claude Code automatically provides:
- "Other" option for custom text input
- Arrow key navigation (built-in)
- Enter to select (built-in)

For cancel, user can select "Other" and type "cancel" or just not respond.

---

## Implementation Ideas

### Idea 1: Standard Command Pattern

Create a reusable pattern for all craft commands:

```markdown
# Command Template

## When Invoked

### Step 0: Mode Selection (if no arguments)

If no mode argument provided, use AskUserQuestion:

Question: "What would you like to do?"
Header: "Mode"
Options: [defined per command]

### Step 1: Execute Selected Mode

[mode-specific logic]

### Step 2: Show Next Steps

Always end with:
- What was done
- Quick tip for next time
- Related commands
```

### Idea 2: Command Router Pattern

```markdown
# /craft:site:nav

## Mode Router

Parse arguments or show menu:

| Input | Mode | Action |
|-------|------|--------|
| (none) | menu | Show AskUserQuestion |
| `adhd` | adhd | Skip to ADHD execution |
| `apply` | apply | Skip to apply execution |
| `preview` | preview | Skip to preview execution |
| `--help` | help | Show full help |

## Mode: Menu

[AskUserQuestion implementation]

## Mode: Default (Analyze)

[Analysis implementation]

## Mode: ADHD

[ADHD-constrained analysis]

...
```

### ⭐ Idea 3: Consistent Footer Pattern

Every command ends with:

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ Done: [what was accomplished]                            │
├─────────────────────────────────────────────────────────────┤
│ Quick tip: /craft:site:nav adhd  ← skip menu next time     │
│ Related:   /craft:site:audit     ← audit content next      │
└─────────────────────────────────────────────────────────────┘
```

---

## Recommendations

### Top 3 Ideas

| Rank | Idea | Why | First Step |
|------|------|-----|------------|
| 1 | **Hybrid approach** | Best UX for all users | Define mode detection logic |
| 2 | **AskUserQuestion menu** | Uses existing tool | Create standard question format |
| 3 | **Consistent footer** | Teaches shortcuts | Add to command template |

### Proposed Standard

```markdown
# /craft:site:nav - Navigation Reorganization

## Arguments

| Arg | Alias | Description |
|-----|-------|-------------|
| (default) | | Analyze & propose changes |
| `adhd` | `-a` | Enforce ADHD-friendly limits |
| `apply` | | Apply previous proposal |
| `preview` | `-p` | Show diff without applying |

## When Invoked

### Without Arguments → Show Menu

Use AskUserQuestion with options above.

### With Arguments → Direct Execution

Skip menu, run specified mode.

### Always → End with Tips

Show shortcut tip and related commands.
```

---

## Quick Wins

1. ⚡ **Add `--help` to all commands** - Document options
2. ⚡ **Standardize argument names** - `adhd`, `full`, `preview` across commands
3. ⚡ **Add footer tips** - "Next time: /craft:site:nav adhd"

## Long-Term

1. 🏗️ **Command template generator** - Scaffold new commands with standard pattern
2. 🏗️ **Mode state management** - Remember last used mode
3. 🏗️ **Cross-command coordination** - Pass context between related commands

---

## Next Steps

1. [ ] Choose approach (recommend: Hybrid with AskUserQuestion)
2. [ ] Implement `/craft:site:nav` as proof of concept
3. [ ] Test UX with real usage
4. [ ] Apply pattern to other commands
5. [ ] Document standard in craft README
