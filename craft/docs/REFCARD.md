# Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│  CRAFT PLUGIN QUICK REFERENCE                               │
├─────────────────────────────────────────────────────────────┤
│  Version: 1.15.0                                            │
│  Commands: 69 | Agents: 7 | Skills: 17                      │
│  Docs: https://data-wise.github.io/claude-plugins/craft/    │
└─────────────────────────────────────────────────────────────┘
```

## Essential Commands

| Command | Description |
|---------|-------------|
| `/craft:do <task>` | Universal command - routes to best workflow |
| `/craft:check` | Pre-flight checks (commit/pr/release) |
| `/craft:help` | Context-aware help and suggestions |
| `/craft:hub` | Command discovery hub |

## Smart Documentation (13 commands)

| Command | Description |
|---------|-------------|
| `/craft:docs:update` | Smart-Full: Detect → Generate → Check → Changelog |
| `/craft:docs:sync` | Detection: Classify changes, report stale docs |
| `/craft:docs:check` | Validation: Links + stale + nav + auto-fix |
| `/craft:docs:website` | **NEW** ADHD-friendly enhancement with scoring |
| `/craft:docs:guide` | Feature guide + demo + refcard generator |
| `/craft:docs:demo` | VHS tape generator for GIF demos |
| `/craft:docs:mermaid` | Mermaid diagram templates (6 types) |

**Quick examples:**
```bash
/craft:docs:update                    # Full smart cycle
/craft:docs:website --phase 1         # Quick wins: TL;DR, mermaid fixes
/craft:docs:check --report-only       # CI-safe mode
```

## Site Commands (12 commands)

| Command | Description |
|---------|-------------|
| `/craft:site:create` | Full site wizard with 8 ADHD-friendly presets |
| `/craft:site:nav` | Navigation reorganization (max 7 sections) |
| `/craft:site:audit` | Content inventory & audit |
| `/craft:site:consolidate` | Merge duplicate/overlapping docs |
| `/craft:site:status` | Dashboard and health check |
| `/craft:site:deploy` | Deploy to GitHub Pages |

**Quick examples:**
```bash
/craft:site:create --preset data-wise --quick
/craft:site:status
```

## Code & Testing (12 commands)

| Command | Modes | Description |
|---------|-------|-------------|
| `/craft:code:lint` | all | Linting with auto-fix |
| `/craft:test:run` | all | Test runner with watch mode |
| `/craft:code:debug` | - | Systematic debugging |
| `/craft:code:refactor` | - | Refactoring guidance |

**Modes:** `default` (<10s) | `debug` (<120s) | `optimize` (<180s) | `release` (<300s)

**Quick examples:**
```bash
/craft:code:lint optimize       # Parallel, fast
/craft:test:run debug           # Verbose with suggestions
```

## Git Commands (9 commands)

| Command | Description |
|---------|-------------|
| `/craft:git:worktree` | Parallel development with git worktrees |
| `/craft:git:sync` | Smart git sync |
| `/craft:git:clean` | Clean merged branches |
| `/craft:git:recap` | Activity summary |
| `/craft:git:branch` | Branch management |

**Quick examples:**
```bash
/craft:git:worktree add feature-auth
/craft:git:sync
/craft:git:clean
```

## Orchestrator (Enhanced v2.1)

```bash
/craft:orchestrate "add auth" optimize    # Fast parallel (4 agents)
/craft:orchestrate "prep release" release # Thorough audit
/craft:orchestrate status                 # Agent dashboard
/craft:orchestrate timeline               # Execution timeline
/craft:orchestrate continue               # Resume session
```

**Features:**
- Mode-aware execution
- Subagent monitoring
- Chat compression
- ADHD-optimized status tracking

## Skills (17 total)

Auto-triggered expertise:

| Skill | Triggers |
|-------|----------|
| `backend-designer` | API, database, auth |
| `frontend-designer` | UI/UX, components |
| `test-strategist` | Test strategy |
| `system-architect` | System design |
| `project-planner` | Feature planning |

## Agents (7 specialized)

| Agent | Specialty |
|-------|-----------|
| `backend-architect` | Scalable APIs, microservices |
| `docs-architect` | Technical documentation |
| `api-documenter` | OpenAPI, developer portals |
| `tutorial-engineer` | Step-by-step tutorials |
| `mermaid-expert` | Diagram creation |

## Configuration

### Mode System

| Mode | Time | Use Case |
|------|------|----------|
| **default** | <10s | Quick checks |
| **debug** | <120s | Verbose output |
| **optimize** | <180s | Parallel, performance |
| **release** | <300s | Comprehensive audit |

### ADHD-Friendly Presets

| Preset | Description |
|--------|-------------|
| `data-wise` | DT's standard (blue/orange) |
| `adhd-focus` | Calm forest green |
| `adhd-calm` | Warm earth tones |
| `adhd-dark` | Dark-first, reduced eye strain |
| `adhd-light` | Warm light, never harsh white |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Command not found | Verify installation: `/craft:hub` |
| Skill not triggering | Check skill definitions in plugin |
| Build fails | Run `/craft:check` for diagnostics |

## Links

- **[Full Documentation](guide/getting-started.md)**
- **[GitHub Issues](https://github.com/Data-Wise/claude-plugins/issues)**
- **[ROADMAP](https://github.com/Data-Wise/claude-plugins/blob/main/craft/ROADMAP.md)**
