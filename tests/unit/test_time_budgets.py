"""
Unit tests for time budget validation and enforcement.

Tests cover:
- Time budget assignment per mode
- Budget enforcement logic
- Timeout warnings
- Partial result handling
- Budget exceeded scenarios
"""
import pytest
import time
from typing import Dict
from unittest.mock import Mock, patch


class TimeBudgetManager:
    """Manage time budgets for different modes."""

    BUDGETS = {
        "default": {"seconds": 10, "requirement": "MUST"},
        "debug": {"seconds": 120, "requirement": "SHOULD"},
        "optimize": {"seconds": 180, "requirement": "SHOULD"},
        "release": {"seconds": 300, "requirement": "SHOULD"}
    }

    def __init__(self, mode: str):
        """Initialize with mode."""
        if mode not in self.BUDGETS:
            raise ValueError(f"Invalid mode: {mode}")
        self.mode = mode
        self.budget = self.BUDGETS[mode]["seconds"]
        self.requirement = self.BUDGETS[mode]["requirement"]
        self.start_time = None
        self.elapsed = 0

    def start(self):
        """Start the timer."""
        self.start_time = time.time()
        return self

    def elapsed_seconds(self) -> float:
        """Get elapsed time in seconds."""
        if self.start_time is None:
            return 0
        return time.time() - self.start_time

    def is_budget_exceeded(self) -> bool:
        """Check if time budget has been exceeded."""
        return self.elapsed_seconds() > self.budget

    def remaining_seconds(self) -> float:
        """Get remaining time in budget."""
        return max(0, self.budget - self.elapsed_seconds())

    def percent_used(self) -> float:
        """Get percentage of budget used."""
        return (self.elapsed_seconds() / self.budget) * 100

    def should_warn(self, threshold: float = 0.8) -> bool:
        """Check if we should warn user (80% of budget used)."""
        return self.percent_used() >= (threshold * 100)

    def get_status(self) -> Dict:
        """Get current budget status."""
        return {
            "mode": self.mode,
            "budget_seconds": self.budget,
            "elapsed_seconds": self.elapsed_seconds(),
            "remaining_seconds": self.remaining_seconds(),
            "percent_used": self.percent_used(),
            "exceeded": self.is_budget_exceeded(),
            "should_warn": self.should_warn(),
            "requirement": self.requirement
        }


# --- Tests ---

@pytest.mark.unit
@pytest.mark.time_budget
class TestTimeBudgetAssignment:
    """Test time budget assignment for each mode."""

    def test_default_mode_budget_10_seconds(self):
        """Test default mode has 10 second budget."""
        manager = TimeBudgetManager("default")
        assert manager.budget == 10
        assert manager.requirement == "MUST"

    def test_debug_mode_budget_120_seconds(self):
        """Test debug mode has 120 second budget."""
        manager = TimeBudgetManager("debug")
        assert manager.budget == 120
        assert manager.requirement == "SHOULD"

    def test_optimize_mode_budget_180_seconds(self):
        """Test optimize mode has 180 second budget."""
        manager = TimeBudgetManager("optimize")
        assert manager.budget == 180
        assert manager.requirement == "SHOULD"

    def test_release_mode_budget_300_seconds(self):
        """Test release mode has 300 second budget."""
        manager = TimeBudgetManager("release")
        assert manager.budget == 300
        assert manager.requirement == "SHOULD"

    def test_invalid_mode_raises_error(self):
        """Test invalid mode raises ValueError."""
        with pytest.raises(ValueError, match="Invalid mode"):
            TimeBudgetManager("invalid_mode")


@pytest.mark.unit
@pytest.mark.time_budget
class TestTimeBudgetTracking:
    """Test time tracking functionality."""

    def test_start_initializes_timer(self):
        """Test start() initializes the timer."""
        manager = TimeBudgetManager("default")
        assert manager.start_time is None

        manager.start()
        assert manager.start_time is not None

    def test_elapsed_seconds_before_start(self):
        """Test elapsed_seconds() returns 0 before start."""
        manager = TimeBudgetManager("default")
        assert manager.elapsed_seconds() == 0

    @patch('time.time')
    def test_elapsed_seconds_calculation(self, mock_time):
        """Test elapsed_seconds() calculates correctly."""
        manager = TimeBudgetManager("default")

        # Start at t=0
        mock_time.return_value = 0
        manager.start()

        # Check at t=5
        mock_time.return_value = 5
        assert manager.elapsed_seconds() == 5

        # Check at t=8
        mock_time.return_value = 8
        assert manager.elapsed_seconds() == 8

    @patch('time.time')
    def test_remaining_seconds_calculation(self, mock_time):
        """Test remaining_seconds() calculates correctly."""
        manager = TimeBudgetManager("default")  # 10 second budget

        mock_time.return_value = 0
        manager.start()

        # After 3 seconds, 7 should remain
        mock_time.return_value = 3
        assert manager.remaining_seconds() == 7

        # After 10 seconds, 0 should remain
        mock_time.return_value = 10
        assert manager.remaining_seconds() == 0

        # After 12 seconds, still 0 (not negative)
        mock_time.return_value = 12
        assert manager.remaining_seconds() == 0

    @patch('time.time')
    def test_percent_used_calculation(self, mock_time):
        """Test percent_used() calculates correctly."""
        manager = TimeBudgetManager("default")  # 10 second budget

        mock_time.return_value = 0
        manager.start()

        # After 5 seconds, 50% used
        mock_time.return_value = 5
        assert manager.percent_used() == 50.0

        # After 8 seconds, 80% used
        mock_time.return_value = 8
        assert manager.percent_used() == 80.0

        # After 10 seconds, 100% used
        mock_time.return_value = 10
        assert manager.percent_used() == 100.0


@pytest.mark.unit
@pytest.mark.time_budget
class TestBudgetExceeded:
    """Test budget exceeded detection."""

    @patch('time.time')
    def test_budget_not_exceeded_within_limit(self, mock_time):
        """Test is_budget_exceeded() returns False within limit."""
        manager = TimeBudgetManager("default")  # 10 second budget

        mock_time.return_value = 0
        manager.start()

        mock_time.return_value = 5
        assert manager.is_budget_exceeded() is False

        mock_time.return_value = 9.9
        assert manager.is_budget_exceeded() is False

    @patch('time.time')
    def test_budget_exceeded_over_limit(self, mock_time):
        """Test is_budget_exceeded() returns True over limit."""
        manager = TimeBudgetManager("default")  # 10 second budget

        mock_time.return_value = 0
        manager.start()

        mock_time.return_value = 10.1
        assert manager.is_budget_exceeded() is True

        mock_time.return_value = 15
        assert manager.is_budget_exceeded() is True

    @patch('time.time')
    def test_budget_exactly_at_limit(self, mock_time):
        """Test is_budget_exceeded() at exactly the limit."""
        manager = TimeBudgetManager("default")  # 10 second budget

        mock_time.return_value = 0
        manager.start()

        mock_time.return_value = 10.0
        # At exactly 10 seconds, not exceeded (>= would make this True)
        assert manager.is_budget_exceeded() is False


@pytest.mark.unit
@pytest.mark.time_budget
class TestWarningThreshold:
    """Test warning threshold for approaching budget."""

    @patch('time.time')
    def test_should_warn_at_80_percent(self, mock_time):
        """Test should_warn() returns True at 80% threshold."""
        manager = TimeBudgetManager("default")  # 10 second budget

        mock_time.return_value = 0
        manager.start()

        # At 7.9 seconds (79%), no warning
        mock_time.return_value = 7.9
        assert manager.should_warn() is False

        # At 8.0 seconds (80%), warning
        mock_time.return_value = 8.0
        assert manager.should_warn() is True

        # At 9 seconds (90%), warning
        mock_time.return_value = 9
        assert manager.should_warn() is True

    @patch('time.time')
    def test_should_warn_custom_threshold(self, mock_time):
        """Test should_warn() with custom threshold."""
        manager = TimeBudgetManager("default")  # 10 second budget

        mock_time.return_value = 0
        manager.start()

        # Custom threshold: 90%
        mock_time.return_value = 8.9
        assert manager.should_warn(threshold=0.9) is False

        mock_time.return_value = 9.0
        assert manager.should_warn(threshold=0.9) is True


@pytest.mark.unit
@pytest.mark.time_budget
class TestBudgetStatus:
    """Test budget status reporting."""

    @patch('time.time')
    def test_get_status_structure(self, mock_time):
        """Test get_status() returns complete status dict."""
        manager = TimeBudgetManager("default")

        mock_time.return_value = 0
        manager.start()

        mock_time.return_value = 5
        status = manager.get_status()

        # Check all expected keys present
        assert "mode" in status
        assert "budget_seconds" in status
        assert "elapsed_seconds" in status
        assert "remaining_seconds" in status
        assert "percent_used" in status
        assert "exceeded" in status
        assert "should_warn" in status
        assert "requirement" in status

    @patch('time.time')
    def test_get_status_values(self, mock_time):
        """Test get_status() returns correct values."""
        manager = TimeBudgetManager("debug")  # 120 second budget

        mock_time.return_value = 0
        manager.start()

        mock_time.return_value = 60  # 50% through
        status = manager.get_status()

        assert status["mode"] == "debug"
        assert status["budget_seconds"] == 120
        assert status["elapsed_seconds"] == 60
        assert status["remaining_seconds"] == 60
        assert status["percent_used"] == 50.0
        assert status["exceeded"] is False
        assert status["should_warn"] is False
        assert status["requirement"] == "SHOULD"


@pytest.mark.unit
@pytest.mark.time_budget
class TestModeSpecificBudgets:
    """Test mode-specific budget behaviors."""

    def test_default_mode_strict_requirement(self):
        """Test default mode has MUST requirement (strict)."""
        manager = TimeBudgetManager("default")
        assert manager.requirement == "MUST"

    def test_other_modes_should_requirement(self):
        """Test other modes have SHOULD requirement (flexible)."""
        for mode in ["debug", "optimize", "release"]:
            manager = TimeBudgetManager(mode)
            assert manager.requirement == "SHOULD"

    @patch('time.time')
    def test_default_mode_warning_critical(self, mock_time):
        """Test default mode budget exceeded is critical (MUST)."""
        manager = TimeBudgetManager("default")

        mock_time.return_value = 0
        manager.start()

        mock_time.return_value = 11  # Over 10s budget
        status = manager.get_status()

        assert status["exceeded"] is True
        assert status["requirement"] == "MUST"
        # This should be treated as critical failure

    @patch('time.time')
    def test_debug_mode_warning_flexible(self, mock_time):
        """Test debug mode budget exceeded is acceptable (SHOULD)."""
        manager = TimeBudgetManager("debug")

        mock_time.return_value = 0
        manager.start()

        mock_time.return_value = 130  # Over 120s budget
        status = manager.get_status()

        assert status["exceeded"] is True
        assert status["requirement"] == "SHOULD"
        # This should return partial results, not fail


@pytest.mark.unit
@pytest.mark.time_budget
class TestRealTimeExecution:
    """Test with real time execution (integration-like)."""

    @pytest.mark.slow
    def test_real_timer_accuracy(self):
        """Test timer accuracy with real sleep."""
        manager = TimeBudgetManager("default")
        manager.start()

        time.sleep(0.1)  # Sleep 100ms
        elapsed = manager.elapsed_seconds()

        # Allow 10ms tolerance
        assert 0.09 <= elapsed <= 0.11

    @pytest.mark.slow
    def test_warning_triggers_in_real_time(self):
        """Test warning triggers correctly with real time."""
        # Use very short budget for testing
        manager = TimeBudgetManager("default")
        manager.budget = 0.2  # Override to 200ms for test

        manager.start()

        # At 100ms, should not warn (50%)
        time.sleep(0.1)
        assert manager.should_warn() is False

        # At 200ms, should warn (100%)
        time.sleep(0.1)
        assert manager.should_warn() is True
