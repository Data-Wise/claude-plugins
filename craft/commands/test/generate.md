---
description: Generate dogfooding test suites (automated + interactive) for any project
arguments:
  - name: project_path
    description: Path to project (default: current directory)
    required: false
  - name: type
    description: "Project type override: cli, plugin, library, package"
    required: false
---

# /craft:test:generate

Generate comprehensive dogfooding test suites for any project type.

## What It Does

1. **Detects project type** (CLI tool, Claude plugin, library, etc.)
2. **Analyzes structure** (commands, features, entry points)
3. **Generates two test suites:**
   - `automated-tests.sh` - CI-ready, non-interactive
   - `interactive-tests.sh` - Human-guided QA with expected/actual comparison
4. **Creates test infrastructure** (logs directory, README)

## Project Type Detection

| Files Present | Detected Type | Test Focus |
|--------------|---------------|------------|
| `.claude-plugin/plugin.json` | Claude Plugin | Structure, commands, skills, agents |
| `pyproject.toml` + `[project.scripts]` | Python CLI | CLI commands, subcommands, exit codes |
| `pyproject.toml` (library) | Python Library | Imports, API surface |
| `package.json` + `bin` | Node CLI | Commands, npm scripts |
| `DESCRIPTION` | R Package | Package structure, exports |
| `Cargo.toml` + `[[bin]]` | Rust CLI | Binary commands |
| `go.mod` + `main.go` | Go CLI | Commands |

## Output Structure

```
tests/
└── cli/
    ├── README.md              # How to run tests
    ├── automated-tests.sh     # Non-interactive (CI)
    ├── interactive-tests.sh   # Human-guided QA
    └── logs/                  # Execution logs
```

## Generated Test Categories

### For CLI Tools
1. **Smoke Tests** - Version, help, aliases
2. **Core Commands** - Each subcommand
3. **Subcommand Groups** - Nested commands
4. **Error Handling** - Invalid commands, exit codes
5. **Help Accessibility** - All --help flags

### For Claude Plugins
1. **Plugin Structure** - plugin.json validity
2. **Directories** - commands/, skills/, agents/
3. **File Counts** - Commands, skills, agents
4. **Content Validation** - Non-empty files
5. **Markdown Syntax** - Code fences, frontmatter

## Usage Examples

```bash
# Current directory
/craft:test:generate

# Specific project
/craft:test:generate ~/projects/my-tool

# Force project type
/craft:test:generate . cli

# Plugin project
/craft:test:generate ~/projects/my-plugin plugin
```

## Implementation

When this command runs, I will:

### Step 1: Detect Project Type

```bash
# Check for project indicators
if [[ -f ".claude-plugin/plugin.json" ]]; then
    TYPE="plugin"
elif [[ -f "pyproject.toml" ]] && grep -q "project.scripts" pyproject.toml; then
    TYPE="python-cli"
elif [[ -f "package.json" ]] && jq -e '.bin' package.json >/dev/null 2>&1; then
    TYPE="node-cli"
elif [[ -f "DESCRIPTION" ]]; then
    TYPE="r-package"
else
    TYPE="generic"
fi
```

### Step 2: Analyze Project Structure

**For CLI:**
- Extract CLI name from pyproject.toml/package.json
- List all subcommands from --help output
- Identify command groups

**For Plugin:**
- Parse plugin.json for name, version
- Count commands, skills, agents
- Map directory structure

### Step 3: Generate Automated Tests

Template structure:
```bash
#!/bin/bash
# Automated CLI Test Suite for: [PROJECT_NAME]
# Generated: [DATE]

set -euo pipefail

PASS=0
FAIL=0
TOTAL=0

# Test functions...

# Tests based on detected structure...

# Summary...
```

### Step 4: Generate Interactive Tests

Template structure:
```bash
#!/bin/bash
# Interactive Test Suite for: [PROJECT_NAME]
# Generated: [DATE]

TOTAL_TESTS=[COUNT]

run_test() {
    # Show test, run command, compare expected/actual
    # Single prompt: y/n/q
}

# Tests...

print_summary
```

### Step 5: Create README

Document how to run both test suites.

## Test Script Features

### Automated Tests
- ✅ Non-interactive (CI-ready)
- ✅ Exit code validation
- ✅ Pattern matching
- ✅ Colored output
- ✅ Summary with pass/fail counts
- ✅ `set -euo pipefail` safe

### Interactive Tests
- ✅ Run → Show Expected → Show Actual → Judge
- ✅ Single keystroke (y=pass, n=fail, q=quit)
- ✅ Logging to `logs/` directory
- ✅ Progress indicator (TEST X/Y)
- ✅ Summary at end

## Integration

After generation:
```bash
# Run automated tests
bash tests/cli/automated-tests.sh

# Run interactive tests
bash tests/cli/interactive-tests.sh

# Add to CI (.github/workflows/test.yml)
- name: Run CLI tests
  run: bash tests/cli/automated-tests.sh
```

## Customization After Generation

The generated tests are starting points. Customize by:
- Adding project-specific test cases
- Modifying expected output descriptions
- Adding environment-specific tests
- Adjusting test categories
