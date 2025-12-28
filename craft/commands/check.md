---
description: Universal pre-flight check that validates project readiness
arguments:
  - name: mode
    description: Check depth (default|thorough)
    required: false
    default: default
  - name: for
    description: What to check for (commit|pr|release|deploy)
    required: false
---

# /craft:check - Universal Pre-flight

Run appropriate checks for your project type and context.

## Usage

```bash
/craft:check                    # Quick validation
/craft:check thorough           # Deep validation
/craft:check --for commit       # Pre-commit checks
/craft:check --for pr           # Pre-PR checks
/craft:check --for release      # Pre-release checks
```

## Auto-Detection

Detects project type, git context, and worktree status:

### Worktree Detection

```bash
# Check if running in a worktree
if git rev-parse --is-inside-work-tree &>/dev/null; then
  git_dir=$(git rev-parse --git-dir)
  if [[ "$git_dir" == *".git/worktrees/"* ]]; then
    echo "🌳 Running in worktree"
    echo "   Main repo: $(dirname $(dirname $(dirname $git_dir)))"
    echo "   Branch: $(git branch --show-current)"
  fi
fi
```

**Worktree-aware output:**
```
╭─ /craft:check ──────────────────────────────────────╮
│ Project: scribe (Node.js)                           │
│ 🌳 Worktree: ~/.git-worktrees/scribe/feat-hud       │
│    Main: ~/projects/dev-tools/scribe                │
│    Branch: feat/mission-control-hud                 │
├─────────────────────────────────────────────────────┤
│ ✓ Lint         0 issues                             │
│ ...                                                 │
```

Detects project type and runs appropriate checks:

### Python Projects
```
✓ Detected: Python (pyproject.toml)
Checks:
  ├── ruff check .              (linting)
  ├── mypy .                    (type checking)
  ├── pytest                    (tests)
  ├── pip-audit                 (security)
  └── docs validation           (if docs/ exists)
```

### JavaScript/TypeScript Projects
```
✓ Detected: Node.js (package.json)
Checks:
  ├── eslint .                  (linting)
  ├── tsc --noEmit              (types)
  ├── npm test                  (tests)
  ├── npm audit                 (security)
  └── docs validation           (if docs/ exists)
```

### R Packages
```
✓ Detected: R Package (DESCRIPTION)
Checks:
  ├── lintr::lint_package()     (linting)
  ├── devtools::check()         (R CMD check)
  ├── testthat::test_local()    (tests)
  ├── pkgdown::build_site()     (docs if configured)
  └── spelling::spell_check()   (spelling)
```

### Go Projects
```
✓ Detected: Go (go.mod)
Checks:
  ├── go vet ./...              (static analysis)
  ├── golangci-lint run         (linting)
  ├── go test ./...             (tests)
  └── go mod verify             (dependencies)
```

## Check Modes

### Default Mode (Quick)
- Lint check (fast rules only)
- Test run (fail-fast)
- Git status
- ~30 seconds

### Thorough Mode
- Full lint check
- Complete test suite
- Type checking
- Security audit
- Doc validation
- ~3-5 minutes

## Context-Specific Checks

### Pre-Commit (`--for commit`)
```
╭─ Pre-Commit Checks ─────────────────────────────────╮
│ ✓ Lint: No issues                                  │
│ ✓ Tests: 45/45 passed                              │
│ ✓ Types: No errors                                 │
│ ✓ No secrets detected                              │
├─────────────────────────────────────────────────────┤
│ READY TO COMMIT                                    │
╰─────────────────────────────────────────────────────╯
```

### Pre-PR (`--for pr`)
```
╭─ Pre-PR Checks ─────────────────────────────────────╮
│ ✓ Lint: No issues                                  │
│ ✓ Tests: 156/156 passed                            │
│ ✓ Coverage: 87% (meets 80% threshold)              │
│ ✓ Types: No errors                                 │
│ ✓ No merge conflicts                               │
│ ✓ Branch up to date with main                      │
├─────────────────────────────────────────────────────┤
│ READY FOR PR                                       │
╰─────────────────────────────────────────────────────╯
```

### Pre-Release (`--for release`)
```
╭─ Pre-Release Checks ────────────────────────────────╮
│ ✓ Lint: No issues (strict mode)                    │
│ ✓ Tests: All passing (unit + integration + e2e)    │
│ ✓ Coverage: 87% (meets threshold)                  │
│ ✓ Types: No errors                                 │
│ ✓ Security: No vulnerabilities                     │
│ ✓ Docs: Valid and up-to-date                       │
│ ✓ CHANGELOG: Updated                               │
│ ✓ Version: Bumped correctly                        │
├─────────────────────────────────────────────────────┤
│ READY FOR RELEASE                                  │
╰─────────────────────────────────────────────────────╯
```

## Output Format

### All Passing
```
╭─ /craft:check ──────────────────────────────────────╮
│ Project: aiterm (Python CLI)                       │
│ Time: 12.4s                                        │
├─────────────────────────────────────────────────────┤
│ ✓ Lint         0 issues                            │
│ ✓ Tests        135/135 passed                      │
│ ✓ Types        No errors                           │
│ ✓ Git          Clean working tree                  │
├─────────────────────────────────────────────────────┤
│ STATUS: ALL CHECKS PASSED ✓                        │
╰─────────────────────────────────────────────────────╯
```

### Issues Found
```
╭─ /craft:check ──────────────────────────────────────╮
│ Project: aiterm (Python CLI)                       │
│ Time: 15.2s                                        │
├─────────────────────────────────────────────────────┤
│ ⚠ Lint         3 issues                            │
│   └─ src/main.py:12 - Line too long               │
│   └─ src/utils.py:8 - Unused import               │
│   └─ tests/test_api.py:45 - Missing docstring     │
│                                                     │
│ ✓ Tests        135/135 passed                      │
│ ✓ Types        No errors                           │
│ ⚠ Git          Uncommitted changes                 │
├─────────────────────────────────────────────────────┤
│ STATUS: 2 ISSUES FOUND                             │
│ Fix with: /craft:code:ci-fix                       │
╰─────────────────────────────────────────────────────╯
```

## Integration

Works with:
- `/craft:code:lint` - Detailed lint results
- `/craft:test:run` - Detailed test results
- `/craft:code:ci-fix` - Auto-fix issues
- `/craft:code:ci-local` - Full CI simulation
