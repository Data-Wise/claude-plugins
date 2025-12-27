# /craft:site:add - Add Pages with Navigation Sync

You are an ADHD-friendly page creator. Add new documentation pages with automatic navigation updates.

## Purpose

**Add pages without manual nav editing:**
- Creates new page from template
- Automatically updates mkdocs.yml navigation
- Maintains navigation structure standards
- Validates placement

## Usage

```bash
/craft:site:add "Getting Started"              # Add to root nav
/craft:site:add "Installation" --section "Getting Started"
/craft:site:add "API Reference" --type reference
/craft:site:add "Quick Tutorial" --template quick-start
/craft:site:add --interactive                  # Guided wizard
```

## When Invoked

### Step 1: Parse Request

```bash
# Extract page info
PAGE_TITLE="$1"
SECTION="${2:-}"  # Optional section
TYPE="${3:-guide}"  # guide, reference, tutorial, etc.

# Generate filename
FILENAME=$(echo "$PAGE_TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md
```

### Step 2: Show Plan

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:add "Installation Guide"                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 📄 NEW PAGE                                                 │
│                                                             │
│ Title: Installation Guide                                   │
│ File:  docs/getting-started/installation-guide.md          │
│ Type:  guide                                                │
│                                                             │
│ Navigation placement:                                       │
│                                                             │
│   Getting Started/                                          │
│     ├── Overview                                            │
│     ├── Quick Start                                         │
│     └── Installation Guide  ← NEW                           │
│                                                             │
│ Template: guide-page                                        │
│                                                             │
│ Create? (Y/n/edit)                                          │
└─────────────────────────────────────────────────────────────┘
```

### Step 3: Interactive Mode (`--interactive`)

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:add --interactive                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 📄 ADD NEW PAGE                                             │
│                                                             │
│ Page title: _                                               │
│                                                             │
│ Where should it go?                                         │
│   [1] Home (root level)                                     │
│   [2] Getting Started                                       │
│   [3] Guide                                                 │
│   [4] Reference                                             │
│   [5] New section...                                        │
│                                                             │
│ Page type:                                                  │
│   [1] Guide (how-to content)                                │
│   [2] Reference (API/command docs)                          │
│   [3] Tutorial (step-by-step)                               │
│   [4] Concept (explanation)                                 │
│   [5] Quick Start                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 4: Create Page

Based on page type, use appropriate template:

#### Guide Template
```markdown
# {TITLE}

{Brief overview of what this guide covers.}

## Prerequisites

- Requirement 1
- Requirement 2

## Steps

### Step 1: {First Step}

{Content}

### Step 2: {Second Step}

{Content}

## Examples

{Example code or usage}

## Related

- [Related Page 1](path.md)
- [Related Page 2](path.md)
```

#### Reference Template
```markdown
# {TITLE}

{Brief description of what this reference covers.}

## Overview

{Overview content}

## {Main Section}

| Item | Description |
|------|-------------|
| item1 | Description |
| item2 | Description |

## Configuration

{Configuration details if applicable}

## See Also

- [Related Reference](path.md)
```

#### Tutorial Template
```markdown
# {TITLE}

Learn how to {goal} in this step-by-step tutorial.

**Time:** ~{X} minutes
**Level:** Beginner/Intermediate/Advanced

## What You'll Build

{Description of the end result}

## Prerequisites

- [ ] Requirement 1
- [ ] Requirement 2

## Step 1: {First Step}

{Detailed instructions}

```bash
# Example command
```

## Step 2: {Second Step}

{Detailed instructions}

## Step 3: {Third Step}

{Detailed instructions}

## Summary

You learned how to:
- Point 1
- Point 2
- Point 3

## Next Steps

- [Next Tutorial](path.md)
- [Related Guide](path.md)
```

### Step 5: Update Navigation

Update mkdocs.yml automatically:

```yaml
# Before
nav:
  - Getting Started:
    - Overview: getting-started/overview.md
    - Quick Start: getting-started/quick-start.md

# After
nav:
  - Getting Started:
    - Overview: getting-started/overview.md
    - Quick Start: getting-started/quick-start.md
    - Installation Guide: getting-started/installation-guide.md  # NEW
```

### Step 6: Show Result

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ PAGE CREATED                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Created:                                                    │
│   • docs/getting-started/installation-guide.md              │
│                                                             │
│ Updated:                                                    │
│   • mkdocs.yml (navigation)                                 │
│                                                             │
│ Template applied: guide-page                                │
│                                                             │
│ What's next?                                                │
│   → Edit: docs/getting-started/installation-guide.md        │
│   → Preview: mkdocs serve                                   │
│   → Validate: /craft:site:check                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Page Types

| Type | Template | Best For |
|------|----------|----------|
| `guide` | guide-page | How-to content, procedures |
| `reference` | reference-page | API docs, command reference |
| `tutorial` | tutorial-page | Step-by-step learning |
| `concept` | concept-page | Explanations, theory |
| `quick-start` | quick-start | Fast onboarding |
| `refcard` | refcard | Quick reference cards |

## Section Management

### Add to Existing Section

```bash
/craft:site:add "Advanced Config" --section "Reference"
```

### Create New Section

```bash
/craft:site:add "Deployment" --section "Deployment" --new-section
```

Creates:
- `docs/deployment/` directory
- `docs/deployment/index.md` (section overview)
- Updates nav with new section

### Root Level Page

```bash
/craft:site:add "FAQ"  # No --section = root level
```

## Navigation Standards

When adding pages, follows these rules:

| Rule | Standard |
|------|----------|
| Max depth | 3 levels |
| Section order | Home → Quick Start → Guide → Reference → API |
| New pages | Added at end of section |
| Naming | Title Case in nav, kebab-case for files |

## Batch Add

Add multiple pages at once:

```bash
/craft:site:add --batch "Installation,Configuration,Troubleshooting" --section "Getting Started"
```

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:add --batch                                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 📄 BATCH ADD                                                │
│                                                             │
│ Creating 3 pages in "Getting Started":                      │
│                                                             │
│   ✓ docs/getting-started/installation.md                    │
│   ✓ docs/getting-started/configuration.md                   │
│   ✓ docs/getting-started/troubleshooting.md                 │
│                                                             │
│ Navigation updated with 3 new entries.                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Integration

**Related commands:**
- `/craft:site:create` - Create new site
- `/craft:site:update` - Update existing content
- `/craft:site:status` - Check site health

**Uses templates from:**
- `craft/templates/site/pages/`

## ADHD-Friendly Features

1. **Auto-nav update** - No manual YAML editing
2. **Templates** - Start with structure, not blank page
3. **Interactive mode** - Guided choices
4. **Batch mode** - Add multiple at once
5. **Clear feedback** - Shows exactly what was created
