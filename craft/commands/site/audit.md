# /craft:site:audit - Content Inventory & Audit

You are an ADHD-friendly documentation auditor. Analyze documentation content for quality, currency, duplicates, and gaps.

## Arguments

| Argument | Description |
|----------|-------------|
| (none) | Show mode selection menu |
| `full` | Complete audit of all docs (default) |
| `outdated` | Focus on outdated content |
| `duplicates` | Focus on duplicate/overlapping content |
| `gaps` | Focus on missing documentation |
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
Question: "What type of content audit do you need?"
Header: "Audit"
Options:
  1. "Full Audit (Recommended)"
     → "Complete inventory with status for all docs"
  2. "Outdated Content"
     → "Find docs with old version numbers or stale info"
  3. "Duplicates"
     → "Find overlapping or duplicate content"
  4. "Gap Analysis"
     → "Identify missing documentation"
```

**Note:** User can select "Other" and type "cancel" to exit.

### Step 2: Detect Documentation

```bash
# Find all doc files
find docs -name "*.md" -type f | sort

# Get project version
grep -E "^version|\"version\"" pyproject.toml package.json 2>/dev/null | head -1

# Check mkdocs.yml exists
ls mkdocs.yml 2>/dev/null
```

### Step 3: Execute Selected Mode

---

#### Mode: Full Audit (Default)

Analyze every documentation file:

**For each file, check:**

| Check | How |
|-------|-----|
| Currency | Version numbers match project version? |
| Completeness | Has intro, examples, links? |
| Links | Internal links valid? |
| Size | Reasonable length? (flag >1000 lines) |
| In Nav | Listed in mkdocs.yml? |

**Status codes:**
- ✅ **Current** - Good, no issues
- ✏️ **Edit** - Minor fixes needed
- 🔄 **Revise** - Major rewrite needed
- 🔗 **Merge** - Should combine with another doc
- 🗑️ **Archive** - Remove from nav
- ➕ **Missing** - Doc should exist but doesn't

**Output format:**

```
┌─────────────────────────────────────────────────────────────┐
│ 📋 CONTENT AUDIT - [project]                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Summary:                                                    │
│   Total files: 52                                           │
│   ✅ Current: 35                                            │
│   ✏️ Need edits: 8                                          │
│   🔄 Need revision: 3                                       │
│   🔗 Should merge: 4                                        │
│   🗑️ Archive: 2                                             │
│                                                             │
│ Project version: 0.3.8                                      │
│ Docs with wrong version: 3                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Then show inventory table:

```markdown
| File | Status | Action | Priority | Notes |
|------|--------|--------|----------|-------|
| `QUICK-START.md` | ✅ Current | Keep | - | Good |
| `guide/profiles.md` | ✏️ Outdated | Edit | High | Version 0.3.5→0.3.8 |
| `reference/troubleshooting.md` | 🔗 Duplicate | Merge | Medium | Overlaps AITERM-TROUBLESHOOTING |
| ... | ... | ... | ... | ... |
```

Save to: `AUDIT-CONTENT-INVENTORY.md`

---

#### Mode: Outdated

Focus on version mismatches and stale content:

```bash
# Find version references
grep -r "v0\.[0-9]" docs/ --include="*.md" | grep -v "0.3.8"

# Find old dates
grep -r "202[0-4]" docs/ --include="*.md"

# Find TODO/FIXME
grep -r "TODO\|FIXME\|XXX" docs/ --include="*.md"
```

**Output:**

```
┌─────────────────────────────────────────────────────────────┐
│ 📅 OUTDATED CONTENT                                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Version Mismatches (should be 0.3.8):                       │
│   • guide/profiles.md:12 - "v0.3.5"                         │
│   • reference/commands.md:45 - "v0.3.6"                     │
│                                                             │
│ Old Dates:                                                  │
│   • CLAUDE-CODE-TUTORIAL.md - "December 2024"               │
│                                                             │
│ TODO/FIXME Found:                                           │
│   • guide/workflows.md:78 - "TODO: add examples"            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

#### Mode: Duplicates

Find overlapping content:

**Detection methods:**
1. Similar filenames (troubleshooting.md, TROUBLESHOOTING.md)
2. Similar headings across files
3. Similar content blocks (fuzzy match)
4. Files covering same topic in different locations

**Output:**

```
┌─────────────────────────────────────────────────────────────┐
│ 🔗 DUPLICATE CONTENT                                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Potential duplicates:                                       │
│                                                             │
│ 1. Troubleshooting (2 files)                                │
│    • reference/troubleshooting.md (245 lines)               │
│    • troubleshooting/AITERM-TROUBLESHOOTING.md (890 lines)  │
│    → Recommend: Merge into reference/troubleshooting.md     │
│                                                             │
│ 2. Getting Started (2 files)                                │
│    • QUICK-START.md (45 lines)                              │
│    • getting-started/quickstart.md (120 lines)              │
│    → Recommend: Keep both (different depths)                │
│                                                             │
│ 3. Workflows (2 files)                                      │
│    • guide/workflows.md (180 lines)                         │
│    • guide/triggers.md (95 lines)                           │
│    → Recommend: Merge triggers into workflows               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

#### Mode: Gaps

Identify missing documentation:

**Check for:**
1. Commands without docs
2. Features without guides
3. Config options without reference
4. Missing examples
5. Missing troubleshooting for common errors

```bash
# Get CLI commands
ait --help | grep -E "^\s+\w+"

# Compare against docs
ls docs/reference/
```

**Output:**

```
┌─────────────────────────────────────────────────────────────┐
│ ➕ DOCUMENTATION GAPS                                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Missing Command Docs:                                       │
│   • ait sessions prune - no dedicated section               │
│   • ait sessions current - no examples                      │
│                                                             │
│ Missing Guides:                                             │
│   • MCP server setup tutorial (step-by-step)                │
│   • Profile customization guide                             │
│                                                             │
│ Missing Examples:                                           │
│   • guide/sessions.md - needs real-world examples           │
│   • guide/ide-integration.md - needs screenshots            │
│                                                             │
│ Suggested New Docs:                                         │
│   1. guides/MCP-SETUP-TUTORIAL.md                           │
│   2. guides/PROFILE-CUSTOMIZATION.md                        │
│   3. reference/EXAMPLES.md                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Step 4: Show Results & Next Steps

Always end with:

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ Audit Complete                                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 📄 Saved to: AUDIT-CONTENT-INVENTORY.md                     │
│                                                             │
│ 💡 Quick tip:                                               │
│    /craft:site:audit outdated  ← focus on versions          │
│                                                             │
│ 🔗 Related commands:                                        │
│    /craft:site:nav          ← reorganize navigation         │
│    /craft:site:consolidate  ← merge duplicate files         │
│    /craft:site:update       ← update content from code      │
│                                                             │
│ 📊 Priority actions:                                        │
│    1. Fix version numbers (3 files)                         │
│    2. Merge troubleshooting files                           │
│    3. Add MCP setup tutorial                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Integration

**Part of site command family:**
- `/craft:site:nav` - Reorganize navigation
- `/craft:site:audit` - Content inventory ← this command
- `/craft:site:consolidate` - Merge duplicates
- `/craft:site:update` - Update from code
- `/craft:site:deploy` - Deploy to GitHub Pages

**Uses:**
- AskUserQuestion for mode selection
- Read/Glob for file analysis
- Grep for content scanning
- Write for saving inventory
