---
description: Context-aware help that suggests relevant commands
arguments:
  - name: topic
    description: Topic or question to get help with
    required: false
---

# /craft:help - Context-Aware Help

Get intelligent help based on your project and question.

## Usage

```bash
/craft:help                     # Show relevant commands for current project
/craft:help <topic>             # Get help on specific topic
/craft:help "how do I..."       # Answer questions about workflows
```

## Context-Aware Suggestions

### Based on Project Type

**Python Project:**
```
╭─ Suggested Commands for Python Project ─────────────╮
│                                                     │
│ Development:                                        │
│   /craft:code:lint         ruff, flake8 checks     │
│   /craft:test:run          pytest runner           │
│   /craft:test:coverage     coverage report         │
│                                                     │
│ Quality:                                            │
│   /craft:code:deps-audit   pip-audit security      │
│   /craft:code:ci-local     pre-commit simulation   │
│                                                     │
│ Release:                                            │
│   /craft:code:release      PyPI workflow           │
│   /craft:docs:changelog    update CHANGELOG.md     │
│                                                     │
╰─────────────────────────────────────────────────────╯
```

**R Package:**
```
╭─ Suggested Commands for R Package ──────────────────╮
│                                                     │
│ Development:                                        │
│   /craft:test:run          testthat runner         │
│   /craft:code:lint         lintr checks            │
│   /craft:code:docs-check   roxygen2 validation     │
│                                                     │
│ Quality:                                            │
│   /craft:code:ci-local     R CMD check simulation  │
│   /craft:arch:analyze      package structure       │
│                                                     │
│ Release:                                            │
│   /craft:code:release      CRAN submission prep    │
│   /craft:site:build        pkgdown site            │
│                                                     │
╰─────────────────────────────────────────────────────╯
```

### Based on Current State

**Uncommitted Changes:**
```
╭─ You have uncommitted changes ──────────────────────╮
│                                                     │
│ Suggested:                                          │
│   /craft:check             Quick validation        │
│   /craft:git:sync          Commit and push         │
│   /craft:git:recap         What did you change?    │
│                                                     │
╰─────────────────────────────────────────────────────╯
```

**Failing Tests:**
```
╭─ Tests are failing ─────────────────────────────────╮
│                                                     │
│ Suggested:                                          │
│   /craft:test:debug        Debug the failures      │
│   /craft:code:debug        Investigate root cause  │
│   /craft:test:run debug    Verbose test output     │
│                                                     │
╰─────────────────────────────────────────────────────╯
```

## Topic-Based Help

### Testing
```bash
/craft:help testing

╭─ Testing Commands ──────────────────────────────────╮
│                                                     │
│ /craft:test:run [mode]     Run tests               │
│   Modes: default, debug, optimize, release         │
│                                                     │
│ /craft:test:watch          Watch mode              │
│   Re-runs tests when files change                  │
│                                                     │
│ /craft:test:coverage       Coverage analysis       │
│   Shows untested code paths                        │
│                                                     │
│ /craft:test:debug          Debug failures          │
│   Step through failing tests                       │
│                                                     │
│ Related:                                            │
│   /craft:code:test-gen     Generate test files     │
│   /craft:code:ci-local     Run full CI checks      │
│                                                     │
╰─────────────────────────────────────────────────────╯
```

### Architecture
```bash
/craft:help architecture

╭─ Architecture Commands ─────────────────────────────╮
│                                                     │
│ /craft:arch:analyze [mode] Analyze structure       │
│   Modes: default, debug, optimize, release         │
│                                                     │
│ /craft:arch:plan           Design features         │
│   Architecture planning assistance                 │
│                                                     │
│ /craft:arch:review         Review changes          │
│   Check architecture consistency                   │
│                                                     │
│ /craft:arch:diagram        Generate diagrams       │
│   Creates Mermaid diagrams                         │
│                                                     │
╰─────────────────────────────────────────────────────╯
```

## Question Answering

```bash
/craft:help "how do I run tests?"
→ Use /craft:test:run to run your test suite

/craft:help "how do I prepare a release?"
→ Use /craft:code:release for the full release workflow

/craft:help "how do I check code quality?"
→ Use /craft:check for quick validation
→ Use /craft:code:ci-local for full CI simulation

/craft:help "what commands are available?"
→ Use /craft:hub to see all 42+ commands
```

## Quick Reference

| Category | Commands | For |
|----------|----------|-----|
| **Code** | lint, coverage, deps-check, ci-local | Development |
| **Test** | run, watch, coverage, debug | Testing |
| **Arch** | analyze, plan, review, diagram | Design |
| **Plan** | feature, sprint, roadmap | Planning |
| **Docs** | sync, changelog, validate | Documentation |
| **Site** | init, build, preview, deploy | Doc sites |
| **Git** | branch, sync, clean, recap | Git workflow |

## Integration

For complete command listing:
- `/craft:hub` - Full command discovery
- `/craft:hub <category>` - Category deep dive
