"""
Unit tests for output format handling.

Tests cover:
- Format parameter parsing
- Terminal format with colors/emojis
- JSON format (machine-readable)
- Markdown format (documentation)
- Format validation
- Invalid format handling
"""
import pytest
import json
import sys
from pathlib import Path
from typing import Dict, Any

# Add rforge/lib to path so we can import formatters
rforge_lib = Path(__file__).parent.parent.parent / "rforge" / "lib"
sys.path.insert(0, str(rforge_lib))

from formatters import (
    format_json,
    format_terminal,
    format_markdown,
    get_formatter,
    validate_json_output,
    FORMATTERS
)


class FormatHandler:
    """Handle output formatting for different formats (test adapter)."""

    VALID_FORMATS = list(FORMATTERS.keys())

    @classmethod
    def parse_format(cls, arguments: Dict[str, Any]) -> str:
        """
        Parse format from command arguments.

        Defaults to 'terminal' if not specified.
        """
        format_arg = arguments.get("format", "terminal").lower()

        if format_arg not in cls.VALID_FORMATS:
            raise ValueError(f"Invalid format: {format_arg}. Valid formats: {cls.VALID_FORMATS}")

        return format_arg

    @classmethod
    def validate_format(cls, format_name: str) -> bool:
        """Check if format is valid."""
        return format_name.lower() in cls.VALID_FORMATS

    @classmethod
    def format_output(cls, data: Dict[str, Any], format_type: str, mode: str = "default") -> str:
        """Format data according to format type."""
        formatter = get_formatter(format_type)
        return formatter(data, mode=mode)


# --- Tests ---

@pytest.mark.unit
@pytest.mark.mode_system
class TestFormatParsing:
    """Test format parameter parsing."""

    def test_default_format_terminal(self):
        """Test missing format defaults to 'terminal'."""
        arguments = {}
        format_type = FormatHandler.parse_format(arguments)
        assert format_type == "terminal"

    def test_explicit_format_json(self):
        """Test explicit JSON format."""
        arguments = {"format": "json"}
        format_type = FormatHandler.parse_format(arguments)
        assert format_type == "json"

    def test_explicit_format_markdown(self):
        """Test explicit markdown format."""
        arguments = {"format": "markdown"}
        format_type = FormatHandler.parse_format(arguments)
        assert format_type == "markdown"

    def test_explicit_format_terminal(self):
        """Test explicit terminal format."""
        arguments = {"format": "terminal"}
        format_type = FormatHandler.parse_format(arguments)
        assert format_type == "terminal"

    def test_format_case_insensitive(self):
        """Test format parsing is case-insensitive."""
        test_cases = [
            {"format": "JSON"},
            {"format": "Json"},
            {"format": "MARKDOWN"},
            {"format": "Markdown"},
            {"format": "TERMINAL"},
        ]
        expected = ["json", "json", "markdown", "markdown", "terminal"]

        for arguments, expected_format in zip(test_cases, expected):
            format_type = FormatHandler.parse_format(arguments)
            assert format_type == expected_format

    def test_invalid_format_raises_error(self):
        """Test invalid format raises ValueError."""
        arguments = {"format": "invalid_format"}
        with pytest.raises(ValueError, match="Invalid format"):
            FormatHandler.parse_format(arguments)


@pytest.mark.unit
@pytest.mark.mode_system
class TestFormatValidation:
    """Test format validation."""

    def test_validate_all_valid_formats(self):
        """Test all valid formats return True."""
        for format_name in ["terminal", "json", "markdown"]:
            assert FormatHandler.validate_format(format_name) is True

    def test_validate_invalid_format(self):
        """Test invalid format returns False."""
        assert FormatHandler.validate_format("invalid") is False
        assert FormatHandler.validate_format("") is False

    def test_validate_format_case_insensitive(self):
        """Test validation is case-insensitive."""
        assert FormatHandler.validate_format("JSON") is True
        assert FormatHandler.validate_format("Markdown") is True


@pytest.mark.unit
@pytest.mark.mode_system
class TestJSONFormatting:
    """Test JSON output formatting."""

    def test_json_format_basic_structure(self):
        """Test JSON format produces valid JSON with metadata."""
        data = {
            "title": "Test Result",
            "status": "success",
            "data": {"health": 87, "issues": 2}
        }

        output = FormatHandler.format_output(data, "json", mode="debug")

        # Should be valid JSON
        parsed = json.loads(output)

        # Check structure includes metadata
        assert "timestamp" in parsed
        assert "mode" in parsed
        assert "results" in parsed

        # Check mode is correct
        assert parsed["mode"] == "debug"

        # Check results contain original data
        assert parsed["results"]["title"] == "Test Result"
        assert parsed["results"]["status"] == "success"
        assert parsed["results"]["data"]["health"] == 87

    def test_json_format_indented(self):
        """Test JSON output is indented (human-readable)."""
        data = {"key": "value"}
        output = FormatHandler.format_output(data, "json")

        # Indented JSON has newlines
        assert "\n" in output
        assert "  " in output  # 2-space indent

    def test_json_format_nested_data(self):
        """Test JSON format handles nested structures."""
        data = {
            "title": "Analysis",
            "data": {
                "packages": {
                    "medfit": {"health": 92},
                    "probmed": {"health": 78}
                }
            }
        }

        output = FormatHandler.format_output(data, "json")
        parsed = json.loads(output)

        # Check nested data is preserved in results
        assert parsed["results"]["data"]["packages"]["medfit"]["health"] == 92
        assert parsed["results"]["data"]["packages"]["probmed"]["health"] == 78

    def test_json_format_validates(self):
        """Test JSON output validates as valid JSON."""
        data = {"status": "pass", "tests": 15}
        output = FormatHandler.format_output(data, "json")

        # Should validate
        assert validate_json_output(output) is True

    def test_json_format_includes_timestamp(self):
        """Test JSON includes timestamp."""
        data = {"status": "pass"}
        output = FormatHandler.format_output(data, "json")
        parsed = json.loads(output)

        assert "timestamp" in parsed
        assert len(parsed["timestamp"]) > 0  # Non-empty timestamp


@pytest.mark.unit
@pytest.mark.mode_system
class TestMarkdownFormatting:
    """Test Markdown output formatting."""

    def test_markdown_format_has_title(self):
        """Test Markdown output includes title header."""
        data = {"title": "Test Result", "status": "success"}
        output = FormatHandler.format_output(data, "markdown")

        assert "# Test Result" in output

    def test_markdown_format_has_status(self):
        """Test Markdown output includes status."""
        data = {"title": "Test", "status": "success"}
        output = FormatHandler.format_output(data, "markdown")

        assert "**Status:** success" in output

    def test_markdown_format_with_data(self):
        """Test Markdown output includes data as code block."""
        data = {
            "title": "Analysis",
            "status": "success",
            "data": {"health": 87}
        }
        output = FormatHandler.format_output(data, "markdown")

        assert "## Data" in output
        assert "```json" in output
        assert "```" in output
        assert '"health": 87' in output

    def test_markdown_format_structure(self):
        """Test Markdown output has proper structure."""
        data = {"title": "Test", "status": "success", "data": {}}
        output = FormatHandler.format_output(data, "markdown")

        lines = output.split("\n")
        assert lines[0].startswith("# ")  # Title
        assert any("**Status:**" in line for line in lines)  # Status


@pytest.mark.unit
@pytest.mark.mode_system
class TestTerminalFormatting:
    """Test terminal output formatting."""

    def test_terminal_format_has_emoji(self):
        """Test terminal output includes emojis."""
        data = {"title": "Test Result", "status": "success"}
        output = FormatHandler.format_output(data, "terminal")

        assert "✅" in output or "❌" in output

    def test_terminal_format_success_emoji(self):
        """Test terminal shows success emoji for success status."""
        data = {"title": "Test", "status": "success"}
        output = FormatHandler.format_output(data, "terminal")

        assert "✅" in output

    def test_terminal_format_failure_emoji(self):
        """Test terminal shows failure emoji for non-success status."""
        data = {"title": "Test", "status": "error"}
        output = FormatHandler.format_output(data, "terminal")

        assert "❌" in output

    def test_terminal_format_with_data(self):
        """Test terminal output includes data as bullet list."""
        data = {
            "title": "Analysis",
            "status": "success",
            "data": {"health": 87, "issues": 2}
        }
        output = FormatHandler.format_output(data, "terminal")

        # Check for bullet points and data (may have ANSI color codes)
        assert "• health:" in output
        assert "87" in output
        assert "• issues:" in output
        assert "2" in output

    def test_terminal_format_readable(self):
        """Test terminal output is human-readable."""
        data = {
            "title": "Package Status",
            "status": "success",
            "data": {"package": "medfit", "version": "2.1.0"}
        }
        output = FormatHandler.format_output(data, "terminal")

        # Should be readable (has spacing, bullets)
        assert "\n" in output
        assert "•" in output


@pytest.mark.unit
@pytest.mark.mode_system
class TestFormatConsistency:
    """Test format consistency across different data."""

    def test_same_data_different_formats(self):
        """Test same data produces valid output in all formats."""
        data = {
            "title": "Test",
            "status": "success",
            "data": {"key": "value"}
        }

        json_output = FormatHandler.format_output(data, "json")
        markdown_output = FormatHandler.format_output(data, "markdown")
        terminal_output = FormatHandler.format_output(data, "terminal")

        # All should be non-empty strings
        assert len(json_output) > 0
        assert len(markdown_output) > 0
        assert len(terminal_output) > 0

        # JSON should be valid
        json.loads(json_output)

        # All should contain the title somehow
        assert "Test" in json_output
        assert "Test" in markdown_output
        assert "Test" in terminal_output

    def test_empty_data_all_formats(self):
        """Test empty data handled in all formats."""
        data = {"title": "Empty", "status": "success"}

        json_output = FormatHandler.format_output(data, "json")
        markdown_output = FormatHandler.format_output(data, "markdown")
        terminal_output = FormatHandler.format_output(data, "terminal")

        # All should still work
        assert len(json_output) > 0
        assert len(markdown_output) > 0
        assert len(terminal_output) > 0


@pytest.mark.unit
@pytest.mark.mode_system
class TestFormatModeIntegration:
    """Test format works with different modes."""

    def test_format_independent_of_mode(self):
        """Test format parameter works with any mode."""
        # Format should be independent of mode
        test_cases = [
            {"mode": "default", "format": "json"},
            {"mode": "debug", "format": "markdown"},
            {"mode": "optimize", "format": "terminal"},
            {"mode": "release", "format": "json"},
        ]

        for arguments in test_cases:
            format_type = FormatHandler.parse_format(arguments)
            assert format_type in FormatHandler.VALID_FORMATS

    def test_default_format_with_explicit_mode(self):
        """Test default format when mode is explicit."""
        arguments = {"mode": "debug"}  # mode but no format
        format_type = FormatHandler.parse_format(arguments)
        assert format_type == "terminal"  # Should default to terminal
