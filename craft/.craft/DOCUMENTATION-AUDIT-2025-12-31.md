# Craft Documentation Audit - December 31, 2025

## Executive Summary

**Actual Inventory:**
- **74 commands** (docs claim 69 - outdated by 5)
- **21 skills** (docs claim 17 - outdated by 4)
- **8 agents** (docs claim 7 - outdated by 1)

**Status:** Documentation needs updating to reflect actual feature count and add missing workflow GIFs.

---

## Command Inventory (74 total)

### Smart Commands (4)
- [x] `/craft:do`
- [x] `/craft:orchestrate`
- [x] `/craft:check`
- [ ] `/craft:hub` - MISSING from smart.md
- [ ] `/craft:smart-help` - MISSING entirely (alias for help?)

### Documentation Commands (13)
- [x] `/craft:docs:update`
- [x] `/craft:docs:sync`
- [x] `/craft:docs:check`
- [x] `/craft:docs:api`
- [x] `/craft:docs:changelog`
- [x] `/craft:docs:guide`
- [x] `/craft:docs:demo`
- [x] `/craft:docs:mermaid`
- [x] `/craft:docs:tutorial`
- [x] `/craft:docs:website`
- [ ] `/craft:docs:claude-md` - MISSING
- [ ] `/craft:docs:nav-update` - MISSING
- [ ] `/craft:docs:prompt` - MISSING
- [ ] `/craft:docs:site` - MISSING (duplicate of site commands?)

### Site Commands (15 actual, docs say 12)
- [x] `/craft:site:create`
- [x] `/craft:site:init`
- [x] `/craft:site:build`
- [x] `/craft:site:preview`
- [x] `/craft:site:deploy`
- [x] `/craft:site:status`
- [x] `/craft:site:theme`
- [x] `/craft:site:update`
- [x] `/craft:site:nav`
- [x] `/craft:site:audit`
- [x] `/craft:site:consolidate`
- [ ] `/craft:site:add` - MISSING
- [ ] `/craft:site:check` - MISSING
- [ ] `/craft:site:docs/frameworks` - MISSING (internal doc?)

### Code & Testing Commands (17 actual, docs say 12)
- [x] `/craft:code:lint`
- [x] `/craft:code:debug`
- [x] `/craft:code:refactor`
- [x] `/craft:code:test-gen`
- [x] `/craft:code:coverage`
- [x] `/craft:test:run`
- [x] `/craft:test:debug`
- [x] `/craft:test:coverage`
- [x] `/craft:test:generate`
- [ ] `/craft:code:ci-fix` - MISSING
- [ ] `/craft:code:ci-local` - MISSING
- [ ] `/craft:code:demo` - MISSING
- [ ] `/craft:code:deps-audit` - MISSING
- [ ] `/craft:code:deps-check` - MISSING
- [ ] `/craft:code:docs-check` - MISSING
- [ ] `/craft:code:release` - MISSING
- [ ] `/craft:test:cli-gen` - MISSING
- [ ] `/craft:test:cli-run` - MISSING
- [ ] `/craft:test:watch` - MISSING

### Git Commands (13 actual, docs say 12)
- [x] `/craft:git:worktree`
- [x] `/craft:git:sync`
- [x] `/craft:git:clean`
- [x] `/craft:git:recap` - Listed as `/craft:git:git-recap` in files
- [x] `/craft:git:branch`
- [ ] `/craft:git:docs/learning-guide` - MISSING (internal doc?)
- [ ] `/craft:git:docs/refcard` - MISSING (internal doc?)
- [ ] `/craft:git:docs/safety-rails` - MISSING (internal doc?)
- [ ] `/craft:git:docs/undo-guide` - MISSING (internal doc?)

### CI Commands (3)
- [x] `/craft:ci:detect`
- [x] `/craft:ci:generate`
- [x] `/craft:ci:validate`

### Architecture Commands (7)
- [ ] `/craft:arch:analyze` - NOT DOCUMENTED
- [ ] `/craft:arch:diagram` - NOT DOCUMENTED
- [ ] `/craft:arch:plan` - NOT DOCUMENTED
- [ ] `/craft:arch:review` - NOT DOCUMENTED
- Plus 3 more mentioned in overview

### Distribution Commands (3 actual, docs say 2)
- [ ] `/craft:dist:homebrew` - NOT DOCUMENTED
- [ ] `/craft:dist:curl-install` - NOT DOCUMENTED
- [ ] `/craft:dist:pypi` - MISSING

### Planning Commands (3)
- [ ] `/craft:plan:feature` - NOT DOCUMENTED
- [ ] `/craft:plan:sprint` - NOT DOCUMENTED
- [ ] `/craft:plan:roadmap` - NOT DOCUMENTED

---

## Skills Inventory (21 total, docs say 17)

### Documented (17)
1. backend-designer
2. frontend-designer
3. devops-helper
4. test-generator
5. test-strategist
6. system-architect
7. project-planner
8. task-analyzer
9. distribution-strategist
10. homebrew-formula-expert
11. homebrew-setup-wizard
12. homebrew-workflow-expert
13. doc-classifier
14. mermaid-linter
15. changelog-automation
16. openapi-spec-generation
17. mode-controller

### MISSING from docs (4)
18. **homebrew-multi-formula** - Distribution skill
19. **session-state** - Orchestration skill
20. **project-detector** - CI skill
21. **architecture-decision-records** - Docs skill

---

## Agents Inventory (8 total, docs say 7)

### Documented (7)
1. docs-architect
2. api-documenter
3. tutorial-engineer
4. mermaid-expert
5. reference-builder
6. demo-engineer
7. orchestrator-v2

### MISSING from docs (1)
8. **orchestrator** - Legacy orchestrator (still in use?)

---

## Workflows Needing GIFs

### Priority 1: Core Workflows (from workflows/index.md)
1. **Documentation Workflow** - `/craft:docs:update` flow
2. **Site Creation Workflow** - `/craft:site:create` wizard
3. **Release Workflow** - `/craft:check --for release`
4. **Development Workflow** - Git worktree workflow
5. **AI Routing Workflow** - `/craft:do` in action

### Priority 2: Additional Workflows
6. **Testing Workflow** - `/craft:test:run debug`
7. **Linting Workflow** - `/craft:code:lint optimize`
8. **Git Worktree Workflow** - Create, switch, merge
9. **Homebrew Distribution** - `/craft:dist:homebrew`
10. **Pre-commit Check** - `/craft:check` before commit

---

## Missing Documentation Pages

### High Priority
1. **Architecture Commands** - Complete category missing
2. **Distribution Commands** - Complete category missing
3. **Planning Commands** - Complete category missing
4. **Skills Reference** - Needs 4 new skills
5. **Agents Reference** - Needs 1 new agent

### Medium Priority
6. **Advanced Testing Guide** - CLI testing, watch mode
7. **CI/CD Integration Guide** - Local CI, auto-fixes
8. **Dependency Management** - deps-audit, deps-check
9. **Release Management** - code:release workflow

### Low Priority
10. **Git Documentation Suite** - learning-guide, safety-rails, undo-guide (internal docs?)
11. **Docs Site Frameworks** - site:docs/frameworks (internal?)

---

## Action Items

### Phase 1: Update Counts (< 30 min)
- [ ] Update homepage: 69 → 74 commands, 17 → 21 skills, 7 → 8 agents
- [ ] Update commands/overview.md with accurate counts
- [ ] Update REFCARD.md
- [ ] Update README.md

### Phase 2: Document Missing Features (< 2 hours)
- [ ] Create docs/commands/arch.md (Architecture commands)
- [ ] Create docs/commands/dist.md (Distribution commands)
- [ ] Create docs/commands/plan.md (Planning commands)
- [ ] Update docs/commands/code.md (add missing 9 commands)
- [ ] Update docs/commands/site.md (add missing 3 commands)
- [ ] Update docs/guide/skills-agents.md (add 4 skills, 1 agent)

### Phase 3: Create GIFs (< 3 hours)
- [ ] Set up VHS (brew install vhs)
- [ ] Create 5 core workflow GIFs (Priority 1)
- [ ] Create 5 additional workflow GIFs (Priority 2)
- [ ] Embed GIFs in workflows/index.md
- [ ] Add GIF gallery to homepage

### Phase 4: Polish (< 1 hour)
- [ ] Run mkdocs build --strict
- [ ] Validate all internal links
- [ ] Update mkdocs.yml navigation
- [ ] Deploy updated docs

---

## Notes

- Some commands may be internal/deprecated (git:docs/*, site:docs/*)
- Need to verify if smart-help is an alias or separate command
- orchestrator vs orchestrator-v2 - clarify which is current
