---
description: Generate CLI test suites (interactive and automated)
arguments:
  - name: mode
    description: Test suite mode (interactive|automated)
    required: false
    default: interactive
  - name: app_name
    description: CLI application name to test
    required: false
---

# /craft:test:cli-gen - CLI Test Suite Generator

Generate comprehensive test suites for command-line applications.

## Purpose

Create test suites that verify CLI behavior:
- **Interactive mode** - Human-guided testing with prompts
- **Automated mode** - CI-ready test scripts

## Modes

| Mode | Output | Best For |
|------|--------|----------|
| **interactive** | Step-by-step test script | Manual QA, demos |
| **automated** | CI-ready test suite | Continuous integration |

## Usage

```bash
/craft:test:cli-gen                          # Interactive mode (default)
/craft:test:cli-gen interactive "ait"        # Interactive tests for 'ait'
/craft:test:cli-gen automated "aiterm"       # CI tests for 'aiterm'
/craft:test:cli-gen automated --output tests/cli/
```

## Step-by-Step Process

### Step 1: Detect CLI Application

```bash
# Find CLI entry points
cat pyproject.toml 2>/dev/null | grep -A5 "\[project.scripts\]"
cat package.json 2>/dev/null | grep -A5 '"bin"'
ls -la bin/ 2>/dev/null
```

**Detected CLI:**
```
📦 CLI APPLICATION DETECTED
═══════════════════════════════════════════════════════════════

Name: aiterm
Entry points:
  • aiterm - Main CLI
  • ait - Shorthand alias

Commands found: 23
  doctor, detect, switch, claude, mcp, sessions, ide, ...

Framework: Typer (Python)
```

### Step 2: Analyze Commands

```bash
# Get command structure
${CLI_NAME} --help
${CLI_NAME} <subcommand> --help
```

**Command Tree:**
```
aiterm/ait
├── doctor           # System check
├── detect           # Context detection
├── switch           # Profile switching
├── claude
│   ├── settings     # Show settings
│   ├── backup       # Backup config
│   └── approvals    # Manage approvals
├── mcp
│   ├── list         # List servers
│   ├── test         # Test server
│   └── validate     # Validate config
└── sessions
    ├── live         # Active sessions
    ├── conflicts    # Detect conflicts
    └── history      # Session history
```

### Step 3: Generate Test Suite

#### Interactive Mode

Creates a guided test script:

```bash
#!/bin/bash
# Interactive CLI Test Suite for: aiterm
# Generated: 2025-12-26
# Run: bash tests/cli/interactive-tests.sh

set -e

echo "═══════════════════════════════════════════════════════════════"
echo "  INTERACTIVE CLI TEST SUITE: aiterm"
echo "═══════════════════════════════════════════════════════════════"

# Test 1: Version check
echo ""
echo "▶ TEST 1: Version Check"
echo "  Command: aiterm --version"
echo "  Expected: Version string (e.g., 'aiterm 0.3.0')"
echo ""
read -p "Run test? (y/n/skip) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    aiterm --version
    read -p "Did this match expected? (y/n) " -n 1 -r
    echo ""
    [[ $REPLY =~ ^[Yy]$ ]] && echo "✅ PASS" || echo "❌ FAIL"
fi

# Test 2: Doctor check
echo ""
echo "▶ TEST 2: Doctor Check"
echo "  Command: aiterm doctor"
echo "  Expected: System diagnostics with pass/warn status"
echo ""
read -p "Run test? (y/n/skip) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    aiterm doctor
    read -p "Did this run correctly? (y/n) " -n 1 -r
    echo ""
    [[ $REPLY =~ ^[Yy]$ ]] && echo "✅ PASS" || echo "❌ FAIL"
fi

# ... more tests
```

#### Automated Mode

Creates CI-ready test script:

```bash
#!/bin/bash
# Automated CLI Test Suite for: aiterm
# Generated: 2025-12-26
# Run: bash tests/cli/automated-tests.sh

set -e

PASS=0
FAIL=0
SKIP=0

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

log_pass() { ((PASS++)); echo -e "${GREEN}✅ PASS${NC}: $1"; }
log_fail() { ((FAIL++)); echo -e "${RED}❌ FAIL${NC}: $1"; }
log_skip() { ((SKIP++)); echo -e "${YELLOW}⏭️ SKIP${NC}: $1"; }

echo "═══════════════════════════════════════════════════════════════"
echo "  AUTOMATED CLI TEST SUITE: aiterm"
echo "═══════════════════════════════════════════════════════════════"

# Test: CLI is installed
if command -v aiterm &> /dev/null; then
    log_pass "CLI is installed"
else
    log_fail "CLI not found in PATH"
    exit 1
fi

# Test: Version returns successfully
if aiterm --version > /dev/null 2>&1; then
    log_pass "Version command works"
else
    log_fail "Version command failed"
fi

# Test: Help is accessible
if aiterm --help > /dev/null 2>&1; then
    log_pass "Help is accessible"
else
    log_fail "Help command failed"
fi

# Test: Doctor runs without error
if aiterm doctor > /dev/null 2>&1; then
    log_pass "Doctor command completes"
else
    log_fail "Doctor command failed"
fi

# Test: Detect returns JSON-like output
if aiterm detect 2>&1 | grep -q "type\|project\|context"; then
    log_pass "Detect returns context info"
else
    log_fail "Detect output unexpected"
fi

# Test: Invalid command shows error
if aiterm nonexistent-command 2>&1 | grep -qi "error\|usage\|invalid"; then
    log_pass "Invalid commands handled gracefully"
else
    log_fail "Invalid command not handled"
fi

# Summary
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  RESULTS"
echo "═══════════════════════════════════════════════════════════════"
echo -e "  Passed: ${GREEN}${PASS}${NC}"
echo -e "  Failed: ${RED}${FAIL}${NC}"
echo -e "  Skipped: ${YELLOW}${SKIP}${NC}"
echo ""

# Exit code
[ $FAIL -eq 0 ] && exit 0 || exit 1
```

## Output Format

```
✅ CLI TEST SUITE GENERATED
═══════════════════════════════════════════════════════════════

Generated files:
  📄 tests/cli/interactive-tests.sh (interactive mode)
  📄 tests/cli/automated-tests.sh (CI mode)
  📄 tests/cli/README.md (test documentation)

Test coverage:
  • 23 commands discovered
  • 35 test cases generated
  • Estimated run time: 45s (automated)

Next steps:
  1. Review: cat tests/cli/automated-tests.sh
  2. Run interactive: bash tests/cli/interactive-tests.sh
  3. Run automated: bash tests/cli/automated-tests.sh
  4. Add to CI: See tests/cli/README.md
```

## Test Categories

| Category | Description | Example |
|----------|-------------|---------|
| **Smoke** | Basic functionality | `--version`, `--help` |
| **Commands** | Each command works | `doctor`, `detect` |
| **Arguments** | Args parsed correctly | `--verbose`, `--output` |
| **Errors** | Invalid input handled | bad args, missing files |
| **Output** | Output format correct | JSON, table, plain |
| **Exit codes** | Correct exit status | 0 success, 1 error |

## Shell Framework Support

| Framework | File Extension | Features |
|-----------|---------------|----------|
| **bash** | `.sh` | Portable, CI-friendly |
| **zsh** | `.zsh` | Rich features |
| **bats** | `.bats` | Test framework |

## Integration

Works with:
- `/craft:test:cli-run` - Run generated test suites
- `/craft:test:run` - Unified test runner
- `/craft:code:ci-local` - CI checks
