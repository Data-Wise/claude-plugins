# Test Coverage Analysis

Analyze test coverage and identify untested code.

## Usage

```bash
/craft:test:coverage [options]
```

## What This Does

1. **Runs tests with coverage** instrumentation
2. **Analyzes coverage data** by file, function, line
3. **Identifies gaps** in test coverage
4. **Suggests tests** for uncovered code

## Coverage Metrics

| Metric | Description |
|--------|-------------|
| Line | Percentage of lines executed |
| Branch | Percentage of branches taken |
| Function | Percentage of functions called |
| Statement | Percentage of statements executed |

## Options

- `--report <type>` - Report type: terminal, html, json
- `--threshold <N>` - Minimum coverage percentage
- `--show-missing` - Show uncovered line numbers
- `--by-file` - Breakdown by file
- `--suggest` - Suggest tests for gaps

## Examples

```bash
# Basic coverage report
/craft:test:coverage

# HTML report
/craft:test:coverage --report html

# Show missing lines
/craft:test:coverage --show-missing

# Enforce threshold
/craft:test:coverage --threshold 80

# Get test suggestions
/craft:test:coverage --suggest
```

## Output

```
Running tests with coverage...

Coverage Report
─────────────────────────────────────────
File                     Lines   Branch
─────────────────────────────────────────
src/auth.py               95%     88%
src/api/handlers.py       72%     65%
src/utils.py             100%    100%
src/db/models.py          85%     80%
─────────────────────────────────────────
TOTAL                     87%     82%

Uncovered lines:
  src/api/handlers.py: 45-48, 72-80, 95

Suggested tests:
  - test_handler_error_cases (lines 45-48)
  - test_handler_edge_cases (lines 72-80)
```

## Integration

Works with:
- `/craft:test:run` - Run tests
- `/craft:code:coverage` - Code coverage command
- `/craft:code:ci-local` - CI checks
