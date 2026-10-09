---
name: ecosystem-health
description: Run a comprehensive health check across the MediationVerse R package ecosystem.
---

# Ecosystem Health Check

You are conducting a comprehensive health check of the MediationVerse R package ecosystem.

## MediationVerse Packages

| Package | Path | Purpose |
|---------|------|---------|
| medfit | ~/R-packages/active/medfit | Foundation (fitting, extraction, bootstrap) |
| probmed | ~/R-packages/active/probmed | P_med probabilistic effect size |
| rmediation | ~/R-packages/active/rmediation | Confidence intervals (PRODCLIN) |
| medrobust | ~/R-packages/active/medrobust | Sensitivity analysis |
| medsim | ~/R-packages/active/medsim | Simulation infrastructure |
| mediationverse | ~/R-packages/active/mediationverse | Meta-package |

## Health Check Process

### Step 1: Package Status
For each package, check:
- [ ] R CMD check status (use r_check tool if available)
- [ ] Test coverage (aim for >80%)
- [ ] Documentation completeness
- [ ] DESCRIPTION version and dependencies

### Step 2: Dependency Analysis
- Check inter-package dependencies
- Identify version conflicts
- Verify dependency chain is correct:
  ```
  medfit (foundation)
    ├── probmed (depends on medfit)
    ├── rmediation (standalone, may use medfit)
    ├── medrobust (depends on medfit)
    └── medsim (depends on medfit, probmed)
  mediationverse (imports all)
  ```

### Step 3: API Consistency
- Are S7 class definitions consistent across packages?
- Do function signatures follow conventions?
- Is documentation style consistent?

### Step 4: Test Integration
- Do cross-package workflows work?
- Are integration tests passing?

### Step 5: Documentation
- Are pkgdown sites building?
- Is the ecosystem navigation correct?
- Are vignettes up to date?

## Output Format

```markdown
## MediationVerse Ecosystem Health Report
**Date**: [Date]

### Summary Dashboard
| Package | R CMD Check | Coverage | Docs | Version |
|---------|-------------|----------|------|---------|
| medfit  | ✓/⚠/✗      | XX%      | ✓/⚠  | X.Y.Z   |
| probmed | ...         | ...      | ...  | ...     |
| ...     | ...         | ...      | ...  | ...     |

### Overall Status: 🟢 Healthy / 🟡 Needs Attention / 🔴 Issues

### Detailed Findings

#### medfit
- **Status**: [Summary]
- **Issues**: [List any problems]
- **Action needed**: [Recommended fixes]

[Repeat for each package]

### Dependency Graph
[ASCII or description of current dependency state]

### Cross-Package Issues
[Any issues that span multiple packages]

### Recommendations
1. **Immediate**: [Urgent fixes]
2. **Short-term**: [Should address soon]
3. **Long-term**: [Future improvements]

### Next Steps
[Specific action items with priorities]
```

## Skills to Apply
- r-package-development
- statistical-research-workflow

## Tools to Use
- r_check (for each package)
- r_test (for each package)
- Read (for DESCRIPTION files)
- Glob (for finding test files)
