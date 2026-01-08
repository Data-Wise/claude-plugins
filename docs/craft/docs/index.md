# Craft Plugin

[![Craft CI](https://github.com/Data-Wise/claude-plugins/actions/workflows/craft-ci.yml/badge.svg)](https://github.com/Data-Wise/claude-plugins/actions/workflows/craft-ci.yml)
[![Validate Plugins](https://github.com/Data-Wise/claude-plugins/actions/workflows/validate-plugins.yml/badge.svg)](https://github.com/Data-Wise/claude-plugins/actions/workflows/validate-plugins.yml)

> **TL;DR** (30 seconds)
> - **What:** Full-stack developer toolkit with 74 commands, 8 AI agents, and 21 auto-triggered skills
> - **Why:** Automate documentation, testing, git workflows, and site creation with one command
> - **How:** Install via `claude plugin install craft@local-plugins`
> - **Next:** Run `/craft:do "your task"` and let AI route to the best workflow

> Full-stack developer toolkit for Claude Code - 74 commands, 8 agents, 21 skills with smart orchestration and ADHD-friendly workflows

## Features

<div class="grid cards" markdown>

- :rocket: **74 Commands**

    Smart commands, docs, site management, code, testing, git, CI, architecture, distribution, and planning - all in one toolkit

- :brain: **8 Specialized Agents**

    Backend architect, docs architect, mermaid expert, API documenter, tutorial engineer, demo engineer, reference builder, and orchestrators

- :sparkles: **21 Skills**

    Auto-triggered expertise for backend/frontend design, DevOps, testing, architecture, planning, distribution, and documentation automation

- :zap: **Smart Orchestration**

    Enhanced orchestrator v2.1 with mode-aware execution, subagent monitoring, and timeline tracking

- :art: **8 ADHD-Friendly Presets**

    Documentation site designs optimized for focus, calm, and quick comprehension

- :books: **Documentation Excellence**

    Smart doc generation, consolidation (16→13 commands), TL;DR boxes, time estimates, mermaid validation

</div>

## Quick Start

```bash
# Install via Claude Code
claude plugin install craft@local-plugins

# Or create symlink
ln -s ~/projects/dev-tools/claude-plugins/craft ~/.claude/plugins/craft
```

**First command:**

```bash
/craft:do "add user authentication"
```

The universal `/craft:do` command routes your task to the best workflow automatically.

!!! success "Quick Win: Try It Now"
    Run `/craft:hub` to see all 69 commands organized by category - takes 5 seconds and shows everything craft can do.

## What's New in v1.15.0

**ADHD-Friendly Website Enhancement**

New `/craft:docs:website` command with ADHD scoring algorithm (0-100) across 5 categories:

- Visual Hierarchy (25%): TL;DR boxes, emojis, heading structure
- Time Estimates (20%): Tutorial duration info
- Workflow Diagrams (20%): Mermaid diagrams without errors
- Mobile Responsive (15%): Overflow fixes, touch targets
- Content Density (20%): Paragraph length, callout boxes

3-phase enhancement: Quick Wins (<2h), Structure (<4h), Polish (<8h)

## Popular Workflows

<div class="grid cards" markdown>

- :memo: **Documentation Automation**

    Update all docs from code changes in one command

    → [Learn more](workflows/index.md#documentation-workflow)

- :globe_with_meridians: **Site Creation**

    Zero to deployed docs site in < 5 minutes

    → [Learn more](workflows/index.md#site-creation-workflow)

- :rocket: **Release Management**

    Pre-release checks to published in one flow

    → [Learn more](workflows/index.md#release-workflow)

- :computer: **Development Workflow**

    Feature branches with git worktrees

    → [Learn more](workflows/index.md#development-workflow)

</div>

## Documentation

<div class="grid cards" markdown>

- :rocket: **[Quick Start](QUICK-START.md)**

    Get running in 30 seconds

- :brain: **[ADHD Guide](ADHD-QUICK-START.md)**

    Under 2 minutes, zero cognitive load

- :bar_chart: **[Visual Workflows](workflows/index.md)**

    5 diagrams showing complete flows

- :books: **[Commands Overview](commands/overview.md)**

    All 69 commands organized

- :sparkles: **[Skills & Agents](guide/skills-agents.md)**

    Understanding the AI system

- :page_facing_up: **[Quick Reference](REFCARD.md)**

    Command cheat sheet

</div>

## Key Command Categories

| Category | Count | Description |
|----------|-------|-------------|
| **Smart** | 4 | Universal command, orchestrator, checks, help, hub |
| **Documentation** | 17 | Smart docs with update, sync, check, website, API, changelog, guides |
| **Site** | 15 | Full site wizard with 8 ADHD-friendly presets, theme, nav, audit |
| **Code & Testing** | 17 | Linting, testing, debugging, refactoring, CI fixes, deps management |
| **Git** | 5 | Branch management, worktrees, sync, recap, clean |
| **CI** | 3 | Detection, generation, validation |
| **Architecture** | 4 | Analysis, diagrams, planning, reviews |
| **Distribution** | 3 | Homebrew, PyPI, curl installers |
| **Planning** | 3 | Feature planning, sprints, roadmaps |
| **Total** | **74** | **Complete development workflow coverage** |

## Links

- [GitHub Repository](https://github.com/Data-Wise/claude-plugins)
- [Issue Tracker](https://github.com/Data-Wise/claude-plugins/issues)
- [ROADMAP](https://github.com/Data-Wise/claude-plugins/blob/main/craft/ROADMAP.md)
