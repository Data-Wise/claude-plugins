---
name: rforge:status
description: Ecosystem-wide status dashboard showing health, tests, and readiness
---

# /rforge:status - Status Dashboard

Get a comprehensive status dashboard for your R package ecosystem.

## What It Does

Uses the `rforge_status` MCP tool to provide:
- Package health scores
- Test results and coverage
- CRAN check status
- Documentation completeness
- Version information

## Usage

```bash
# Status for current package/ecosystem
/rforge:status

# Status for specific package
/rforge:status medfit

# Detailed status
/rforge:status --detailed
```

## Output

Returns dashboard with:
- **Health Score**: 0-100 overall rating
- **Tests**: Pass/fail counts and coverage %
- **CRAN**: Check results (OK/NOTE/WARNING/ERROR)
- **Docs**: Documentation completeness
- **Dependencies**: Dependency health

## Examples

### Single Package
```
📊 STATUS: medfit v2.1.0

Health: 92/100 (A-)
Tests: 187/187 passing (94% coverage)
CRAN: ✅ All checks OK
Docs: ⚠️ NEWS.md needs update
Dependencies: ✅ All current
```

### Ecosystem
```
📊 STATUS: mediationverse ecosystem

Overall Health: 87/100 (B+)

medfit:           92/100 ✅
probmed:          88/100 ✅
medsim:           82/100 ⚠️
mediationverse:   91/100 ✅

Issues: 2 packages need doc updates
```

## Use When

- Daily development check-in
- Before committing changes
- Planning releases
- Monitoring ecosystem health

## Related Commands

- `/rforge:detect` - Find packages first
- `/rforge:doc-check` - Detailed doc analysis
- `/rforge:analyze` - Full analysis with recommendations
