# Commands Overview

> **TL;DR** (30 seconds)
> - **What:** 69 commands organized into 9 categories (Smart, Docs, Site, Code, Git, CI, etc.)
> - **Why:** One plugin handles your entire development workflow from docs to deployment
> - **How:** Use `/craft:hub` to discover all commands by category
> - **Next:** Start with `/craft:do` for AI-powered task routing or `/craft:check` for pre-flight validation

Craft provides **69 commands** across 9 categories for full-stack development workflows.

## Command Categories

### 🎯 Smart Commands (4)

Universal commands with AI-powered routing:

- `/craft:do <task>` - Universal task router
- `/craft:orchestrate <task> [mode]` - Enhanced orchestrator v2.1
- `/craft:check [--for]` - Pre-flight checks
- `/craft:help [topic]` - Context-aware help

[Learn more →](smart.md)

### 📚 Documentation Commands (13)

Smart documentation generation and validation:

- Super Commands: `update`, `sync`, `check`
- **NEW:** `/craft:docs:website` - ADHD-friendly enhancement
- Specialized: `api`, `changelog`, `guide`, `demo`, `mermaid`

[Learn more →](docs.md)

### 🌐 Site Commands (12)

Full documentation site management:

- `/craft:site:create` - Wizard with 8 ADHD-friendly presets
- Navigation & audit: `nav`, `audit`, `consolidate`
- Management: `status`, `update`, `deploy`

[Learn more →](site.md)

### 💻 Code & Testing Commands (12)

Development workflow tools:

- Linting: `/craft:code:lint [mode]`
- Testing: `/craft:test:run [mode]`
- Debugging: `/craft:code:debug`
- Refactoring: `/craft:code:refactor`

[Learn more →](code.md)

### 🔀 Git & CI Commands (12)

Version control and continuous integration:

- Git: `worktree`, `sync`, `clean`, `recap`, `branch`
- CI: `detect`, `generate`, `validate`

[Learn more →](git.md)

### 📦 Other Categories

- **Architecture** (7): System design, tech stack analysis
- **Distribution** (2): Homebrew formulas, curl installers
- **Planning** (3): Feature planning, sprints, roadmaps
- **Discovery** (1): Command hub

## Mode System

Many commands support execution modes:

| Mode | Time | Description |
|------|------|-------------|
| `default` | <10s | Quick checks |
| `debug` | <120s | Verbose output with suggestions |
| `optimize` | <180s | Parallel execution, performance focused |
| `release` | <300s | Comprehensive audit |

**Example:**
```bash
/craft:code:lint optimize    # Fast parallel linting
/craft:test:run debug        # Verbose test output
```

## Quick Navigation

| I want to... | Use this command |
|--------------|------------------|
| Generate docs | `/craft:docs:update` |
| Create a site | `/craft:site:create` |
| Run tests | `/craft:test:run` |
| Manage git worktrees | `/craft:git:worktree` |
| Check before commit | `/craft:check` |
| Get help | `/craft:help` |
| Discover commands | `/craft:hub` |
