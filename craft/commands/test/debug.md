# Debug Failing Tests

Deep debugging for test failures with traces and context.

## Usage

```bash
/craft:test:debug [test_name]
```

## What This Does

1. **Runs failing test** with maximum verbosity
2. **Captures full stack trace** and context
3. **Shows variable values** at failure point
4. **Suggests potential fixes** based on error

## Debug Features

| Feature | Description |
|---------|-------------|
| Stack traces | Full call stack with locals |
| Variable inspection | Values at failure point |
| Diff output | Expected vs actual comparison |
| Code context | Source lines around failure |
| History | Previous test runs |

## Options

- `--pdb` - Drop into debugger on failure
- `--trace` - Full execution trace
- `--last` - Debug last failed test
- `--diff` - Show detailed diff
- `--context <N>` - Lines of context around failure

## Examples

```bash
# Debug specific test
/craft:test:debug test_login

# Debug with debugger
/craft:test:debug test_login --pdb

# Debug last failure
/craft:test:debug --last

# Show execution trace
/craft:test:debug test_api --trace
```

## Output

```
Debugging: test_auth.py::test_login

FAILURE
───────
AssertionError: assert 401 == 200

Stack Trace:
  tests/test_auth.py:25 in test_login
    response = client.post("/login", json=data)
  > assert response.status_code == 200

Variables at failure:
  data = {"username": "test", "password": "wrong"}
  response.status_code = 401
  response.json() = {"error": "Invalid credentials"}

Code Context:
  23│   data = {"username": "test", "password": "wrong"}
  24│   response = client.post("/login", json=data)
> 25│   assert response.status_code == 200
  26│   assert "token" in response.json()

Possible Causes:
  1. Password is incorrect in test data
  2. Auth endpoint returning 401 for valid creds
  3. Missing authentication headers

Suggested Fix:
  Update test data with valid credentials or
  mock the authentication service
```

## Integration

Works with:
- `/craft:test:run` - Run tests
- `/craft:test:watch` - Watch mode
- `/craft:code:debug` - Code debugging
