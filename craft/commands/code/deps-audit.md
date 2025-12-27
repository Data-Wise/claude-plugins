# Security Audit

Audit dependencies for known security vulnerabilities.

## Usage

```bash
/craft:code:deps-audit [options]
```

## What This Does

1. **Scans dependencies** including transitive dependencies
2. **Checks vulnerability databases** (CVE, GitHub Advisory, etc.)
3. **Reports severity levels** (critical, high, medium, low)
4. **Suggests remediations** with upgrade paths

## Project Type Detection

| Project | Tool | Database |
|---------|------|----------|
| Python | pip-audit, safety | PyPI Advisory |
| JavaScript | npm audit | npm Advisory |
| R | oysteR | R Advisory |
| Go | govulncheck | Go Vuln DB |
| Rust | cargo audit | RustSec |

## Options

- `--fix` - Auto-fix where possible
- `--json` - Output as JSON
- `--ignore <CVE>` - Ignore specific CVE
- `--fail-on <level>` - Fail on severity level

## Examples

```bash
# Run security audit
/craft:code:deps-audit

# Auto-fix vulnerabilities
/craft:code:deps-audit --fix

# CI mode - fail on high severity
/craft:code:deps-audit --fail-on high

# Ignore known false positive
/craft:code:deps-audit --ignore CVE-2023-1234
```

## Output

```
Security audit...

CRITICAL (1):
  requests 2.28.0
    CVE-2023-32681 - Unintended leak of Proxy-Auth header
    Fix: upgrade to >= 2.31.0

HIGH (0):
  None

MEDIUM (2):
  numpy 1.24.0
    CVE-2023-XXXX - Buffer overflow in...
    Fix: upgrade to >= 1.25.0

  pillow 9.4.0
    CVE-2023-YYYY - DoS via crafted image
    Fix: upgrade to >= 9.5.0

Summary: 1 critical, 0 high, 2 medium, 0 low
Run with --fix to auto-fix
```

## Integration

Works with:
- `/craft:code:deps-check` - Dependency health
- `/craft:code:ci-local` - Pre-commit checks
- `/craft:code:release` - Release validation
