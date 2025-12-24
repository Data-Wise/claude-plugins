"""
Shared pytest fixtures and configuration for RForge plugin tests.
"""
import json
import pytest
from pathlib import Path
from typing import Dict, Any
from unittest.mock import Mock, MagicMock


# --- Test Data Fixtures ---

@pytest.fixture
def sample_command_request():
    """Sample command request for testing mode parsing."""
    return {
        "command": "rforge:analyze",
        "arguments": {},
        "context": ""
    }


@pytest.fixture
def mode_default():
    """Default mode configuration."""
    return {
        "name": "default",
        "time_budget": 10,
        "description": "Fast, balanced analysis"
    }


@pytest.fixture
def mode_debug():
    """Debug mode configuration."""
    return {
        "name": "debug",
        "time_budget": 120,
        "description": "Deep inspection with detailed traces"
    }


@pytest.fixture
def mode_optimize():
    """Optimize mode configuration."""
    return {
        "name": "optimize",
        "time_budget": 180,
        "description": "Performance analysis and bottleneck detection"
    }


@pytest.fixture
def mode_release():
    """Release mode configuration."""
    return {
        "name": "release",
        "time_budget": 300,
        "description": "Pre-release validation and CRAN checks"
    }


@pytest.fixture
def all_modes(mode_default, mode_debug, mode_optimize, mode_release):
    """All available modes."""
    return {
        "default": mode_default,
        "debug": mode_debug,
        "optimize": mode_optimize,
        "release": mode_release
    }


# --- Command Fixtures ---

@pytest.fixture
def analyze_command_yaml():
    """Sample analyze.md command YAML frontmatter."""
    return """---
name: rforge:analyze
description: Analyze R package ecosystem with mode-specific behavior depth
arguments:
  - name: context
    description: What changed or what to focus on
    required: false
    type: string
  - name: mode
    description: Analysis depth (debug, optimize, release)
    required: false
    type: string
    default: "default"
  - name: format
    description: Output format (json, markdown, terminal)
    required: false
    type: string
    default: "terminal"
tags: ["rforge", "analysis", "ecosystem"]
version: 2.0.0
---"""


@pytest.fixture
def status_command_yaml():
    """Sample status.md command YAML frontmatter."""
    return """---
name: rforge:status
description: Ecosystem-wide status dashboard with mode-specific detail levels
arguments:
  - name: package
    description: Package name (optional, defaults to current or ecosystem)
    required: false
    type: string
  - name: mode
    description: Status detail level (debug, optimize, release)
    required: false
    type: string
    default: "default"
  - name: format
    description: Output format (json, markdown, terminal)
    required: false
    type: string
    default: "terminal"
tags: ["rforge", "status", "ecosystem"]
version: 2.0.0
---"""


# --- Mock Fixtures ---

@pytest.fixture
def mock_mcp_tool():
    """Mock MCP tool for testing without real RForge MCP server."""
    mock = MagicMock()
    mock.call.return_value = {
        "status": "success",
        "data": {"health": 87, "issues": []},
        "execution_time": 2.5
    }
    return mock


@pytest.fixture
def mock_timer():
    """Mock timer for time budget testing."""
    class MockTimer:
        def __init__(self):
            self.start_time = 0
            self.elapsed = 0

        def start(self):
            self.start_time = 0
            return self

        def elapsed_seconds(self):
            return self.elapsed

        def set_elapsed(self, seconds):
            self.elapsed = seconds

    return MockTimer()


# --- File System Fixtures ---

@pytest.fixture
def temp_plugin_dir(tmp_path):
    """Temporary plugin directory structure for testing."""
    plugin_dir = tmp_path / "rforge"

    # Create directory structure
    (plugin_dir / "commands").mkdir(parents=True)
    (plugin_dir / "agents").mkdir(parents=True)
    (plugin_dir / "lib").mkdir(parents=True)
    (plugin_dir / ".claude-plugin").mkdir(parents=True)

    return plugin_dir


@pytest.fixture
def temp_command_file(temp_plugin_dir, analyze_command_yaml):
    """Temporary command file for testing."""
    command_file = temp_plugin_dir / "commands" / "analyze.md"
    command_file.write_text(analyze_command_yaml)
    return command_file


# --- Request Parsing Fixtures ---

@pytest.fixture
def request_with_explicit_mode():
    """Command request with explicit mode parameter."""
    return {
        "command": "rforge:analyze",
        "arguments": {
            "mode": "debug",
            "context": "Fix bootstrap NA handling"
        }
    }


@pytest.fixture
def request_with_implicit_mode_debug():
    """Command request with context implying debug mode."""
    return {
        "command": "rforge:analyze",
        "arguments": {
            "context": "Debugging the bootstrap algorithm issue"
        }
    }


@pytest.fixture
def request_with_implicit_mode_optimize():
    """Command request with context implying optimize mode."""
    return {
        "command": "rforge:analyze",
        "arguments": {
            "context": "Tests are running too slow, need performance analysis"
        }
    }


@pytest.fixture
def request_with_implicit_mode_release():
    """Command request with context implying release mode."""
    return {
        "command": "rforge:analyze",
        "arguments": {
            "context": "Preparing for CRAN submission"
        }
    }


@pytest.fixture
def request_no_mode():
    """Command request with no mode (should default)."""
    return {
        "command": "rforge:analyze",
        "arguments": {
            "context": "Updated bootstrap algorithm"
        }
    }


# --- Format Testing Fixtures ---

@pytest.fixture
def format_terminal():
    """Terminal format specification."""
    return {"format": "terminal", "supports_emoji": True, "supports_color": True}


@pytest.fixture
def format_json():
    """JSON format specification."""
    return {"format": "json", "machine_readable": True}


@pytest.fixture
def format_markdown():
    """Markdown format specification."""
    return {"format": "markdown", "supports_code_blocks": True}


# --- Time Budget Fixtures ---

@pytest.fixture
def time_budgets():
    """All mode time budgets."""
    return {
        "default": 10,    # 10 seconds (MUST)
        "debug": 120,     # 2 minutes (SHOULD)
        "optimize": 180,  # 3 minutes (SHOULD)
        "release": 300    # 5 minutes (SHOULD)
    }


# --- Backward Compatibility Fixtures ---

@pytest.fixture
def legacy_request_no_arguments():
    """Legacy request with no arguments (should work with default mode)."""
    return {
        "command": "rforge:analyze",
        "arguments": {}
    }


@pytest.fixture
def legacy_request_context_only():
    """Legacy request with context only (should work with default mode)."""
    return {
        "command": "rforge:analyze",
        "arguments": {
            "context": "Updated algorithm"
        }
    }


# --- Performance Testing Fixtures ---

@pytest.fixture
def benchmark_config():
    """Configuration for benchmark tests."""
    return {
        "min_rounds": 5,
        "max_time": 2.0,
        "warmup": True
    }


# --- Pytest Configuration ---

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: Unit tests (fast, isolated)"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests (may require external services)"
    )
    config.addinivalue_line(
        "markers", "performance: Performance benchmark tests"
    )
    config.addinivalue_line(
        "markers", "e2e: End-to-end tests (slow, full workflow)"
    )
    config.addinivalue_line(
        "markers", "mode_system: Tests specific to mode system"
    )
    config.addinivalue_line(
        "markers", "backward_compat: Backward compatibility tests"
    )
    config.addinivalue_line(
        "markers", "time_budget: Time budget validation tests"
    )


def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on location."""
    for item in items:
        # Mark tests based on directory
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "performance" in str(item.fspath):
            item.add_marker(pytest.mark.performance)
        elif "e2e" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)
