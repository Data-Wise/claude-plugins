# SPEC: Documentation Standards Update

**Status:** draft
**Created:** 2026-01-09
**Reference:** flow-cli DOCUMENTATION-MAKING-GUIDE.md
**Priority:** MEDIUM
**Effort:** 3-4 hours
**Target Completion:** 2026-01-10

---

## Overview

Update claude-plugins documentation to adopt flow-cli's proven ADHD-friendly documentation standards, including proper markdown spacing, template markers, and footer standards.

**Problem Statement:**
Current plugin documentation (Phase 2/3 complete) lacks consistent formatting standards, has spacing issues (128 instances), and doesn't use template markers or standard footers that improve scannability and maintenance.

**Solution:**
Apply flow-cli's DOCUMENTATION-MAKING-GUIDE.md standards to claude-plugins documentation.

---

## Standards to Adopt

### 1. Template Markers

**From flow-cli:**
```markdown
> Brief description of what this document provides
```

**Requirements:**
- Blockquote format (`>`)
- One sentence, under 15 words
- Clear, action-oriented, specific
- Located after title, before content

**Examples:**
```markdown
✅ Good:
> Complete R package ecosystem orchestrator with 15 commands

✅ Good:
> Statistical research toolkit for literature, manuscripts, and simulations

❌ Bad:
> This document describes RForge

❌ Bad (too long):
> This is a comprehensive guide to using the RForge plugin for managing R package ecosystems
```

### 2. Standard Footers

**From flow-cli:**
```markdown
---

**Last Updated:** YYYY-MM-DD
**Document Version:** vX.Y.Z
**Status:** ✅ Production ready with [key features]
```

**Status Formats:**
- `✅ Production ready with [feature1, feature2, feature3]`
- `🚧 Beta - [known limitations]`
- `📝 Draft - [completion status]`

**Apply to:**
- Plugin landing pages (docs/plugins/*.md)
- Plugin-specific docs (*/docs/*.md)
- Major guides (docs/MODE-USAGE-GUIDE.md, etc.)

### 3. Markdown List Spacing

**Rule:** Always add blank line before and after lists

**From flow-cli:**
```markdown
✅ Good:
### Heading

Content paragraph.

- List item 1
- List item 2

Next paragraph or heading.

❌ Bad:
### Heading
- List item 1
- List item 2
### Next Heading
```

**Affected Files:** 128 instances across all documentation

### 4. Synopsis Sections (Commands)

**From flow-cli:**
```markdown
## Synopsis

```bash
command [OPTIONS] [ARGUMENTS]
```

**Quick examples:**
```bash
# Most common usage
command arg

# With options
command --option arg
```
```

**Apply to:**
- Command reference pages
- Plugin commands documentation

### 5. See Also Sections

**From flow-cli:**
```markdown
## See Also

- **Command:** [Related Command](../commands/related.md) - Why it's related
- **Tutorial:** [Tutorial Name](../tutorials/01-name.md) - What it teaches
- **Reference:** [Reference Name](../reference/NAME.md) - What it documents
```

**Format:** Category prefix, link, brief context

---

## Implementation Phases

### Phase 1: Fix Markdown Spacing (1 hour)

**Fix 128 spacing issues:**

```python
# Automated fix script
for file in all_md_files:
    lines = read_file(file)
    for i, line in enumerate(lines):
        # Add blank line after header before list
        if is_header(line) and is_list(lines[i+1]):
            insert_blank_line(i+1)

        # Add blank line after list before header
        if is_list(line) and is_header(lines[i+1]):
            insert_blank_line(i+1)
    write_file(file, lines)
```

**Files affected:** All .md files in docs/ and plugin docs/
**Validation:** `mkdocs build` should still succeed

### Phase 2: Add Template Markers (1 hour)

**Apply to plugin landing pages:**

```markdown
# Before:
# RForge - R Package Ecosystem Management

**Version:** 1.1.0 | **Status:** Production-Ready

Complete R package ecosystem orchestrator...

# After:
# RForge - R Package Ecosystem Management

> Complete R package ecosystem orchestrator with 15 commands for dependency analysis and release planning

**Version:** 1.1.0 | **Status:** Production-Ready

RForge is a comprehensive R package development toolkit...
```

**Files affected:**
- docs/plugins/rforge.md
- docs/plugins/craft.md
- docs/plugins/workflow.md
- docs/plugins/statistical-research.md
- docs/plugins/index.md

### Phase 3: Add Standard Footers (1-1.5 hours)

**Apply to all plugin documentation:**

```markdown
---

**Last Updated:** 2026-01-09
**Document Version:** v1.1.0
**Status:** ✅ Production ready with mode system, parallel execution, and comprehensive analysis
```

**Files affected:**
- Plugin landing pages (5 files)
- Plugin-specific docs (13 files)
- Major guides (MODE-USAGE-GUIDE.md, PUBLISHING.md, etc.)

### Phase 4: Update Spec Document (30 min)

**Update SPEC-documentation-architecture-2026-01-09.md:**
- Add "Documentation Standards" section
- Reference flow-cli DOCUMENTATION-MAKING-GUIDE.md
- Document template markers, footers, spacing rules
- Add validation checklist

---

## Quality Standards Checklist

### Template Marker
- [ ] Present at top of document after title
- [ ] Uses blockquote format (`>`)
- [ ] One sentence, under 15 words
- [ ] Clear, specific, action-oriented

### Standard Footer
- [ ] Present at end of document
- [ ] Horizontal rule separator (`---`)
- [ ] Last Updated date (YYYY-MM-DD)
- [ ] Document/Plugin Version
- [ ] Status line with key features (1-3 max)
- [ ] Emoji status indicator (✅/🚧/📝)

### Markdown Spacing
- [ ] Blank line after header before list
- [ ] Blank line after list before header
- [ ] Blank line after list before paragraph
- [ ] No spacing issues detected by checker

### Content Quality
- [ ] Headers create logical hierarchy
- [ ] Examples before explanations
- [ ] Consistent terminology
- [ ] No broken internal links

---

## Validation

### Automated Checks

```bash
# 1. Check spacing
python3 scripts/check-markdown-spacing.py

# 2. Check template compliance
python3 scripts/check-template-compliance.py

# 3. Build documentation
mkdocs build

# 4. Validate links
mkdocs build --strict
```

### Manual Checks

- [ ] Spot-check 5 random files for formatting
- [ ] Verify template markers are descriptive
- [ ] Check footers have correct dates/versions
- [ ] Verify status indicators match plugin state

---

## Success Criteria

- [ ] Zero spacing issues (currently 128)
- [ ] 100% template marker coverage (landing pages + plugin docs)
- [ ] 100% footer coverage (landing pages + plugin docs)
- [ ] `mkdocs build` succeeds
- [ ] Documentation deploys successfully
- [ ] Spec document updated with standards

---

## Files to Update

### Phase 1: Spacing (128 files)
- All .md files in docs/
- All .md files in plugin docs/ directories

### Phase 2: Template Markers (5 files)
- docs/plugins/index.md
- docs/plugins/rforge.md
- docs/plugins/craft.md
- docs/plugins/workflow.md
- docs/plugins/statistical-research.md

### Phase 3: Footers (18+ files)
- Plugin landing pages (5)
- RForge docs (3)
- Craft docs (4)
- Statistical Research docs (4)
- Workflow docs (2)
- Major guides (MODE-USAGE-GUIDE.md, PUBLISHING.md, etc.)

---

## Reference

**flow-cli Standards:**
- `~/projects/dev-tools/flow-cli/docs/conventions/DOCUMENTATION-MAKING-GUIDE.md`
- `~/projects/dev-tools/flow-cli/docs/conventions/adhd/HELP-PAGE-TEMPLATE.md`
- `~/projects/dev-tools/flow-cli/docs/conventions/adhd/REFCARD-TEMPLATE.md`

**Current Documentation:**
- `docs/specs/SPEC-documentation-architecture-2026-01-09.md`
- `.STATUS` (documentation progress)

---

**Last Updated:** 2026-01-09
**Spec Version:** 1.0.0
**Status:** 📝 Draft - Ready for implementation
