---
name: rforge:release
description: Plan CRAN submission sequence based on dependencies
argument-hint: Optional package name or version
---

# /rforge:release - CRAN Release Planner

Plan the optimal CRAN submission sequence for your R package ecosystem.

## What It Does

Uses the `rforge_release_plan` MCP tool to:
- Calculate submission order
- Identify blockers
- Check readiness
- Estimate approval timeline
- Generate submission checklist

## Usage

```bash
# Plan release for ecosystem
/rforge:release

# Plan for specific package
/rforge:release medfit

# Detailed release plan
/rforge:release --detailed
```

## Output

Returns release plan with:
- **Submission Order**: Dependency-based sequence
- **Readiness Check**: Per-package status
- **Blockers**: What's preventing releases
- **Timeline**: Expected approval dates
- **Checklist**: Pre-submission tasks

## Examples

### Simple Release Plan
```
🚀 CRAN RELEASE PLAN

Submission Order (by dependency):
1. medfit v2.2.0
   Status: ✅ Ready
   Blockers: None
   Submit: Now

2. probmed v1.5.0
   Status: ⏳ Waiting (needs medfit on CRAN)
   Blockers: medfit not yet approved
   Submit: +2 weeks (after medfit approval)

3. medsim v1.3.0
   Status: ⏳ Waiting
   Submit: +2 weeks

4. mediationverse v1.1.0
   Status: ⏳ Waiting (needs all deps)
   Submit: +4 weeks

Timeline: 4-6 weeks total
```

### Complex Release (With Blockers)
```
⚠️ CRAN RELEASE PLAN

Submission Order:
1. medfit v2.2.0
   Status: ❌ NOT READY
   Blockers:
     • 3 failing tests
     • NEWS.md incomplete
     • R CMD check has 1 NOTE
   Fix time: ~4 hours

2. probmed v1.5.0
   Status: ✅ Ready (but blocked by medfit)
   Blockers: Waiting for medfit

3-4. [Waiting for previous]

Recommendations:
  1. Fix medfit blockers (4 hours)
  2. Submit medfit
  3. Wait for approval (~2 weeks)
  4. Submit dependents in parallel
  5. Wait for approvals (~2 weeks)
  6. Submit meta-package

Total timeline: 5-7 weeks
```

## Use When

- Planning major releases
- Coordinating ecosystem updates
- Before CRAN submissions
- Managing versioning strategy

## Related Commands

- `/rforge:status` - Check readiness
- `/rforge:cascade` - Plan updates
- `/rforge:deps` - See dependency order
