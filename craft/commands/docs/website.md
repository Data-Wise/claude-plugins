# /craft:docs:website - ADHD-Friendly Website Enhancement

You are a website optimization expert specializing in ADHD-friendly documentation.

## Purpose

**One command to make any documentation site ADHD-friendly:**
1. Analyze current ADHD-friendliness score (0-100)
2. Generate enhancement plan (3 phases)
3. Execute improvements automatically
4. Validate with strict checks
5. Report measurable improvements

**Target Users:** ADHD developers seeking quick, scannable, time-estimated documentation

---

## Usage

```bash
/craft:docs:website                  # Full enhancement (all 3 phases)
/craft:docs:website --analyze        # Show ADHD score only
/craft:docs:website --phase 1        # Quick wins only (< 2 hours)
/craft:docs:website --phase 2        # Structure improvements (< 4 hours)
/craft:docs:website --phase 3        # Polish & mobile (< 8 hours)
/craft:docs:website --dry-run        # Preview changes without writing
/craft:docs:website --validate       # Validate current state
```

---

## When Invoked

### Step 0: Detect Project Type

First, determine if this is a documentation site and what framework:

```bash
# Check for MkDocs
if [ -f mkdocs.yml ]; then
  echo "✅ MkDocs detected"
  SITE_TYPE="mkdocs"
fi

# Check for Quarto
if [ -f _quarto.yml ]; then
  echo "✅ Quarto detected"
  SITE_TYPE="quarto"
fi

# Check for Sphinx
if [ -f conf.py ] && grep -q "sphinx" conf.py 2>/dev/null; then
  echo "✅ Sphinx detected"
  SITE_TYPE="sphinx"
fi

# Get project name
PROJECT_NAME=$(basename $(pwd))
```

**Supported Frameworks:**
- MkDocs Material (primary)
- Quarto (partial support)
- Sphinx (basic support)

**If unsupported:** Exit with helpful message suggesting to add support

---

### Step 1: Analyze Current State

Calculate ADHD-friendliness score using 5-category algorithm:

```
┌─────────────────────────────────────────────────────────────┐
│ 📊 ADHD-FRIENDLINESS ANALYSIS                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Project: [PROJECT_NAME]                                     │
│ Site Type: [SITE_TYPE]                                      │
│ Pages: [COUNT] markdown files                               │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ CATEGORY SCORES (0-100)                                     │
│                                                             │
│ 🎨 Visual Hierarchy (25% weight)                            │
│    Score: [SCORE]/100 [PROGRESS_BAR]                        │
│    • TL;DR boxes: [X]/[TOTAL] pages                         │
│    • Emojis in headings: [X]/[TOTAL] pages                  │
│    • Heading hierarchy: [✅/⚠️] valid                        │
│                                                             │
│ ⏱️ Time Estimates (20% weight)                              │
│    Score: [SCORE]/100 [PROGRESS_BAR]                        │
│    • Tutorials with time: [X]/[TOTAL]                       │
│    • Guides with time: [X]/[TOTAL]                          │
│                                                             │
│ 📊 Workflow Diagrams (20% weight)                           │
│    Score: [SCORE]/100 [PROGRESS_BAR]                        │
│    • Mermaid diagrams: [COUNT] found                        │
│    • Syntax errors: [COUNT] errors                          │
│    • Workflow page exists: [✅/❌]                           │
│                                                             │
│ 📱 Mobile Responsive (15% weight)                           │
│    Score: [SCORE]/100 [PROGRESS_BAR]                        │
│    • Responsive CSS: [✅/❌] present                         │
│    • Mermaid overflow: [✅/❌] fixed                         │
│    • Touch targets: [✅/⚠️] adequate                         │
│                                                             │
│ 📝 Content Density (20% weight)                             │
│    Score: [SCORE]/100 [PROGRESS_BAR]                        │
│    • Dense paragraphs: [COUNT] (>5 sentences)               │
│    • Callout boxes: [COUNT] found                           │
│    • Visual breaks: [✅/⚠️] adequate                         │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ 🎯 OVERALL ADHD SCORE: [SCORE]/100 [PROGRESS_BAR]          │
│                                                             │
│ Grade: [A/B/C/D/F]                                          │
│   A (90-100): Exemplary ADHD-friendly                       │
│   B (80-89):  Good, minor improvements needed               │
│   C (70-79):  Acceptable, some work needed                  │
│   D (60-69):  Needs significant improvement                 │
│   F (<60):    Poor ADHD accessibility                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### ADHD Scoring Algorithm

**Category 1: Visual Hierarchy (25% weight)**

```python
def score_visual_hierarchy(site):
    score = 0

    # TL;DR boxes (40 points)
    tldr_pages = count_pages_with_tldr(site)
    total_pages = count_total_pages(site, types=['guide', 'tutorial', 'reference'])
    if total_pages > 0:
        score += 40 * (tldr_pages / total_pages)

    # Emojis in headings (30 points)
    emoji_pages = count_pages_with_emoji_headings(site)
    if total_pages > 0:
        score += 30 * (emoji_pages / total_pages)

    # Valid heading hierarchy (30 points)
    if validate_heading_hierarchy(site):
        score += 30

    return min(100, score)
```

**Category 2: Time Estimates (20% weight)**

```python
def score_time_estimates(site):
    score = 0

    # Tutorials with time estimates (60 points)
    tutorials = count_tutorials(site)
    tutorials_with_time = count_tutorials_with_time(site)
    if tutorials > 0:
        score += 60 * (tutorials_with_time / tutorials)

    # Guides with time estimates (40 points)
    guides = count_guides(site)
    guides_with_time = count_guides_with_time(site)
    if guides > 0:
        score += 40 * (guides_with_time / guides)

    return min(100, score)
```

**Category 3: Workflow Diagrams (20% weight)**

```python
def score_workflow_diagrams(site):
    score = 0

    # Mermaid diagrams present (40 points)
    mermaid_count = count_mermaid_diagrams(site)
    if mermaid_count > 0:
        score += min(40, mermaid_count * 5)  # 5 points per diagram, max 40

    # No syntax errors (40 points)
    error_count = count_mermaid_errors(site)
    if mermaid_count > 0:
        error_rate = error_count / mermaid_count
        score += 40 * (1 - error_rate)  # Full points if 0 errors

    # Dedicated workflow page exists (20 points)
    if has_visual_workflows_page(site):
        score += 20

    return min(100, score)
```

**Category 4: Mobile Responsive (15% weight)**

```python
def score_mobile_responsive(site):
    score = 0

    # Responsive CSS present (40 points)
    if has_responsive_css(site):
        score += 40

    # Mermaid overflow fixed (40 points)
    if has_mermaid_overflow_fix(site):
        score += 40

    # Touch targets adequate (20 points)
    if validate_touch_targets(site):
        score += 20

    return min(100, score)
```

**Category 5: Content Density (20% weight)**

```python
def score_content_density(site):
    score = 100  # Start at 100, deduct for issues

    # Dense paragraphs (deduct up to 40 points)
    dense_paragraphs = count_dense_paragraphs(site)  # >5 sentences
    total_paragraphs = count_total_paragraphs(site)
    if total_paragraphs > 0:
        density_rate = dense_paragraphs / total_paragraphs
        score -= min(40, density_rate * 100)

    # Callout boxes (add up to 30 points if missing)
    callout_boxes = count_callout_boxes(site)
    total_pages = count_total_pages(site)
    if total_pages > 0:
        callout_rate = callout_boxes / total_pages
        if callout_rate < 0.3:  # Less than 30% of pages have callouts
            score -= 30 * (1 - (callout_rate / 0.3))

    # Visual breaks (add 30 points if adequate)
    if has_adequate_visual_breaks(site):
        score += 30

    return max(0, min(100, score))
```

**Overall Score Calculation:**

```python
def calculate_adhd_score(site):
    scores = {
        'visual_hierarchy': score_visual_hierarchy(site),
        'time_estimates': score_time_estimates(site),
        'workflow_diagrams': score_workflow_diagrams(site),
        'mobile_responsive': score_mobile_responsive(site),
        'content_density': score_content_density(site)
    }

    weights = {
        'visual_hierarchy': 0.25,
        'time_estimates': 0.20,
        'workflow_diagrams': 0.20,
        'mobile_responsive': 0.15,
        'content_density': 0.20
    }

    overall = sum(scores[k] * weights[k] for k in scores)
    return {
        'overall': round(overall),
        'breakdown': scores,
        'grade': get_grade(overall)
    }

def get_grade(score):
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'
```

---

### Step 2: Generate Enhancement Plan

Based on current score, generate phased improvement plan:

```
┌─────────────────────────────────────────────────────────────┐
│ 📋 ENHANCEMENT PLAN                                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Current Score: [CURRENT]/100 (Grade [GRADE])                │
│ Target Score: 97/100 (Grade A)                              │
│ Improvement: +[DELTA] points needed                         │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ PHASE 1: QUICK WINS ⏱️ < 2 hours                            │
│ Impact: +[POINTS] points → [NEW_SCORE]/100                  │
│                                                             │
│ [X] Fix mermaid syntax errors                               │
│     • [COUNT] errors found                                  │
│     • Validate with mkdocs build --strict                   │
│                                                             │
│ [X] Add TL;DR boxes to major pages                          │
│     • [COUNT] pages need TL;DR boxes                        │
│     • Template: What/Why/How/Next (30 seconds)              │
│                                                             │
│ [X] Add time estimates to tutorials                         │
│     • [COUNT] tutorials missing time estimates              │
│     • Format: ⏱️ X minutes • 🟢 Level • ✓ Y steps           │
│                                                             │
│ [X] Create ADHD Quick Start page                            │
│     • New top-level page: ADHD-QUICK-START.md               │
│     • First 30 seconds + Next 5 minutes + Stuck?            │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ PHASE 2: STRUCTURE ⏱️ < 4 hours                             │
│ Impact: +[POINTS] points → [NEW_SCORE]/100                  │
│                                                             │
│ [X] Create Visual Workflows page                            │
│     • New page: docs/workflows/index.md                     │
│     • 5 mermaid diagrams (onboarding, daily, context, etc)  │
│                                                             │
│ [X] Flatten navigation hierarchy                            │
│     • Move ADHD guide to top-level                          │
│     • Add Visual Workflows to main nav                      │
│                                                             │
│ [X] Add visual callout boxes                                │
│     • 💡 Pro Tip, ⚠️ Warning, ✅ Success, 🎯 ADHD-Friendly  │
│     • Apply to [COUNT] pages                                │
│                                                             │
│ [X] Homepage restructure (card-based layout)                │
│     • Hero section with 3 CTAs                              │
│     • 4 "Choose Your Path" cards                            │
│     • Feature grid (card-based)                             │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ PHASE 3: POLISH ⏱️ < 8 hours                                │
│ Impact: +[POINTS] points → [NEW_SCORE]/100                  │
│                                                             │
│ [X] Mobile responsive CSS                                   │
│     • Mermaid overflow fix                                  │
│     • Simplified mobile navigation                          │
│     • 44px touch targets                                    │
│                                                             │
│ [X] Interactive mermaid diagrams                            │
│     • Clickable nodes linking to docs                       │
│     • Zoom/pan controls                                     │
│                                                             │
│ [X] Progress indicators in tutorials                        │
│     • Step X of Y [progress bar]                            │
│     • Time remaining estimates                              │
│                                                             │
│ [X] Command playground (optional)                           │
│     • Interactive terminal demo                             │
│     • Safe, read-only commands                              │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ RECOMMENDED APPROACH:                                       │
│   → Start with Phase 1 (highest impact, lowest effort)      │
│   → Validate score improvement before Phase 2               │
│   → Phase 3 is optional polish (diminishing returns)        │
│                                                             │
│ Execute which phase? (1/2/3/all/cancel)                     │
└─────────────────────────────────────────────────────────────┘
```

---

### Step 3: Execute Phase 1 - Quick Wins

When Phase 1 selected, execute these enhancements:

#### 3.1: Fix Mermaid Syntax Errors

```bash
# Find all mermaid code blocks
find docs -name "*.md" -exec grep -l '```mermaid' {} \;

# For each file with mermaid:
# - Read the file
# - Extract mermaid blocks
# - Validate syntax (look for common errors):
#   - Missing closing ```
#   - Invalid node syntax
#   - Unclosed quotes
#   - Invalid keywords
# - Fix automatically if possible
# - Report unfixable errors
```

**Common Errors to Fix:**

| Error | Fix |
|-------|-----|
| Missing closing backticks | Add ``` at end |
| `graph TD` without nodes | Add placeholder node |
| Unclosed string `"text` | Add closing quote |
| Invalid characters in node IDs | Replace with valid chars |
| Wrong arrow syntax `--->` | Change to `-->` |

**Validation:**
```bash
# After fixes, validate with mkdocs
mkdocs build --strict 2>&1 | grep -i mermaid

# Should return no errors
```

#### 3.2: Add TL;DR Boxes

**Template:**
```markdown
> **TL;DR** (30 seconds)
> - **What:** [One sentence description]
> - **Why:** [One benefit statement]
> - **How:** [One command or one link]
> - **Next:** [One next step]
```

**Target Pages:**
- All pages in `docs/guide/`
- All pages in `docs/tutorials/`
- `docs/index.md` (homepage)
- `docs/QUICK-START.md`
- `docs/GETTING-STARTED.md`
- `docs/REFCARD.md`

**Insertion Logic:**
```python
def add_tldr_box(file_path, page_type):
    content = read_file(file_path)

    # Skip if TL;DR already exists
    if "TL;DR" in content:
        return "Already has TL;DR"

    # Extract key info from page
    heading = extract_h1(content)
    first_paragraph = extract_first_paragraph(content)

    # Generate TL;DR based on page type
    if page_type == "guide":
        what = summarize_to_one_sentence(first_paragraph)
        why = extract_benefit(content)
        how = extract_first_command_or_link(content)
        next_step = extract_next_step_from_content(content)
    elif page_type == "tutorial":
        what = f"Learn {heading} in {estimate_duration(content)} minutes"
        why = extract_learning_outcome(content)
        how = f"Run `{extract_first_command(content)}`"
        next_step = extract_next_tutorial(content)

    # Format TL;DR box
    tldr = f'''> **TL;DR** (30 seconds)
> - **What:** {what}
> - **Why:** {why}
> - **How:** {how}
> - **Next:** {next_step}

'''

    # Insert after H1, before first paragraph
    new_content = insert_after_h1(content, tldr)
    write_file(file_path, new_content)
    return "Added TL;DR"
```

#### 3.3: Add Time Estimates

**Template:**
```markdown
⏱️ **10 minutes** • 🟢 Beginner • ✓ 7 steps
```

**Target Pages:**
- All tutorial pages
- All guide pages with step-by-step instructions

**Insertion Logic:**
```python
def add_time_estimate(file_path):
    content = read_file(file_path)

    # Skip if time estimate already exists
    if "⏱️" in content or "minutes" in content[:200]:
        return "Already has time estimate"

    # Estimate duration
    word_count = count_words(content)
    code_blocks = count_code_blocks(content)
    steps = count_numbered_steps(content)

    # Formula: 2 min per 500 words + 1 min per code block + 1 min per step
    duration = (word_count / 500) * 2 + code_blocks + steps
    duration = round(duration)

    # Determine difficulty level
    if any(word in content.lower() for word in ['advanced', 'expert', 'complex']):
        level = "🔴 Advanced"
    elif any(word in content.lower() for word in ['intermediate', 'moderate']):
        level = "🔵 Intermediate"
    else:
        level = "🟢 Beginner"

    # Format time estimate
    estimate = f"⏱️ **{duration} minutes** • {level}"
    if steps > 0:
        estimate += f" • ✓ {steps} steps"
    estimate += "\n\n"

    # Insert after H1
    new_content = insert_after_h1(content, estimate)
    write_file(file_path, new_content)
    return f"Added: {estimate.strip()}"
```

#### 3.4: Create ADHD Quick Start Page

**Location:** `docs/ADHD-QUICK-START.md`

**Template:**
```markdown
# ADHD Quick Start

> Get started with [PROJECT_NAME] in **under 2 minutes**

## ⏱️ First 30 Seconds

The absolute essentials to get running:

```bash
[primary-command]     # [What it does]
[second-command]      # [What it does]
[third-command]       # [What it does]
```

## ⏱️ Next 5 Minutes

Once basics work, explore these:

- **Learn:** [Link to main tutorial]
- **Configure:** [Link to settings]
- **Status:** `[status-command]`

## 🆘 Stuck? Run These

If something's not working:

- **Diagnose:** `[diagnostic-command]`
- **Help:** `[help-command]`
- **Details:** `[info-command]`

## 🎯 ADHD-Friendly Features

This project is optimized for ADHD users:

- ⏱️ **Time estimates** on every task
- 🎨 **Visual context** cues (colors, emojis)
- 📊 **Workflow diagrams** for visual learners
- ✅ **Quick wins** highlighted first
- 🚀 **One-command** solutions when possible

## 📚 Full Documentation

Ready for more? Check out:

- [Full Getting Started Guide](GETTING-STARTED.md)
- [Reference Card](REFCARD.md)
- [Interactive Tutorials](tutorials/index.md)
- [Visual Workflows](workflows/index.md)
```

**Generation Logic:**
```python
def create_adhd_quick_start(project_name, site_type):
    # Detect primary commands from documentation
    primary_cmd = detect_primary_command(site_type)
    commands = extract_essential_commands(limit=3)

    # Generate content from template
    content = render_template("adhd-quick-start.md", {
        'project_name': project_name,
        'commands': commands,
        'tutorial_link': find_main_tutorial(),
        'settings_link': find_settings_page(),
        'status_command': detect_status_command(),
        'diagnostic_command': detect_diagnostic_command(),
        'help_command': f"{primary_cmd} --help",
        'info_command': detect_info_command()
    })

    write_file("docs/ADHD-QUICK-START.md", content)
    return "Created ADHD Quick Start page"
```

---

### Step 4: Validate Changes

After executing enhancements, validate results:

```bash
# Build site with strict mode
mkdocs build --strict 2>&1

# Check for errors
if [ $? -eq 0 ]; then
  echo "✅ Build successful"
else
  echo "❌ Build failed - review errors above"
  exit 1
fi

# Recalculate ADHD score
NEW_SCORE=$(calculate_adhd_score)

# Show improvement
echo "Score improved: $OLD_SCORE → $NEW_SCORE (+$(($NEW_SCORE - $OLD_SCORE)) points)"
```

---

### Step 5: Report Results

Show comprehensive report:

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ PHASE 1 COMPLETE - Quick Wins                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Duration: [TIME] (under 2 hours ✓)                          │
│                                                             │
│ CHANGES MADE:                                               │
│   ✓ Fixed [COUNT] mermaid syntax errors                    │
│   ✓ Added TL;DR boxes to [COUNT] pages                     │
│   ✓ Added time estimates to [COUNT] pages                  │
│   ✓ Created ADHD Quick Start page                          │
│                                                             │
│ SCORE IMPROVEMENT:                                          │
│   Before: [OLD_SCORE]/100 (Grade [OLD_GRADE])              │
│   After:  [NEW_SCORE]/100 (Grade [NEW_GRADE])              │
│   Change: +[DELTA] points ✅                                │
│                                                             │
│ CATEGORY BREAKDOWN:                                         │
│   Visual Hierarchy:   [OLD] → [NEW] (+[DELTA])             │
│   Time Estimates:     [OLD] → [NEW] (+[DELTA])             │
│   Workflow Diagrams:  [OLD] → [NEW] (+[DELTA])             │
│   Mobile Responsive:  [OLD] → [NEW] (+0, no changes yet)   │
│   Content Density:    [OLD] → [NEW] (+[DELTA])             │
│                                                             │
│ FILES MODIFIED: [COUNT]                                     │
│   [list of modified files]                                  │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ 🎯 NEXT STEPS:                                              │
│                                                             │
│ Option 1: Continue to Phase 2                               │
│   /craft:docs:website --phase 2                             │
│   Impact: +[POINTS] points (→ [SCORE]/100)                  │
│   Duration: ~4 hours                                        │
│                                                             │
│ Option 2: Stop here and validate                            │
│   mkdocs serve                    # Preview changes         │
│   mkdocs build --strict           # Validate build          │
│   mkdocs gh-deploy                # Deploy (if ready)       │
│                                                             │
│ Option 3: Get user feedback first                           │
│   Share site with ADHD users                                │
│   Measure time-to-first-success                             │
│   Iterate on Phase 1 if needed                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Integration

**Works with existing craft commands:**
- `/craft:docs:update` - Can call `--website-mode` for enhancements
- `/craft:site:status` - Shows ADHD score in output
- `/craft:docs:check` - Validates website enhancements

**Uses these internal functions:**
- `detect_site_type()` - From existing site commands
- `count_files()` - From existing analysis tools
- `validate_markdown()` - From existing validation

---

## ADHD-Friendly Features

1. **Clear Phases** - 3 distinct phases with time estimates
2. **Measurable Progress** - Numeric scores show improvement
3. **Quick Wins First** - Highest impact, lowest effort in Phase 1
4. **Preview Mode** - See changes before committing
5. **Stop Anytime** - Each phase is independent
6. **Visual Progress** - Progress bars for all scores

---

## Error Handling

```
┌─────────────────────────────────────────────────────────────┐
│ ❌ ERROR: Unsupported Site Type                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ This command currently supports:                            │
│   ✓ MkDocs Material                                         │
│   ✓ Quarto (partial)                                        │
│   ✓ Sphinx (basic)                                          │
│                                                             │
│ Your site: [DETECTED_TYPE]                                  │
│                                                             │
│ 💡 Suggestion:                                              │
│    Open an issue to request support:                        │
│    https://github.com/Data-Wise/claude-plugins/issues       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Success Criteria

This command is successful when:

- [x] Detects MkDocs Material sites accurately
- [ ] Calculates ADHD score matching spec algorithm
- [ ] Fixes common mermaid syntax errors automatically
- [ ] Generates appropriate TL;DR boxes
- [ ] Estimates task duration accurately (±20%)
- [ ] Creates ADHD Quick Start page with project-specific content
- [ ] Improves score by at least +10 points in Phase 1
- [ ] Validates with `mkdocs build --strict` passing
- [ ] Completes Phase 1 in under 2 hours

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-12-31 | Initial implementation - Phase 1 only |

---

## Next Commands to Implement

After this command works:

1. **Phase 2 implementation** - Structure enhancements
2. **Phase 3 implementation** - Polish & mobile
3. **`/craft:docs:update --website-mode`** - Integration
4. **`/craft:site:status` ADHD scoring** - Show score in output
