# Craft Plugin Review & Enhancement Proposal

**Generated:** 2025-12-27
**Context:** craft v1.5.0 (current) → v1.6.0 planning
**Reviewer:** Claude Code session

---

## Executive Summary

Craft is a **mature, well-organized plugin** with impressive breadth (53 commands, 13 skills, 7 agents). After thorough review, I've identified **3 critical fixes**, **5 medium-effort improvements**, and **7 future enhancements**.

**Overall Assessment:** A+ quality, with minor consistency issues to address.

---

## Critical Issues (Fix Now)

### 1. Version Metadata Out of Sync

| File | Version | Should Be |
|------|---------|-----------|
| `.claude-plugin/plugin.json` | 1.3.0 | **1.5.0** |
| `README.md` header | "51 commands, 11 skills" | **53 commands, 13 skills** |
| `ROADMAP.md` | 1.6.0-dev | (correct for dev) |

**Impact:** Users may see wrong version info in Claude Code plugin manager.

**Fix:**
```json
{
  "name": "craft",
  "version": "1.5.0",
  "description": "Full-stack developer toolkit - 53 commands, 7 agents, 13 skills for code, git, site, docs, testing, architecture, and distribution"
}
```

---

### 2. README Header Stats Mismatch

**Current (line 3):**
```
Craft provides 51 commands, 7 specialized agents, 11 skills...
```

**Should be:**
```
Craft provides 53 commands, 7 specialized agents, 13 skills...
```

---

### 3. Orphan Orchestrator v1

**Issue:** Two orchestrator agents exist:
- `orchestrator.md` - Original v1
- `orchestrator-v2.md` - Enhanced v2.1

**Options:**

| Option | Approach | Recommendation |
|--------|----------|----------------|
| A | Keep both, mark v1 as legacy | ❌ Confusing |
| B | Deprecate v1, add redirect | ✅ **Recommended** |
| C | Remove v1 entirely | ⚠️ Breaking change |

**Recommended Fix (Option B):**
```markdown
# orchestrator.md
---
deprecated: true
redirect: orchestrator-v2
---
**DEPRECATED:** Use `orchestrator-v2` instead. This agent is preserved for backwards compatibility but will be removed in v2.0.0.
```

---

## Quick Wins (< 30 min each)

### 1. Add Version Sync Script

Create `scripts/sync-version.sh`:
```bash
#!/bin/bash
VERSION="$1"
# Update plugin.json
jq ".version = \"$VERSION\"" .claude-plugin/plugin.json > tmp && mv tmp .claude-plugin/plugin.json
# Update README header (sed)
# Update ROADMAP dev version
echo "✅ Version synced to $VERSION"
```

**Benefit:** Prevents future version drift.

---

### 2. Add Command Count Validation

Create `scripts/validate-counts.sh`:
```bash
#!/bin/bash
CMDS=$(find commands -name "*.md" | wc -l)
SKILLS=$(find skills -name "*.md" -o -name "SKILL.md" | wc -l)
AGENTS=$(find agents -name "*.md" | wc -l)
echo "Commands: $CMDS | Skills: $SKILLS | Agents: $AGENTS"
```

**Benefit:** Quick sanity check before releases.

---

### 3. Add Missing Mode Support Indicators

Several commands could benefit from mode support but aren't marked:
- `/craft:code:refactor` → Could use `debug` mode for verbose analysis
- `/craft:code:deps-audit` → Could use `release` mode for deep scan
- `/craft:arch:plan` → Could use `optimize` for parallel design exploration

**Benefit:** Consistency in mode adoption across commands.

---

## Medium Effort (1-2 hours each)

### 1. Consolidate Similar Skills

**Current overlaps:**
| Skill A | Skill B | Recommendation |
|---------|---------|----------------|
| `test-strategist` | `cli-test-strategist` | Merge into `test-strategist` with CLI mode |
| `backend-designer` | `system-architect` | Keep separate (different scope) |

**Proposed merge:**
```markdown
# test-strategist.md
## Modes
- **unit** - Unit test strategies
- **integration** - Integration test strategies
- **cli** - CLI/interactive test strategies (absorbed from cli-test-strategist)
```

---

### 2. Add Skill Auto-Discovery Index

Create `skills/index.md`:
```markdown
# Craft Skills Index

| Skill | Category | Auto-Triggers |
|-------|----------|---------------|
| backend-designer | Design | "API", "database", "auth" |
| frontend-designer | Design | "UI", "component", "CSS" |
...
```

**Benefit:** Single source of truth for skill discovery.

---

### 3. Command Category Rebalancing

**Current distribution:**
| Category | Count | % | Assessment |
|----------|-------|---|------------|
| Code | 12 | 23% | Heavy (could split) |
| Docs | 7 | 13% | Good |
| Site | 6 | 11% | Good |
| Test | 6 | 11% | Good |
| Git | 4 | 8% | Light (expand?) |
| Arch | 4 | 8% | Good |
| Plan | 3 | 6% | Light (expand?) |
| Dist | 2 | 4% | New, growing |
| Smart | 5 | 9% | Good |
| Discovery | 1 | 2% | Minimal |

**Suggestions:**
- Split `code/` into `code/` (runtime) and `quality/` (lint, coverage, audit)
- Expand `git/` with `git:stash`, `git:rebase-guide`, `git:conflict-resolve`
- Expand `plan/` with `plan:retro`, `plan:standup`

---

### 4. Add Command Aliases

**Problem:** Long command names like `/craft:docs:changelog`

**Solution:** Add aliases in command frontmatter:
```yaml
---
description: Auto-update CHANGELOG
aliases:
  - changelog
  - log
---
```

**Usage:** `/craft:changelog` → routes to `/craft:docs:changelog`

---

### 5. Create Workflow Recipes (Link to aiterm v0.4.0)

**Current:** Workflows documented in README as text
**Proposed:** Machine-readable workflow definitions

```yaml
# workflows/daily.yaml
name: daily
description: Daily development workflow
steps:
  - /craft:check
  - /craft:test:run
  - /craft:git:sync
```

**Benefit:** Enables aiterm v0.4.0 `ait recipes` integration.

---

## Long-Term Enhancements (Future Sessions)

### 1. v1.6.0: Release Automation (from ROADMAP)
- `/craft:dist:pypi` - PyPI publishing
- `/craft:dist:npm` - npm publishing
- `/craft:dist:cargo` - Cargo publishing
- `/craft:dist:release` - Multi-channel orchestrator

### 2. v1.7.0: CI/CD Integration (from ROADMAP)
- `/craft:ci:matrix` - Test matrix generation
- `/craft:ci:workflow` - GitHub Actions creation
- `/craft:ci:badge` - Badge management

### 3. Agent Pool Management
- Max parallel agent limits
- Priority queues for tasks
- Cost tracking per agent
- Result caching (reuse recent analysis)

### 4. Cross-Session Continuity
- Agent memory across sessions
- Project-specific learned preferences
- Smart defaults based on history

### 5. Monorepo Support
- Per-package commands
- Dependency graph awareness
- Coordinated releases

### 6. MCP Server Version
Convert craft to MCP server for:
- External tool integration
- IDE plugins (VS Code, Cursor)
- Programmatic access from aiterm

### 7. Community Marketplace
- User-submitted commands/skills
- Rating system
- Version management

---

## Recommended Next Step

**Priority:** Fix Critical Issues First

```
1. [ ] Update plugin.json version to 1.5.0
2. [ ] Update README header stats
3. [ ] Deprecate orchestrator v1
4. [ ] Create version sync script
5. [ ] Run validate-counts.sh
```

**Time estimate:** 30-45 minutes for all critical + quick wins

---

## Summary Table

| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| **Critical** | Version sync | 5 min | High |
| **Critical** | README stats | 2 min | Medium |
| **Critical** | Deprecate orchestrator v1 | 10 min | Medium |
| Quick | Version sync script | 15 min | High |
| Quick | Count validation script | 10 min | Medium |
| Quick | Mode support expansion | 20 min | Low |
| Medium | Consolidate skills | 1 hr | Medium |
| Medium | Skill index | 30 min | Medium |
| Medium | Command aliases | 1 hr | High |
| Medium | Workflow recipes | 2 hr | High |
| Future | v1.6.0 dist commands | 4-6 hr | High |
| Future | MCP server version | 8-12 hr | Very High |

---

## Files Changed by This Proposal

If all recommendations implemented:

```
Modified:
- .claude-plugin/plugin.json (version bump)
- README.md (stats fix)
- agents/orchestrator.md (deprecation notice)
- skills/testing/test-strategist.md (CLI mode added)

Created:
- scripts/sync-version.sh
- scripts/validate-counts.sh
- skills/index.md
- workflows/ directory

Removed:
- (none - backwards compatible)
```

---

**Ready for Implementation**
