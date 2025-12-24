---
name: rforge:doc-check
description: Check for documentation drift and inconsistencies across packages
---

# /rforge:doc-check - Documentation Drift Checker

Check for documentation inconsistencies and drift across your R package ecosystem.

## What It Does

Uses the `rforge_doc_check` MCP tool to:
- Verify NEWS.md completeness
- Check API contract consistency
- Find outdated examples
- Identify missing documentation
- Cross-reference vignettes

## Usage

```bash
# Check all documentation
/rforge:doc-check

# Check specific package
/rforge:doc-check medfit

# Detailed check with examples
/rforge:doc-check --detailed
```

## Output

Returns documentation audit with:
- **NEWS.md Status**: Up-to-date or needs entries
- **API Contracts**: Consistency across packages
- **Examples**: Outdated or broken examples
- **Vignettes**: Cross-references and accuracy
- **Recommendations**: What to update

## Examples

### Clean Documentation
```
📝 DOCUMENTATION CHECK

NEWS.md: ✅ Current (last entry: 2025-01-15)
API Contracts: ✅ Consistent across ecosystem
Examples: ✅ All working
Vignettes: ✅ Up-to-date

Status: EXCELLENT
No action needed.
```

### Documentation Drift
```
⚠️ DOCUMENTATION CHECK

NEWS.md: ⚠️ Missing 3 recent changes
  • extract_mediation refactor (2025-01-10)
  • New bootstrap method (2025-01-08)
  • Bug fix #234 (2025-01-05)

API Contracts: ❌ Inconsistency detected
  • probmed expects old signature
  • medsim docs reference deprecated function

Examples: ⚠️ 2 outdated
  • README example uses old API
  • Vignette 2 has broken code

Recommendations:
  1. Update NEWS.md (5 min)
  2. Fix probmed function calls (15 min)
  3. Update examples (20 min)
  4. Regenerate vignettes (10 min)

Total work: ~50 minutes
```

## Use When

- Before releases
- After API changes
- During code reviews
- Maintaining ecosystem health

## Related Commands

- `/rforge:status` - Overall health check
- `/rforge:impact` - See change impact
- `/rforge:cascade` - Plan documentation updates
