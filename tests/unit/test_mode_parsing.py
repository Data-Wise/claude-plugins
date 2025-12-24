"""
Unit tests for mode parsing and detection in RForge plugin commands.

Tests cover:
- Explicit mode parameter parsing
- Implicit mode detection from context
- Default mode fallback
- Invalid mode handling
- Case-insensitive mode names
"""
import pytest
from typing import Dict, Any


# Mock mode parser (represents the logic from commands)
class ModeParser:
    """Parse mode from command request."""

    VALID_MODES = ["default", "debug", "optimize", "release"]

    # Keywords that trigger specific modes
    DEBUG_KEYWORDS = ["debug", "debugging", "investigate", "trace", "detailed"]
    OPTIMIZE_KEYWORDS = ["optimize", "performance", "slow", "speed", "bottleneck"]
    RELEASE_KEYWORDS = ["release", "cran", "submit", "publish", "ready"]

    @classmethod
    def parse_mode(cls, arguments: Dict[str, Any]) -> str:
        """
        Parse mode from command arguments.

        Priority:
        1. Explicit --mode argument
        2. Implicit detection from context
        3. Default to "default"
        """
        # Check explicit mode argument
        if "mode" in arguments:
            mode = arguments["mode"].lower()
            if mode in cls.VALID_MODES:
                return mode
            else:
                raise ValueError(f"Invalid mode: {mode}. Valid modes: {cls.VALID_MODES}")

        # Check implicit mode from context (handle None gracefully)
        context = arguments.get("context", "") or ""
        context = context.lower()
        if any(keyword in context for keyword in cls.DEBUG_KEYWORDS):
            return "debug"
        if any(keyword in context for keyword in cls.OPTIMIZE_KEYWORDS):
            return "optimize"
        if any(keyword in context for keyword in cls.RELEASE_KEYWORDS):
            return "release"

        # Default mode
        return "default"

    @classmethod
    def validate_mode(cls, mode: str) -> bool:
        """Check if mode is valid."""
        return mode.lower() in cls.VALID_MODES


# --- Tests ---

@pytest.mark.unit
@pytest.mark.mode_system
class TestExplicitModeDetection:
    """Test explicit mode parameter parsing."""

    def test_explicit_mode_debug(self):
        """Test explicit debug mode is parsed correctly."""
        arguments = {"mode": "debug", "context": "Some context"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "debug"

    def test_explicit_mode_optimize(self):
        """Test explicit optimize mode is parsed correctly."""
        arguments = {"mode": "optimize"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "optimize"

    def test_explicit_mode_release(self):
        """Test explicit release mode is parsed correctly."""
        arguments = {"mode": "release"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "release"

    def test_explicit_mode_default(self):
        """Test explicit default mode is parsed correctly."""
        arguments = {"mode": "default"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "default"

    def test_explicit_mode_case_insensitive(self):
        """Test mode parsing is case-insensitive."""
        test_cases = [
            {"mode": "DEBUG"},
            {"mode": "Debug"},
            {"mode": "DeBuG"},
        ]
        for arguments in test_cases:
            mode = ModeParser.parse_mode(arguments)
            assert mode == "debug", f"Failed for: {arguments['mode']}"

    def test_invalid_mode_raises_error(self):
        """Test invalid mode raises ValueError."""
        arguments = {"mode": "invalid_mode"}
        with pytest.raises(ValueError, match="Invalid mode"):
            ModeParser.parse_mode(arguments)

    def test_explicit_mode_overrides_context(self):
        """Test explicit mode takes priority over context keywords."""
        # Context suggests debug, but explicit mode is optimize
        arguments = {"mode": "optimize", "context": "debugging the issue"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "optimize"


@pytest.mark.unit
@pytest.mark.mode_system
class TestImplicitModeDetection:
    """Test implicit mode detection from context."""

    def test_implicit_debug_from_debug_keyword(self):
        """Test 'debug' keyword triggers debug mode."""
        arguments = {"context": "debug the bootstrap algorithm"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "debug"

    def test_implicit_debug_from_debugging_keyword(self):
        """Test 'debugging' keyword triggers debug mode."""
        arguments = {"context": "debugging NA handling issue"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "debug"

    def test_implicit_debug_from_investigate_keyword(self):
        """Test 'investigate' keyword triggers debug mode."""
        arguments = {"context": "investigate test failures"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "debug"

    def test_implicit_optimize_from_performance_keyword(self):
        """Test 'performance' keyword triggers optimize mode."""
        arguments = {"context": "performance analysis needed"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "optimize"

    def test_implicit_optimize_from_slow_keyword(self):
        """Test 'slow' keyword triggers optimize mode."""
        arguments = {"context": "tests are running too slow"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "optimize"

    def test_implicit_release_from_cran_keyword(self):
        """Test 'CRAN' keyword triggers release mode."""
        arguments = {"context": "preparing for CRAN submission"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "release"

    def test_implicit_release_from_release_keyword(self):
        """Test 'release' keyword triggers release mode."""
        arguments = {"context": "release validation needed"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "release"

    def test_implicit_detection_case_insensitive(self):
        """Test implicit detection works with different cases."""
        test_cases = [
            {"context": "DEBUG the issue"},
            {"context": "Debug this problem"},
            {"context": "OPTIMIZE performance"},
            {"context": "CRAN submission"},
        ]
        expected = ["debug", "debug", "optimize", "release"]

        for arguments, expected_mode in zip(test_cases, expected):
            mode = ModeParser.parse_mode(arguments)
            assert mode == expected_mode


@pytest.mark.unit
@pytest.mark.mode_system
class TestDefaultModeDetection:
    """Test default mode fallback."""

    def test_no_mode_no_context_uses_default(self):
        """Test missing mode and context defaults to 'default'."""
        arguments = {}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "default"

    def test_no_mode_generic_context_uses_default(self):
        """Test generic context (no keywords) defaults to 'default'."""
        arguments = {"context": "Updated bootstrap algorithm"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "default"

    def test_empty_context_uses_default(self):
        """Test empty context defaults to 'default'."""
        arguments = {"context": ""}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "default"


@pytest.mark.unit
@pytest.mark.mode_system
class TestModeValidation:
    """Test mode validation helper."""

    def test_validate_all_valid_modes(self):
        """Test all valid modes return True."""
        for mode in ["default", "debug", "optimize", "release"]:
            assert ModeParser.validate_mode(mode) is True

    def test_validate_invalid_mode(self):
        """Test invalid mode returns False."""
        assert ModeParser.validate_mode("invalid") is False
        assert ModeParser.validate_mode("") is False

    def test_validate_mode_case_insensitive(self):
        """Test validation is case-insensitive."""
        assert ModeParser.validate_mode("DEBUG") is True
        assert ModeParser.validate_mode("Debug") is True


@pytest.mark.unit
@pytest.mark.mode_system
class TestEdgeCases:
    """Test edge cases in mode parsing."""

    def test_multiple_keywords_first_match_wins(self):
        """Test when context has multiple keywords, first match wins."""
        # Has both "debug" and "optimize" - debug comes first in check order
        arguments = {"context": "debug performance issues"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "debug"

    def test_partial_keyword_match(self):
        """Test partial keyword matches work."""
        # "debugging" contains "debug"
        arguments = {"context": "currently debugging"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "debug"

    def test_mode_in_middle_of_sentence(self):
        """Test keyword detection works mid-sentence."""
        arguments = {"context": "We need to investigate the root cause"}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "debug"

    def test_none_arguments_defaults(self):
        """Test None context handled gracefully."""
        arguments = {"context": None}
        mode = ModeParser.parse_mode(arguments)
        assert mode == "default"
