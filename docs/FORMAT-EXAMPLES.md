# Format Handler Examples

**Version:** 1.0.0
**Updated:** 2026-01-07
**Status:** Complete

This document shows examples of all three output formats (Terminal, JSON, Markdown) with the same sample data.

---

## Sample Analysis Data

All examples below use this data structure:

```python
data = {
    "title": "R Package Analysis",
    "status": "success",
    "data": {
        "health": 87,
        "issues": 2,
        "packages_analyzed": 4
    }
}
```

---

## Terminal Format (Default)

**Purpose:** Human-readable output for interactive terminal use

**Features:**
- Emoji status indicators (✅ ❌ ⚠️ ℹ️)
- Rich library colored output
- Bullet-point data display
- Bold title

**Output:**

```
✅ R Package Analysis

  • health: 87
  • issues: 2
  • packages_analyzed: 4

```

**ANSI Codes:**
- Numbers are colored cyan (Rich automatic formatting)
- Title is bold
- Emoji automatically matches status field

**Usage:**

```bash
/rforge:analyze "Update bootstrap"
# Uses terminal format by default

/rforge:analyze "Update bootstrap" --format terminal
# Explicit terminal format
```

---

## JSON Format

**Purpose:** Machine-readable output for scripting and automation

**Features:**
- Valid JSON (parseable)
- ISO 8601 timestamp
- Mode metadata
- Results wrapped in envelope
- Optional custom metadata

**Output:**

```json
{
  "timestamp": "2026-01-07T14:30:15.123456",
  "mode": "default",
  "results": {
    "title": "R Package Analysis",
    "status": "success",
    "data": {
      "health": 87,
      "issues": 2,
      "packages_analyzed": 4
    }
  }
}
```

**With Optional Metadata:**

```json
{
  "timestamp": "2026-01-07T14:30:15.123456",
  "mode": "default",
  "results": {
    "title": "R Package Analysis",
    "status": "success",
    "data": {
      "health": 87,
      "issues": 2,
      "packages_analyzed": 4
    }
  },
  "metadata": {
    "package_name": "mediationverse",
    "version": "2.1.0"
  }
}
```

**Usage:**

```bash
/rforge:analyze "Update bootstrap" --format json
# JSON output for scripting

/rforge:analyze "Update bootstrap" --format json > analysis.json
# Save to file for processing
```

**Parsing Example:**

```python
import json

# Parse JSON output
with open('analysis.json') as f:
    result = json.load(f)

print(f"Mode: {result['mode']}")
print(f"Health: {result['results']['data']['health']}")
print(f"Timestamp: {result['timestamp']}")
```

---

## Markdown Format

**Purpose:** Documentation-ready output for reports and docs

**Features:**
- H1 title
- Bold status line
- JSON code block for data
- Ready to paste into docs

**Output:**

```markdown
# R Package Analysis

**Status:** success

## Data

```json
{
  "health": 87,
  "issues": 2,
  "packages_analyzed": 4
}
```
```

**Rendered Preview:**

# R Package Analysis

**Status:** success

## Data

```json
{
  "health": 87,
  "issues": 2,
  "packages_analyzed": 4
}
```

**Usage:**

```bash
/rforge:analyze "Update bootstrap" --format markdown
# Markdown output for documentation

/rforge:analyze "Update bootstrap" --format markdown > ANALYSIS.md
# Save as markdown file
```

---

## Comparison Table

| Feature | Terminal | JSON | Markdown |
|---------|----------|------|----------|
| **Human-readable** | ✅ Excellent | ❌ No | ✅ Good |
| **Machine-readable** | ❌ No (ANSI codes) | ✅ Excellent | ⚠️ Limited |
| **Emojis** | ✅ Yes | ❌ No | ❌ No |
| **Colors** | ✅ Yes (Rich) | ❌ No | ❌ No |
| **Metadata** | ❌ No | ✅ Yes (timestamp, mode) | ❌ No |
| **Pasteable to docs** | ❌ No (ANSI codes) | ⚠️ Limited | ✅ Excellent |
| **Scripting** | ❌ No | ✅ Excellent | ⚠️ Limited |
| **File size** | Medium | Large (metadata) | Small |
| **Default format** | ✅ Yes | ❌ No | ❌ No |

---

## Status Examples (Different Status Values)

### Success Status

**Terminal:**
```
✅ Package Analysis
  • health: 92
```

**JSON:**
```json
{
  "timestamp": "2026-01-07T14:30:15.123456",
  "mode": "default",
  "results": {
    "title": "Package Analysis",
    "status": "success",
    "data": {"health": 92}
  }
}
```

**Markdown:**
```markdown
# Package Analysis

**Status:** success

## Data

```json
{"health": 92}
```
```

### Error Status

**Terminal:**
```
❌ Package Analysis
  • health: 45
  • errors: 5
```

**JSON:**
```json
{
  "timestamp": "2026-01-07T14:30:15.123456",
  "mode": "default",
  "results": {
    "title": "Package Analysis",
    "status": "error",
    "data": {"health": 45, "errors": 5}
  }
}
```

**Markdown:**
```markdown
# Package Analysis

**Status:** error

## Data

```json
{"health": 45, "errors": 5}
```
```

### Warning Status

**Terminal:**
```
⚠️  Package Analysis
  • health: 78
  • warnings: 3
```

**JSON:**
```json
{
  "timestamp": "2026-01-07T14:30:15.123456",
  "mode": "default",
  "results": {
    "title": "Package Analysis",
    "status": "warning",
    "data": {"health": 78, "warnings": 3}
  }
}
```

**Markdown:**
```markdown
# Package Analysis

**Status:** warning

## Data

```json
{"health": 78, "warnings": 3}
```
```

---

## Mode + Format Combinations

All 12 combinations of 4 modes × 3 formats are supported:

| Mode | Terminal | JSON | Markdown |
|------|----------|------|----------|
| **default** | ✅ Quick dashboard | ✅ Fast results | ✅ Quick summary |
| **debug** | ✅ Detailed view | ✅ Complete data | ✅ Full report |
| **optimize** | ✅ Performance metrics | ✅ Timing data | ✅ Performance report |
| **release** | ✅ Release checklist | ✅ Validation data | ✅ Release notes |

**Example Usage:**

```bash
# Debug analysis with JSON output
/rforge:analyze --mode debug --format json

# Release validation with markdown report
/rforge:analyze --mode release --format markdown > RELEASE.md

# Optimize analysis with terminal display
/rforge:analyze --mode optimize --format terminal
```

---

## Integration Examples

### Save Analysis Results

```bash
# Terminal display (default)
/rforge:analyze "Bootstrap update"

# Save JSON for later processing
/rforge:analyze "Bootstrap update" --format json > results.json

# Generate markdown report
/rforge:analyze "Bootstrap update" --format markdown > ANALYSIS.md
```

### Pipe to Other Tools

```bash
# Parse JSON with jq
/rforge:analyze --format json | jq '.results.data.health'

# Filter markdown with grep
/rforge:analyze --format markdown | grep "health"

# Count issues in terminal output (won't work well due to ANSI codes)
/rforge:analyze --format json | jq '.results.data.issues'
```

### Scripting Example

```python
import subprocess
import json

# Run analysis and get JSON
result = subprocess.run(
    ['claude-code', 'skill', 'rforge:analyze', '--format', 'json'],
    capture_output=True,
    text=True
)

# Parse results
data = json.loads(result.stdout)
health = data['results']['data']['health']

# Take action based on health
if health < 70:
    print("⚠️  Health below threshold, investigate!")
else:
    print("✅ Health looks good")
```

---

## Best Practices

### When to Use Each Format

**Terminal (Default):**
- ✅ Interactive command-line use
- ✅ Quick status checks
- ✅ Daily development workflow
- ❌ Scripting/automation
- ❌ Copy-paste to documentation

**JSON:**
- ✅ Automation scripts
- ✅ CI/CD pipelines
- ✅ Parsing with jq/Python
- ✅ Long-term storage
- ❌ Human reading
- ❌ Documentation

**Markdown:**
- ✅ Documentation
- ✅ Reports
- ✅ GitHub issues/PRs
- ✅ Wiki pages
- ⚠️ Scripting (limited)
- ❌ Machine parsing

### Performance Considerations

**Format overhead (relative):**
- Terminal: Medium (Rich rendering)
- JSON: Low (simple JSON encoding)
- Markdown: Low (string formatting)

**File size (relative):**
- Terminal: Medium (ANSI codes)
- JSON: Large (metadata envelope)
- Markdown: Small (minimal formatting)

---

## Troubleshooting

### "ANSI codes in output"

**Problem:** Terminal output has escape codes like `\x1b[1m`

**Solution:** This is normal for terminal format. Use `--format json` or `--format markdown` for clean output.

### "Can't parse JSON"

**Problem:** JSON output invalid

**Solution:** Ensure you're using `--format json` and redirecting ONLY stdout (not stderr):

```bash
/rforge:analyze --format json > output.json 2>/dev/null
```

### "Markdown not rendering"

**Problem:** Markdown output doesn't render correctly

**Solution:** Ensure code block fences are properly formatted. Save to `.md` file for proper rendering.

---

## Technical Details

### Formatter Implementation

Located in: `rforge/lib/formatters.py`

**Functions:**
- `format_terminal(data, mode)` - Rich console output
- `format_json(data, mode, **metadata)` - JSON with metadata
- `format_markdown(data, mode)` - Structured markdown
- `format_output(data, format_name, mode, **metadata)` - Unified interface
- `get_formatter(format_name)` - Formatter lookup
- `validate_json_output(json_string)` - JSON validator

**Data Contract:**

```python
{
    "title": str,        # Required: Display title
    "status": str,       # Required: "success", "error", "warning", "info"
    "data": dict         # Optional: Your analysis data
}
```

### Testing

**Test Suite:** `tests/unit/test_format_handling.py`

**Coverage:**
- 27 tests total
- Format parsing (6 tests)
- Format validation (3 tests)
- JSON formatting (5 tests)
- Markdown formatting (4 tests)
- Terminal formatting (5 tests)
- Consistency checks (2 tests)
- Mode integration (2 tests)

**Run Tests:**

```bash
pytest tests/unit/test_format_handling.py -v
# 27 passed in 0.07s
```

---

## See Also

- **Mode System:** `docs/MODE-SYSTEM.md` - Complete mode documentation
- **Commands:** `rforge/commands/analyze.md`, `rforge/commands/status.md`
- **Implementation:** `rforge/lib/formatters.py`
- **Tests:** `tests/unit/test_format_handling.py`

---

**Last Updated:** 2026-01-07
**Maintainer:** Claude Code
**Status:** ✅ Production Ready
