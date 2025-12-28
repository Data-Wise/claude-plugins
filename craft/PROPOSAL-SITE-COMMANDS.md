# Proposal: New Site Reorganization Commands

**Generated:** 2025-12-28
**Context:** Based on aiterm docs reorganization session

---

## Gap Analysis

What we just did manually that craft doesn't automate yet:

| Task | Current Solution | Gap |
|------|------------------|-----|
| Navigation reorganization | Manual mkdocs.yml editing | No command |
| Content audit | Manual file review | No command |
| Content consolidation | Manual merge | No command |
| Prompt generation | Manual writing | No command |
| Ongoing maintenance plan | Manual planning | No command |

---

## Proposal A: Single Command (Minimal)

### `/craft:site:reorganize`

**One command that does it all:**

```bash
/craft:site:reorganize              # Full reorganization wizard
/craft:site:reorganize nav          # Navigation only
/craft:site:reorganize audit        # Content audit only
/craft:site:reorganize --prompt     # Generate prompt for future use
```

**Covers:**
- Navigation restructuring (max 7 sections, ADHD-friendly)
- Content inventory with status
- Duplicate detection
- Implementation phases
- Saves proposal file

**Pros:**
- Single command to learn
- Unified workflow

**Cons:**
- Large command scope
- Harder to use incrementally

---

## Proposal B: Command Family (Recommended)

### Add 4 New Commands

#### 1. `/craft:site:nav` - Navigation Reorganization

```bash
/craft:site:nav                     # Analyze and propose new nav
/craft:site:nav --apply             # Apply proposed changes
/craft:site:nav --adhd              # Enforce ADHD-friendly limits (7 sections)
/craft:site:nav --preview           # Show diff without applying
```

**Features:**
- Analyzes current mkdocs.yml nav
- Detects issues (too many sections, duplicates, buried content)
- Proposes ADHD-friendly structure
- Generates YAML for new nav

#### 2. `/craft:site:audit` - Content Inventory

```bash
/craft:site:audit                   # Full content audit
/craft:site:audit --outdated        # Focus on outdated content
/craft:site:audit --duplicates      # Focus on duplicates
/craft:site:audit --gaps            # Focus on missing content
```

**Features:**
- Inventories all docs with status (current/outdated/duplicate/incomplete)
- Checks version numbers against project version
- Detects duplicate/overlapping content
- Identifies gaps (missing docs)
- Outputs markdown table

#### 3. `/craft:site:consolidate` - Merge Duplicate Content

```bash
/craft:site:consolidate             # Interactive merge wizard
/craft:site:consolidate FILE1 FILE2 # Merge specific files
/craft:site:consolidate --preview   # Show what would be merged
```

**Features:**
- Detects files with overlapping content
- Proposes merge strategy
- Handles redirects
- Updates nav and internal links

#### 4. `/craft:docs:prompt` - Generate Maintenance Prompts

```bash
/craft:docs:prompt reorganize       # Generate docs reorganization prompt
/craft:docs:prompt audit            # Generate content audit prompt
/craft:docs:prompt edit FILE        # Generate editing prompt for specific file
/craft:docs:prompt full             # Generate complete maintenance prompt
```

**Features:**
- Generates reusable prompt templates
- Fills in project-specific details
- Saves to project for future use
- ADHD-friendly format

---

## Proposal C: Skill-Based (Lightweight)

### Add 2 Skills Instead of Commands

#### `site-reorganizer` Skill

**Triggers:** "reorganize site", "restructure nav", "ADHD-friendly docs"

```markdown
# site-reorganizer Skill

Expert in documentation site reorganization with ADHD-friendly design.

## Capabilities
- Navigation analysis and restructuring
- Content inventory and audit
- ADHD-friendly design principles (max 7 sections)
- Progressive disclosure patterns

## When Triggered
Provide:
1. Current nav analysis
2. Issue detection
3. Proposed structure
4. Implementation phases
```

#### `content-auditor` Skill

**Triggers:** "audit docs", "content inventory", "find outdated docs"

```markdown
# content-auditor Skill

Expert in documentation content auditing and maintenance.

## Capabilities
- Content currency checking
- Duplicate detection
- Gap analysis
- Version number validation
- Maintenance planning
```

---

## Recommendation

**Proposal B (Command Family)** is recommended because:

1. **Incremental** - Can use one command without learning all
2. **Composable** - Commands work together in workflows
3. **Focused** - Each command has clear purpose
4. **ADHD-friendly** - Small, focused tools

### Suggested Implementation Order

| Priority | Command | Effort | Why First |
|----------|---------|--------|-----------|
| 1 | `/craft:site:nav` | 2 hours | Most immediate need |
| 2 | `/craft:site:audit` | 2 hours | Enables maintenance |
| 3 | `/craft:docs:prompt` | 1 hour | Reusable templates |
| 4 | `/craft:site:consolidate` | 3 hours | Less frequent need |

### Integration with Existing Commands

```
/craft:site:create       # Create new site
/craft:site:update       # Update content from code
/craft:site:status       # Dashboard
/craft:site:theme        # Change theme
/craft:site:add          # Add new pages
/craft:site:build        # Build
/craft:site:preview      # Preview
/craft:site:deploy       # Deploy

# NEW
/craft:site:nav          # Reorganize navigation
/craft:site:audit        # Content inventory
/craft:site:consolidate  # Merge duplicates

# In /craft:docs:
/craft:docs:prompt       # Generate maintenance prompts
```

---

## Workflow Example

```bash
# Quarterly docs maintenance workflow
/craft:site:audit                  # See what needs attention
/craft:site:nav --adhd             # Check nav structure
/craft:site:consolidate --preview  # See what can be merged
/craft:site:update full            # Update all content
/craft:site:deploy                 # Push to production

# Generate prompt for future sessions
/craft:docs:prompt full            # Save reusable prompt
```

---

## Next Steps

1. [ ] Review this proposal
2. [ ] Choose approach (A, B, or C)
3. [ ] Implement priority 1 command
4. [ ] Test with aiterm project
5. [ ] Release in craft v1.9.0
