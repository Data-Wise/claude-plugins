# Craft Commands Reference

Complete reference for all 67 Craft commands organized by category. Craft provides intelligent automation across the full development lifecycle.

## Quick Reference

**Smart Commands:** `/craft:do`, `/craft:check`, `/craft:help`, `/craft:hub`
**13 Categories:** arch, ci, code, dist, docs, git, plan, site, test

Use `/craft:hub` to discover all available commands interactively.

## Smart Commands

### /craft:do
Universal command - AI routes to appropriate workflow.

```bash
/craft:do "add user authentication"
/craft:do "optimize database queries"
/craft:do "prepare for release"
```

### /craft:orchestrate
Multi-agent orchestrator with mode-aware execution.

```bash
/craft:orchestrate "add auth" optimize    # Fast parallel
/craft:orchestrate "prep release" release # Thorough audit
/craft:orchestrate status                 # Agent dashboard
```

**Modes:** optimize (4 agents), release (comprehensive), debug (verbose)

###/craft:check
Pre-flight validation for commits, PRs, and releases.

```bash
/craft:check                  # Quick validation
/craft:check --for commit     # Pre-commit checks
/craft:check --for release    # Full release audit
```

### /craft:help
Context-aware help and suggestions.

```bash
/craft:help                   # Project-specific suggestions
/craft:help testing           # Deep dive into testing
```

## Architecture Commands (arch/)

### /craft:arch:analyze
Analyze codebase architecture with mode support.

```bash
/craft:arch:analyze
/craft:arch:analyze optimize   # Performance analysis
```

## CI/CD Commands (ci/)

### /craft:ci:detect
Detect project type, build tools, and test frameworks.

```bash
/craft:ci:detect
```

**Detects:** Language, framework, build system, test runner, dependencies

### /craft:ci:generate
Generate GitHub Actions workflow from project detection.

```bash
/craft:ci:generate
/craft:ci:generate --template node-typescript
```

**Generates:** .github/workflows/ci.yml with tests, linting, build steps

### /craft:ci:validate
Validate existing CI workflow against project configuration.

```bash
/craft:ci:validate
```

## Code Quality Commands (code/)

### /craft:code:lint
Code style and quality checks with mode support.

```bash
/craft:code:lint              # Quick check
/craft:code:lint debug        # Verbose with suggestions
```

## Distribution Commands (dist/)

### /craft:dist:curl-install
Generate curl-based installation scripts for GitHub releases.

```bash
/craft:dist:curl-install
```

**Generates:** install.sh with release detection, platform support

## Documentation Commands (docs/)

### /craft:docs:mermaid
Generate Mermaid diagram templates.

```bash
/craft:docs:mermaid flowchart
/craft:docs:mermaid sequence
/craft:docs:mermaid er
```

### /craft:docs:api-documenter
Create API documentation with OpenAPI support.

```bash
/craft:docs:api-documenter
```

### /craft:docs:tutorial-engineer
Build step-by-step tutorials from code.

```bash
/craft:docs:tutorial-engineer "Getting started guide"
```

### /craft:docs:reference-builder
Generate technical references and API docs.

```bash
/craft:docs:reference-builder
```

## Git Commands (git/)

### /craft:git:worktree
Git worktree management for parallel development.

```bash
/craft:git:worktree list
/craft:git:worktree add feature-branch
/craft:git:worktree remove feature-branch
```

### /craft:git:clean
Clean up merged branches safely.

```bash
/craft:git:clean              # Interactive mode
/craft:git:clean --force      # Auto-delete merged branches
```

## Test Commands (test/)

### /craft:test:run
Unified test runner with mode support.

```bash
/craft:test:run                   # Quick tests
/craft:test:run release           # Full suite with coverage
```

### /craft:test:cli-gen
Generate CLI test suites (interactive and automated).

```bash
/craft:test:cli-gen
```

### /craft:test:cli-run
Run CLI test suites.

```bash
/craft:test:cli-run              # Run all CLI tests
/craft:test:cli-run --suite e2e  # Specific suite
```

## Mode System

All applicable commands support 4 execution modes:

| Mode | Time | Use Case |
|------|------|----------|
| **default** | <10s | Quick checks |
| **debug** | <120s | Verbose output |
| **optimize** | <180s | Parallel execution |
| **release** | <300s | Comprehensive audit |

**Usage:**
```bash
/craft:code:lint debug
/craft:test:run release
/craft:arch:analyze optimize
```

## Category Breakdown

- **Smart (4):** do, orchestrate, check, help, hub
- **Architecture (1):** analyze
- **CI/CD (3):** detect, generate, validate
- **Code (1):** lint
- **Distribution (1):** curl-install
- **Documentation (4):** mermaid, api-documenter, tutorial-engineer, reference-builder
- **Git (2):** worktree, clean
- **Test (3):** run, cli-gen, cli-run

## See Also

- **[Skills & Agents Guide](skills-agents.md)** - 17 skills, 7 agents
- **[Architecture Guide](architecture.md)** - How Craft works
- **[Orchestrator Guide](orchestrator.md)** - Multi-agent coordination
- **[Mode System](../../docs/MODE-USAGE-GUIDE.md)** - Mode system deep dive
