# Craft Docs Commands - Complete Workflow Proposal

**Generated:** 2025-12-27
**Focus:** Comprehensive doc updates after features + workflow commands
**Key Insight:** Keep individual commands, ADD workflow orchestrators

---

## Your Workflow Needs

After adding a feature, you want ALL of these updated:
- [ ] CLI help text (if command has `--help`)
- [ ] Website docs (`docs/reference/commands.md`, etc.)
- [ ] README.md (feature list, badges)
- [ ] REFCARD.md (quick reference)
- [ ] Tutorials (if feature has learning curve)
- [ ] CLAUDE.md (project status)
- [ ] CHANGELOG.md (for release)
- [ ] mkdocs.yml nav (if new pages)

**Current Problem:** You have to remember which individual commands to run.

**Solution:** Add **workflow commands** that orchestrate multiple updates.

---

## Proposed Command Structure

### Keep All Individual Commands (Unchanged)

```
/craft:docs:sync        - Detect changes, update affected docs
/craft:docs:changelog   - Update CHANGELOG.md
/craft:docs:claude-md   - Update CLAUDE.md / .STATUS
/craft:docs:nav-update  - Update mkdocs.yml navigation
/craft:docs:validate    - Check links, code examples
/craft:docs:generate    - Create new docs with agents
/craft:docs:api         - OpenAPI spec generation
```

### ⭐ ADD: Workflow Commands (NEW)

```
/craft:docs:update      - Smart update (detects what needs updating)
/craft:docs:feature     - Full update after adding a feature
/craft:docs:done        - End-of-session doc updates
/craft:docs:site        - Website-focused updates
/craft:docs:recent      - Update based on recent commits
```

---

## New Commands Explained

### ⭐ 1. `/craft:docs:update [scope]` - The Universal Updater

**Purpose:** One command to update everything that needs updating.

```bash
/craft:docs:update              # Smart: detect what changed, update relevant
/craft:docs:update full         # Update ALL doc types
/craft:docs:update all          # Alias for full
/craft:docs:update --preview    # Show what would be updated (dry run)
```

**What it updates (when relevant):**

| Doc Type | When Updated | Files |
|----------|--------------|-------|
| CLI Help | New/changed commands | `src/*/cli/*.py` epilogs |
| Commands Reference | CLI changes | `docs/reference/commands.md` |
| README | New features, badges | `README.md` |
| REFCARD | New commands/features | `docs/REFCARD.md`, `docs/reference/REFCARD-*.md` |
| Tutorials | Major features | `docs/guide/*.md` |
| CLAUDE.md | Always | `CLAUDE.md` |
| Navigation | New doc files | `mkdocs.yml` |

**How it decides what to update:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:docs:update                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Analyzing recent changes...                                 │
│                                                             │
│ Detected:                                                   │
│   • 2 new CLI commands (src/aiterm/cli/hello.py)            │
│   • 1 modified config (pyproject.toml version bump)         │
│   • 3 new doc files (docs/guide/sessions.md, ...)           │
│                                                             │
│ Will update:                                                │
│   ✓ docs/reference/commands.md (new commands)               │
│   ✓ docs/REFCARD.md (new commands)                          │
│   ✓ README.md (feature list)                                │
│   ✓ CLAUDE.md (version, status)                             │
│   ✓ mkdocs.yml (new nav entries)                            │
│   ○ CHANGELOG.md (skipped - use docs:changelog for release) │
│                                                             │
│ Proceed? (y/n/select)                                       │
└─────────────────────────────────────────────────────────────┘
```

**`/craft:docs:update full` updates EVERYTHING:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:docs:update full                                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Full documentation update:                                  │
│                                                             │
│ Phase 1: Code Analysis                                      │
│   • Scanning CLI commands...                                │
│   • Extracting docstrings...                                │
│   • Reading current docs...                                 │
│                                                             │
│ Phase 2: Updates                                            │
│   ✓ CLI Help epilogs (3 commands updated)                   │
│   ✓ docs/reference/commands.md (+45 lines)                  │
│   ✓ docs/REFCARD.md (+12 lines)                             │
│   ✓ docs/reference/REFCARD-SESSIONS.md (new file)           │
│   ✓ README.md (badges, feature list)                        │
│   ✓ CLAUDE.md (version, quick reference)                    │
│   ✓ mkdocs.yml (4 new nav entries)                          │
│                                                             │
│ Phase 3: Validation                                         │
│   ✓ All links valid                                         │
│   ✓ Code examples compile                                   │
│                                                             │
│ ✅ 7 files updated, 0 errors                                │
└─────────────────────────────────────────────────────────────┘
```

---

### ⭐ 2. `/craft:docs:feature [name]` - After Adding a Feature

**Purpose:** Comprehensive update after implementing a new feature.

```bash
/craft:docs:feature                    # Detect feature from recent commits
/craft:docs:feature "session tracking" # Specify feature name
/craft:docs:feature --interactive      # Guide through each doc type
```

**What it does:**

1. **Detects feature scope** from recent commits
2. **Updates CLI help** if new commands
3. **Updates commands reference** with new commands
4. **Updates REFCARD** with quick reference
5. **Suggests tutorial** if feature is complex
6. **Updates README** feature list
7. **Updates CLAUDE.md** with feature in "Just Completed"
8. **Updates mkdocs nav** if new pages created
9. **Validates** all changes

**Output:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:docs:feature "session tracking"                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 📦 FEATURE: Session Tracking                                │
│                                                             │
│ Detected components:                                        │
│   • 5 new CLI commands (sessions live/task/conflicts/...)   │
│   • 2 new hooks (session-register, session-cleanup)         │
│   • 1 new module (src/aiterm/sessions/)                     │
│                                                             │
│ Documentation updates:                                      │
│                                                             │
│ 1. CLI Help                                                 │
│    ✓ Added epilog examples to 5 commands                    │
│                                                             │
│ 2. Commands Reference                                       │
│    ✓ docs/reference/commands.md (+85 lines)                 │
│    ✓ Added "Sessions" section with all 5 commands           │
│                                                             │
│ 3. REFCARD                                                  │
│    ✓ docs/REFCARD.md (+8 lines, sessions section)           │
│    ✓ docs/reference/REFCARD-SESSIONS.md (NEW - 120 lines)   │
│                                                             │
│ 4. Guide                                                    │
│    ✓ docs/guide/sessions.md (NEW - 250 lines)               │
│    ⭐ Suggests: Create tutorial? (y/n)                       │
│                                                             │
│ 5. README                                                   │
│    ✓ Added "Session Coordination" to features               │
│                                                             │
│ 6. CLAUDE.md                                                │
│    ✓ Added to "Just Completed" section                      │
│    ✓ Updated Quick Reference with session commands          │
│                                                             │
│ 7. Navigation                                               │
│    ✓ mkdocs.yml: Added guide/sessions.md                    │
│    ✓ mkdocs.yml: Added reference/REFCARD-SESSIONS.md        │
│                                                             │
│ ✅ Feature documentation complete!                          │
│                                                             │
│ Next: /craft:docs:validate (recommended)                    │
└─────────────────────────────────────────────────────────────┘
```

---

### 3. `/craft:docs:done` - End of Session Updates

**Purpose:** Quick updates when finishing a coding session.

```bash
/craft:docs:done                  # Update status, sync recent changes
/craft:docs:done "implemented X"  # With session summary
```

**What it does:**

1. **Updates CLAUDE.md** "Just Completed" section
2. **Updates .STATUS** file
3. **Runs docs:sync** for any recent code changes
4. **Validates** (quick internal-only check)

**Output:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:docs:done "implemented session tracking"             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 📝 SESSION DOCUMENTATION                                    │
│                                                             │
│ Updated:                                                    │
│   ✓ CLAUDE.md - Added to "Just Completed"                   │
│   ✓ .STATUS - Updated progress, next action                 │
│   ✓ docs/reference/commands.md - Synced recent changes      │
│                                                             │
│ Session stats:                                              │
│   • 5 commits                                               │
│   • +450/-23 lines                                          │
│   • 3 new files                                             │
│                                                             │
│ ✅ Ready to commit: git add -A && git commit                │
└─────────────────────────────────────────────────────────────┘
```

---

### 4. `/craft:docs:site` - Website Documentation Focus

**Purpose:** Update all website-related docs (for mkdocs/docusaurus).

```bash
/craft:docs:site              # Update website docs
/craft:docs:site --preview    # Preview changes
/craft:docs:site --deploy     # Update + deploy to GitHub Pages
```

**What it does:**

1. **Updates** all files in `docs/` directory
2. **Updates mkdocs.yml** navigation
3. **Validates** links and structure
4. **Optionally deploys** to GitHub Pages

**Targets:**

```
docs/
├── index.md              ← Updated (badges, overview)
├── REFCARD.md            ← Updated (quick reference)
├── QUICK-START.md        ← Updated (installation)
├── getting-started/      ← Updated (installation, setup)
├── guide/                ← Updated (feature guides)
├── reference/            ← Updated (commands, config, refcards)
├── api/                  ← Updated (if applicable)
└── troubleshooting/      ← Updated (common issues)
```

---

### 5. `/craft:docs:recent` - Update Based on Recent Commits

**Purpose:** Update docs based on what changed in recent commits.

```bash
/craft:docs:recent           # Last 5 commits
/craft:docs:recent 10        # Last 10 commits
/craft:docs:recent --since v0.3.0  # Since tag
```

**What it does:**

1. **Analyzes** recent commits for doc-worthy changes
2. **Identifies** which docs need updating
3. **Updates** only relevant docs
4. **Shows** what was changed

---

## Complete Command Reference

### Workflow Commands (NEW)

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/craft:docs:update` | Smart update everything | After any changes |
| `/craft:docs:update full` | Force update ALL docs | Major milestones |
| `/craft:docs:feature` | Full feature documentation | After adding feature |
| `/craft:docs:done` | Session end updates | End of coding session |
| `/craft:docs:site` | Website docs only | Before deploying site |
| `/craft:docs:recent` | Recent commits only | Quick sync |

### Individual Commands (Keep)

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/craft:docs:sync` | Detect & update changed | After code changes |
| `/craft:docs:changelog` | Update CHANGELOG | Before release |
| `/craft:docs:claude-md` | Update CLAUDE.md | Status updates |
| `/craft:docs:nav-update` | Update mkdocs nav | After adding doc files |
| `/craft:docs:validate` | Check links/code | Before deploy |
| `/craft:docs:generate` | Create from scratch | New project/feature |
| `/craft:docs:api` | OpenAPI generation | API projects |

---

## Workflow Cheat Sheet

```
┌─────────────────────────────────────────────────────────────┐
│ 📝 DOCS WORKFLOW CHEAT SHEET                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ AFTER ADDING A FEATURE:                                     │
│   → /craft:docs:feature                                     │
│   (updates: CLI, reference, refcard, readme, claude-md)     │
│                                                             │
│ END OF SESSION:                                             │
│   → /craft:docs:done                                        │
│   (updates: claude-md, .status, syncs recent changes)       │
│                                                             │
│ BEFORE RELEASE:                                             │
│   → /craft:docs:changelog                                   │
│   → /craft:docs:update full                                 │
│   → /craft:docs:validate                                    │
│                                                             │
│ BEFORE DEPLOYING SITE:                                      │
│   → /craft:docs:site --deploy                               │
│   (updates: all website docs, validates, deploys)           │
│                                                             │
│ QUICK UPDATE (any time):                                    │
│   → /craft:docs:update                                      │
│   (smart detection of what needs updating)                  │
│                                                             │
│ COMPREHENSIVE UPDATE:                                       │
│   → /craft:docs:update full                                 │
│   (updates EVERYTHING regardless of changes)                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## What Gets Updated (Matrix)

| Doc Type | update | feature | done | site | sync |
|----------|--------|---------|------|------|------|
| CLI Help (epilogs) | ✓ | ✓ | - | - | - |
| commands.md | ✓ | ✓ | ✓ | ✓ | ✓ |
| REFCARD.md | ✓ | ✓ | - | ✓ | - |
| REFCARD-*.md | ✓ | ✓ | - | ✓ | - |
| README.md | ✓ | ✓ | - | - | - |
| CLAUDE.md | ✓ | ✓ | ✓ | - | - |
| .STATUS | - | - | ✓ | - | - |
| Guide docs | ✓ | ✓ | - | ✓ | ✓ |
| Tutorials | opt | opt | - | ✓ | - |
| mkdocs.yml | ✓ | ✓ | - | ✓ | - |
| CHANGELOG.md | - | - | - | - | - |

Legend: ✓ = always, opt = optional/suggested, - = not updated

---

## Implementation Priority

### Phase 1: Core Workflow Commands (1-2 days)

1. **`/craft:docs:update`** - The universal updater
   - `update` = smart detection
   - `update full` = everything

2. **`/craft:docs:feature`** - After feature implementation
   - Detects new commands, modules, files
   - Updates all relevant docs

### Phase 2: Session Commands (1 day)

3. **`/craft:docs:done`** - End of session
   - Quick CLAUDE.md + .STATUS update
   - Syncs recent changes

4. **`/craft:docs:recent`** - Recent commits
   - Analyze commit history
   - Update affected docs

### Phase 3: Site Focus (1 day)

5. **`/craft:docs:site`** - Website focus
   - All docs/ updates
   - Optional deploy

---

## Example: Your Complete Workflow

### 1. You add a new feature (session tracking)

```bash
# After implementing...
/craft:docs:feature "session tracking"

# Updates:
# - CLI help for new commands
# - docs/reference/commands.md
# - docs/REFCARD.md
# - docs/reference/REFCARD-SESSIONS.md (new)
# - docs/guide/sessions.md (new)
# - README.md feature list
# - CLAUDE.md "Just Completed"
# - mkdocs.yml navigation
```

### 2. You fix a bug

```bash
# After fixing...
/craft:docs:update

# Detects: No CLI changes, just code fix
# Updates: Only affected docs (maybe none)
```

### 3. End of session

```bash
/craft:docs:done "fixed session conflicts, added prune command"

# Updates:
# - CLAUDE.md
# - .STATUS
# - Syncs any recent doc-worthy changes
```

### 4. Before release

```bash
/craft:docs:changelog    # Update CHANGELOG
/craft:docs:update full  # Ensure everything is current
/craft:docs:validate     # Check for issues
```

### 5. Deploy website

```bash
/craft:docs:site --deploy

# Updates all website docs
# Validates
# Deploys to GitHub Pages
```

---

## Summary

| Need | Command | Updates |
|------|---------|---------|
| "Update everything smart" | `docs:update` | Auto-detects |
| "Update EVERYTHING" | `docs:update full` | All doc types |
| "I added a feature" | `docs:feature` | CLI, ref, refcard, readme, claude |
| "Session done" | `docs:done` | Claude, status, sync |
| "Deploy website" | `docs:site` | Website docs, nav |
| "Recent changes" | `docs:recent` | Based on commits |

**Key Principle:** Workflow commands CALL individual commands. You can still use individual commands when needed.

---

**Ready for Implementation**
