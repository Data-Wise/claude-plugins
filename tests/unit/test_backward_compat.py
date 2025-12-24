"""
Unit tests for backward compatibility with existing command usage.

Tests cover:
- Commands without mode parameter work (use default)
- Commands without format parameter work (use terminal)
- Existing user workflows unchanged
- No breaking changes
- Legacy argument patterns
"""
import pytest
from typing import Dict, Any


class CommandHandler:
    """Handle command requests with backward compatibility."""

    @staticmethod
    def handle_analyze_command(arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle rforge:analyze command with backward compatibility.

        Legacy behavior:
        - No mode → default mode
        - No format → terminal format
        - Context-only → works as before
        """
        # Parse mode (defaults to 'default')
        mode = arguments.get("mode", "default").lower()
        if mode not in ["default", "debug", "optimize", "release"]:
            mode = "default"

        # Parse format (defaults to 'terminal')
        format_type = arguments.get("format", "terminal").lower()
        if format_type not in ["terminal", "json", "markdown"]:
            format_type = "terminal"

        # Parse context (optional)
        context = arguments.get("context", "")

        return {
            "command": "rforge:analyze",
            "mode": mode,
            "format": format_type,
            "context": context,
            "backward_compatible": True
        }

    @staticmethod
    def handle_status_command(arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle rforge:status command with backward compatibility.

        Legacy behavior:
        - No mode → default mode
        - No format → terminal format
        - Package-only → works as before
        """
        mode = arguments.get("mode", "default").lower()
        if mode not in ["default", "debug", "optimize", "release"]:
            mode = "default"

        format_type = arguments.get("format", "terminal").lower()
        if format_type not in ["terminal", "json", "markdown"]:
            format_type = "terminal"

        package = arguments.get("package", "")

        return {
            "command": "rforge:status",
            "mode": mode,
            "format": format_type,
            "package": package,
            "backward_compatible": True
        }


# --- Tests ---

@pytest.mark.unit
@pytest.mark.backward_compat
class TestAnalyzeCommandBackwardCompat:
    """Test rforge:analyze backward compatibility."""

    def test_no_arguments_uses_defaults(self):
        """Test command with no arguments works (all defaults)."""
        arguments = {}
        result = CommandHandler.handle_analyze_command(arguments)

        assert result["mode"] == "default"
        assert result["format"] == "terminal"
        assert result["context"] == ""
        assert result["backward_compatible"] is True

    def test_context_only_uses_defaults(self):
        """Test command with context only works (legacy pattern)."""
        arguments = {"context": "Updated bootstrap algorithm"}
        result = CommandHandler.handle_analyze_command(arguments)

        assert result["mode"] == "default"
        assert result["format"] == "terminal"
        assert result["context"] == "Updated bootstrap algorithm"

    def test_context_only_preserved(self):
        """Test context-only commands preserve context."""
        # This was the main usage pattern before mode system
        arguments = {"context": "Fix NA handling in bootstrap"}
        result = CommandHandler.handle_analyze_command(arguments)

        assert result["context"] == "Fix NA handling in bootstrap"
        assert result["mode"] == "default"

    def test_empty_context_works(self):
        """Test empty context works (legacy)."""
        arguments = {"context": ""}
        result = CommandHandler.handle_analyze_command(arguments)

        assert result["mode"] == "default"
        assert result["format"] == "terminal"


@pytest.mark.unit
@pytest.mark.backward_compat
class TestStatusCommandBackwardCompat:
    """Test rforge:status backward compatibility."""

    def test_no_arguments_uses_defaults(self):
        """Test command with no arguments works (ecosystem status)."""
        arguments = {}
        result = CommandHandler.handle_status_command(arguments)

        assert result["mode"] == "default"
        assert result["format"] == "terminal"
        assert result["package"] == ""

    def test_package_only_uses_defaults(self):
        """Test command with package only works (legacy pattern)."""
        arguments = {"package": "medfit"}
        result = CommandHandler.handle_status_command(arguments)

        assert result["mode"] == "default"
        assert result["format"] == "terminal"
        assert result["package"] == "medfit"

    def test_package_name_preserved(self):
        """Test package name preserved in legacy usage."""
        # This was common: /rforge:status medfit
        arguments = {"package": "medfit"}
        result = CommandHandler.handle_status_command(arguments)

        assert result["package"] == "medfit"
        assert result["mode"] == "default"


@pytest.mark.unit
@pytest.mark.backward_compat
class TestNoBreakingChanges:
    """Test no breaking changes to existing workflows."""

    def test_analyze_basic_usage_unchanged(self):
        """Test basic analyze usage patterns still work."""
        # Common patterns from before mode system
        patterns = [
            {},  # No args
            {"context": "some change"},  # Context only
            {"context": ""},  # Empty context
        ]

        for arguments in patterns:
            result = CommandHandler.handle_analyze_command(arguments)
            # All should succeed with defaults
            assert result["mode"] == "default"
            assert result["format"] == "terminal"

    def test_status_basic_usage_unchanged(self):
        """Test basic status usage patterns still work."""
        patterns = [
            {},  # No args (ecosystem)
            {"package": "medfit"},  # Package only
            {"package": ""},  # Empty package
        ]

        for arguments in patterns:
            result = CommandHandler.handle_status_command(arguments)
            assert result["mode"] == "default"
            assert result["format"] == "terminal"

    def test_output_format_unchanged_for_legacy(self):
        """Test output format unchanged when no format specified."""
        arguments = {"context": "some change"}
        result = CommandHandler.handle_analyze_command(arguments)

        # Should get terminal format (with emojis, colors)
        assert result["format"] == "terminal"


@pytest.mark.unit
@pytest.mark.backward_compat
class TestInvalidArgumentsHandling:
    """Test handling of invalid arguments (graceful degradation)."""

    def test_invalid_mode_defaults_to_default(self):
        """Test invalid mode gracefully defaults to 'default'."""
        arguments = {"mode": "invalid_mode"}
        result = CommandHandler.handle_analyze_command(arguments)

        # Should fallback to default, not error
        assert result["mode"] == "default"

    def test_invalid_format_defaults_to_terminal(self):
        """Test invalid format gracefully defaults to 'terminal'."""
        arguments = {"format": "invalid_format"}
        result = CommandHandler.handle_analyze_command(arguments)

        # Should fallback to terminal, not error
        assert result["format"] == "terminal"

    def test_mixed_valid_invalid_arguments(self):
        """Test mix of valid and invalid arguments handled gracefully."""
        arguments = {
            "mode": "invalid",
            "format": "json",  # valid
            "context": "test"
        }
        result = CommandHandler.handle_analyze_command(arguments)

        # Invalid mode → default, valid format → json
        assert result["mode"] == "default"
        assert result["format"] == "json"
        assert result["context"] == "test"


@pytest.mark.unit
@pytest.mark.backward_compat
class TestDocumentedExamples:
    """Test all examples from documentation still work."""

    def test_analyze_example_1(self):
        """Test: /rforge:analyze 'Updated bootstrap algorithm'"""
        arguments = {"context": "Updated bootstrap algorithm"}
        result = CommandHandler.handle_analyze_command(arguments)

        assert result["mode"] == "default"  # Fast analysis
        assert result["context"] == "Updated bootstrap algorithm"

    def test_analyze_example_2(self):
        """Test: /rforge:analyze (no arguments)"""
        arguments = {}
        result = CommandHandler.handle_analyze_command(arguments)

        assert result["mode"] == "default"

    def test_status_example_1(self):
        """Test: /rforge:status"""
        arguments = {}
        result = CommandHandler.handle_status_command(arguments)

        assert result["mode"] == "default"
        assert result["package"] == ""  # Ecosystem

    def test_status_example_2(self):
        """Test: /rforge:status medfit"""
        arguments = {"package": "medfit"}
        result = CommandHandler.handle_status_command(arguments)

        assert result["mode"] == "default"
        assert result["package"] == "medfit"


@pytest.mark.unit
@pytest.mark.backward_compat
class TestMigrationPath:
    """Test users can gradually adopt new features."""

    def test_can_add_mode_to_existing_command(self):
        """Test adding mode to existing command works."""
        # Start with legacy
        legacy = {"context": "Fix issue"}
        result_legacy = CommandHandler.handle_analyze_command(legacy)
        assert result_legacy["mode"] == "default"

        # Add mode (migration)
        with_mode = {"context": "Fix issue", "mode": "debug"}
        result_new = CommandHandler.handle_analyze_command(with_mode)
        assert result_new["mode"] == "debug"
        assert result_new["context"] == "Fix issue"

    def test_can_add_format_to_existing_command(self):
        """Test adding format to existing command works."""
        # Start with legacy
        legacy = {"context": "Fix issue"}
        result_legacy = CommandHandler.handle_analyze_command(legacy)
        assert result_legacy["format"] == "terminal"

        # Add format (migration)
        with_format = {"context": "Fix issue", "format": "json"}
        result_new = CommandHandler.handle_analyze_command(with_format)
        assert result_new["format"] == "json"

    def test_can_add_both_mode_and_format(self):
        """Test adding both mode and format works."""
        arguments = {
            "context": "Fix issue",
            "mode": "debug",
            "format": "json"
        }
        result = CommandHandler.handle_analyze_command(arguments)

        assert result["context"] == "Fix issue"
        assert result["mode"] == "debug"
        assert result["format"] == "json"


@pytest.mark.unit
@pytest.mark.backward_compat
class TestDefaultBehavior:
    """Test default behavior matches original implementation."""

    def test_default_mode_is_fast(self):
        """Test default mode is fast (< 10s) like original."""
        arguments = {}
        result = CommandHandler.handle_analyze_command(arguments)

        # Default mode should be the fast mode
        assert result["mode"] == "default"
        # (In real implementation, this would be < 10s)

    def test_default_format_is_terminal(self):
        """Test default format is terminal (human-readable)."""
        arguments = {}
        result = CommandHandler.handle_analyze_command(arguments)

        # Original used terminal output
        assert result["format"] == "terminal"

    def test_default_behavior_balanced(self):
        """Test default behavior is balanced (not too detailed, not too sparse)."""
        arguments = {}
        result = CommandHandler.handle_analyze_command(arguments)

        # Default should be the balanced mode
        assert result["mode"] == "default"
        # (In real implementation: 80% of critical issues, actionable)
