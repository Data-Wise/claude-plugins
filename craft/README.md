# Craft - Full Stack Developer Toolkit Plugin

A comprehensive full-stack developer toolkit for Claude Code. Craft provides 50 commands, 6 specialized agents, 11 skills with mode support, smart orchestration, and intelligent task routing.

## Installation

```bash
# From local marketplace
claude plugin install craft@local-plugins

# Or create symlink
ln -s /path/to/claude-plugins/craft ~/.claude/plugins/craft
```

## Quick Start - Smart Commands

```bash
# Universal command - AI routes to best workflow
/craft:do "add user authentication"

# Pre-flight checks
/craft:check                    # Quick validation
/craft:check --for release      # Full release audit

# Context-aware help
/craft:help                     # Suggestions for your project
/craft:help testing             # Deep dive into testing

# Discover all commands
/craft:hub
```

## Mode System (NEW in v1.2.0)

Commands support execution modes for different use cases:

| Mode | Time | Use Case |
|------|------|----------|
| **default** | < 10s | Quick checks |
| **debug** | < 120s | Verbose output, traces |
| **optimize** | < 180s | Parallel, performance |
| **release** | < 300s | Comprehensive audit |

```bash
/craft:code:lint                # Quick check
/craft:code:lint debug          # Verbose with suggestions
/craft:test:run release         # Full suite with coverage
/craft:arch:analyze optimize    # Performance analysis
```

## Commands (50 total)

### Smart Commands (3) - NEW
| Command | Description |
|---------|-------------|
| `/craft:do <task>` | Universal command - routes to appropriate workflow |
| `/craft:check` | Pre-flight checks (commit/pr/release) |
| `/craft:help` | Context-aware help and suggestions |

### Code Commands (12)
| Command | Description | Modes |
|---------|-------------|-------|
| `/craft:code:debug` | Systematic debugging | - |
| `/craft:code:demo` | Create demonstrations | - |
| `/craft:code:docs-check` | Pre-flight doc check | - |
| `/craft:code:refactor` | Refactoring guidance | - |
| `/craft:code:release` | Release workflow | - |
| `/craft:code:test-gen` | Generate test files | - |
| `/craft:code:lint` | Code style checks | ✓ |
| `/craft:code:coverage` | Coverage report | ✓ |
| `/craft:code:deps-check` | Dependency health | - |
| `/craft:code:deps-audit` | Security scan | - |
| `/craft:code:ci-local` | CI checks locally | - |
| `/craft:code:ci-fix` | Fix CI failures | - |

### Test Commands (6)
| Command | Description | Modes |
|---------|-------------|-------|
| `/craft:test:run` | Unified test runner | ✓ |
| `/craft:test:watch` | Watch mode | - |
| `/craft:test:coverage` | Coverage analysis | ✓ |
| `/craft:test:debug` | Debug failing tests | - |
| `/craft:test:cli-gen` | Generate CLI test suites | - |
| `/craft:test:cli-run` | Run CLI test suites | - |

### Architecture Commands (4)
| Command | Description | Modes |
|---------|-------------|-------|
| `/craft:arch:analyze` | Architecture analysis | ✓ |
| `/craft:arch:plan` | Design architecture | - |
| `/craft:arch:review` | Review changes | - |
| `/craft:arch:diagram` | Generate diagrams | - |

### Planning Commands (3)
| Command | Description |
|---------|-------------|
| `/craft:plan:feature` | Plan features with tasks |
| `/craft:plan:sprint` | Sprint planning |
| `/craft:plan:roadmap` | Generate roadmaps |

### Documentation Commands (7)
| Command | Description |
|---------|-------------|
| `/craft:docs:generate` | Full documentation generation (NEW) |
| `/craft:docs:api` | OpenAPI/Swagger documentation (NEW) |
| `/craft:docs:sync` | Sync docs with code |
| `/craft:docs:changelog` | Auto-update CHANGELOG |
| `/craft:docs:claude-md` | Update CLAUDE.md |
| `/craft:docs:validate` | Validate links |
| `/craft:docs:nav-update` | Update mkdocs.yml |

### Site Commands (6)
| Command | Description |
|---------|-------------|
| `/craft:site:init` | Initialize doc site |
| `/craft:site:build` | Build site |
| `/craft:site:preview` | Preview locally |
| `/craft:site:deploy` | Deploy to GitHub Pages |
| `/craft:site:check` | Validate site |
| `/craft:site:frameworks` | Compare frameworks |

### Git Commands (4 + 4 guides)
| Command | Description |
|---------|-------------|
| `/craft:git:branch` | Branch management |
| `/craft:git:sync` | Smart git sync |
| `/craft:git:clean` | Clean merged branches |
| `/craft:git:recap` | Activity summary |

**Git Guides:** refcard, undo-guide, safety-rails, learning-guide

### Discovery
| Command | Description |
|---------|-------------|
| `/craft:hub` | Command discovery hub |

## Skills (11)

| Skill | Category | Triggers |
|-------|----------|----------|
| `backend-designer` | Design | API, database, auth |
| `frontend-designer` | Design | UI/UX, components |
| `devops-helper` | Design | CI/CD, deployment |
| `test-strategist` | Testing | Test strategy |
| `cli-test-strategist` | Testing | CLI testing (NEW) |
| `system-architect` | Architecture | System design |
| `project-planner` | Planning | Feature planning |
| `mode-controller` | Modes | Mode behavior |
| `task-analyzer` | Orchestration | Task routing |
| `changelog-automation` | Documentation | Changelog patterns (NEW) |
| `architecture-decision-records` | Documentation | ADR generation (NEW) |
| `openapi-spec-generation` | Documentation | OpenAPI specs (NEW) |

## Agents (6)

| Agent | Purpose |
|-------|---------|
| `orchestrator` | Smart delegation to skills |
| `docs-architect` | Long-form technical documentation (NEW) |
| `tutorial-engineer` | Step-by-step tutorials (NEW) |
| `api-documenter` | OpenAPI/Swagger documentation (NEW) |
| `reference-builder` | Technical reference guides (NEW) |
| `mermaid-expert` | Mermaid diagram generation (NEW) |

## Workflows

### Daily Development
```
/craft:check → /craft:test:run → /craft:git:sync
```

### Release Preparation
```
/craft:check --for release
# OR
/craft:code:deps-audit → /craft:test:run release → /craft:code:release
```

### Feature Development
```
/craft:do "add feature name"
# Routes to: arch:plan → code:test-gen → git:branch
```

## Version

- **Version:** 1.3.0
- **Author:** DT (Data-Wise)
- **License:** MIT

## Changelog

### [1.3.0] - 2025-12-26
#### Added
- 5 documentation agents (ported from documentation-generation plugin)
  - `docs-architect` - Long-form technical documentation
  - `tutorial-engineer` - Step-by-step tutorials
  - `api-documenter` - OpenAPI/Swagger documentation
  - `reference-builder` - Technical reference guides
  - `mermaid-expert` - Mermaid diagram generation
- 3 documentation skills
  - `changelog-automation` - Changelog patterns
  - `architecture-decision-records` - ADR generation
  - `openapi-spec-generation` - OpenAPI specs
- 4 new commands
  - `/craft:docs:generate` - Full documentation generation
  - `/craft:docs:api` - OpenAPI/Swagger documentation
  - `/craft:test:cli-gen` - Generate CLI test suites
  - `/craft:test:cli-run` - Run CLI test suites
- Total: 50 commands, 11 skills, 6 agents

### [1.2.0] - 2025-12-26
#### Added
- Mode system (default, debug, optimize, release)
- 3 smart commands (do, check, help)
- 2 new skills (mode-controller, task-analyzer)
- Mode support for lint, test:run, arch:analyze, coverage
- Total: 46 commands, 8 skills, 1 agent

### [1.1.0] - 2025-12-26
#### Added
- 6 new code commands (lint, coverage, deps-check, deps-audit, ci-local, ci-fix)
- 4 new test commands (run, watch, coverage, debug)
- 4 new architecture commands (analyze, plan, review, diagram)
- 3 new planning commands (feature, sprint, roadmap)
- 3 new skills (test-strategist, system-architect, project-planner)
- Total: 42 commands, 6 skills, 1 agent

### [1.0.0] - 2025-12-26
#### Added
- Initial release with 26 commands
- 6 code, 6 site, 8 git, 5 docs commands
- 3 skills (backend, frontend, devops)
- 1 orchestrator agent
- Hub command for discovery
