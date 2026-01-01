# Quick Start

⏱️ **2 minutes** • 🟢 Beginner • ✓ 4 steps

> **TL;DR** (30 seconds)
> - **What:** Get craft plugin installed and verify it works
> - **Why:** Start automating your development workflow immediately
> - **How:** `claude plugin install craft@local-plugins` then run `/craft:hub`
> - **Next:** Try `/craft:do "your first task"` to see AI routing in action

Get craft running in 30 seconds.

## Install

=== "Claude Code Plugin"

    ```bash
    # From local marketplace
    claude plugin install craft@local-plugins
    ```

=== "Symlink"

    ```bash
    # Create symlink to development location
    ln -s ~/projects/dev-tools/claude-plugins/craft ~/.claude/plugins/craft
    ```

## Verify Installation

```bash
/craft:hub
```

Expected output:
```
┌─────────────────────────────────────────────────────────────┐
│ /craft:hub - Command Discovery                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 69 commands available across 9 categories                   │
│                                                             │
│ [Command listing...]                                        │
└─────────────────────────────────────────────────────────────┘
```

## First Commands

### Universal Task Execution

```bash
/craft:do "add user authentication"
```

The AI routes your task to the best workflow automatically.

### Pre-Flight Checks

```bash
/craft:check                    # Quick validation
/craft:check --for release      # Full release audit
```

### Context-Aware Help

```bash
/craft:help                     # Suggestions for your project
/craft:help testing             # Deep dive into testing
```

### Smart Documentation

```bash
/craft:docs:update              # Smart detection → full execution
/craft:docs:sync                # Quick stale docs check
/craft:docs:check               # Full validation with auto-fixes
```

### Create Documentation Site

```bash
/craft:site:create              # Interactive wizard
/craft:site:create --preset data-wise --quick
```

## Next Steps

- **[Commands Overview](commands/overview.md)** - Explore all 69 commands
- **[Skills & Agents](guide/skills-agents.md)** - Understand the AI system
- **[Orchestrator](guide/orchestrator.md)** - Advanced mode-aware execution
- **[Quick Reference](REFCARD.md)** - Command cheat sheet

## Common Workflows

### Documentation Workflow

```bash
# 1. Update docs from code changes
/craft:docs:update

# 2. Check for issues
/craft:docs:check

# 3. Deploy
/craft:site:deploy
```

### Release Workflow

```bash
# 1. Pre-release audit
/craft:check --for release

# 2. Generate changelog
/craft:docs:changelog

# 3. Git cleanup
/craft:git:clean
```

### Development Workflow

```bash
# 1. Create feature branch with worktree
/craft:git:worktree add feature-name

# 2. Run tests in watch mode
/craft:test:run debug

# 3. Lint with auto-fix
/craft:code:lint optimize
```
