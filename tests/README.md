# RForge Plugin Test Suite

Comprehensive test infrastructure for the RForge plugin mode system.

## Directory Structure

```
tests/
├── unit/                  # Fast, isolated unit tests
│   ├── test_mode_parsing.py
│   ├── test_time_budgets.py
│   ├── test_format_handling.py
│   └── test_backward_compat.py
├── integration/           # Integration tests (may require MCP server)
├── performance/           # Performance benchmarks
├── e2e/                   # End-to-end workflow tests
├── fixtures/              # Test data and fixtures
├── mocks/                 # Mock objects and responses
├── conftest.py            # Shared pytest fixtures
├── requirements-test.txt  # Test dependencies
└── README.md              # This file
```

## Quick Start

### Install Test Dependencies

```bash
# From project root
pip install -r tests/requirements-test.txt
```

### Run All Tests

```bash
# Run all tests with coverage
pytest

# Run with verbose output
pytest -v

# Run specific test category
pytest -m unit
pytest -m integration
pytest -m performance
```

### Run Specific Test Files

```bash
# Run mode parsing tests
pytest tests/unit/test_mode_parsing.py -v

# Run time budget tests
pytest tests/unit/test_time_budgets.py -v

# Run format handling tests
pytest tests/unit/test_format_handling.py -v

# Run backward compatibility tests
pytest tests/unit/test_backward_compat.py -v
```

## Test Categories

### Unit Tests (`-m unit`)

**Fast, isolated tests** - Run in < 5 seconds total

- **test_mode_parsing.py**: Mode detection and validation
  - Explicit mode parameters
  - Implicit mode from context
  - Default mode fallback
  - Invalid mode handling
  - Case-insensitive parsing

- **test_time_budgets.py**: Time budget enforcement
  - Budget assignment per mode
  - Timer functionality
  - Budget exceeded detection
  - Warning thresholds
  - Requirement levels (MUST vs SHOULD)

- **test_format_handling.py**: Output format handling
  - Format parameter parsing
  - JSON formatting
  - Markdown formatting
  - Terminal formatting (colors/emojis)
  - Format validation

- **test_backward_compat.py**: Backward compatibility
  - Commands without mode work
  - Commands without format work
  - No breaking changes
  - Legacy argument patterns
  - Graceful degradation

### Integration Tests (`-m integration`)

**Tests with external dependencies** - May require MCP server

- Command execution with real MCP tools
- Multi-command workflows
- State management
- Error propagation

### Performance Tests (`-m performance`)

**Benchmark tests** - Track performance over time

- Mode execution time validation
- Memory usage tracking
- Throughput testing
- Regression detection

### End-to-End Tests (`-m e2e`)

**Full workflow tests** - Slow but comprehensive

- Complete user scenarios
- Multi-step workflows
- Real file system operations
- Full command pipeline

## Coverage Requirements

Target: **90% code coverage**

```bash
# Generate coverage report
pytest --cov=rforge --cov-report=html

# View HTML report
open htmlcov/index.html
```

## Test Markers

Use markers to run specific test categories:

```bash
# Run only unit tests
pytest -m unit

# Run only mode system tests
pytest -m mode_system

# Run only backward compatibility tests
pytest -m backward_compat

# Run only time budget tests
pytest -m time_budget

# Exclude slow tests
pytest -m "not slow"
```

## Writing Tests

### Test Structure (AAA Pattern)

```python
def test_example():
    # Arrange: Set up test data
    arguments = {"mode": "debug"}

    # Act: Execute functionality
    result = parse_mode(arguments)

    # Assert: Verify results
    assert result == "debug"
```

### Test Naming Convention

Format: `test_[what]_[condition]`

```python
def test_mode_parsing_explicit_debug_mode()
def test_time_budget_exceeded_default_mode()
def test_format_handling_invalid_format_raises_error()
```

### Using Fixtures

```python
def test_with_fixture(all_modes, mock_mcp_tool):
    # Fixtures automatically injected
    assert "default" in all_modes
    mock_mcp_tool.call()
```

## Continuous Integration

Tests run automatically on:
- Push to `main` branch
- Pull requests
- Release tags

See `.github/workflows/test.yml` for CI configuration.

## Performance Guarantees

Tests verify these time budgets:

| Mode     | Budget | Requirement |
|----------|--------|-------------|
| default  | 10s    | MUST        |
| debug    | 120s   | SHOULD      |
| optimize | 180s   | SHOULD      |
| release  | 300s   | SHOULD      |

**MUST** = Hard requirement (test fails if exceeded)
**SHOULD** = Soft target (warning if exceeded)

## Test Data

### Fixtures (`tests/fixtures/`)

- Sample command YAML files
- Mock MCP responses
- Test configuration files

### Mocks (`tests/mocks/`)

- Mock MCP tools
- Mock timers
- Mock file systems

## Debugging Tests

### Run with debugging output

```bash
# Show print statements
pytest -s

# Show locals on failure
pytest -l

# Drop into debugger on failure
pytest --pdb
```

### Run specific test

```bash
# By name
pytest tests/unit/test_mode_parsing.py::TestExplicitModeDetection::test_explicit_mode_debug

# By keyword
pytest -k "explicit_mode"
```

## Common Issues

### Tests failing due to missing dependencies

```bash
# Install all test dependencies
pip install -r tests/requirements-test.txt
```

### Coverage too low

```bash
# See what's not covered
pytest --cov=rforge --cov-report=term-missing
```

### Slow tests

```bash
# Skip slow tests
pytest -m "not slow"

# Run tests in parallel
pytest -n auto
```

## Next Steps

After unit tests pass:

1. Implement integration tests
2. Add performance benchmarks
3. Create e2e workflow tests
4. Set up CI/CD pipeline
5. Add mutation testing

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
- [pytest-benchmark documentation](https://pytest-benchmark.readthedocs.io/)

## Test Statistics

Current coverage: **Target 90%**

```
Unit Tests:        40+ tests
Integration Tests: 0 tests (planned)
Performance Tests: 0 tests (planned)
E2E Tests:         0 tests (planned)
Total:             40+ tests
```

---

**Last Updated:** 2024-12-24
**Test Suite Version:** 1.0.0
**Mode System Version:** 2.0.0
