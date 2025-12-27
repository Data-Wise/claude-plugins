# Fix CI Failures

Automatically diagnose and fix common CI failures.

## Usage

```bash
/craft:code:ci-fix [options]
```

## What This Does

1. **Analyzes CI failure** from logs or local run
2. **Identifies root cause** of each failure
3. **Suggests or applies fixes** automatically
4. **Re-runs checks** to verify fix

## Common Fixes

| Issue | Auto-Fix |
|-------|----------|
| Lint errors | `--fix` flag on linters |
| Formatting | Run formatters (black, prettier) |
| Missing deps | Add to requirements/package.json |
| Type errors | Add type annotations |
| Test failures | Debug mode with traces |
| Coverage drop | Identify untested code |

## Options

- `--auto` - Apply all safe fixes automatically
- `--dry-run` - Show what would be fixed
- `--from-log <url>` - Analyze CI log from URL
- `--interactive` - Confirm each fix

## Examples

```bash
# Diagnose and suggest fixes
/craft:code:ci-fix

# Auto-fix everything safe
/craft:code:ci-fix --auto

# Dry run to see changes
/craft:code:ci-fix --dry-run

# Fix from GitHub Actions log
/craft:code:ci-fix --from-log https://github.com/.../runs/123
```

## Output

```
Analyzing CI failures...

LINT FAILURES (3):
  src/main.py:15 - trailing whitespace
  src/api.py:42 - line too long
  src/utils.py:8 - unused import

  [AUTO-FIXABLE] Run: ruff --fix src/

TEST FAILURES (2):
  test_auth.py::test_login
    AssertionError: expected 200, got 401
    Cause: Missing auth header in test

  test_auth.py::test_logout
    AttributeError: 'NoneType' has no attribute 'id'
    Cause: Fixture not returning user object

  [MANUAL FIX REQUIRED] See test output above

Apply auto-fixes? [y/N]
```

## Integration

Works with:
- `/craft:code:ci-local` - Run CI locally
- `/craft:test:debug` - Debug failing tests
- `/craft:code:lint --fix` - Fix lint issues
