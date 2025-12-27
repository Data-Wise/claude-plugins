# /craft:hub - Command Discovery Hub

You are a command discovery assistant for the craft plugin. Help users find the right command.

## When Invoked (`/craft:hub`)

### Step 1: Detect Project Context

```
Detection Rules (check in order):
1. DESCRIPTION file → R Package
2. pyproject.toml → Python Package
3. package.json → Node.js Project
4. _quarto.yml → Quarto Project
5. mkdocs.yml → MkDocs Project
6. Otherwise → Generic Project
```

### Step 2: Display Hub

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 🛠️ CRAFT - Full Stack Developer Toolkit v1.2.0                          │
│ 📍 [PROJECT_NAME] ([PROJECT_TYPE]) on [GIT_BRANCH]                      │
│ 📊 46 Commands | 8 Skills | 1 Agent | 4 Modes                           │
├─────────────────────────────────────────────────────────────────────────┤
│ ⚡ SMART COMMANDS (Start Here):                                         │
│    /craft:do <task>     Universal command - AI routes to best workflow │
│    /craft:check         Pre-flight checks for commit/pr/release        │
│    /craft:help          Context-aware help and suggestions             │
├─────────────────────────────────────────────────────────────────────────┤
│ 🎚️ MODES (default|debug|optimize|release):                             │
│    default  < 10s   Quick analysis, minimal output                     │
│    debug    < 120s  Verbose traces, detailed fixes                     │
│    optimize < 180s  Performance focus, parallel execution              │
│    release  < 300s  Comprehensive checks, full audit                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ 💻 CODE (12)                     🧪 TEST (4)                            │
│   /craft:code:debug                /craft:test:run [mode]               │
│   /craft:code:demo                 /craft:test:watch                    │
│   /craft:code:docs-check           /craft:test:coverage                 │
│   /craft:code:refactor             /craft:test:debug                    │
│   /craft:code:release                                                   │
│   /craft:code:test-gen           🏗️ ARCH (4)                            │
│   /craft:code:lint [mode]          /craft:arch:analyze [mode]           │
│   /craft:code:coverage             /craft:arch:plan                     │
│   /craft:code:deps-check           /craft:arch:review                   │
│   /craft:code:deps-audit           /craft:arch:diagram                  │
│   /craft:code:ci-local                                                  │
│   /craft:code:ci-fix             📋 PLAN (3)                            │
│                                    /craft:plan:feature                  │
│ 📄 DOCS (5)                        /craft:plan:sprint                   │
│   /craft:docs:sync                 /craft:plan:roadmap                  │
│   /craft:docs:changelog                                                 │
│   /craft:docs:claude-md          📖 SITE (6)                            │
│   /craft:docs:validate             /craft:site:init                     │
│   /craft:docs:nav-update           /craft:site:build                    │
│                                    /craft:site:preview                  │
│ 🔀 GIT (4+4 guides)                /craft:site:deploy                   │
│   /craft:git:branch                /craft:site:check                    │
│   /craft:git:sync                  /craft:site:frameworks               │
│   /craft:git:clean                                                      │
│   /craft:git:recap                                                      │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│ 🎯 Quick Actions:                                                       │
│    /craft:do "fix bug"    /craft:check --for pr    /craft:help testing │
│    /craft:test:run debug  /craft:arch:analyze      /craft:git:sync     │
└─────────────────────────────────────────────────────────────────────────┘
```

## Smart Commands (NEW!)

### `/craft:do <task>` - Universal Command
```
Intelligently routes your task to the right workflow:

/craft:do add authentication    → arch:plan + code:test-gen + git:branch
/craft:do fix login bug         → code:debug + test:run + test:debug
/craft:do improve quality       → code:lint + test:coverage + code:refactor
/craft:do prepare release       → deps-audit + test:run release + code:release
```

### `/craft:check` - Universal Pre-flight
```
Auto-detects project type and runs appropriate checks:

/craft:check                   Quick validation (lint + tests + types)
/craft:check --for commit      Pre-commit checks
/craft:check --for pr          Pre-PR validation (+ coverage + conflicts)
/craft:check --for release     Full release audit (+ security + docs)
```

### `/craft:help` - Context-Aware Help
```
/craft:help                    Shows relevant commands for your project
/craft:help testing            Deep dive into testing commands
/craft:help "how do I..."      Answer workflow questions
```

## Mode System (NEW!)

Many commands support modes for different use cases:

| Mode | Time Budget | Use Case |
|------|-------------|----------|
| **default** | < 10-30s | Day-to-day quick checks |
| **debug** | < 120s | Investigating issues, verbose output |
| **optimize** | < 180s | Performance focus, parallel execution |
| **release** | < 300s | Pre-release comprehensive checks |

### Mode Examples
```bash
/craft:code:lint                # default mode - quick
/craft:code:lint debug          # verbose with fix suggestions
/craft:code:lint release        # comprehensive with security

/craft:test:run                 # quick smoke tests
/craft:test:run debug           # verbose with traces
/craft:test:run optimize        # parallel execution
/craft:test:run release         # full suite with coverage

/craft:arch:analyze             # quick overview
/craft:arch:analyze debug       # deep pattern analysis
/craft:arch:analyze release     # full architectural audit
```

## Category Deep Dive

### `/craft:hub code`
```
💻 CODE COMMANDS (12)
─────────────────────────────────────────────────────────────────────────
Command                  │ Description                    │ Modes
─────────────────────────┼────────────────────────────────┼─────────────
/craft:code:debug        │ Systematic debugging           │ -
/craft:code:demo         │ Create demonstrations          │ -
/craft:code:docs-check   │ Pre-flight doc check           │ -
/craft:code:refactor     │ Refactoring guidance           │ -
/craft:code:release      │ Release workflow               │ -
/craft:code:test-gen     │ Generate test files            │ -
/craft:code:lint         │ Code style & quality checks    │ ✓
/craft:code:coverage     │ Test coverage report           │ ✓
/craft:code:deps-check   │ Check dependency health        │ -
/craft:code:deps-audit   │ Security vulnerability scan    │ -
/craft:code:ci-local     │ Run CI checks locally          │ -
/craft:code:ci-fix       │ Fix CI failures                │ -
─────────────────────────────────────────────────────────────────────────
```

### `/craft:hub test`
```
🧪 TEST COMMANDS (4) - Testing & Quality
─────────────────────────────────────────────────────────────────────────
Command                  │ Description                    │ Modes
─────────────────────────┼────────────────────────────────┼─────────────
/craft:test:run          │ Unified test runner            │ ✓
/craft:test:watch        │ Watch mode (re-run on change)  │ -
/craft:test:coverage     │ Coverage analysis              │ ✓
/craft:test:debug        │ Debug failing tests            │ -
─────────────────────────────────────────────────────────────────────────
```

### `/craft:hub arch`
```
🏗️ ARCH COMMANDS (4) - Architecture & Design
─────────────────────────────────────────────────────────────────────────
Command                  │ Description                    │ Modes
─────────────────────────┼────────────────────────────────┼─────────────
/craft:arch:analyze      │ Analyze architecture patterns  │ ✓
/craft:arch:plan         │ Design architecture            │ -
/craft:arch:review       │ Review architecture changes    │ -
/craft:arch:diagram      │ Generate Mermaid diagrams      │ -
─────────────────────────────────────────────────────────────────────────
```

### `/craft:hub plan`
```
📋 PLAN COMMANDS (3) - Planning & Project Management
─────────────────────────────────────────────────────────────────────────
Command                  │ Description
─────────────────────────┼────────────────────────────────────────────
/craft:plan:feature      │ Plan features with tasks and estimates
/craft:plan:sprint       │ Sprint planning with capacity
/craft:plan:roadmap      │ Generate project roadmaps
─────────────────────────────────────────────────────────────────────────
```

### `/craft:hub docs`
```
📄 DOCS COMMANDS (5) - Documentation Automation
─────────────────────────────────────────────────────────────────────────
Command                  │ Description
─────────────────────────┼────────────────────────────────────────────
/craft:docs:sync         │ Sync docs with code changes
/craft:docs:changelog    │ Auto-update CHANGELOG.md
/craft:docs:claude-md    │ Update CLAUDE.md
/craft:docs:validate     │ Validate links, code, structure
/craft:docs:nav-update   │ Update mkdocs.yml navigation
─────────────────────────────────────────────────────────────────────────
```

### `/craft:hub site`
```
📖 SITE COMMANDS (6) - Documentation Sites
─────────────────────────────────────────────────────────────────────────
Command                  │ R Package        │ Other (MkDocs)
─────────────────────────┼──────────────────┼─────────────────────
/craft:site:init         │ pkgdown/altdoc   │ mkdocs init
/craft:site:build        │ pkgdown::build   │ mkdocs build
/craft:site:preview      │ preview locally  │ mkdocs serve
/craft:site:deploy       │ gh-pages push    │ mkdocs gh-deploy
/craft:site:check        │ validate site    │ validate site
/craft:site:frameworks   │ compare options  │ compare options
─────────────────────────────────────────────────────────────────────────
```

### `/craft:hub git`
```
🔀 GIT COMMANDS (4 commands + 4 guides)
─────────────────────────────────────────────────────────────────────────
Commands:
  /craft:git:branch     Branch management (create, switch, delete)
  /craft:git:sync       Smart sync with remote (pull, rebase, push)
  /craft:git:clean      Clean up merged branches safely
  /craft:git:recap      Git activity summary (what changed?)

Guides:
  /craft:git:refcard    Quick reference card
  /craft:git:undo-guide Emergency undo guide
  /craft:git:safety-rails Safety rails guide
  /craft:git:learning-guide Learning guide
─────────────────────────────────────────────────────────────────────────
```

## Skills (8 Auto-Activated)

| Skill | Category | Triggers On |
|-------|----------|-------------|
| `backend-designer` | Design | API design, database, auth discussions |
| `frontend-designer` | Design | UI/UX, components, accessibility |
| `devops-helper` | Design | CI/CD, deployment, Docker |
| `test-strategist` | Testing | Test strategy, coverage, flaky tests |
| `system-architect` | Architecture | System design, patterns, trade-offs |
| `project-planner` | Planning | Feature planning, sprints, roadmaps |
| `mode-controller` | Modes | Mode selection and behavior |
| `task-analyzer` | Orchestration | Task routing for /craft:do |

## Context-Aware Suggestions

### Python Package (pyproject.toml detected)
```
💡 SUGGESTED FOR PYTHON PROJECT:

  /craft:do "run all checks"  Smart workflow
  /craft:code:lint            Run ruff/flake8
  /craft:test:run             Run pytest
  /craft:code:ci-local        Pre-push validation
  /craft:code:release         PyPI release workflow
```

### R Package (DESCRIPTION detected)
```
💡 SUGGESTED FOR R PACKAGE:

  /craft:do "check package"   Smart workflow
  /craft:test:run             Run testthat
  /craft:code:release         CRAN submission prep
  /craft:site:init            Setup pkgdown/altdoc
  /craft:arch:analyze         Check package structure
```

### Node.js Project (package.json detected)
```
💡 SUGGESTED FOR NODE PROJECT:

  /craft:do "validate all"    Smart workflow
  /craft:code:lint            Run ESLint/Prettier
  /craft:test:run             Run Jest/Vitest
  /craft:code:deps-audit      Security scan
  /craft:code:release         npm publish workflow
```

## Quick Reference

```
┌────────────────────────────────────────────────────────────────────────┐
│ CRAFT QUICK REFERENCE - 46 COMMANDS                                    │
├────────────────────────────────────────────────────────────────────────┤
│ Start Here:                                                            │
│   /craft:do <task>   → AI routes to best workflow                     │
│   /craft:check       → Quick validation                               │
│   /craft:help        → Context-aware suggestions                      │
│                                                                        │
│ Development Workflow:                                                  │
│   /craft:code:lint [mode] → /craft:test:run [mode] →                  │
│   /craft:code:coverage → /craft:code:ci-local → /craft:git:sync       │
│                                                                        │
│ Architecture:                                                          │
│   /craft:arch:analyze [mode] → /craft:arch:plan → /craft:arch:diagram │
│                                                                        │
│ Before Release:                                                        │
│   /craft:check --for release  OR                                       │
│   /craft:code:deps-audit → /craft:test:run release →                  │
│   /craft:docs:changelog → /craft:code:release                          │
│                                                                        │
│ Daily:                                                                 │
│   /craft:git:recap → /craft:check → /craft:git:sync                   │
└────────────────────────────────────────────────────────────────────────┘
```

## Agents

| Agent | Purpose |
|-------|---------|
| `orchestrator` | Smart delegation to skills based on task context |
