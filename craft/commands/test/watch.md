# Test Watch Mode

Automatically re-run tests when files change.

## Usage

```bash
/craft:test:watch [options]
```

## What This Does

1. **Watches source files** for changes
2. **Re-runs affected tests** on each change
3. **Shows live results** in terminal
4. **Filters intelligently** to run only related tests

## Smart Test Selection

| Change | Tests Run |
|--------|-----------|
| `src/auth.py` | `tests/test_auth.py` |
| `src/api/*.py` | `tests/test_api*.py` |
| `tests/conftest.py` | All tests |
| `pyproject.toml` | All tests |

## Options

- `--all` - Run all tests on each change
- `--filter <pattern>` - Only watch matching files
- `--clear` - Clear screen between runs
- `--notify` - Desktop notifications

## Examples

```bash
# Start watch mode
/craft:test:watch

# Watch with notifications
/craft:test:watch --notify

# Clear screen between runs
/craft:test:watch --clear

# Run all tests on each change
/craft:test:watch --all
```

## Output

```
Watching for changes... (Ctrl+C to stop)

[12:34:56] src/auth.py changed
  Running: tests/test_auth.py
  ✓ 3/3 tests passed (0.35s)

[12:35:12] tests/test_api.py changed
  Running: tests/test_api.py
  ✗ 4/5 tests passed (0.52s)
  FAILED: test_delete_user

[12:35:30] src/api/handlers.py changed
  Running: tests/test_api.py
  ✓ 5/5 tests passed (0.48s)
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `a` | Run all tests |
| `f` | Run failed tests only |
| `q` | Quit watch mode |
| `Enter` | Re-run last tests |

## Integration

Works with:
- `/craft:test:run` - Manual test runs
- `/craft:test:debug` - Debug failures
