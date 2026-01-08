# CI Detection Rollout Plan

Scheduled testing of `/craft:ci:detect` on all active dev-tools projects.

## Priority 1: Core Projects (Have Active Development)

| Project | Type | Status | Notes |
|---------|------|--------|-------|
| aiterm | Python/uv | ✅ Done | Main CLI tool, exemplary CI |
| scribe | Tauri | ✅ Done | Desktop app, needs test CI |
| atlas | Node/npm | ✅ Done | Project state engine, exemplary CI |
| flow-cli | ZSH Plugin | ✅ Done | Hybrid: ZSH + Node tooling |

## Priority 2: MCP Servers

| Project | Type | Status | Notes |
|---------|------|--------|-------|
| statistical-research | MCP/Bun | ✅ Done | 14 tools, has CI |
| shell | MCP/Node | ✅ Done | Minimal, no CI needed |
| project-refactor | MCP/Node | ✅ Done | Needs test CI |

## Priority 3: Python CLIs

| Project | Type | Status | Notes |
|---------|------|--------|-------|
| obsidian-cli-ops | Python/pip | ✅ Done | Has CI |
| nexus-cli | Python/uv | ✅ Done | Exemplary CI (6 workflows) |

## Priority 4: Infrastructure

| Project | Type | Status | Notes |
|---------|------|--------|-------|
| homebrew-tap | Homebrew | ✅ Skip | No CI needed |
| data-wise.github.io | Static | ✅ Skip | No CI needed |
| zsh-claude-workflow | ZSH Config | ✅ Done | Docs CI only |

## Detection Validation Checklist

For each project, verify:
- [ ] Project type detected correctly
- [ ] Build tool/package manager identified
- [ ] Test framework found (if applicable)
- [ ] Python/Node versions appropriate
- [ ] Existing CI detected (if present)
- [ ] Recommended template makes sense

## Commands to Run

```bash
# Run detection on each project
cd ~/projects/dev-tools/aiterm && claude "/craft:ci:detect"
cd ~/projects/dev-tools/scribe && claude "/craft:ci:detect"
cd ~/projects/dev-tools/atlas && claude "/craft:ci:detect"
cd ~/projects/dev-tools/flow-cli && claude "/craft:ci:detect"
cd ~/projects/dev-tools/mcp-servers/statistical-research && claude "/craft:ci:detect"
cd ~/projects/dev-tools/mcp-servers/shell && claude "/craft:ci:detect"
cd ~/projects/dev-tools/mcp-servers/project-refactor && claude "/craft:ci:detect"
cd ~/projects/dev-tools/homebrew-tap && claude "/craft:ci:detect"
cd ~/projects/dev-tools/obsidian-cli-ops && claude "/craft:ci:detect"
cd ~/projects/dev-tools/nexus-cli && claude "/craft:ci:detect"
cd ~/projects/dev-tools/zsh-claude-workflow && claude "/craft:ci:detect"
```

---

## Results Log

### flow-cli ✅
- **Date:** 2025-12-28
- **Type Detected:** ZSH Plugin (hybrid with Node tooling)
- **Primary Marker:** `flow.plugin.zsh`
- **Secondary:** package.json (devDeps: ESLint, Prettier, Husky)
- **Test Framework:** ZSH tests (10+), bash CLI tests
- **Existing CI:** ✅ test.yml, docs.yml, release.yml
- **Recommendation:** CI already well-configured, no changes needed
- **Detection Issue:** Should detect as ZSH Plugin, not Node (priority fix)

### aiterm ✅
- **Date:** 2025-12-28
- **Type Detected:** Python/uv (hatchling build)
- **Python Versions:** 3.10, 3.11, 3.12 (correct from pyproject.toml)
- **Test Framework:** pytest (with pytest-cov)
- **Linting:** ruff, black, mypy
- **Existing CI:** ✅ 5 workflows
  - test.yml (multi-platform × multi-python matrix)
  - docs.yml (MkDocs → GitHub Pages)
  - workflow.yml (PyPI publishing)
  - claude-code-review.yml, claude.yml
- **Recommendation:** CI is comprehensive and production-ready
- **Issues:** None - exemplary setup

### scribe ✅
- **Date:** 2025-12-28
- **Type Detected:** Tauri (Rust 2021 + Vite/React)
- **Frontend:** React 18, TypeScript, Tailwind, Vitest
- **Backend:** Rust 1.77.2+, Tauri 2.9.5
- **Test Framework:** Vitest (frontend), cargo-test (Rust, default)
- **Existing CI:** ⚠️ 2 workflows (missing tests)
  - release.yml (multi-arch macOS build + Homebrew cask update)
  - docs.yml
- **Missing CI:**
  - test.yml - Vitest + cargo test automation
  - lint workflow (clippy, eslint)
- **Recommendation:** Add test.yml for both frontend and Rust tests
- **Issues:** No automated testing in CI despite vitest being configured

### atlas ✅
- **Date:** 2025-12-28
- **Type Detected:** Node/npm (main, bin, exports, dependencies)
- **Node Versions:** 18, 20, 22 (matrix)
- **Test Framework:** Jest (unit, integration, e2e, dogfood)
- **Linting:** ESLint, Prettier
- **Existing CI:** ✅ 3 workflows (comprehensive)
  - test.yml (multi-node matrix, unit/integration/dogfood/e2e)
  - docs.yml
  - demos.yml
- **Recommendation:** CI is comprehensive, well-designed
- **Issues:** None - exemplary setup

### statistical-research ✅
- **Date:** 2025-12-28
- **Type Detected:** MCP Server (Bun + @modelcontextprotocol/sdk)
- **Runtime:** Bun with TypeScript
- **Test Framework:** Shell scripts (run-all.sh, test-server-start.sh, etc.)
- **Existing CI:** ✅ 2 workflows
  - ci.yml
  - docs.yml
- **Recommendation:** CI exists, adequate for MCP server
- **Issues:** None

### shell ✅
- **Date:** 2025-12-28
- **Type Detected:** MCP Server (Node + @modelcontextprotocol/sdk)
- **Test Framework:** None (minimal project)
- **Existing CI:** ❌ None
- **Recommendation:** Add basic CI if tests added in future
- **Issues:** Minimal project, no tests - CI low priority

### project-refactor ✅
- **Date:** 2025-12-28
- **Type Detected:** MCP Server (Node + @modelcontextprotocol/sdk)
- **Test Framework:** Node test runner (--test)
- **Existing CI:** ❌ None
- **Recommendation:** Add test.yml - tests exist but not automated
- **Issues:** Has tests but no CI workflow

### homebrew-tap ✅
- **Date:** 2025-12-28
- **Type Detected:** Homebrew Tap (Formula/ + Casks/)
- **Test Framework:** N/A (Homebrew handles formula validation)
- **Existing CI:** ❌ None
- **Recommendation:** No CI needed - Homebrew validates formulas on tap update
- **Issues:** None - skip CI

### obsidian-cli-ops ✅
- **Date:** 2025-12-28
- **Type Detected:** Python/pip (has pytest, ESLint for JS tests)
- **Test Framework:** pytest + __tests__ (JS)
- **Linting:** ESLint, Prettier
- **Existing CI:** ✅ 2 workflows
  - ci.yml
  - deploy-docs.yml
- **Recommendation:** CI exists, adequate
- **Issues:** None

### nexus-cli ✅
- **Date:** 2025-12-28
- **Type Detected:** Python/uv (hatchling build)
- **Python Versions:** 3.11, 3.12, 3.13
- **Test Framework:** pytest (with cov, mock, benchmark)
- **Linting:** ruff, mypy, bandit
- **Existing CI:** ✅ 6 workflows (comprehensive)
  - test.yml, ci.yml, quality.yml
  - docs.yml, publish.yml, release.yml
- **Recommendation:** CI is comprehensive and production-ready
- **Issues:** None - exemplary setup

### zsh-claude-workflow ✅
- **Date:** 2025-12-28
- **Type Detected:** ZSH Configuration (commands/, claude-commands/)
- **Test Framework:** None
- **Existing CI:** ✅ 1 workflow
  - docs.yml (documentation only)
- **Recommendation:** No test CI needed - shell configuration project
- **Issues:** None

---

## Rollout Summary

**Completed:** 2025-12-28

| Category | Projects | With CI | Needs CI | Skip |
|----------|----------|---------|----------|------|
| Core | 4 | 4 (aiterm, atlas, flow-cli exemplary; scribe needs tests) | 1 | 0 |
| MCP | 3 | 1 | 1 | 1 |
| Python | 2 | 2 (nexus-cli exemplary) | 0 | 0 |
| Infrastructure | 3 | 1 | 0 | 2 |
| **Total** | **12** | **8** | **2** | **3** |

**Exemplary CI setups:** aiterm, atlas, nexus-cli (use as templates)
**Needs test CI:** scribe (Tauri), project-refactor (MCP)

---

## Detection Issues Found

| Issue | Project | Priority | Status |
|-------|---------|----------|--------|
| ZSH Plugin should take priority over Node | flow-cli | High | ✅ Fixed |

**Fix Applied:** Added `is_real_node_project()` function that checks for main/bin/dependencies/exports fields. Projects with only devDependencies (like tooling-only package.json) now skip Node detection, allowing ZSH Plugin detection to take priority.

## Improvements Made

Based on rollout findings:

1. ✅ **Priority adjustment:** Special types (ZSH, Homebrew, Elisp) now checked BEFORE Node.js
2. ✅ **Real Node detection:** `is_real_node_project()` distinguishes real Node projects from tooling-only
3. ⬜ **CI quality check:** Future - Add validation for existing CI completeness

---
*Created: 2025-12-28*
*Last Updated: 2025-12-28*
*Rollout Completed: 2025-12-28*
