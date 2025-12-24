#!/bin/bash
# Run RForge plugin tests

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🧪 RForge Plugin Test Suite"
echo "============================"
echo ""

# Check if pytest is installed
if ! command -v pytest >/dev/null 2>&1; then
    echo "❌ pytest not found. Installing test dependencies..."
    pip install -r "$PROJECT_ROOT/tests/requirements-test.txt"
fi

# Default: run all unit tests
TEST_TYPE="${1:-unit}"

case "$TEST_TYPE" in
    unit)
        echo "Running unit tests..."
        pytest "$PROJECT_ROOT/tests/unit" -v --tb=short
        ;;

    integration)
        echo "Running integration tests..."
        pytest "$PROJECT_ROOT/tests/integration" -v --tb=short
        ;;

    performance)
        echo "Running performance tests..."
        pytest "$PROJECT_ROOT/tests/performance" -v --benchmark-only
        ;;

    e2e)
        echo "Running end-to-end tests..."
        pytest "$PROJECT_ROOT/tests/e2e" -v --tb=short
        ;;

    all)
        echo "Running all tests..."
        pytest "$PROJECT_ROOT/tests" -v --tb=short
        ;;

    coverage)
        echo "Running tests with coverage..."
        pytest "$PROJECT_ROOT/tests" -v --cov=rforge --cov-report=term-missing --cov-report=html
        echo ""
        echo "✅ Coverage report generated: htmlcov/index.html"
        ;;

    quick)
        echo "Running quick tests (no slow tests)..."
        pytest "$PROJECT_ROOT/tests" -v -m "not slow" --tb=short
        ;;

    *)
        echo "Usage: $0 [unit|integration|performance|e2e|all|coverage|quick]"
        echo ""
        echo "Test categories:"
        echo "  unit         - Fast unit tests (< 5s total)"
        echo "  integration  - Integration tests with MCP"
        echo "  performance  - Performance benchmarks"
        echo "  e2e          - End-to-end workflow tests"
        echo "  all          - All tests"
        echo "  coverage     - All tests with coverage report"
        echo "  quick        - Fast tests only (exclude slow)"
        echo ""
        exit 1
        ;;
esac
