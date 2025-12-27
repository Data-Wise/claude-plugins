---
description: Unified test runner with mode support
arguments:
  - name: mode
    description: Execution mode (default|debug|optimize|release)
    required: false
    default: default
  - name: path
    description: Test file or directory
    required: false
  - name: filter
    description: Test name filter pattern
    required: false
---

# /craft:test:run - Unified Test Runner

Run tests with configurable depth and verbosity.

## Modes

| Mode | Time | Focus |
|------|------|-------|
| **default** | < 30s | Quick smoke tests |
| **debug** | < 120s | Verbose with traces |
| **optimize** | < 180s | Parallel execution |
| **release** | < 300s | Full test suite |

## Usage

```bash
/craft:test:run                     # Quick tests (default)
/craft:test:run debug               # Verbose with traces
/craft:test:run optimize            # Parallel execution
/craft:test:run release             # Full suite
/craft:test:run debug tests/        # Debug specific directory
/craft:test:run --filter="auth"     # Filter by name
```

## Project Type Detection

| Project | Framework | Discovery |
|---------|-----------|-----------|
| Python | pytest, unittest | tests/, test_*.py |
| JavaScript | jest, vitest, mocha | *.test.js, *.spec.js |
| R | testthat | tests/testthat/ |
| Go | go test | *_test.go |
| Rust | cargo test | tests/, #[test] |

## Mode Behaviors

### Default Mode (< 30s)
```bash
# Python: pytest -x -q --tb=no
# JavaScript: jest --bail --silent
# R: testthat::test_local(stop_on_failure = TRUE)
```

**Output:**
```
✓ Tests passed (45/45) in 12.3s
```

### Debug Mode (< 120s)
```bash
# Python: pytest -v --tb=long --capture=no
# JavaScript: jest --verbose --detectOpenHandles
```

**Output:**
```
╭─ Test Results (Debug Mode) ─────────────────────────╮
│ Suite: tests/ | Time: 45.2s                         │
├─────────────────────────────────────────────────────┤
│ ✓ test_auth.py::test_login              0.12s      │
│ ✓ test_auth.py::test_logout             0.08s      │
│ ✗ test_api.py::test_create_user         0.23s      │
│   │ AssertionError: Expected 201, got 400          │
│   │ at test_api.py:45                              │
├─────────────────────────────────────────────────────┤
│ Passed: 44 | Failed: 1 | Skipped: 0                │
╰─────────────────────────────────────────────────────╯
```

### Optimize Mode (< 180s)
```bash
# Python: pytest -n auto --dist loadfile
# JavaScript: jest --maxWorkers=4
```

**Output:**
```
╭─ Test Results (Optimize Mode) ──────────────────────╮
│ Workers: 4 | Time: 23.1s (vs 89.4s sequential)     │
│ Speedup: 3.9x                                       │
├─────────────────────────────────────────────────────┤
│ Slowest Tests:                                      │
│   test_integration.py::test_full_flow     8.2s     │
│   test_api.py::test_batch_upload          4.1s     │
├─────────────────────────────────────────────────────┤
│ Optimization Suggestions:                           │
│   - test_full_flow: Consider mocking external API  │
╰─────────────────────────────────────────────────────╯
```

### Release Mode (< 300s)
```bash
# Python: pytest --cov=src --cov-report=term-missing
# JavaScript: jest --coverage --coverageThreshold
```

**Output:**
```
╭─ Test Results (Release Mode) ───────────────────────╮
│ Status: ✓ READY FOR RELEASE                        │
├─────────────────────────────────────────────────────┤
│ Tests:                                              │
│   ✓ Unit tests: 156 passed                         │
│   ✓ Integration tests: 23 passed                   │
│   ✓ E2E tests: 8 passed                            │
├─────────────────────────────────────────────────────┤
│ Coverage: Lines 87% | Branches 72% | Functions 91% │
│ Quality Gates: All Passed                          │
╰─────────────────────────────────────────────────────╯
```

## Options

- `--filter <pattern>` - Run only matching tests
- `--verbose` - Show detailed output
- `--parallel` - Run tests in parallel
- `--fail-fast` - Stop on first failure

## Integration

Works with:
- `/craft:test:watch` - Watch mode
- `/craft:test:coverage` - Coverage report
- `/craft:test:debug` - Debug failures
- `/craft:code:ci-local` - CI checks
