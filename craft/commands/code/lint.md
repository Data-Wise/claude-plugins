---
description: Code style and quality checks with mode support
arguments:
  - name: mode
    description: Execution mode (default|debug|optimize|release)
    required: false
    default: default
  - name: path
    description: File or directory to lint
    required: false
---

# /craft:code:lint - Code Linting

Run code style and quality checks with configurable depth.

## Modes

| Mode | Time | Focus |
|------|------|-------|
| **default** | < 10s | Quick style check |
| **debug** | < 120s | All rules + fix suggestions |
| **optimize** | < 180s | Performance-focused rules |
| **release** | < 300s | Comprehensive + strict |

## Usage

```bash
/craft:code:lint                    # Quick check (default)
/craft:code:lint debug              # Verbose with suggestions
/craft:code:lint optimize           # Performance rules
/craft:code:lint release            # Full pre-release check
/craft:code:lint debug src/         # Debug mode on specific path
```

## Project Type Detection

| Project | Linter | Config Files |
|---------|--------|--------------|
| Python | ruff, flake8, pylint | pyproject.toml, .flake8 |
| JavaScript/TypeScript | ESLint, Prettier | .eslintrc.*, prettier.config.* |
| R | lintr | .lintr |
| Go | golint, staticcheck | - |
| Rust | clippy | - |

## Mode Behaviors

### Default Mode (< 10s)
```bash
# Python: ruff check . --select=E,W,F
# JavaScript: eslint . --quiet
# R: Rscript -e "lintr::lint_package()"
```

**Output:**
```
✓ Lint passed (12 files, 0 issues)
```

### Debug Mode (< 120s)
```bash
# Python: ruff check . --show-fixes --show-source
# JavaScript: eslint . --format=stylish
```

**Output:**
```
╭─ Lint Results (Debug Mode) ─────────────────────────╮
│ Files: 12 | Rules: 45 active                        │
├─────────────────────────────────────────────────────┤
│ src/main.py:12:81 - E501 Line too long (85 > 80)   │
│   → Suggestion: Split into multiple lines          │
│ src/utils.py:8:1 - D100 Missing docstring          │
│   → Suggestion: Add module docstring               │
├─────────────────────────────────────────────────────┤
│ Auto-fix available: ruff check --fix               │
╰─────────────────────────────────────────────────────╯
```

### Optimize Mode (< 180s)
```bash
# Python: ruff check . --select=PERF,C4,SIM
# Focus on performance anti-patterns
```

**Output:**
```
╭─ Performance Lint (Optimize Mode) ──────────────────╮
│ Performance Issues: 3                               │
├─────────────────────────────────────────────────────┤
│ src/main.py:30 - PERF401 Use list comprehension    │
│   Estimated speedup: ~15%                          │
│ src/utils.py:15 - SIM118 Use `key in dict`         │
│   Estimated speedup: ~5%                           │
╰─────────────────────────────────────────────────────╯
```

### Release Mode (< 300s)
```bash
# Python: ruff check . && mypy . && bandit -r .
# JavaScript: eslint . && tsc --noEmit
# R: R CMD check --as-cran .
```

**Output:**
```
╭─ Release Lint Check ────────────────────────────────╮
│ Status: ✓ READY FOR RELEASE                        │
├─────────────────────────────────────────────────────┤
│ ✓ Style: 0 issues (45 rules checked)               │
│ ✓ Types: No type errors                            │
│ ✓ Security: No vulnerabilities                     │
│ ✓ Docs: 95% coverage                               │
├─────────────────────────────────────────────────────┤
│ Quality Score: 98/100                              │
╰─────────────────────────────────────────────────────╯
```

## Options

- `--fix` - Auto-fix issues where possible
- `--strict` - Treat warnings as errors
- `--files <pattern>` - Only lint matching files

## Integration

Works with:
- `/craft:code:ci-local` - Pre-commit checks
- `/craft:code:ci-fix` - Auto-fix lint issues
- `/craft:code:release` - Release validation
