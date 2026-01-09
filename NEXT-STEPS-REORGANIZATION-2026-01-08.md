# Plugin Reorganization - Next Steps

**Generated:** 2026-01-08
**Context:** Product strategy analysis complete, ready for execution decisions

---

## Quick Decision Summary

| Question | Recommendation | Rationale |
|----------|----------------|-----------|
| Keep monorepo or split? | **Keep monorepo** | Weekly cross-plugin changes, shared infra |
| Merge workflow+craft? | **Yes** | Same persona, complementary features |
| research-teaching MVP scope? | **14 existing + 3 teaching commands** | Bootstrap fast, iterate later |
| Migration approach? | **Wizard script** | Automated, low user effort |

---

## Recommended Next Steps

### Option A: Start Phase 1 Now (2-4 hours)

Create research-teaching skeleton immediately.

```bash
# Actions:
1. mkdir -p research-teaching/.claude-plugin
2. Copy statistical-research commands/skills/lib
3. Create basic install.sh
4. Create plugin.json
5. Test installation

# Expected outcome:
- Working research-teaching plugin
- All 14 existing commands functional
- Ready for teaching command additions
```

**Why now?**
- Lowest risk phase
- Validates migration approach
- Immediate progress visible

---

### Option B: Deeper Planning First (1-2 hours)

Before coding, finalize:

1. **Command namespace decisions**
   - Keep `/research:manuscript:*` or simplify to `/manuscript:*`?
   - Teaching command names: `/teaching:*` or `/teach:*`?

2. **Shared code strategy**
   - Create `shared/` package for common utilities?
   - Or keep lib/ duplicated in each plugin?

3. **Documentation architecture**
   - Separate docs site per product?
   - Or unified site with clear sections (current)?

**Why wait?**
- Avoid rework from namespace changes
- Clearer architecture decisions upfront

---

### Option C: User Research First (1 hour)

Validate assumptions before building:

1. **Self-assessment questions:**
   - How often do you actually use statistical-research commands?
   - Which teaching workflows would save most time?
   - What's the #1 maintenance pain point today?

2. **Review existing usage:**
   - Check which commands have most recent updates
   - Identify which skills are actually activated

**Why validate?**
- Ensure building what's actually needed
- Might discover different priorities

---

## Quick Wins (< 30 min each)

### 1. Create research-teaching directory (15 min)

```bash
cd /Users/dt/projects/dev-tools/claude-plugins
mkdir -p research-teaching/{.claude-plugin,commands,skills,lib,scripts,tests}
```

### 2. Draft plugin.json (10 min)

```json
{
  "name": "research-teaching",
  "version": "1.0.0",
  "description": "Academic workflow - literature review, manuscript writing, teaching materials",
  "author": {
    "name": "Data-Wise"
  }
}
```

### 3. Create migration checklist (15 min)

Add to `.STATUS` or separate file tracking what needs to migrate.

---

## Long-term Items (Future sessions)

- [ ] Build teaching commands (Phase 3)
- [ ] Merge workflow into craft (Phase 2)
- [ ] User announcement draft
- [ ] Migration wizard implementation
- [ ] Documentation consolidation

---

## Files Created This Session

| File | Purpose |
|------|---------|
| `docs/specs/PRODUCT-STRATEGY-plugin-reorganization-2026-01-08.md` | Full strategy analysis (650+ lines) |
| `NEXT-STEPS-REORGANIZATION-2026-01-08.md` | This action-oriented summary |

---

## My Recommendation

**Start with Option A (Phase 1)** because:

1. Low risk - just copying existing code
2. Validates the migration approach
3. Creates visible progress
4. Can iterate on namespace/structure later

The strategy document captures the full plan. Execution can be incremental.

---

**Ready to proceed?** Let me know which option, or if you want to discuss any aspect of the strategy first.
