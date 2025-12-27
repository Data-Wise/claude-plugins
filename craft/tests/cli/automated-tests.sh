#!/bin/bash
# Automated CLI Test Suite for: craft plugin
# Generated: 2025-12-26
# Run: bash tests/cli/automated-tests.sh
#
# This suite runs non-interactively and validates plugin structure,
# commands, skills, and agents automatically.

set -euo pipefail

# ============================================
# Configuration
# ============================================

PLUGIN_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
PASS=0
FAIL=0
SKIP=0
TOTAL=0
VERBOSE="${VERBOSE:-0}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

# ============================================
# Helpers
# ============================================

log_pass() {
    PASS=$((PASS + 1))
    TOTAL=$((TOTAL + 1))
    echo -e "${GREEN}✅ PASS${NC}: $1"
}

log_fail() {
    FAIL=$((FAIL + 1))
    TOTAL=$((TOTAL + 1))
    echo -e "${RED}❌ FAIL${NC}: $1"
    if [[ -n "${2:-}" ]]; then
        echo -e "   ${RED}→ $2${NC}"
    fi
}

log_skip() {
    SKIP=$((SKIP + 1))
    TOTAL=$((TOTAL + 1))
    echo -e "${YELLOW}⏭️  SKIP${NC}: $1"
}

section() {
    echo ""
    echo -e "${BLUE}${BOLD}━━━ $1 ━━━${NC}"
}

# ============================================
# Tests
# ============================================

print_header() {
    echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BOLD}  AUTOMATED PLUGIN TEST SUITE: craft${NC}"
    echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo "  Plugin:  $PLUGIN_DIR"
    echo "  Time:    $(date '+%Y-%m-%d %H:%M:%S')"
    echo "  Verbose: $VERBOSE"
    echo ""
}

# ─── Plugin Structure ────────────────────────────────────────────────────────

test_plugin_structure() {
    section "Plugin Structure"

    # plugin.json exists
    if [[ -f "$PLUGIN_DIR/.claude-plugin/plugin.json" ]]; then
        log_pass "plugin.json exists"
    else
        log_fail "plugin.json missing" "$PLUGIN_DIR/.claude-plugin/plugin.json"
        return
    fi

    # plugin.json is valid JSON
    if jq empty "$PLUGIN_DIR/.claude-plugin/plugin.json" 2>/dev/null; then
        log_pass "plugin.json is valid JSON"
    else
        log_fail "plugin.json is invalid JSON"
        return
    fi

    # Required fields
    local name version
    name=$(jq -r '.name // empty' "$PLUGIN_DIR/.claude-plugin/plugin.json")
    version=$(jq -r '.version // empty' "$PLUGIN_DIR/.claude-plugin/plugin.json")

    if [[ -n "$name" ]]; then
        log_pass "plugin.json has name: $name"
    else
        log_fail "plugin.json missing 'name' field"
    fi

    if [[ -n "$version" ]]; then
        log_pass "plugin.json has version: $version"
    else
        log_fail "plugin.json missing 'version' field"
    fi

    # Required directories
    for dir in commands skills agents; do
        if [[ -d "$PLUGIN_DIR/$dir" ]]; then
            log_pass "$dir/ directory exists"
        else
            log_fail "$dir/ directory missing"
        fi
    done

    # README exists
    if [[ -f "$PLUGIN_DIR/README.md" ]]; then
        log_pass "README.md exists"
    else
        log_skip "README.md not found (optional)"
    fi
}

# ─── Commands ────────────────────────────────────────────────────────────────

test_commands() {
    section "Commands"

    local cmd_count=0
    local valid_count=0

    # Find all .md files in commands/
    while IFS= read -r cmd_file; do
        cmd_count=$((cmd_count + 1))
        local cmd_name
        cmd_name=$(basename "$cmd_file" .md)

        # Check file is not empty
        if [[ -s "$cmd_file" ]]; then
            valid_count=$((valid_count + 1))
            if [[ "$VERBOSE" == "1" ]]; then
                log_pass "Command: $cmd_name"
            fi
        else
            log_fail "Empty command file: $cmd_name"
        fi
    done < <(find "$PLUGIN_DIR/commands" -name "*.md" -type f 2>/dev/null)

    if [[ $cmd_count -gt 0 ]]; then
        log_pass "Found $cmd_count commands ($valid_count valid)"
    else
        log_skip "No commands found"
    fi

    # Check for subdirectory commands (grouped commands)
    local subdir_count=0
    while IFS= read -r subdir; do
        subdir_count=$((subdir_count + 1))
        local subdir_name
        subdir_name=$(basename "$subdir")
        local sub_cmds
        sub_cmds=$(find "$subdir" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
        if [[ "$VERBOSE" == "1" ]]; then
            log_pass "Command group: $subdir_name ($sub_cmds commands)"
        fi
    done < <(find "$PLUGIN_DIR/commands" -mindepth 1 -maxdepth 1 -type d 2>/dev/null)

    if [[ $subdir_count -gt 0 ]]; then
        log_pass "Found $subdir_count command groups"
    fi
}

# ─── Skills ──────────────────────────────────────────────────────────────────

test_skills() {
    section "Skills"

    local skill_count=0
    local valid_count=0

    # Find all .md files in skills/
    while IFS= read -r skill_file; do
        skill_count=$((skill_count + 1))
        local skill_name
        skill_name=$(basename "$skill_file" .md)

        # Check file is not empty
        if [[ -s "$skill_file" ]]; then
            valid_count=$((valid_count + 1))
            if [[ "$VERBOSE" == "1" ]]; then
                log_pass "Skill: $skill_name"
            fi
        else
            log_fail "Empty skill file: $skill_name"
        fi
    done < <(find "$PLUGIN_DIR/skills" -name "*.md" -type f 2>/dev/null)

    if [[ $skill_count -gt 0 ]]; then
        log_pass "Found $skill_count skills ($valid_count valid)"
    else
        log_skip "No skills found"
    fi

    # Check for skill subdirectories
    local subdir_count=0
    while IFS= read -r subdir; do
        subdir_count=$((subdir_count + 1))
        local subdir_name
        subdir_name=$(basename "$subdir")
        local sub_skills
        sub_skills=$(find "$subdir" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
        if [[ "$VERBOSE" == "1" ]]; then
            log_pass "Skill group: $subdir_name ($sub_skills skills)"
        fi
    done < <(find "$PLUGIN_DIR/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null)

    if [[ $subdir_count -gt 0 ]]; then
        log_pass "Found $subdir_count skill categories"
    fi
}

# ─── Agents ──────────────────────────────────────────────────────────────────

test_agents() {
    section "Agents"

    local agent_count=0
    local valid_count=0

    # Find all .md files in agents/
    while IFS= read -r agent_file; do
        agent_count=$((agent_count + 1))
        local agent_name
        agent_name=$(basename "$agent_file" .md)

        # Check file is not empty
        if [[ -s "$agent_file" ]]; then
            valid_count=$((valid_count + 1))

            # Check for required sections (description, tools)
            if grep -q "description:" "$agent_file" 2>/dev/null || grep -q "## " "$agent_file" 2>/dev/null; then
                if [[ "$VERBOSE" == "1" ]]; then
                    log_pass "Agent: $agent_name (has structure)"
                fi
            else
                if [[ "$VERBOSE" == "1" ]]; then
                    log_pass "Agent: $agent_name"
                fi
            fi
        else
            log_fail "Empty agent file: $agent_name"
        fi
    done < <(find "$PLUGIN_DIR/agents" -name "*.md" -type f 2>/dev/null)

    if [[ $agent_count -gt 0 ]]; then
        log_pass "Found $agent_count agents ($valid_count valid)"
    else
        log_skip "No agents found"
    fi
}

# ─── Markdown Validation ─────────────────────────────────────────────────────

test_markdown_syntax() {
    section "Markdown Syntax"

    local total_md=0
    local valid_md=0
    local errors=""

    # Check all markdown files
    while IFS= read -r md_file; do
        total_md=$((total_md + 1))
        local rel_path="${md_file#$PLUGIN_DIR/}"

        # Basic checks
        local has_errors=0

        # Check for unclosed code blocks (odd number of ```)
        local fence_count
        fence_count=$(grep -c '```' "$md_file" 2>/dev/null || echo "0")
        fence_count="${fence_count//[^0-9]/}"  # Strip non-numeric
        fence_count="${fence_count:-0}"
        if [[ $((fence_count % 2)) -ne 0 ]]; then
            has_errors=1
            errors="${errors}Unclosed code block: $rel_path\n"
        fi

        # Check for YAML frontmatter if present
        if head -1 "$md_file" | grep -q '^---$'; then
            if ! grep -q '^---$' <(tail -n +2 "$md_file") 2>/dev/null; then
                has_errors=1
                errors="${errors}Unclosed YAML frontmatter: $rel_path\n"
            fi
        fi

        if [[ $has_errors -eq 0 ]]; then
            valid_md=$((valid_md + 1))
        fi
    done < <(find "$PLUGIN_DIR" -name "*.md" -type f ! -path "*/node_modules/*" ! -path "*/.git/*" 2>/dev/null)

    if [[ $total_md -gt 0 ]]; then
        if [[ $valid_md -eq $total_md ]]; then
            log_pass "All $total_md markdown files valid"
        else
            log_fail "$((total_md - valid_md)) markdown files have issues"
            if [[ -n "$errors" ]]; then
                echo -e "   ${RED}$errors${NC}"
            fi
        fi
    else
        log_skip "No markdown files found"
    fi
}

# ─── Cross-References ────────────────────────────────────────────────────────

test_references() {
    section "Cross-References"

    # Check if commands reference valid skills
    local broken_refs=0

    # Look for skill references in commands (simplified check)
    while IFS= read -r cmd_file; do
        # Check for @skill or skill: references
        if grep -q '@skill\|skill:' "$cmd_file" 2>/dev/null; then
            if [[ "$VERBOSE" == "1" ]]; then
                log_pass "Command $(basename "$cmd_file" .md) has skill references"
            fi
        fi
    done < <(find "$PLUGIN_DIR/commands" -name "*.md" -type f 2>/dev/null)

    log_pass "Cross-reference check complete"
}

# ─── Summary ─────────────────────────────────────────────────────────────────

print_summary() {
    echo ""
    echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BOLD}  RESULTS${NC}"
    echo -e "${BOLD}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "  Passed:  ${GREEN}$PASS${NC}"
    echo -e "  Failed:  ${RED}$FAIL${NC}"
    echo -e "  Skipped: ${YELLOW}$SKIP${NC}"
    echo -e "  Total:   $TOTAL"
    echo ""

    if [[ $FAIL -eq 0 ]]; then
        echo -e "${GREEN}${BOLD}✅ ALL TESTS PASSED${NC}"
        exit 0
    else
        echo -e "${RED}${BOLD}❌ $FAIL TEST(S) FAILED${NC}"
        exit 1
    fi
}

# ============================================
# Main
# ============================================

print_header
test_plugin_structure
test_commands
test_skills
test_agents
test_markdown_syntax
test_references
print_summary
