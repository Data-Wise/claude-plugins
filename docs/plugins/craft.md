# Craft - Full-Stack Developer Toolkit

**Version:** 1.10.0 | **Status:** Active Development

Comprehensive production-ready toolkit for Claude Code featuring smart orchestration, ADHD-friendly workflows, multi-agent coordination, and complete documentation coverage.

**Components:** 67 commands | 17 skills | 7 agents

## Overview

Craft is a full-stack developer toolkit that provides intelligent orchestration across 13 command categories. It excels at automating complex development workflows through smart delegation, parallel execution, and mode-aware operations.

**Key Innovation:** Universal `/craft:do` command that uses AI to route tasks to appropriate workflows, eliminating the need to memorize specific commands.

## Key Features

### 🎯 Smart Commands
- **`/craft:do <task>`** - Universal command that routes to appropriate workflow
- **`/craft:orchestrate <task>`** - Multi-agent orchestrator with context tracking
- **`/craft:check`** - Pre-flight checks for commits, PRs, and releases
- **`/craft:help`** - Context-aware help and suggestions

### 🔧 13 Command Categories
1. **Architecture** (arch) - System design and analysis
2. **CI/CD** (ci) - GitHub Actions workflow generation
3. **Code** (code) - Linting and quality checks
4. **Distribution** (dist) - Homebrew and package publishing
5. **Documentation** (docs) - Mermaid diagrams and API docs
6. **Git** (git) - Worktree management and cleanup
7. **Plan** (plan) - Task planning and breakdowns
8. **Site** (site) - Static site generation
9. **Test** (test) - Test running and coverage

### ⚡ Mode System
Four execution modes for different use cases:
- **default** (<10s) - Quick checks and validation
- **debug** (<120s) - Verbose output with traces
- **optimize** (<180s) - Parallel execution for performance
- **release** (<300s) - Comprehensive audit and validation

### 🤖 Orchestrator v2
Enhanced multi-agent orchestration with:
- Mode-aware execution (optimize, release modes)
- Context tracking and budget monitoring
- Timeline view of agent execution
- Subagent monitoring and coordination

### 🧠 ADHD-Friendly Design
- Fast feedback with progress indicators
- Clear structure and visual hierarchy
- Reduced decision paralysis
- Context-aware suggestions

## Installation

### Quick Install

```bash
# One-command installation
curl -fsSL https://raw.githubusercontent.com/Data-Wise/claude-plugins/main/craft/install.sh | bash
```

**Then restart Claude Code to load the plugin.**

### Alternative Methods

```bash
# Via npm (when published)
npm install -g @data-wise/claude-craft-plugin

# Development mode (symlink)
cd craft
./scripts/install.sh --dev

# Manual installation
git clone https://github.com/Data-Wise/claude-plugins.git
cp -r claude-plugins/craft ~/.claude/plugins/
```

## Quick Start

### Universal Command

```bash
# Let AI route to best workflow
/craft:do "add user authentication"
/craft:do "optimize database queries"
/craft:do "prepare for release"
```

### Pre-Flight Checks

```bash
# Quick validation
/craft:check

# Release audit
/craft:check --for release
```

### Context-Aware Help

```bash
# Project-specific suggestions
/craft:help

# Deep dive into category
/craft:help testing
/craft:help architecture
```

## Core Commands

### Smart Commands (4)
- **`/craft:do`** - Universal command with AI routing
- **`/craft:orchestrate`** - Multi-agent orchestrator (v2.1)
- **`/craft:check`** - Pre-flight validation
- **`/craft:help`** - Context-aware suggestions

### Architecture (arch)
- **`/craft:arch:analyze`** - Analyze codebase architecture

### CI/CD (ci)
- **`/craft:ci:detect`** - Detect project type and build tools
- **`/craft:ci:generate`** - Generate GitHub Actions workflows
- **`/craft:ci:validate`** - Validate existing CI configuration

### Code (code)
- **`/craft:code:lint`** - Code style and quality checks

### Distribution (dist)
- **`/craft:dist:curl-install`** - Generate curl-based installation scripts

### Documentation (docs)
- **`/craft:docs:mermaid`** - Generate Mermaid diagram templates
- **`/craft:docs:api-documenter`** - Create API documentation
- **`/craft:docs:tutorial-engineer`** - Build step-by-step tutorials
- **`/craft:docs:reference-builder`** - Generate technical references

### Git (git)
- **`/craft:git:worktree`** - Git worktree management
- **`/craft:git:clean`** - Clean up merged branches

### Test (test)
- **`/craft:test:run`** - Unified test runner with mode support
- **`/craft:test:cli-gen`** - Generate CLI test suites
- **`/craft:test:cli-run`** - Run CLI test suites

## Mode System

Commands support execution modes for different contexts:

```bash
# Default mode (fast)
/craft:code:lint

# Debug mode (verbose)
/craft:code:lint debug

# Optimize mode (parallel)
/craft:test:run optimize

# Release mode (comprehensive)
/craft:test:run release
```

### Mode Characteristics

| Mode | Time Budget | Use Case | Tools Enabled |
|------|-------------|----------|---------------|
| **default** | <10s | Quick checks, CI/CD | Basic validation |
| **debug** | <120s | Issue investigation | Verbose logging, traces |
| **optimize** | <180s | Performance | Parallel execution |
| **release** | <300s | Production prep | Full audit, coverage |

## Orchestrator Features

### Multi-Agent Coordination

```bash
# Launch orchestrator with mode
/craft:orchestrate "add authentication" optimize

# Monitor agent status
/craft:orchestrate status

# View execution timeline
/craft:orchestrate timeline

# Track context budget
/craft:orchestrate budget
```

### Orchestrator Modes
- **optimize** - 4 parallel agents, fast execution
- **release** - Thorough audit with comprehensive checks
- **debug** - Verbose output with execution traces

## Skills & Agents

### 17 Built-in Skills
Skills automatically activate based on context:
- API architecture
- Code review
- Performance optimization
- Security analysis
- Documentation writing
- Test strategy
- DevOps engineering

### 7 Specialized Agents
- **backend-architect** - Server-side design
- **performance-engineer** - Optimization
- **testing-specialist** - Test strategy
- **security-specialist** - Security audits
- **devops-engineer** - CI/CD and deployment
- **tech-lead** - Architecture decisions
- **code-quality-reviewer** - Code standards

## Python Testing Framework

Craft includes a comprehensive Python-based testing framework:

```bash
# Run all tests
cd craft
pytest tests/

# Run with coverage
pytest tests/ --cov=craft --cov-report=html

# Run specific test markers
pytest -m unit              # Unit tests only
pytest -m integration       # Integration tests
```

## Documentation

- **[Commands Reference](../craft/docs/commands.md)** - All 67 commands with examples
- **[Skills & Agents](../craft/docs/skills-agents.md)** - Auto-activating skills and specialized agents
- **[Architecture](../craft/docs/architecture.md)** - Smart routing and orchestrator design
- **[Orchestrator Guide](../craft/docs/orchestrator.md)** - Multi-agent coordination

## Related

- **[Mode System](../MODE-SYSTEM.md)** - Shared mode system architecture
- **[Plugin Development](../PLUGIN-DEVELOPMENT.md)** - Creating new plugins
- **[CI/CD Guide](../CICD.md)** - Continuous integration patterns

## Support

- **GitHub Issues:** [https://github.com/Data-Wise/claude-plugins/issues](https://github.com/Data-Wise/claude-plugins/issues)
- **npm Package:** [https://www.npmjs.com/package/@data-wise/claude-craft-plugin](https://www.npmjs.com/package/@data-wise/claude-craft-plugin) *(coming soon)*
- **Documentation Site:** [https://data-wise.github.io/claude-plugins](https://data-wise.github.io/claude-plugins)

## Status

### Production-Ready Features
- ✅ 67 commands across 13 categories
- ✅ 17 auto-activating skills
- ✅ 7 specialized agents
- ✅ Orchestrator v2 with mode support
- ✅ Python testing framework
- ✅ Comprehensive CI/CD automation

### Active Development
- 🔄 Documentation completion (commands, skills, architecture)
- 🔄 npm package publication
- 🔄 Additional skills and agents
- 🔄 Performance optimizations
