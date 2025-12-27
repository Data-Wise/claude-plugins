#!/bin/bash
# Interactive Test Suite for: craft plugin
# Generated: 2025-12-26
# Run: bash tests/cli/interactive-tests.sh
#
# Tests plugin commands by invoking them in Claude Code context.
# Each test runs, shows expected vs actual, prompts for pass/fail.

set -euo pipefail

# ============================================
# Configuration
# ============================================

PASS=0
FAIL=0
TOTAL=0
TOTAL_TESTS=15

# Logging
LOG_DIR="${LOG_DIR:-tests/cli/logs}"
mkdir -p "$LOG_DIR" 2>/dev/null || LOG_DIR="/tmp"
LOG_FILE="$LOG_DIR/interactive-test-$(date +%Y%m%d-%H%M%S).log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

log "=== Interactive Test Session Started ==="
log "Working directory: $(pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# ============================================
# Helpers
# ============================================

print_header() {
    echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BOLD}  INTERACTIVE PLUGIN TEST SUITE: craft ($TOTAL_TESTS tests)${NC}"
    echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "  ${BLUE}Keys:${NC} y=pass, n=fail, q=quit"
    echo -e "  ${BLUE}Log:${NC}  $LOG_FILE"
    echo ""
}

run_test() {
    local test_num=$1
    local test_name=$2
    local command=$3
    local expected=$4

    TOTAL=$((TOTAL + 1))

    # Header
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}TEST $test_num/$TOTAL_TESTS: $test_name${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "  ${BLUE}Command:${NC} $command"
    echo ""

    log "TEST $test_num: $test_name"
    log "  Command: $command"

    # Run command and capture output
    local output
    output=$(bash -c "$command" 2>&1) || true
    log "  Output: $output"

    # Show expected vs actual
    echo -e "${BLUE}EXPECTED:${NC} $expected"
    echo ""
    echo -e "${GREEN}ACTUAL:${NC}"
    echo "$output"
    echo ""

    # Single prompt: pass/fail/quit
    read -p "[y=pass, n=fail, q=quit] " -n 1 -r
    echo ""

    case "$REPLY" in
        [Yy])
            PASS=$((PASS + 1))
            log "  Result: PASS"
            echo -e "${GREEN}✅ PASS${NC}"
            ;;
        [Qq])
            log "User quit at test $test_num"
            echo -e "${YELLOW}Exiting...${NC}"
            print_summary
            exit 0
            ;;
        *)
            FAIL=$((FAIL + 1))
            log "  Result: FAIL"
            echo -e "${RED}❌ FAIL${NC}"
            ;;
    esac
}

print_summary() {
    echo ""
    echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BOLD}  RESULTS: $PASS passed, $FAIL failed (of $TOTAL run)${NC}"
    echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"

    if [[ $FAIL -eq 0 ]]; then
        echo -e "${GREEN}${BOLD}🎉 ALL TESTS PASSED!${NC}"
        log "Final: ALL TESTS PASSED ($PASS/$TOTAL)"
    else
        echo -e "${RED}${BOLD}⚠️  $FAIL TEST(S) FAILED${NC}"
        log "Final: $FAIL TESTS FAILED"
    fi

    log "Summary: $PASS passed, $FAIL failed"
    echo -e "Log: ${BLUE}$LOG_FILE${NC}"
    echo ""
}

# ============================================
# Main
# ============================================

print_header

# ============================================
# PLUGIN STRUCTURE TESTS
# ============================================

run_test 1 "Plugin JSON Exists" \
    "test -f .claude-plugin/plugin.json && echo 'Found' || echo 'Missing'" \
    "Found"

run_test 2 "Plugin Name" \
    "jq -r '.name' .claude-plugin/plugin.json 2>/dev/null || echo 'Error'" \
    "craft (or plugin name)"

run_test 3 "Plugin Version" \
    "jq -r '.version' .claude-plugin/plugin.json 2>/dev/null || echo 'Error'" \
    "Version string (e.g., 1.3.0)"

# ============================================
# DIRECTORY STRUCTURE
# ============================================

run_test 4 "Commands Directory" \
    "ls commands/ | head -10" \
    "List of command files/directories"

run_test 5 "Skills Directory" \
    "ls skills/ | head -10" \
    "List of skill files/directories"

run_test 6 "Agents Directory" \
    "ls agents/ | head -10" \
    "List of agent files"

# ============================================
# COMMAND COUNTS
# ============================================

run_test 7 "Command Count" \
    "find commands -name '*.md' -type f | wc -l | tr -d ' '" \
    "Number of command files (10+)"

run_test 8 "Skill Count" \
    "find skills -name '*.md' -type f | wc -l | tr -d ' '" \
    "Number of skill files (10+)"

run_test 9 "Agent Count" \
    "find agents -name '*.md' -type f | wc -l | tr -d ' '" \
    "Number of agent files (1+)"

# ============================================
# COMMAND CONTENT VALIDATION
# ============================================

run_test 10 "Hub Command" \
    "head -20 commands/hub.md 2>/dev/null || echo 'Not found'" \
    "Hub command content with frontmatter"

run_test 11 "Do Command" \
    "head -20 commands/do.md 2>/dev/null || echo 'Not found'" \
    "Do command content with description"

run_test 12 "Check Command" \
    "head -20 commands/check.md 2>/dev/null || echo 'Not found'" \
    "Check command for validation"

# ============================================
# SKILL CONTENT VALIDATION
# ============================================

run_test 13 "Planning Skills" \
    "ls skills/planning/ 2>/dev/null || echo 'No planning skills'" \
    "List of planning-related skills"

run_test 14 "Testing Skills" \
    "ls skills/testing/ 2>/dev/null || echo 'No testing skills'" \
    "List of testing-related skills"

# ============================================
# MARKDOWN VALIDATION
# ============================================

run_test 15 "Markdown Fence Balance" \
    "for f in \$(find . -name '*.md' -type f | head -20); do c=\$(grep -c '\`\`\`' \"\$f\" 2>/dev/null || echo 0); if (( c % 2 != 0 )); then echo \"Unbalanced: \$f\"; fi; done || echo 'All balanced'" \
    "All balanced (no unclosed code blocks)"

# ============================================
# Summary
# ============================================

log "=== Session Completed ==="
print_summary
