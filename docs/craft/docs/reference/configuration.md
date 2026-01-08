# Configuration

Craft plugin configuration and customization.

## Plugin Location

```
~/.claude/plugins/craft/
```

## Configuration Files

### .craft/site-design.yaml

Created by `/craft:site:create`, stores site design preferences:

```yaml
preset: "data-wise"

branding:
  name: "Your Project"
  tagline: "Description"
  logo: null

colors:
  primary: "#1a73e8"
  accent: "#ff6b35"
  scheme: "auto"

navigation:
  style: "tabs"
  max_depth: 3

features:
  search: true
  dark_mode: true
  code_copy: true
  edit_on_github: true
```

## Mode Configuration

Execution modes can be customized per project.

**Default mode settings:**

| Mode | Timeout | Use Case |
|------|---------|----------|
| default | 10s | Quick checks |
| debug | 120s | Verbose output |
| optimize | 180s | Parallel execution |
| release | 300s | Comprehensive audit |

## ADHD Score Thresholds

Website enhancement scoring:

| Grade | Score Range | Description |
|-------|-------------|-------------|
| A | 90-100 | Excellent ADHD-friendliness |
| B | 80-89 | Good |
| C | 70-79 | Acceptable |
| D | 60-69 | Needs improvement |
| F | <60 | Poor |

**Target:** Achieve C (70+) minimum for production docs.

## Environment Variables

Currently, craft uses Claude Code's built-in configuration. No additional environment variables required.

## Next Steps

- [Presets Reference](presets.md) - Design preset details
- [Quick Reference](../REFCARD.md) - Command cheat sheet
