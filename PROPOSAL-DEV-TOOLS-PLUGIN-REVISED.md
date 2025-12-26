# Dev-Tools Plugin - Revised Proposal

**Generated:** 2025-12-26
**Context:** Claude Plugins consolidation - comprehensive dev-tools plugin

## Overview

Consolidate ALL remaining user commands into a unified `dev-tools` plugin while adding documentation and CI automation capabilities. This proposal combines the lean approach (Plan A) with comprehensive coverage (Plan B).

---

## Current State: User Commands Inventory

### Commands to Migrate (32 total)

| Category | Commands | Count |
|----------|----------|-------|
| **code/** | debug, demo, docs-check, refactor, release, test-gen | 6 |
| **site/** | init, build, preview, deploy, check + docs/frameworks | 6 |
| **git/** | branch, sync, clean, git-recap + 4 docs | 8 |
| **help/** | getting-started, refcard + refcards/ | 3 |
| **root** | github.md, help.md, hub.md, site.md, workflow.md | 5 |
| **research/** | cite, manuscript, revision, sim-design (kept - more comprehensive) | 4 |

### Already Migrated (39 commands in 3 plugins)

- **workflow** (v2.1.0): 10 commands - ADHD workflow
- **rforge** (v1.1.0): 15 commands - R package ecosystem
- **statistical-research** (v1.1.0): 14 commands - Research workflows

---

## Plan A: Lean & Fast (12 commands, 2-3 hours)

**Philosophy:** Migrate essentials only, add key automation, ship fast.

### Structure
```
dev-tools/
├── .claude-plugin/plugin.json
├── commands/
│   ├── code/
│   │   ├── debug.md          # From user commands
│   │   ├── docs-check.md     # From user commands
│   │   ├── refactor.md       # From user commands
│   │   ├── release.md        # From user commands
│   │   ├── test-gen.md       # From user commands
│   │   └── demo.md           # From user commands
│   └── docs/
│       ├── sync.md           # NEW: Sync docs with code
│       ├── changelog.md      # NEW: Auto-update changelog
│       ├── validate.md       # NEW: Validate docs
│       └── check.md          # NEW: Pre-flight check
├── skills/
│   └── code-quality.md       # Code review patterns
└── README.md
```

### Command List (12)
1. `/dev:debug` - Debug assistance
2. `/dev:docs-check` - Documentation pre-flight
3. `/dev:refactor` - Refactoring guidance
4. `/dev:release` - Release workflow
5. `/dev:test-gen` - Generate tests
6. `/dev:demo` - Code demonstration
7. `/dev:docs:sync` - Sync docs with code changes
8. `/dev:docs:changelog` - Auto-update CHANGELOG
9. `/dev:docs:validate` - Validate documentation
10. `/dev:docs:check` - Pre-deployment check
11. `/dev:ci:local` - Run CI checks locally
12. `/dev:ci:fix` - Fix CI failures

### Effort: 2-3 hours
### Pros: Fast to ship, focused, easy to maintain
### Cons: Leaves site/, git/, help/ as separate user commands

---

## Plan B: Comprehensive (32+ commands, 1-2 days)

**Philosophy:** Consolidate ALL user commands into organized namespaces.

### Structure
```
dev-tools/
├── .claude-plugin/plugin.json
├── commands/
│   ├── code/                 # Development (6 migrated + 6 new)
│   │   ├── debug.md
│   │   ├── demo.md
│   │   ├── docs-check.md
│   │   ├── refactor.md
│   │   ├── release.md
│   │   ├── test-gen.md
│   │   ├── lint.md           # NEW
│   │   ├── coverage.md       # NEW
│   │   ├── deps-check.md     # NEW
│   │   ├── deps-audit.md     # NEW
│   │   ├── ci-local.md       # NEW
│   │   └── ci-fix.md         # NEW
│   │
│   ├── site/                 # Documentation sites (6 migrated)
│   │   ├── init.md
│   │   ├── build.md
│   │   ├── preview.md
│   │   ├── deploy.md
│   │   ├── check.md
│   │   └── docs/
│   │       └── frameworks.md
│   │
│   ├── git/                  # Git operations (8 migrated)
│   │   ├── branch.md
│   │   ├── sync.md
│   │   ├── clean.md
│   │   ├── recap.md
│   │   └── docs/
│   │       ├── safety-rails.md
│   │       ├── undo-guide.md
│   │       ├── learning-guide.md
│   │       └── refcard.md
│   │
│   ├── docs/                 # Documentation automation (NEW)
│   │   ├── sync.md           # Sync docs with code
│   │   ├── changelog.md      # Auto-update changelog
│   │   ├── claude-md.md      # Update CLAUDE.md
│   │   ├── validate.md       # Validate all docs
│   │   └── nav-update.md     # Update mkdocs nav
│   │
│   └── hub.md                # Command discovery (migrated)
│
├── skills/
│   ├── code-quality.md
│   ├── git-safety.md
│   └── docs-automation.md
│
├── agents/
│   └── orchestrator.md       # Smart delegation
│
├── docs/
│   ├── getting-started.md    # From help/
│   └── refcard.md            # From help/
│
└── README.md
```

### Command List (38 total)

**Code (12)**
| Command | Source | Description |
|---------|--------|-------------|
| `/dev:debug` | Migrated | Debug assistance |
| `/dev:demo` | Migrated | Code demonstration |
| `/dev:docs-check` | Migrated | Pre-flight check |
| `/dev:refactor` | Migrated | Refactoring guidance |
| `/dev:release` | Migrated | Release workflow |
| `/dev:test-gen` | Migrated | Generate tests |
| `/dev:lint` | NEW | Code style check |
| `/dev:coverage` | NEW | Test coverage report |
| `/dev:deps-check` | NEW | Check dependencies |
| `/dev:deps-audit` | NEW | Security audit |
| `/dev:ci-local` | NEW | Run CI locally |
| `/dev:ci-fix` | NEW | Fix CI failures |

**Site (6)**
| Command | Source | Description |
|---------|--------|-------------|
| `/dev:site:init` | Migrated | Initialize docs site |
| `/dev:site:build` | Migrated | Build site |
| `/dev:site:preview` | Migrated | Preview locally |
| `/dev:site:deploy` | Migrated | Deploy to Pages |
| `/dev:site:check` | Migrated | Validate site |
| `/dev:site:frameworks` | Migrated | Framework comparison |

**Git (8)**
| Command | Source | Description |
|---------|--------|-------------|
| `/dev:git:branch` | Migrated | Branch management |
| `/dev:git:sync` | Migrated | Smart git sync |
| `/dev:git:clean` | Migrated | Clean merged branches |
| `/dev:git:recap` | Migrated | Activity summary |
| `/dev:git:safety` | Migrated | Safety rails guide |
| `/dev:git:undo` | Migrated | Undo guide |
| `/dev:git:learn` | Migrated | Learning guide |
| `/dev:git:refcard` | Migrated | Quick reference |

**Docs Automation (5)**
| Command | Source | Description |
|---------|--------|-------------|
| `/dev:docs:sync` | NEW | Sync docs with code |
| `/dev:docs:changelog` | NEW | Auto-update CHANGELOG |
| `/dev:docs:claude-md` | NEW | Update CLAUDE.md |
| `/dev:docs:validate` | NEW | Validate all docs |
| `/dev:docs:nav` | NEW | Update mkdocs nav |

**Hub (1)**
| Command | Source | Description |
|---------|--------|-------------|
| `/dev:hub` | Migrated | Command discovery |

**Help (integrated into docs/)**

### Effort: 1-2 days
### Pros: Complete consolidation, clean namespaces, comprehensive
### Cons: More work upfront, larger plugin

---

## Plan C: Hybrid (Recommended)

**Philosophy:** Plan A speed + Plan B organization. Ship in phases.

### Phase 1: Core (Day 1, 2-3 hours)
Ship essential code/ commands + docs automation:

```
dev-tools/
├── commands/
│   ├── code/           # 6 migrated
│   ├── docs/           # 5 new automation
│   └── hub.md          # Discovery
└── skills/
    └── code-quality.md
```

**Commands:** 12 total
**Result:** Immediately useful, docs automation working

### Phase 2: Git & Site (Day 2, 2-3 hours)
Add git/ and site/ namespaces:

```
dev-tools/
├── commands/
│   ├── code/           # 6
│   ├── docs/           # 5
│   ├── git/            # 8 migrated
│   ├── site/           # 6 migrated
│   └── hub.md
└── skills/
    ├── code-quality.md
    └── git-safety.md
```

**Commands:** 26 total
**Result:** All user commands migrated

### Phase 3: Enhancement (Day 3+, optional)
Add new capabilities:

- CI automation commands (ci-local, ci-fix)
- Advanced code commands (lint, coverage, deps-*)
- Orchestrator agent for smart delegation
- Integration with marketplace plugins

**Commands:** 32-38 total
**Result:** Full-featured dev-tools suite

---

## Comparison Matrix

| Aspect | Plan A | Plan B | Plan C |
|--------|--------|--------|--------|
| **Commands** | 12 | 38 | 12→26→38 |
| **Time** | 2-3 hrs | 1-2 days | Phased |
| **User commands left** | 26 | 0 | 0 (after P2) |
| **Docs automation** | ✅ | ✅ | ✅ |
| **CI automation** | Basic | Full | Full (P3) |
| **Git commands** | ❌ | ✅ | ✅ (P2) |
| **Site commands** | ❌ | ✅ | ✅ (P2) |
| **Ship fast** | ✅✅✅ | ❌ | ✅✅ |
| **Complete** | ❌ | ✅✅✅ | ✅✅✅ |

---

## Recommendation: Plan C (Hybrid)

**Why Plan C?**

1. **Ship fast** - Phase 1 in 2-3 hours gives immediate value
2. **Complete eventually** - Phases 2-3 consolidate everything
3. **Incremental** - Test each phase before adding more
4. **Flexible** - Stop after any phase if satisfied
5. **Low risk** - Small commits, easy rollback

**Immediate Action (Phase 1):**
```bash
# Create plugin structure
mkdir -p dev-tools/{.claude-plugin,commands/{code,docs},skills}

# Copy code/ commands
cp ~/.claude/commands/code/*.md dev-tools/commands/code/

# Create docs automation commands
# Create plugin.json
# Test and deploy
```

---

## Quick Wins (Start Now)

1. **Copy code/ commands** (5 min) - Instant 6 commands
2. **Create plugin.json** (5 min) - Plugin metadata
3. **Add docs:sync command** (15 min) - Most requested automation
4. **Add docs:changelog command** (15 min) - Auto CHANGELOG updates
5. **Update hub.md** (10 min) - Point to new locations

**Total: ~50 minutes to working Phase 1**

---

## Next Steps

Choose your path:

| Option | Action |
|--------|--------|
| **A** | Implement Plan A (lean, 12 commands) |
| **B** | Implement Plan B (comprehensive, 38 commands) |
| **C** | Implement Plan C Phase 1 (hybrid start) |
| **C2** | Implement Plan C Phases 1+2 (full migration) |

---

## Files to Delete After Migration

After successful migration and testing:

```bash
# After Phase 1
rm -rf ~/.claude/commands/code/

# After Phase 2
rm -rf ~/.claude/commands/site/
rm -rf ~/.claude/commands/git/
rm -rf ~/.claude/commands/help/
rm ~/.claude/commands/hub.md
rm ~/.claude/commands/github.md
rm ~/.claude/commands/site.md
rm ~/.claude/commands/workflow.md
rm ~/.claude/commands/help.md
```

---

**Last Updated:** 2025-12-26
**Status:** Ready for implementation
