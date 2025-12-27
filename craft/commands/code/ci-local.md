# Run CI Locally

Run continuous integration checks locally before pushing.

## Usage

```bash
/craft:code:ci-local [options]
```

## What This Does

1. **Detects CI configuration** (.github/workflows, .gitlab-ci.yml, etc.)
2. **Runs equivalent checks** locally
3. **Reports failures** before they hit remote CI
4. **Saves time** by catching issues early

## Checks Performed

| Check | Command | Threshold |
|-------|---------|-----------|
| Lint | `/craft:code:lint --strict` | 0 errors |
| Tests | `/craft:test:run` | 100% pass |
| Coverage | `/craft:code:coverage` | 80% minimum |
| Security | `/craft:code:deps-audit` | No critical |
| Types | mypy/tsc/etc. | 0 errors |
| Docs | `/craft:docs:validate` | 0 errors |

## Options

- `--quick` - Skip slow checks (coverage, security)
- `--fix` - Auto-fix issues where possible
- `--verbose` - Show detailed output
- `--only <check>` - Run specific check only

## Examples

```bash
# Full CI check
/craft:code:ci-local

# Quick check before commit
/craft:code:ci-local --quick

# Fix issues automatically
/craft:code:ci-local --fix

# Run only tests
/craft:code:ci-local --only tests
```

## Output

```
Running local CI checks...

[1/6] Lint           ✓ Pass (0 issues)
[2/6] Type check     ✓ Pass (0 errors)
[3/6] Tests          ✓ Pass (42/42)
[4/6] Coverage       ✓ Pass (87% > 80%)
[5/6] Security       ✓ Pass (0 critical)
[6/6] Docs           ✓ Pass (0 errors)

All checks passed! Safe to push.
```

## Failure Output

```
Running local CI checks...

[1/6] Lint           ✗ Fail (3 issues)
  src/main.py:15 - trailing whitespace
  src/api.py:42 - line too long

[2/6] Tests          ✗ Fail (40/42)
  FAILED test_auth.py::test_login
  FAILED test_auth.py::test_logout

2 checks failed. Fix before pushing.
Run with --fix to auto-fix lint issues.
```

## Integration

Works with:
- `/craft:code:ci-fix` - Fix CI failures
- `/craft:git:sync` - Pre-push validation
