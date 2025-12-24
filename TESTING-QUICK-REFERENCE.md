# Testing Quick Reference

Fast reference for running RForge plugin tests.

## Quick Start

```bash
# Run all unit tests
pytest tests/unit -v

# Run specific test file
pytest tests/unit/test_mode_parsing.py -v

# Run with script
./scripts/run-tests.sh unit
```

## Common Commands

### Run All Tests

```bash
pytest tests/unit -v
```

### Run Specific Test File

```bash
# Mode parsing
pytest tests/unit/test_mode_parsing.py -v

# Time budgets
pytest tests/unit/test_time_budgets.py -v

# Format handling
pytest tests/unit/test_format_handling.py -v

# Backward compatibility
pytest tests/unit/test_backward_compat.py -v
```

### Run by Marker

```bash
# Mode system tests only
pytest -m mode_system

# Backward compatibility only
pytest -m backward_compat

# Time budget tests only
pytest -m time_budget

# Exclude slow tests
pytest -m "not slow"
```

### Run Specific Test

```bash
# By class
pytest tests/unit/test_mode_parsing.py::TestExplicitModeDetection -v

# By specific test
pytest tests/unit/test_mode_parsing.py::TestExplicitModeDetection::test_explicit_mode_debug -v

# By keyword
pytest -k "explicit_mode" -v
```

## Test Runner Script

```bash
# Unit tests
./scripts/run-tests.sh unit

# All tests
./scripts/run-tests.sh all

# With coverage
./scripts/run-tests.sh coverage

# Quick tests (no slow)
./scripts/run-tests.sh quick
```

## Coverage

```bash
# Run with coverage
pytest tests/unit --cov=rforge --cov-report=term-missing

# Generate HTML report
pytest tests/unit --cov=rforge --cov-report=html

# View HTML report
open htmlcov/index.html
```

## Debugging

```bash
# Show print statements
pytest tests/unit -s

# Show locals on failure
pytest tests/unit -l

# Stop on first failure
pytest tests/unit -x

# Drop into debugger on failure
pytest tests/unit --pdb

# More verbose output
pytest tests/unit -vv
```

## Test Statistics

- **Total tests:** 96
- **Test files:** 4
- **Execution time:** ~0.4 seconds
- **Pass rate:** 100%

## Test Files

| File | Tests | Focus |
|------|-------|-------|
| test_mode_parsing.py | 30 | Mode detection & validation |
| test_time_budgets.py | 23 | Time budget management |
| test_format_handling.py | 20 | Output formatting |
| test_backward_compat.py | 23 | Backward compatibility |

## Test Markers

| Marker | Description | Count |
|--------|-------------|-------|
| unit | Fast unit tests | 96 |
| mode_system | Mode system specific | ~70 |
| backward_compat | Backward compatibility | 23 |
| time_budget | Time budget tests | 23 |
| slow | Tests > 1 second | 2 |

## Expected Output

```
======================== test session starts =========================
platform darwin -- Python 3.14.2, pytest-9.0.2
collected 96 items

tests/unit/test_backward_compat.py ........ (23 passed)
tests/unit/test_format_handling.py ........ (20 passed)
tests/unit/test_mode_parsing.py ........... (30 passed)
tests/unit/test_time_budgets.py ........... (23 passed)

========================= 96 passed in 0.4s ==========================
```

## Common Issues

### pytest not found

```bash
pip install pytest pytest-cov pytest-mock
```

### Import errors

```bash
# Make sure you're in the project root
cd /Users/dt/projects/dev-tools/claude-plugins

# Check PYTHONPATH
export PYTHONPATH=/Users/dt/projects/dev-tools/claude-plugins:$PYTHONPATH
```

### Tests not discovered

```bash
# Check test files start with test_
ls tests/unit/test_*.py

# Check pytest.ini is present
cat pytest.ini
```

## Next Steps

After unit tests pass:
1. Add integration tests (tests/integration/)
2. Add performance benchmarks (tests/performance/)
3. Add e2e tests (tests/e2e/)
4. Set up CI/CD pipeline

## Resources

- Test documentation: `tests/README.md`
- Complete report: `TEST-INFRASTRUCTURE-COMPLETE.md`
- pytest docs: https://docs.pytest.org/

---

**Quick reference for RForge plugin testing**
**Last updated:** 2024-12-24
