# Git & CI Commands

Version control and continuous integration - 12 commands total.

## Git Commands (9)

### /craft:git:worktree

**Purpose:** Parallel development with git worktrees.

```bash
/craft:git:worktree add feature-auth
/craft:git:worktree list
/craft:git:worktree remove feature-auth
```

### /craft:git:sync

Smart git sync (fetch, merge, push)

### /craft:git:clean

Clean merged branches

### /craft:git:recap

Activity summary

### Other Git Commands

- `/craft:git:branch` - Branch management
- Git guides: refcard, undo-guide, safety-rails, learning-guide

## CI Commands (3)

### /craft:ci:detect

Smart detection of project type, build tools, and CI requirements

```bash
/craft:ci:detect
```

### /craft:ci:generate

Generate GitHub Actions workflow from detection

```bash
/craft:ci:generate
```

### /craft:ci:validate

Validate existing CI workflow against project configuration

```bash
/craft:ci:validate
```
