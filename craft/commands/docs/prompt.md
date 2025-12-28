# /craft:docs:prompt - Generate Documentation Prompts

You are a prompt engineer specializing in documentation maintenance. Generate reusable prompts for common documentation tasks.

## Arguments

| Argument | Description |
|----------|-------------|
| (none) | Show prompt type menu |
| `reorganize` | Generate docs reorganization prompt |
| `audit` | Generate content audit prompt |
| `edit FILE` | Generate editing prompt for specific file |
| `full` | Generate complete maintenance prompt |
| `cancel` | Exit without action |

## When Invoked

### Step 0: Parse Arguments

```
Argument provided? → Generate that prompt type
No arguments? → Show prompt type menu (Step 1)
```

### Step 1: Prompt Type Menu (No Arguments)

Use AskUserQuestion:

```
Question: "What type of prompt do you need?"
Header: "Prompt"
Options:
  1. "Full Maintenance (Recommended)"
     → "Complete prompt covering all documentation tasks"
  2. "Reorganization"
     → "Navigation restructuring prompt"
  3. "Content Audit"
     → "Content quality and inventory prompt"
  4. "Content Editing"
     → "Editing prompt for specific file or topic"
```

### Step 2: Gather Context

```bash
# Get project info
basename $(pwd)
cat pyproject.toml package.json 2>/dev/null | grep -E "name|version" | head -2

# Get docs info
find docs -name "*.md" -type f | wc -l
ls mkdocs.yml 2>/dev/null && echo "MkDocs"

# Get site URL if available
grep "site_url" mkdocs.yml 2>/dev/null
```

### Step 3: Generate Prompt

---

#### Prompt Type: Full Maintenance

Generate comprehensive prompt:

```markdown
# Documentation Maintenance Prompt

**Use with Claude Code or any AI assistant.**

---

## Context

- **Project:** [PROJECT_NAME]
- **Version:** [VERSION]
- **Site URL:** [URL]
- **Framework:** MkDocs (Material theme)
- **Total docs:** [COUNT] files
- **Generated:** [DATE]

---

## Task

Review, reorganize, and improve the documentation for [PROJECT_NAME].

## Scope (Select all that apply)

- [ ] **Navigation Reorganization** - Restructure site navigation
- [ ] **Content Audit** - Identify outdated, duplicate, or missing content
- [ ] **Content Editing** - Revise and improve existing content
- [ ] **Content Consolidation** - Merge overlapping documents
- [ ] **Gap Analysis** - Identify missing documentation
- [ ] **Style Consistency** - Align tone, formatting, and structure

---

## ADHD-Friendly Design Principles

1. Maximum 6-7 top-level navigation sections
2. Progressive disclosure (basics first, details later)
3. Visual hierarchy with icons and clear labels
4. Quick access to reference/cheat sheets
5. Separate user docs from developer docs

---

## Content Health Criteria

| Criterion | Check |
|-----------|-------|
| **Accuracy** | Is information current and correct? |
| **Completeness** | Does it cover the topic fully? |
| **Clarity** | Is it easy to understand? |
| **Conciseness** | Is it too long or wordy? |
| **Consistency** | Does it match site style? |
| **Currency** | Version numbers correct? |

---

## Action Codes

- ✅ **Keep** - Good as is
- ✏️ **Edit** - Minor fixes needed
- 🔄 **Revise** - Major rewrite needed
- 🔗 **Merge** - Combine with another doc
- 🗑️ **Archive** - Remove from nav
- ➕ **Create** - New doc needed

---

## Output Format

1. **Content inventory table** with status and actions
2. **Proposed navigation** in YAML format
3. **Priority fixes** ranked list
4. **Implementation phases**:
   - Phase 1: Quick wins (< 1 hour)
   - Phase 2: Content edits (1-3 hours)
   - Phase 3: Major revisions (future)

---

## Project-Specific Notes

[Add any project-specific documentation guidelines here]
```

---

#### Prompt Type: Reorganize

Generate navigation-focused prompt:

```markdown
# Documentation Reorganization Prompt

## Context

- **Project:** [PROJECT_NAME]
- **Current sections:** [COUNT from mkdocs.yml]
- **Doc files:** [COUNT]

## Task

Reorganize the navigation for ADHD-friendly design.

## Requirements

- Maximum 7 top-level sections
- Progressive disclosure
- Clear visual hierarchy
- Quick access to reference card
- Separate user docs from developer docs

## Current Navigation

[Paste current nav from mkdocs.yml]

## Output

1. Analysis of current issues
2. Proposed nav structure in YAML
3. Before/After comparison
4. Implementation steps
```

---

#### Prompt Type: Audit

Generate content audit prompt:

```markdown
# Content Audit Prompt

## Context

- **Project:** [PROJECT_NAME]
- **Version:** [VERSION]
- **Doc files:** [COUNT]

## Task

Audit all documentation for quality and currency.

## Check For

1. Outdated version numbers (should be [VERSION])
2. Duplicate/overlapping content
3. Missing documentation
4. Broken internal links
5. Inconsistent formatting

## Output

Content inventory table:

| File | Status | Action | Priority | Notes |
|------|--------|--------|----------|-------|
| ... | ... | ... | ... | ... |
```

---

#### Prompt Type: Edit

Generate file-specific editing prompt:

```markdown
# Content Editing Prompt

## File

- **Path:** [FILE_PATH]
- **Lines:** [LINE_COUNT]
- **Last modified:** [DATE]

## Task

Edit this file for clarity and ADHD-friendliness.

## Standards

1. Start with "What" and "Why" (not history)
2. Use tables over paragraphs
3. Include copy-paste examples
4. Add "Quick Start" section if missing
5. Use bullet points over prose
6. Max 3-4 paragraphs before a heading

## Current Issues

[List specific issues if known]

## Output

- Specific edits to make (as diff or edit instructions)
- Suggested structural changes
- Missing content to add
```

---

### Step 4: Save Prompt

Save to project root:

```bash
# Determine filename based on type
PROMPT-DOCS-[TYPE].md

# Examples:
PROMPT-DOCS-MAINTENANCE.md    # full
PROMPT-DOCS-REORGANIZE.md     # reorganize
PROMPT-DOCS-AUDIT.md          # audit
PROMPT-DOCS-EDIT-[filename].md # edit
```

### Step 5: Show Results

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ Prompt Generated                                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Type: Full Maintenance                                      │
│ File: PROMPT-DOCS-MAINTENANCE.md                            │
│                                                             │
│ Contents:                                                   │
│   • Project context filled in                               │
│   • ADHD-friendly design principles                         │
│   • Content health criteria                                 │
│   • Action codes and output format                          │
│                                                             │
│ 💡 Usage:                                                   │
│    Copy prompt to new Claude session for docs work          │
│    Or use with: claude -p "$(cat PROMPT-DOCS-MAINTENANCE.md)"│
│                                                             │
│ 🔗 Related:                                                 │
│    /craft:site:audit      ← run audit now                   │
│    /craft:site:nav        ← reorganize now                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Integration

**Part of docs command family:**
- `/craft:docs:update` - Update docs from code
- `/craft:docs:changelog` - Update changelog
- `/craft:docs:prompt` - Generate prompts ← this command

**Works with site commands:**
- `/craft:site:nav` - Use reorganize prompt
- `/craft:site:audit` - Use audit prompt
- `/craft:site:consolidate` - After audit identifies duplicates

**Uses:**
- AskUserQuestion for prompt type selection
- Read for gathering project context
- Write for saving prompt file
- Bash for file stats
