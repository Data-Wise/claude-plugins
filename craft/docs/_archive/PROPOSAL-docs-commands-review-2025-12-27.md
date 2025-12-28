# Craft Docs Commands Review & Enhancement Proposal

**Generated:** 2025-12-27
**Reviewer:** AI Code Review Specialist
**Scope:** `/craft:docs:*` commands (7 total)

---

## Executive Summary

The docs command suite is **well-designed and comprehensive**, covering the full documentation lifecycle. However, there are opportunities for **consolidation**, **missing capabilities**, and **improved integration**.

**Overall Grade: B+**
- Structure: A
- Coverage: B+
- Integration: B
- Missing Features: Several gaps identified

---

## Current Command Inventory

| Command | Purpose | Lines | Grade |
|---------|---------|-------|-------|
| `/craft:docs:generate` | Orchestrate full doc generation | 210 | A |
| `/craft:docs:sync` | Sync docs with code changes | 127 | B+ |
| `/craft:docs:validate` | Validate links/code/structure | 176 | A |
| `/craft:docs:changelog` | Auto-update CHANGELOG | 192 | A- |
| `/craft:docs:claude-md` | Update CLAUDE.md | 191 | B+ |
| `/craft:docs:api` | OpenAPI/Swagger generation | 233 | A |
| `/craft:docs:nav-update` | Update mkdocs.yml nav | 204 | B+ |

**Total:** 1,333 lines across 7 commands

---

## Detailed Review

### 1. `/craft:docs:generate` - A

**Strengths:**
- Excellent orchestration of 5 documentation agents
- Clear routing matrix (type → agent)
- Progressive phases for full generation
- Good integration with other docs commands

**Issues:**
- Line 171: Progress bar shown but no actual progress tracking mechanism
- No mode support (could benefit from `debug`/`release` modes)
- Badge generation hardcoded to shields.io (no customization)

**Recommendations:**
```yaml
# Add mode support
modes:
  default: Quick update of existing docs
  debug: Verbose output showing agent reasoning
  release: Full generation with validation
```

---

### 2. `/craft:docs:sync` - B+

**Strengths:**
- Smart change classification (feature/fix/refactor/breaking)
- Doc freshness checking with timestamps
- Missing doc detection

**Issues:**
- Code-to-docs mapping is hardcoded and limited
- No support for monorepo structures
- Freshness check doesn't account for doc-only commits

**Recommendations:**

1. **Configurable mapping:**
```yaml
# Support .craft/docs-mapping.yaml
mappings:
  - pattern: "src/api/**/*.py"
    docs: ["docs/reference/api.md", "docs/guide/api-usage.md"]
  - pattern: "pyproject.toml"
    docs: ["docs/getting-started/installation.md"]
```

2. **Add `--scope` flag:**
```bash
/craft:docs:sync --scope api      # Only sync API docs
/craft:docs:sync --scope guide    # Only sync guides
/craft:docs:sync --since v0.3.0   # Since specific tag
```

---

### 3. `/craft:docs:validate` - A

**Strengths:**
- Comprehensive validation (links, code, structure)
- Auto-fix capability
- Good categorization of issues

**Issues:**
- External link checking can be slow (no parallel/async)
- No caching for external URL checks
- Missing spell check integration

**Recommendations:**

1. **Add caching:**
```python
# Cache external URL results for 24 hours
external_link_cache = TTLCache(maxsize=1000, ttl=86400)
```

2. **Parallel external checks:**
```bash
/craft:docs:validate --parallel     # Parallel external link checks
/craft:docs:validate --skip-external # Skip slow external checks
```

3. **Spell check integration:**
```bash
/craft:docs:validate --spell        # Enable spell checking
```

---

### 4. `/craft:docs:changelog` - A-

**Strengths:**
- Conventional commit parsing
- Version suggestion logic
- Keep a Changelog format compliance
- PR/issue linking

**Issues:**
- No support for squash merge commit parsing
- Breaking change detection only via `BREAKING:` prefix
- No support for multiple changelogs (e.g., per-package in monorepo)

**Recommendations:**

1. **Enhanced breaking change detection:**
```python
# Detect breaking changes from:
breaking_indicators = [
    "BREAKING:",
    "BREAKING CHANGE:",
    "!:",  # feat!: or fix!:
    "removes", "deletes", "changes API",
    "incompatible"
]
```

2. **Monorepo support:**
```bash
/craft:docs:changelog --package aiterm  # Update specific package changelog
/craft:docs:changelog --all-packages    # Update all package changelogs
```

---

### 5. `/craft:docs:claude-md` - B+

**Strengths:**
- Good section structure template
- Version sync from package files
- Command discovery from CLI

**Issues:**
- Doesn't handle nested CLAUDE.md files (e.g., `.claude/rules/`)
- No detection of stale "Just Completed" sections
- Missing integration with `.STATUS` file format

**Recommendations:**

1. **Handle multiple CLAUDE.md files:**
```bash
/craft:docs:claude-md              # Root CLAUDE.md
/craft:docs:claude-md --rules      # Update .claude/rules/*.md
/craft:docs:claude-md --all        # Update all CLAUDE.md files
```

2. **Add staleness detection:**
```
⚠️ STALE CONTENT DETECTED

"Just Completed" section references v0.2.0 but current version is v0.3.0.
This content may be outdated.

Archive old content? (y/n)
```

---

### 6. `/craft:docs:api` - A

**Strengths:**
- Multi-framework detection
- OpenAPI 3.1 support (latest)
- SDK generation options
- Spectral validation integration

**Issues:**
- R/plumber support mentioned but not detailed
- No GraphQL schema documentation
- No gRPC proto documentation

**Recommendations:**

1. **Add GraphQL support:**
```bash
/craft:docs:api graphql            # Generate GraphQL schema docs
/craft:docs:api --format graphql   # Output as GraphQL SDL
```

2. **Add gRPC support:**
```bash
/craft:docs:api grpc               # Generate from .proto files
```

---

### 7. `/craft:docs:nav-update` - B+

**Strengths:**
- Smart title inference
- Section detection from paths
- Orphan file handling
- Structure validation

**Issues:**
- Only supports MkDocs (no Docusaurus, VitePress, etc.)
- No support for custom ordering (always alphabetical)
- No detection of duplicate nav entries

**Recommendations:**

1. **Multi-framework support:**
```bash
/craft:docs:nav-update             # Auto-detect (mkdocs/docusaurus)
/craft:docs:nav-update --framework docusaurus
/craft:docs:nav-update --framework vitepress
```

2. **Custom ordering:**
```yaml
# Support .craft/nav-order.yaml
order:
  - index.md           # Always first
  - getting-started/*  # Then getting started
  - guide/*            # Then guides
  - reference/*        # Then reference
  - "*"                # Everything else alphabetically
```

---

## Missing Commands (Proposed Additions)

### 1. `/craft:docs:readme` - NEW

**Purpose:** Generate/update README.md with best practices

```bash
/craft:docs:readme                  # Update existing README
/craft:docs:readme --init           # Generate from template
/craft:docs:readme --badges         # Update badges only
/craft:docs:readme --toc            # Regenerate table of contents
```

**Why needed:**
- README is often the first thing users see
- Currently scattered across `generate` and `claude-md`
- Dedicated command provides focused functionality

**Effort:** Medium (2-3 hours)

---

### 2. `/craft:docs:coverage` - NEW

**Purpose:** Documentation coverage analysis

```bash
/craft:docs:coverage                # Show coverage report
/craft:docs:coverage --report       # Generate detailed report
/craft:docs:coverage --threshold 80 # Fail if below 80%
```

**Output:**
```
📊 DOCUMENTATION COVERAGE

Module Coverage:
  src/aiterm/cli/       ████████░░ 80% (8/10 functions documented)
  src/aiterm/terminal/  ██████████ 100% (5/5 functions documented)
  src/aiterm/opencode/  ████░░░░░░ 40% (4/10 functions documented) ⚠️

Overall: 73% (17/23 public functions)

Undocumented:
  - src/aiterm/cli/ide.py:configure() - Missing docstring
  - src/aiterm/opencode/config.py:validate_schema() - Missing docstring
```

**Why needed:**
- No current way to measure documentation completeness
- Useful for CI/CD quality gates
- Identifies documentation debt

**Effort:** Medium (3-4 hours)

---

### 3. `/craft:docs:translate` - NEW (Future)

**Purpose:** Documentation translation support

```bash
/craft:docs:translate --to es       # Translate to Spanish
/craft:docs:translate --sync        # Sync translations with source
/craft:docs:translate --status      # Show translation status
```

**Why needed:**
- Internationalization becoming important
- AI can assist with initial translation
- Human review workflow support

**Effort:** Large (8-12 hours)

---

### 4. `/craft:docs:diff` - NEW

**Purpose:** Show documentation changes between versions

```bash
/craft:docs:diff v0.2.0 v0.3.0      # Changes between versions
/craft:docs:diff HEAD~5             # Changes in last 5 commits
/craft:docs:diff --breaking         # Only breaking changes
```

**Why needed:**
- Useful for release notes preparation
- Helps identify what documentation changed
- Supports changelog generation

**Effort:** Small (1-2 hours)

---

## Refactoring Recommendations

### 1. Consolidate Overlapping Functionality

**Current overlap:**
- `generate`, `sync`, and `claude-md` all update CLAUDE.md
- `validate` and `nav-update` both check mkdocs.yml

**Proposed refactor:**
```
/craft:docs:generate  → Orchestrator (calls others)
    ├── /craft:docs:readme
    ├── /craft:docs:claude-md
    ├── /craft:docs:changelog
    ├── /craft:docs:api
    └── /craft:docs:nav-update

/craft:docs:sync      → Smart sync (calls others as needed)
    ├── detect changes
    ├── call relevant update commands
    └── validate result

/craft:docs:validate  → Validation only (no updates)
```

---

### 2. Add Shared Configuration

Create `.craft/docs.yaml`:
```yaml
# Documentation configuration
framework: mkdocs  # or docusaurus, vitepress

paths:
  docs: docs/
  api: docs/api/
  changelog: CHANGELOG.md
  readme: README.md
  claude: CLAUDE.md

badges:
  style: flat-square  # or flat, plastic, for-the-badge
  include:
    - version
    - python
    - license
    - tests

sync:
  mappings:
    - pattern: "src/api/**"
      docs: ["docs/reference/api.md"]

validate:
  external_timeout: 10
  cache_ttl: 86400
  spell_check: false
```

---

### 3. Add Mode Support Across All Commands

| Command | default | debug | release |
|---------|---------|-------|---------|
| generate | Quick update | Verbose agents | Full suite |
| sync | Recent changes | Full history | Breaking change focus |
| validate | Internal only | + External | + Spell + All |
| changelog | Auto-categorize | Show reasoning | Manual review |
| api | Update spec | Verbose validation | + SDK gen |

---

## Integration Improvements

### 1. Command Chaining

Add `--chain` flag for automatic follow-up:
```bash
/craft:docs:sync --chain validate    # Sync then validate
/craft:docs:changelog --chain readme # Update changelog then README
```

### 2. CI/CD Ready Flags

```bash
/craft:docs:validate --ci           # Exit code based on errors
/craft:docs:coverage --ci --min 80  # Fail if below threshold
/craft:docs:sync --ci --dry-run     # Show what would change
```

### 3. Git Integration

```bash
/craft:docs:sync --commit           # Auto-commit changes
/craft:docs:validate --pre-commit   # Git pre-commit hook mode
```

---

## Priority Implementation Order

### Quick Wins (< 1 hour each)
1. Add `--skip-external` to validate
2. Add mode support to generate
3. Add `--scope` to sync

### Medium Effort (2-4 hours each)
1. `/craft:docs:readme` command
2. `/craft:docs:diff` command
3. Configuration file support (`.craft/docs.yaml`)

### Larger Effort (4-8 hours each)
1. `/craft:docs:coverage` command
2. Multi-framework nav support
3. Monorepo changelog support

### Future (8+ hours)
1. `/craft:docs:translate` command
2. GraphQL/gRPC documentation
3. Full i18n workflow

---

## Summary

| Category | Finding |
|----------|---------|
| **Strengths** | Good coverage, clear structure, agent integration |
| **Gaps** | README command, coverage analysis, multi-framework |
| **Overlaps** | CLAUDE.md updates in 3 places, mkdocs validation in 2 |
| **Quick Wins** | Mode support, scope flags, skip-external |
| **High Impact** | `/craft:docs:readme`, `/craft:docs:coverage` |

**Recommended Priority:**
1. Add `/craft:docs:readme` (high user value)
2. Add `/craft:docs:coverage` (CI/CD integration)
3. Add mode support across commands (consistency)
4. Create `.craft/docs.yaml` config (maintainability)

---

**Ready for Implementation**
