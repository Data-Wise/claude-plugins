# Test Coverage Report

Generate and analyze test coverage for your project.

## Usage

```bash
/craft:code:coverage [options]
```

## What This Does

1. **Runs test suite** with coverage instrumentation
2. **Generates coverage report** (terminal, HTML, or JSON)
3. **Identifies uncovered code** with file and line details
4. **Tracks coverage trends** over time

## Project Type Detection

| Project | Tool | Config |
|---------|------|--------|
| Python | pytest-cov, coverage.py | pyproject.toml, .coveragerc |
| JavaScript | c8, nyc, jest --coverage | package.json |
| R | covr | - |
| Go | go test -cover | - |
| Rust | cargo tarpaulin | - |

## Options

- `--html` - Generate HTML report
- `--json` - Generate JSON report
- `--fail-under <N>` - Fail if coverage below N%
- `--branch` - Include branch coverage

## Examples

```bash
# Basic coverage report
/craft:code:coverage

# Generate HTML report
/craft:code:coverage --html

# CI mode with threshold
/craft:code:coverage --fail-under 80

# Include branch coverage
/craft:code:coverage --branch
```

## Output

```
Running tests with coverage...

Name                    Stmts   Miss  Cover
-------------------------------------------
src/main.py               120     12    90%
src/utils.py               45      5    89%
src/api/handlers.py        80     20    75%
tests/conftest.py          30      0   100%
-------------------------------------------
TOTAL                     275     37    87%

Uncovered lines:
  src/api/handlers.py: 45-48, 72-80
```

## Integration

Works with:
- `/craft:test:run` - Run tests
- `/craft:code:ci-local` - Pre-commit checks
- `/craft:code:release` - Release validation
