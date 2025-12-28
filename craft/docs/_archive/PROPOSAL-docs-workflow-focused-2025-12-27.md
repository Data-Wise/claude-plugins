# Craft Docs Commands - Workflow-Focused Revision

**Generated:** 2025-12-27
**Focus:** ADHD-friendly workflows for real development scenarios
**Philosophy:** Fewer commands, clearer purpose, obvious when to use each

---

## The Problem

Current docs commands are **feature-complete but workflow-unclear**. When I:
- Finish a feature → Which command?
- Fix a bug → Which command?
- Update planning → Which command?
- Deploy docs → Which command?

**Goal:** Make it obvious which command to use in each scenario.

---

## Revised Command Structure

### The "When Do I Use What?" Cheat Sheet

```
┌─────────────────────────────────────────────────────────────┐
│ 📝 DOCS COMMAND QUICK REFERENCE                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ "I just finished coding..."                                 │
│   → /craft:docs:sync         (detect & update changed docs) │
│                                                             │
│ "I'm releasing a version..."                                │
│   → /craft:docs:changelog    (update CHANGELOG.md)          │
│                                                             │
│ "I need to update project status..."                        │
│   → /craft:docs:claude-md    (update CLAUDE.md/.STATUS)     │
│                                                             │
│ "I added new doc files..."                                  │
│   → /craft:docs:nav-update   (update mkdocs.yml nav)        │
│                                                             │
│ "I want to check docs are valid..."                         │
│   → /craft:docs:validate     (check links, code examples)   │
│                                                             │
│ "I need full documentation from scratch..."                 │
│   → /craft:docs:generate     (create new docs with agents)  │
│                                                             │
│ "I'm building an API..."                                    │
│   → /craft:docs:api          (OpenAPI spec generation)      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Command-by-Command Explanation

### 1. `/craft:docs:sync` - "Update docs after code changes"

**When to use:** After ANY code change (feature, fix, refactor)

**What it does:**
1. Looks at recent git commits
2. Maps code changes → affected docs
3. Shows what needs updating
4. Updates with your confirmation

**Real example:**
```
You just added: src/aiterm/cli/hello.py

/craft:docs:sync detects:
  ⚠️ docs/reference/commands.md - New CLI command not documented
  ⚠️ CLAUDE.md - New feature not in Quick Reference

Updates both automatically.
```

**ADHD-friendly:** Run after every coding session. It figures out what changed.

---

### 2. `/craft:docs:changelog` - "Update CHANGELOG for release"

**When to use:** Before releasing a new version

**What it does:**
1. Reads git commits since last tag
2. Categorizes: Added/Fixed/Changed/Breaking
3. Generates formatted changelog entry
4. Suggests version number

**Real example:**
```
You ran: git tag (last was v0.3.5)

/craft:docs:changelog generates:

## [0.3.6] - 2025-12-27
### Added
- curl installer with auto-detection
- hello/goodbye diagnostic commands

### Fixed
- Version consistency across docs
```

**ADHD-friendly:** Only run at release time. Handles the tedious categorization.

---

### 3. `/craft:docs:claude-md` - "Update project status"

**When to use:** End of session, status changed, planning updates

**What it does:**
1. Reads current CLAUDE.md
2. Detects version mismatches
3. Updates "Just Completed" section
4. Updates "Project Status" section
5. Syncs with .STATUS file

**Real example:**
```
You finished implementing IDE integrations.

/craft:docs:claude-md updates:

## Project Status: v0.3.0 ✅ RELEASED

### Just Completed
- ✅ IDE integrations (VS Code, Cursor, Zed, Positron, Windsurf)
- ✅ Session coordination (hook-based tracking)
```

**ADHD-friendly:** Brain dump your session accomplishments into a clean format.

---

### 4. `/craft:docs:nav-update` - "Add new docs to navigation"

**When to use:** After creating new documentation files

**What it does:**
1. Scans docs/ for all .md files
2. Compares with mkdocs.yml nav
3. Finds orphan files (not in nav)
4. Suggests where to add them
5. Updates mkdocs.yml

**Real example:**
```
You created: docs/guide/sessions.md

/craft:docs:nav-update detects:
  + docs/guide/sessions.md → "Session Management"

Adds to nav under "Guide" section.
```

**ADHD-friendly:** Never forget to add new docs to the nav.

---

### 5. `/craft:docs:validate` - "Check docs are correct"

**When to use:** Before deploying, in CI, when unsure

**What it does:**
1. Checks all internal links work
2. Validates code examples compile
3. Finds missing referenced files
4. Checks external URLs (optional)

**Real example:**
```
/craft:docs:validate finds:

❌ docs/guide/setup.md:45 → docs/config.md (file not found)
❌ docs/reference/api.md:42 → old_function() doesn't exist
✅ 45 other links valid
```

**ADHD-friendly:** Run before deploy. Catches embarrassing broken links.

---

### 6. `/craft:docs:generate` - "Create docs from scratch"

**When to use:** New project, new major feature, comprehensive overhaul

**What it does:**
1. Analyzes entire codebase
2. Routes to specialized agents:
   - `docs-architect` → Architecture docs
   - `tutorial-engineer` → Tutorials
   - `reference-builder` → API reference
   - `mermaid-expert` → Diagrams
3. Creates multiple doc files
4. Updates nav and badges

**Real example:**
```
/craft:docs:generate architecture

Creates:
  📄 docs/architecture/overview.md (500 lines)
  📄 docs/architecture/components.md (300 lines)
  🎨 docs/diagrams/system-flow.md (Mermaid)
```

**ADHD-friendly:** Heavy lift. Use sparingly. For new projects or major milestones.

---

### 7. `/craft:docs:api` - "Generate API documentation"

**When to use:** Building REST/GraphQL APIs

**What it does:**
1. Detects API framework (FastAPI, Flask, Express)
2. Generates OpenAPI 3.1 spec
3. Sets up Swagger UI (optional)
4. Can generate client SDKs

**Real example:**
```
/craft:docs:api generate

Creates:
  📄 openapi.yaml (450 lines)

Run: npx @stoplight/prism-cli mock openapi.yaml
```

**ADHD-friendly:** Specialized. Only for API projects.

---

## ⭐ Workflow Scenarios

### Scenario 1: "I just finished a feature"

```bash
# 1. Update docs that reference changed code
/craft:docs:sync

# 2. Update project status
/craft:docs:claude-md

# 3. If you created new doc files
/craft:docs:nav-update

# 4. Verify everything works
/craft:docs:validate
```

**One-liner (future):**
```bash
/craft:docs:sync --full   # Does all 4 steps
```

---

### Scenario 2: "I fixed a bug"

```bash
# Usually just sync is enough
/craft:docs:sync

# Bug fixes rarely need doc updates, but sync will tell you
```

---

### Scenario 3: "I'm releasing a version"

```bash
# 1. Update changelog with all commits
/craft:docs:changelog

# 2. Update project status to "RELEASED"
/craft:docs:claude-md

# 3. Validate before deploy
/craft:docs:validate

# 4. Deploy
/craft:site:deploy
```

---

### Scenario 4: "I need to update planning docs"

```bash
# Update CLAUDE.md with new status/plans
/craft:docs:claude-md

# Or manually edit, then validate
/craft:docs:validate
```

---

### Scenario 5: "I need to update website docs"

```bash
# If code changed → docs need updating
/craft:docs:sync

# If just reorganizing nav
/craft:docs:nav-update

# Preview
/craft:site:preview

# Deploy
/craft:site:deploy
```

---

## Proposed Refactoring

### Remove/Merge Candidates

| Current | Proposal | Reason |
|---------|----------|--------|
| 7 commands | **5 core + 2 specialized** | Reduce cognitive load |

### Core Commands (Daily Use)

1. **`/craft:docs:sync`** - The workhorse (after any code change)
2. **`/craft:docs:changelog`** - Release time only
3. **`/craft:docs:claude-md`** - Session end / status updates
4. **`/craft:docs:nav-update`** - After adding new doc files
5. **`/craft:docs:validate`** - Before deploy / in CI

### Specialized Commands (Occasional Use)

6. **`/craft:docs:generate`** - New projects, major features
7. **`/craft:docs:api`** - API projects only

---

## ⭐ New: Workflow Presets

Instead of remembering which commands to run, add **workflow presets**:

```bash
# After finishing a feature
/craft:docs:workflow feature
# Runs: sync → claude-md → nav-update → validate

# Before releasing
/craft:docs:workflow release
# Runs: changelog → claude-md → validate

# Quick check
/craft:docs:workflow check
# Runs: validate only

# Full documentation refresh
/craft:docs:workflow full
# Runs: generate → sync → nav-update → validate
```

### Implementation

Add to `/craft:docs:sync` or create `/craft:docs:workflow`:

```yaml
# workflows/docs-feature.yaml
name: feature
description: After finishing a feature
steps:
  - command: /craft:docs:sync
  - command: /craft:docs:claude-md
  - command: /craft:docs:nav-update
    condition: new_docs_exist
  - command: /craft:docs:validate
```

---

## ADHD-Friendly Enhancements

### 1. Command Hints in Output

Every command ends with "What's next?":

```
✅ SYNC COMPLETE

Updated: 2 files

What's next?
  → Update status: /craft:docs:claude-md
  → Validate: /craft:docs:validate
  → Deploy: /craft:site:deploy
```

### 2. Smart Suggestions

When you run the wrong command:

```
You ran: /craft:docs:generate

Hmm, you have recent code changes. Did you mean:
  → /craft:docs:sync (update existing docs from changes)

/craft:docs:generate is for creating NEW documentation.
Continue anyway? (y/n)
```

### 3. Session Memory

```
📝 This session you've:
  ✅ Ran /craft:docs:sync
  ⏳ Haven't updated changelog (5 commits since last release)
  ⏳ Haven't validated

Suggested: /craft:docs:changelog
```

---

## Summary: The Mental Model

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   CODE CHANGES          →  /craft:docs:sync                 │
│                                                             │
│   RELEASING             →  /craft:docs:changelog            │
│                                                             │
│   SESSION END           →  /craft:docs:claude-md            │
│                                                             │
│   NEW DOC FILES         →  /craft:docs:nav-update           │
│                                                             │
│   BEFORE DEPLOY         →  /craft:docs:validate             │
│                                                             │
│   NEW PROJECT/FEATURE   →  /craft:docs:generate             │
│                                                             │
│   API DOCUMENTATION     →  /craft:docs:api                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**The 80/20 Rule:**
- 80% of the time you'll use: `sync`, `changelog`, `validate`
- 20% of the time: `claude-md`, `nav-update`, `generate`, `api`

---

## Action Items

### Quick Wins (< 30 min)
1. [ ] Add "What's next?" hints to all command outputs
2. [ ] Add workflow cheat sheet to craft README
3. [ ] Add `--full` flag to sync (runs sync → claude-md → nav → validate)

### Medium Effort (1-2 hours)
1. [ ] Create `/craft:docs:workflow` command with presets
2. [ ] Add smart suggestions when wrong command detected
3. [ ] Add session memory for doc commands

### Lower Priority
1. [ ] Consolidate redundant CLAUDE.md update logic
2. [ ] Add `/craft:docs:readme` specialized command

---

**Key Insight:** You don't need to remember 7 commands. You need to remember:
- **sync** = after coding
- **changelog** = before release
- **validate** = before deploy

Everything else is occasional.
