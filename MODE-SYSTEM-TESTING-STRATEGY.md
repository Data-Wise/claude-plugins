# Mode System Testing Strategy

**Date:** 2024-12-24
**Version:** 2.0.0
**Status:** Ready for Implementation

---

## Overview

Comprehensive testing strategy for the RForge plugin mode system, ensuring quality, performance, and backward compatibility across all deployment phases.

---

## Table of Contents

1. [Testing Philosophy](#testing-philosophy)
2. [Test Categories](#test-categories)
3. [Unit Tests](#unit-tests)
4. [Integration Tests](#integration-tests)
5. [Performance Tests](#performance-tests)
6. [Regression Tests](#regression-tests)
7. [End-to-End Tests](#end-to-end-tests)
8. [Test Automation](#test-automation)
9. [Test Data](#test-data)
10. [Success Criteria](#success-criteria)

---

## Testing Philosophy

### Principles

1. **Fast Feedback**: Default mode tests complete in < 1 minute
2. **Comprehensive Coverage**: All modes tested, all edge cases covered
3. **Realistic Scenarios**: Test with actual R packages, real workloads
4. **Performance First**: Time budgets are hard requirements
5. **Backward Compatible**: Existing workflows must continue working
6. **Automated**: All tests run in CI/CD pipeline

### Test Pyramid

```
    /\          E2E Tests (10%)
   /  \         - Real Claude Code sessions
  /----\        - Full plugin → MCP → R workflow
 /------\
/--------\      Integration Tests (30%)
|        |      - Plugin command parsing
|        |      - MCP server communication
|________|      - Format handling

----------      Unit Tests (60%)
|        |      - Mode detection
|        |      - Parameter validation
|        |      - Time budget enforcement
|________|      - Output formatting
```

---

## Test Categories

### 1. Unit Tests (60% of tests)

**Scope:** Individual functions, mode detection, parameter parsing

**Location:** `tests/unit/`

**Tools:** Python pytest, mock framework

**Target:** 90%+ code coverage

### 2. Integration Tests (30% of tests)

**Scope:** Plugin → MCP server communication, format handling

**Location:** `tests/integration/`

**Tools:** pytest with actual MCP server, test fixtures

**Target:** All mode + format combinations work

### 3. Performance Tests (5% of tests)

**Scope:** Time budget validation, performance regression

**Location:** `tests/performance/`

**Tools:** pytest-benchmark, custom timers

**Target:** All time budgets met

### 4. Regression Tests (3% of tests)

**Scope:** Backward compatibility, existing workflows

**Location:** `tests/regression/`

**Tools:** pytest with recorded expected outputs

**Target:** Zero breaking changes

### 5. End-to-End Tests (2% of tests)

**Scope:** Full user workflows in Claude Code

**Location:** `tests/e2e/`

**Tools:** Manual testing checklist, automated where possible

**Target:** Real-world scenarios work

---

## Unit Tests

### Mode Detection Tests

**File:** `tests/unit/test_mode_detection.py`

```python
import pytest
from rforge.mode_parser import detect_mode

class TestModeDetection:
    """Test mode detection from user input."""

    def test_explicit_mode_debug(self):
        """Explicit --mode debug flag should set debug mode."""
        result = detect_mode(args=["--mode", "debug"])
        assert result.mode == "debug"
        assert result.explicit is True

    def test_explicit_mode_optimize(self):
        """Explicit --mode optimize flag should set optimize mode."""
        result = detect_mode(args=["--mode", "optimize"])
        assert result.mode == "optimize"
        assert result.explicit is True

    def test_explicit_mode_release(self):
        """Explicit --mode release flag should set release mode."""
        result = detect_mode(args=["--mode", "release"])
        assert result.mode == "release"
        assert result.explicit is True

    def test_default_mode_no_args(self):
        """No mode argument should default to 'default' mode."""
        result = detect_mode(args=[])
        assert result.mode == "default"
        assert result.explicit is False

    def test_default_mode_with_context(self):
        """Context without mode hints should use default mode."""
        result = detect_mode(args=[], context="Update algorithm")
        assert result.mode == "default"
        assert result.explicit is False

    def test_context_hint_debug(self):
        """Context with 'debug' hint should suggest debug mode."""
        result = detect_mode(args=[], context="Debug bootstrap issue")
        assert result.suggested_mode == "debug"
        # But actual mode should still be default (no auto-detection)
        assert result.mode == "default"

    def test_invalid_mode_raises_error(self):
        """Invalid mode should raise clear error."""
        with pytest.raises(ValueError, match="Invalid mode"):
            detect_mode(args=["--mode", "invalid"])

    def test_mode_case_insensitive(self):
        """Mode names should be case-insensitive."""
        for mode in ["DEBUG", "Debug", "deBUG"]:
            result = detect_mode(args=["--mode", mode])
            assert result.mode == "debug"
```

### Time Budget Tests

**File:** `tests/unit/test_time_budget.py`

```python
import pytest
from rforge.time_budget import TimeBudget, TimeBudgetExceeded

class TestTimeBudget:
    """Test time budget enforcement."""

    def test_default_mode_budget(self):
        """Default mode should have 10s budget."""
        budget = TimeBudget(mode="default", command="analyze")
        assert budget.target_seconds == 10
        assert budget.hard_limit is True

    def test_debug_mode_budget(self):
        """Debug mode should have 120s budget."""
        budget = TimeBudget(mode="debug", command="analyze")
        assert budget.target_seconds == 120
        assert budget.hard_limit is False

    def test_status_default_budget(self):
        """Status default mode should have 5s budget."""
        budget = TimeBudget(mode="default", command="status")
        assert budget.target_seconds == 5
        assert budget.hard_limit is True

    def test_budget_exceeded_warning(self):
        """Exceeding soft budget should log warning."""
        budget = TimeBudget(mode="debug", command="analyze")

        with budget.track() as timer:
            # Simulate work exceeding budget
            timer.elapsed = 130

        assert timer.exceeded is True
        assert timer.severity == "warning"

    def test_budget_exceeded_error(self):
        """Exceeding hard budget should raise exception."""
        budget = TimeBudget(mode="default", command="analyze")

        with pytest.raises(TimeBudgetExceeded):
            with budget.track() as timer:
                timer.elapsed = 11
                timer.check()
```

### Format Handler Tests

**File:** `tests/unit/test_format_handlers.py`

```python
import pytest
from rforge.formatters import TerminalFormatter, JSONFormatter, MarkdownFormatter

class TestFormatters:
    """Test output format handlers."""

    @pytest.fixture
    def sample_result(self):
        """Sample analysis result."""
        return {
            "health_score": 87,
            "issues": [
                {"severity": "warning", "message": "Missing NEWS.md entry"}
            ],
            "packages": {
                "medfit": {"health": 92, "tests": "187/187 passing"}
            }
        }

    def test_terminal_formatter(self, sample_result):
        """Terminal formatter should produce rich output."""
        formatter = TerminalFormatter()
        output = formatter.format(sample_result, mode="default")

        assert "📊" in output or "STATUS" in output
        assert "87" in output  # Health score
        assert "medfit" in output

    def test_json_formatter(self, sample_result):
        """JSON formatter should produce valid JSON."""
        formatter = JSONFormatter()
        output = formatter.format(sample_result, mode="default")

        import json
        data = json.loads(output)
        assert data["health_score"] == 87
        assert len(data["issues"]) == 1

    def test_markdown_formatter(self, sample_result):
        """Markdown formatter should produce valid markdown."""
        formatter = MarkdownFormatter()
        output = formatter.format(sample_result, mode="default")

        assert "# " in output or "## " in output  # Headers
        assert "medfit" in output
        assert "87" in output
```

### Parameter Validation Tests

**File:** `tests/unit/test_parameter_validation.py`

```python
import pytest
from rforge.validators import validate_command_params

class TestParameterValidation:
    """Test command parameter validation."""

    def test_valid_mode_parameter(self):
        """Valid mode parameter should pass."""
        params = {"mode": "debug", "format": "terminal"}
        errors = validate_command_params("analyze", params)
        assert len(errors) == 0

    def test_invalid_mode_parameter(self):
        """Invalid mode should return error."""
        params = {"mode": "invalid"}
        errors = validate_command_params("analyze", params)
        assert len(errors) == 1
        assert "mode" in errors[0].lower()

    def test_invalid_format_parameter(self):
        """Invalid format should return error."""
        params = {"format": "xml"}
        errors = validate_command_params("analyze", params)
        assert len(errors) == 1
        assert "format" in errors[0].lower()

    def test_mode_format_combination(self):
        """All mode + format combinations should be valid."""
        modes = ["default", "debug", "optimize", "release"]
        formats = ["terminal", "json", "markdown"]

        for mode in modes:
            for format in formats:
                params = {"mode": mode, "format": format}
                errors = validate_command_params("analyze", params)
                assert len(errors) == 0
```

---

## Integration Tests

### Plugin Command Tests

**File:** `tests/integration/test_analyze_command.py`

```python
import pytest
from rforge.commands import AnalyzeCommand
from unittest.mock import Mock

class TestAnalyzeCommand:
    """Test /rforge:analyze command integration."""

    @pytest.fixture
    def mock_mcp_server(self):
        """Mock MCP server for testing."""
        server = Mock()
        server.analyze = Mock(return_value={"status": "success"})
        return server

    def test_analyze_default_mode(self, mock_mcp_server):
        """Default mode should complete quickly."""
        cmd = AnalyzeCommand(mcp_server=mock_mcp_server)

        import time
        start = time.time()
        result = cmd.execute(mode="default")
        duration = time.time() - start

        assert result["status"] == "success"
        assert duration < 10  # Must complete in < 10s

    def test_analyze_debug_mode(self, mock_mcp_server):
        """Debug mode should call detailed analysis."""
        cmd = AnalyzeCommand(mcp_server=mock_mcp_server)
        result = cmd.execute(mode="debug")

        # Verify detailed analysis was requested
        call_args = mock_mcp_server.analyze.call_args
        assert call_args[1]["detail_level"] == "high"
        assert call_args[1]["include_traces"] is True

    def test_analyze_with_format(self, mock_mcp_server):
        """Format parameter should be passed through."""
        cmd = AnalyzeCommand(mcp_server=mock_mcp_server)
        result = cmd.execute(mode="default", format="json")

        assert "format" in result or isinstance(result, str)
```

### MCP Server Communication Tests

**File:** `tests/integration/test_mcp_communication.py`

```python
import pytest
from rforge.mcp_client import MCPClient

class TestMCPCommunication:
    """Test communication with RForge MCP server."""

    @pytest.fixture
    def mcp_client(self):
        """Create MCP client connected to test server."""
        return MCPClient(server_path="~/projects/dev-tools/mcp-servers/statistical-research")

    def test_rforge_detect_tool(self, mcp_client):
        """Test rforge_detect MCP tool."""
        result = mcp_client.call_tool("rforge_detect", {})

        assert "packages" in result
        assert isinstance(result["packages"], list)

    def test_rforge_status_tool(self, mcp_client):
        """Test rforge_status MCP tool."""
        result = mcp_client.call_tool("rforge_status", {
            "mode": "default"
        })

        assert "health_score" in result
        assert 0 <= result["health_score"] <= 100

    def test_mode_parameter_passed(self, mcp_client):
        """Mode parameter should be passed to MCP server."""
        result = mcp_client.call_tool("rforge_status", {
            "mode": "debug"
        })

        # Debug mode should return more detailed results
        assert "detailed_issues" in result or len(result) > 5
```

### Format Output Tests

**File:** `tests/integration/test_format_output.py`

```python
import pytest
import json
from rforge.commands import AnalyzeCommand, StatusCommand

class TestFormatOutput:
    """Test format output generation."""

    def test_terminal_format_analyze(self):
        """Terminal format should produce rich output."""
        cmd = AnalyzeCommand()
        result = cmd.execute(mode="default", format="terminal")

        # Terminal output should have ANSI codes or emojis
        assert isinstance(result, str)
        assert len(result) > 100

    def test_json_format_analyze(self):
        """JSON format should be valid JSON."""
        cmd = AnalyzeCommand()
        result = cmd.execute(mode="default", format="json")

        # Should be parseable as JSON
        data = json.loads(result)
        assert "mode" in data
        assert "results" in data

    def test_markdown_format_status(self):
        """Markdown format should have proper headers."""
        cmd = StatusCommand()
        result = cmd.execute(mode="default", format="markdown")

        assert "# " in result or "## " in result
        assert "```" not in result or result.count("```") % 2 == 0
```

---

## Performance Tests

### Time Budget Benchmarks

**File:** `tests/performance/test_time_budgets.py`

```python
import pytest
import time
from rforge.commands import AnalyzeCommand, StatusCommand

class TestTimeBudgets:
    """Benchmark time budget compliance."""

    @pytest.mark.benchmark
    def test_analyze_default_mode_speed(self, benchmark):
        """Default mode must complete in < 10s."""
        cmd = AnalyzeCommand()

        def run():
            return cmd.execute(mode="default")

        result = benchmark(run)

        # Hard requirement
        assert benchmark.stats['mean'] < 10.0
        assert benchmark.stats['max'] < 10.0

    @pytest.mark.benchmark
    def test_status_default_mode_speed(self, benchmark):
        """Status default mode must complete in < 5s."""
        cmd = StatusCommand()

        def run():
            return cmd.execute(mode="default")

        result = benchmark(run)

        # Hard requirement
        assert benchmark.stats['mean'] < 5.0
        assert benchmark.stats['max'] < 5.0

    @pytest.mark.benchmark
    def test_debug_mode_speed(self, benchmark):
        """Debug mode should complete in < 120s."""
        cmd = AnalyzeCommand()

        def run():
            return cmd.execute(mode="debug")

        result = benchmark(run)

        # Soft target
        if benchmark.stats['mean'] >= 120.0:
            pytest.warn(f"Debug mode took {benchmark.stats['mean']:.1f}s (target: <120s)")
```

### Performance Regression Tests

**File:** `tests/performance/test_regression.py`

```python
import pytest
from pathlib import Path
import json

class TestPerformanceRegression:
    """Detect performance regressions."""

    @pytest.fixture
    def baseline_metrics(self):
        """Load baseline performance metrics."""
        baseline_file = Path(__file__).parent / "baseline_metrics.json"

        if not baseline_file.exists():
            pytest.skip("No baseline metrics available")

        with open(baseline_file) as f:
            return json.load(f)

    def test_no_regression_analyze_default(self, baseline_metrics, benchmark):
        """Analyze default mode should not regress > 10%."""
        from rforge.commands import AnalyzeCommand

        cmd = AnalyzeCommand()
        result = benchmark(lambda: cmd.execute(mode="default"))

        baseline = baseline_metrics.get("analyze_default_mean", 5.0)
        threshold = baseline * 1.10  # Allow 10% regression

        assert benchmark.stats['mean'] < threshold, \
            f"Performance regression: {benchmark.stats['mean']:.2f}s > {threshold:.2f}s"
```

---

## Regression Tests

### Backward Compatibility Tests

**File:** `tests/regression/test_backward_compatibility.py`

```python
import pytest
from rforge.commands import AnalyzeCommand, StatusCommand

class TestBackwardCompatibility:
    """Ensure existing usage patterns continue working."""

    def test_analyze_without_mode(self):
        """Calling /rforge:analyze without mode should work."""
        cmd = AnalyzeCommand()
        result = cmd.execute()  # No mode parameter

        assert result is not None
        assert "error" not in result.lower()

    def test_analyze_with_context_only(self):
        """Calling /rforge:analyze with context should work."""
        cmd = AnalyzeCommand()
        result = cmd.execute(context="Update algorithm")

        assert result is not None
        assert "error" not in result.lower()

    def test_status_without_parameters(self):
        """Calling /rforge:status without parameters should work."""
        cmd = StatusCommand()
        result = cmd.execute()

        assert result is not None
        assert "health" in result.lower() or "status" in result.lower()

    def test_default_behavior_unchanged(self):
        """Default behavior should match v1.0.0."""
        cmd = AnalyzeCommand()

        # Execute without mode (should use default)
        result_no_mode = cmd.execute()
        result_explicit_default = cmd.execute(mode="default")

        # Both should produce similar results
        assert type(result_no_mode) == type(result_explicit_default)
```

### Output Format Regression Tests

**File:** `tests/regression/test_output_format.py`

```python
import pytest
from pathlib import Path

class TestOutputFormatRegression:
    """Ensure output formats remain consistent."""

    @pytest.fixture
    def expected_outputs(self):
        """Load expected output samples."""
        outputs_dir = Path(__file__).parent / "expected_outputs"
        return {
            "analyze_default": (outputs_dir / "analyze_default.txt").read_text(),
            "status_default": (outputs_dir / "status_default.txt").read_text(),
        }

    def test_analyze_output_structure(self, expected_outputs):
        """Analyze output should maintain structure."""
        from rforge.commands import AnalyzeCommand

        cmd = AnalyzeCommand()
        result = cmd.execute(mode="default", format="terminal")

        expected = expected_outputs["analyze_default"]

        # Check key sections are present
        for section in ["Health", "Issues", "Next"]:
            assert section in result, f"Missing section: {section}"
```

---

## End-to-End Tests

### Real Workflow Tests

**File:** `tests/e2e/test_real_workflows.py`

```python
import pytest

class TestRealWorkflows:
    """Test complete user workflows."""

    @pytest.mark.e2e
    def test_morning_routine_workflow(self):
        """Test morning check-in workflow."""
        from rforge.commands import StatusCommand, NextCommand

        # Step 1: Quick status check
        status_cmd = StatusCommand()
        status = status_cmd.execute()

        assert status is not None

        # Step 2: Check what to work on
        next_cmd = NextCommand()
        next_item = next_cmd.execute()

        assert next_item is not None

    @pytest.mark.e2e
    def test_debugging_workflow(self):
        """Test debugging issue workflow."""
        from rforge.commands import AnalyzeCommand, StatusCommand, DepsCommand

        # Deep analysis
        analyze = AnalyzeCommand()
        result = analyze.execute(mode="debug")

        assert "detailed" in str(result).lower() or len(str(result)) > 500

    @pytest.mark.e2e
    def test_release_workflow(self):
        """Test release preparation workflow."""
        from rforge.commands import AnalyzeCommand, StatusCommand

        # Comprehensive validation
        analyze = AnalyzeCommand()
        result = analyze.execute(mode="release")

        # Should include CRAN readiness
        assert "cran" in str(result).lower() or "readiness" in str(result).lower()
```

---

## Test Automation

### CI/CD Test Pipeline

**File:** `.github/workflows/test-mode-system.yml`

```yaml
name: Mode System Tests

on:
  push:
    branches: [main, dev]
    paths:
      - 'rforge/commands/analyze.md'
      - 'rforge/commands/status.md'
      - 'tests/**'
  pull_request:
    branches: [main]

jobs:
  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install pytest pytest-cov

      - name: Run unit tests
        run: |
          pytest tests/unit/ -v --cov=rforge --cov-report=term

      - name: Check coverage
        run: |
          pytest tests/unit/ --cov=rforge --cov-report=xml
          coverage report --fail-under=80

  integration-tests:
    name: Integration Tests
    runs-on: ubuntu-latest
    needs: unit-tests

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install pytest

      - name: Run integration tests
        run: |
          pytest tests/integration/ -v

  performance-tests:
    name: Performance Tests
    runs-on: ubuntu-latest
    needs: integration-tests

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install pytest pytest-benchmark

      - name: Run performance tests
        run: |
          pytest tests/performance/ -v --benchmark-only

      - name: Check time budgets
        run: |
          pytest tests/performance/test_time_budgets.py -v --benchmark-min-rounds=5

  regression-tests:
    name: Regression Tests
    runs-on: ubuntu-latest
    needs: unit-tests

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install pytest

      - name: Run regression tests
        run: |
          pytest tests/regression/ -v
```

### Pre-Commit Tests

**File:** `.pre-commit-config.yaml` (updated)

```yaml
repos:
  - repo: local
    hooks:
      - id: unit-tests
        name: Run unit tests
        entry: pytest tests/unit/ -v
        language: system
        pass_filenames: false
        stages: [commit]

      - id: validate-mode-system
        name: Validate mode system
        entry: python3 scripts/validate-mode-system.py
        language: system
        pass_filenames: false
        stages: [commit]
```

---

## Test Data

### Fixtures

**File:** `tests/fixtures/sample_packages.py`

```python
import pytest
from pathlib import Path

@pytest.fixture
def sample_r_package():
    """Sample R package for testing."""
    return {
        "name": "medfit",
        "version": "2.1.0",
        "description": "Mediation analysis framework",
        "tests": {
            "total": 187,
            "passing": 187,
            "coverage": 94
        },
        "health_score": 92
    }

@pytest.fixture
def ecosystem_status():
    """Sample ecosystem status."""
    return {
        "packages": {
            "medfit": {"health": 92, "issues": []},
            "probmed": {"health": 78, "issues": ["Missing NEWS.md"]},
            "medsim": {"health": 85, "issues": []},
            "mediationverse": {"health": 91, "issues": []}
        },
        "overall_health": 87
    }
```

### Mock MCP Server

**File:** `tests/mocks/mcp_server.py`

```python
from unittest.mock import Mock

class MockMCPServer:
    """Mock MCP server for testing."""

    def __init__(self):
        self.calls = []

    def rforge_analyze(self, mode="default", **kwargs):
        """Mock rforge_analyze tool."""
        self.calls.append(("rforge_analyze", mode, kwargs))

        if mode == "default":
            return self._quick_analysis()
        elif mode == "debug":
            return self._detailed_analysis()
        elif mode == "optimize":
            return self._performance_analysis()
        elif mode == "release":
            return self._release_analysis()

    def _quick_analysis(self):
        """Quick analysis result."""
        return {
            "health_score": 87,
            "critical_issues": ["Missing NEWS.md entry"],
            "duration": 3.2
        }

    def _detailed_analysis(self):
        """Detailed analysis result."""
        return {
            "health_score": 87,
            "all_issues": [
                {"severity": "warning", "file": "probmed", "message": "Missing NEWS.md"},
                {"severity": "info", "file": "medfit", "message": "Documentation at 96%"}
            ],
            "dependency_tree": {"medfit": ["probmed", "medsim"]},
            "duration": 45.3
        }
```

---

## Success Criteria

### Unit Tests

- ✅ 90%+ code coverage
- ✅ All mode detection cases covered
- ✅ All format handlers tested
- ✅ Time budget enforcement validated

### Integration Tests

- ✅ All mode + format combinations work
- ✅ MCP server communication verified
- ✅ Command parsing validated
- ✅ Error handling tested

### Performance Tests

- ✅ Default mode: MUST complete < 10s (analyze), < 5s (status)
- ✅ Debug mode: SHOULD complete < 120s
- ✅ Optimize mode: SHOULD complete < 180s
- ✅ Release mode: SHOULD complete < 300s
- ✅ No performance regression > 10%

### Regression Tests

- ✅ Existing commands work without changes
- ✅ Default behavior unchanged
- ✅ Output format consistent
- ✅ No breaking changes

### End-to-End Tests

- ✅ Morning routine workflow works
- ✅ Debugging workflow works
- ✅ Release workflow works
- ✅ Real R packages tested

---

## Test Execution

### Local Development

```bash
# Run all tests
pytest tests/ -v

# Run specific test category
pytest tests/unit/ -v
pytest tests/integration/ -v
pytest tests/performance/ -v

# Run with coverage
pytest tests/unit/ --cov=rforge --cov-report=html

# Run performance benchmarks
pytest tests/performance/ --benchmark-only
```

### CI/CD Pipeline

```bash
# Triggered automatically on:
# - Push to main/dev
# - Pull requests
# - Manual workflow_dispatch

# View results:
# https://github.com/Data-Wise/claude-plugins/actions
```

### Pre-Release Testing

```bash
# Full test suite before release
./scripts/test-full-suite.sh

# Generate test report
pytest tests/ --html=report.html --self-contained-html
```

---

## Next Steps

1. **Create test directory structure** (Day 2)
2. **Implement unit tests** (Day 2-3)
3. **Add integration tests** (Day 3)
4. **Set up performance benchmarks** (Day 4)
5. **Validate with real packages** (Day 4-5)
6. **Update CI/CD pipeline** (Day 5)

---

**Status:** Testing strategy defined, ready for implementation

**Next Action:** Create test directory structure and implement first unit tests

---
