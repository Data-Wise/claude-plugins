# Test Generator Skill

Generates dogfooding test suites (automated + interactive) for any project type.

## When to Use

Use this skill when:
- Setting up CLI tests for a new project
- Creating plugin validation tests
- Generating interactive QA test suites
- Need both automated and manual test coverage
- Want consistent test patterns across projects

## Capabilities

### Project Type Detection

Automatically detects project type and generates appropriate tests:

| Project Type | Detection | Test Focus |
|-------------|-----------|------------|
| **CLI Tool** | `pyproject.toml` + CLI entry | Commands, subcommands, exit codes, help |
| **Claude Plugin** | `.claude-plugin/plugin.json` | Structure, commands, skills, agents |
| **Python Library** | `pyproject.toml` (no CLI) | Module imports, API surface |
| **Node Package** | `package.json` + bin | CLI commands, npm scripts |
| **R Package** | `DESCRIPTION` | Package structure, exports |
| **Shell Scripts** | `*.sh` files | Script execution, options |

### Test Suite Generation

Generates two complementary test suites:

#### 1. Automated Tests (`automated-tests.sh`)
- Non-interactive, CI-ready
- Exit code validation
- Output pattern matching
- Structure validation
- Runs in < 60 seconds

#### 2. Interactive Tests (`interactive-tests.sh`)
- Human-guided QA
- Expected vs actual comparison
- Single-key responses (y/n/q)
- Logging to `tests/cli/logs/`
- Visual output validation

### Test Categories by Project Type

**CLI Tools:**
- Smoke tests (version, help, aliases)
- Core commands (each subcommand)
- Error handling (invalid commands)
- Exit codes (success/failure)
- Help accessibility

**Claude Plugins:**
- Plugin structure (plugin.json)
- Directory structure (commands/, skills/, agents/)
- File counts and validity
- Markdown syntax validation
- Cross-reference checks

**Libraries:**
- Import validation
- API surface coverage
- Module structure
- Documentation presence

## Usage

### Basic Generation
```
Generate CLI tests for this project
```

### With Options
```
Generate dogfooding tests:
- Project: ~/projects/my-tool
- Include interactive tests
- Add CI integration
```

### Specific Project Types
```
Create plugin validation tests for craft
Create CLI tests for aiterm
Create package tests for my-r-package
```

## Output Structure

```
tests/
└── cli/
    ├── README.md              # Test documentation
    ├── automated-tests.sh     # CI-ready automated tests
    ├── interactive-tests.sh   # Human-guided QA tests
    └── logs/                  # Test execution logs
        └── interactive-test-YYYYMMDD-HHMMSS.log
```

## Test Script Features

### Automated Tests
```bash
# Colors and formatting
✅ PASS: Test description
❌ FAIL: Test description → Error details
⏭️  SKIP: Test description

# Sections
━━━ Section Name ━━━

# Summary
═══════════════════════════
  RESULTS
═══════════════════════════
  Passed:  15
  Failed:  0
  Total:   15

✅ ALL TESTS PASSED
```

### Interactive Tests
```bash
TEST 1/15: Version Check
  Command: tool --version

EXPECTED: Version string (e.g., 'tool 1.0.0')

ACTUAL:
tool version 1.0.0

[y=pass, n=fail, q=quit]
```

## Integration

Works with:
- `/craft:test:run` - Execute generated tests
- `/craft:code:ci-local` - Add to CI pipeline
- `test-strategist` skill - Test strategy guidance

## Example Prompts

```
"Generate CLI tests for my Python tool"
"Create plugin validation tests"
"Add dogfooding tests like aiterm has"
"Set up automated + interactive tests for this project"
"Generate tests and add to GitHub Actions"
```

## Customization

Tests can be customized after generation:
- Add project-specific test cases
- Modify expected outputs
- Adjust test categories
- Add environment-specific tests
