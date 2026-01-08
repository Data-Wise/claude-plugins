# Spec: Craft Testing Enhancements

**Status:** draft
**Created:** 2025-12-30
**From Brainstorm:** /workflow:brainstorm d f s "craft testing features"

---

## Overview

Enhance craft testing commands for plugin developers, focusing on plugin-aware testing capabilities.

---

## User Stories

### Primary Story

**As a** Claude Code plugin developer
**I want** plugin-specific testing tools
**So that** I can validate my commands, skills, and agents before release

### Acceptance Criteria

- [ ] `test:cli-gen plugin` generates plugin-aware test template
- [ ] Test template covers: commands, skills, arguments, output format
- [ ] Generated tests can run in CI (exit 0/1)
- [ ] Clear documentation for each test command enhancement

---

## Technical Requirements

### Enhancement 1: test:cli-gen plugin

Add `plugin` mode to existing cli-gen command:

```bash
/craft:test:cli-gen plugin "my-plugin"
```

**Generates:**
```
tests/
├── plugin/
│   ├── test-commands.sh      # Command invocation tests
│   ├── test-skills.sh        # Skill execution tests
│   ├── test-arguments.sh     # Argument parsing tests
│   └── fixtures/
│       └── expected-output/  # Snapshot baselines
```

**Test Categories:**
| Category | What It Tests |
|----------|---------------|
| Commands | Each command executes without error |
| Skills | Skill invocation returns expected format |
| Arguments | Required/optional args handled correctly |
| Output | Output matches expected format |

### Enhancement 2: test:run --plugin

Add `--plugin` flag to unified test runner:

```bash
/craft:test:run --plugin           # Run plugin tests
/craft:test:run --plugin --verbose # Verbose output
```

**Behavior:**
- Auto-detects plugin structure from `.claude-plugin/`
- Runs tests in order: structure → commands → skills
- Reports plugin-specific metrics

### Enhancement 3: Verbose Mode (All Commands)

Add consistent `--verbose` flag:

```bash
/craft:test:run --verbose
/craft:test:cli-run --verbose
/craft:test:coverage --verbose
```

**Verbose Output:**
- Show each test as it runs
- Display timing per test
- Show full error messages (not truncated)

---

## Implementation Priority

| Enhancement | Effort | Value | Priority |
|-------------|--------|-------|----------|
| test:cli-gen plugin | 1 hour | High | 1 |
| --verbose flag | 30 min | Medium | 2 |
| test:run --plugin | 1 hour | Medium | 3 |

---

## Open Questions

- [ ] Should plugin tests mock Claude Code environment?
- [ ] Include agent testing or defer to v1.13?
- [ ] Support for testing MCP tool integrations?

---

## Review Checklist

- [ ] Acceptance criteria are testable
- [ ] Technical requirements are complete
- [ ] Dependencies identified
- [ ] No blocking open questions
- [ ] Implementation fits timeline (this session)

---

## Files to Modify

| File | Change |
|------|--------|
| `craft/commands/test/cli-gen.md` | Add `plugin` mode |
| `craft/commands/test/run.md` | Add `--plugin` flag |
| `craft/commands/test/cli-run.md` | Add `--verbose` flag |
| `craft/commands/test/coverage.md` | Add `--verbose` flag |
