---
name: rforge:impact
description: Analyze change impact across ecosystem packages
argument-hint: Optional description of changes (e.g., "Breaking API change in extract_mediation")
---

# /rforge:impact - Change Impact Analysis

Analyze the ripple effects of changes across your R package ecosystem.

## What It Does

Uses the `rforge_impact` MCP tool to:
- Identify affected packages
- Estimate cascade workload
- Find breaking changes
- Calculate update priority
- Provide mitigation strategies

## Usage

```bash
# Impact of recent changes
/rforge:impact

# Impact of specific change
/rforge:impact "Rename extract_mediation to extract_med"

# Impact for function change
/rforge:impact --function extract_mediation
```

## Output

Returns impact assessment with:
- **Severity**: LOW/MEDIUM/HIGH/CRITICAL
- **Affected Packages**: List with details
- **Cascade Workload**: Estimated time
- **Breaking Changes**: Functions/APIs affected
- **Mitigation**: Suggested strategies

## Examples

### Medium Impact
```
📊 IMPACT ANALYSIS

Severity: MEDIUM
Affected: 2 packages (probmed, medsim)

probmed:
  • 1 function call to update
  • Tests: 12 tests reference old API
  • Est. work: 2 hours

medsim:
  • 1 vignette example
  • Est. work: 1 hour

Total cascade: 3 hours
Recommended: Update & release in sequence
```

### High Impact (Breaking Change)
```
⚠️ IMPACT ANALYSIS

Severity: HIGH (Breaking change)
Affected: 3 packages + indirect

Direct Impact:
  • probmed: 5 functions, 47 test cases
  • medsim: 2 examples, 1 vignette
  • sensitivity: 1 function call

Indirect Impact:
  • mediationverse: May need meta-update

Total cascade: 8-12 hours
Recommended: Deprecation path + major version bump
```

## Use When

- Before making API changes
- Planning breaking changes
- Estimating release workload
- Coordinating ecosystem updates

## Related Commands

- `/rforge:deps` - See dependency structure
- `/rforge:cascade` - Plan coordinated updates
- `/rforge:doc-check` - Check documentation impact
