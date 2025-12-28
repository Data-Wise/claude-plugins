# /craft:site:nav - Navigation Reorganization

You are an ADHD-friendly documentation site navigation expert. Analyze and reorganize mkdocs.yml navigation for clarity and reduced cognitive load.

## Arguments

| Argument | Description |
|----------|-------------|
| (none) | Show mode selection menu |
| `analyze` | Analyze current nav, propose changes (default) |
| `adhd` | Enforce ADHD-friendly limits (max 7 sections) |
| `apply` | Apply previous proposal to mkdocs.yml |
| `preview` | Show diff without applying changes |
| `cancel` | Exit without action |

## When Invoked

### Step 0: Parse Arguments

Check if user provided a mode argument:

```
Arguments provided? → Skip to Step 2 with that mode
No arguments? → Show mode selection menu (Step 1)
```

### Step 1: Mode Selection Menu (No Arguments)

Use AskUserQuestion to show interactive menu:

```
Question: "How should I reorganize the navigation?"
Header: "Mode"
Options:
  1. "Analyze & Propose (Recommended)"
     → "Review current nav structure, suggest ADHD-friendly changes"
  2. "ADHD Mode"
     → "Enforce max 7 top-level sections, progressive disclosure"
  3. "Apply Previous"
     → "Apply the proposal from last analysis to mkdocs.yml"
  4. "Preview Only"
     → "Show what would change without modifying files"
```

**Note:** User can select "Other" and type "cancel" to exit.

If user selects "Other" with "cancel":
```
┌─────────────────────────────────────────────────────────────┐
│ Cancelled. No changes made.                                 │
│                                                             │
│ To run directly: /craft:site:nav [mode]                     │
│ Available modes: analyze, adhd, apply, preview              │
└─────────────────────────────────────────────────────────────┘
```
Then stop.

### Step 2: Detect Documentation Framework

```bash
# Check for mkdocs
ls mkdocs.yml 2>/dev/null

# Check current nav structure
cat mkdocs.yml
```

If no mkdocs.yml found:
```
┌─────────────────────────────────────────────────────────────┐
│ ❌ No mkdocs.yml found                                      │
│                                                             │
│ This command works with MkDocs sites.                       │
│ To create a new site: /craft:site:create                    │
└─────────────────────────────────────────────────────────────┘
```
Then stop.

### Step 3: Analyze Current Navigation

```bash
# Count top-level sections
grep -E "^  - " mkdocs.yml | wc -l

# List all doc files
find docs -name "*.md" -type f | wc -l

# Check for orphan files (not in nav)
# Compare docs/*.md against nav entries
```

Display analysis:
```
┌─────────────────────────────────────────────────────────────┐
│ 📊 NAVIGATION ANALYSIS                                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Current Structure:                                          │
│   • Top-level sections: 12  ⚠️ (recommended: ≤7)            │
│   • Total nav items: 45                                     │
│   • Doc files: 52                                           │
│   • Orphan files: 7 (not in nav)                            │
│                                                             │
│ Issues Detected:                                            │
│   ⚠️ Too many top-level sections (12 > 7)                   │
│   ⚠️ Duplicate content paths                                │
│   ⚠️ Deep nesting (>3 levels)                               │
│   ✓ All links valid                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 4: Execute Selected Mode

---

#### Mode: Analyze (Default)

Analyze and propose reorganization:

**ADHD-Friendly Design Principles:**
1. Maximum 6-7 top-level sections
2. Progressive disclosure (basics first, details later)
3. Clear visual hierarchy
4. Quick access to reference/cheat sheets
5. Separate user docs from developer docs

**Proposed Structure Template:**
```yaml
nav:
  # TIER 1: ESSENTIALS
  - Home: index.md
  - Get Started:
      - Quick Install: QUICK-START.md
      - First Steps: GETTING-STARTED.md
  - Reference Card: REFCARD.md

  # TIER 2: CORE FEATURES
  - Features:
      - [grouped by functionality]

  # TIER 3: INTEGRATIONS (if applicable)
  - Integrations:
      - [grouped by tool/service]

  # TIER 4: REFERENCE
  - Reference:
      - [commands, config, troubleshooting]

  # TIER 5: GUIDES
  - Guides:
      - [tutorials, deep dives]

  # TIER 6: DEVELOPMENT (if applicable)
  - Development:
      - [architecture, contributing]
```

Generate specific proposal based on current content.

Save proposal to: `PROPOSAL-NAV-REORGANIZATION.md`

---

#### Mode: ADHD

Same as Analyze, but enforce strict limits:

| Constraint | Limit |
|------------|-------|
| Top-level sections | Maximum 7 |
| Nesting depth | Maximum 3 levels |
| Items per section | Maximum 8 |
| Required sections | Home, Get Started, Reference |

If current nav exceeds limits, propose consolidation.

---

#### Mode: Apply

Check for existing proposal:
```bash
ls PROPOSAL-NAV-REORGANIZATION.md 2>/dev/null || ls PROPOSAL-DOCS-REORGANIZATION.md 2>/dev/null
```

If no proposal found:
```
┌─────────────────────────────────────────────────────────────┐
│ ❌ No proposal found                                        │
│                                                             │
│ Run analysis first: /craft:site:nav analyze                 │
└─────────────────────────────────────────────────────────────┘
```

If proposal exists:
1. Read the proposed nav structure from proposal
2. Show diff between current and proposed
3. Ask for confirmation
4. Apply changes to mkdocs.yml
5. Validate with `mkdocs build`

---

#### Mode: Preview

Same as Analyze, but:
- Show proposed changes as diff
- Do NOT save proposal file
- Do NOT modify any files

```
┌─────────────────────────────────────────────────────────────┐
│ 🔍 PREVIEW MODE (no changes made)                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Proposed changes to mkdocs.yml:                             │
│                                                             │
│ - 12 top-level sections → 7 sections                        │
│ - "Documentation Automation" → removed from nav             │
│ - "Gemini CLI" → moved to Integrations                      │
│ - "Features" → expanded with MCP, Claude, OpenCode          │
│                                                             │
│ To apply: /craft:site:nav apply                             │
│ To save proposal: /craft:site:nav analyze                   │
└─────────────────────────────────────────────────────────────┘
```

---

### Step 5: Show Results & Next Steps

Always end with this footer:

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ Done: [summary of what was accomplished]                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 💡 Quick tip:                                               │
│    /craft:site:nav adhd  ← skip menu, run ADHD mode         │
│                                                             │
│ 🔗 Related commands:                                        │
│    /craft:site:audit      ← audit content quality           │
│    /craft:site:update     ← update content from code        │
│    /craft:site:deploy     ← deploy to GitHub Pages          │
│                                                             │
│ 📄 Files:                                                   │
│    PROPOSAL-NAV-REORGANIZATION.md  ← saved proposal         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Example Outputs

### Successful Analysis

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ Navigation Analysis Complete                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Current: 12 sections → Proposed: 7 sections                 │
│                                                             │
│ Proposed structure:                                         │
│   1. Home                                                   │
│   2. Get Started (4 pages)                                  │
│   3. Reference Card                                         │
│   4. Features (7 pages)                                     │
│   5. Integrations (12 pages)                                │
│   6. Reference (7 pages)                                    │
│   7. Development (6 pages)                                  │
│                                                             │
│ Saved to: PROPOSAL-NAV-REORGANIZATION.md                    │
│                                                             │
│ Next: Review proposal, then /craft:site:nav apply           │
└─────────────────────────────────────────────────────────────┘
```

### Already Optimized

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ Navigation Already Optimized                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Current structure meets ADHD-friendly guidelines:           │
│   ✓ 7 top-level sections (≤7)                               │
│   ✓ Max nesting depth: 2 (≤3)                               │
│   ✓ No orphan files                                         │
│   ✓ Clear hierarchy                                         │
│                                                             │
│ No changes recommended.                                     │
└─────────────────────────────────────────────────────────────┘
```

## Integration

**Part of site command family:**
- `/craft:site:create` - Create new site
- `/craft:site:nav` - Reorganize navigation ← this command
- `/craft:site:audit` - Content audit
- `/craft:site:update` - Update from code
- `/craft:site:deploy` - Deploy to GitHub Pages

**Uses:**
- AskUserQuestion for mode selection
- Read tool for mkdocs.yml analysis
- Write tool for proposal file
- Edit tool for applying changes
