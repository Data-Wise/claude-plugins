---
name: teaching:rubric
description: Generate grading rubrics for assignments and assessments
---

# Create Grading Rubric

I'll help you create a clear, detailed grading rubric for assignments, projects, or assessments.

**Usage:** `/teaching:rubric <assignment-type>` or `/teaching:rubric <assignment-type> <points>`

**Examples:**
- `/teaching:rubric "data analysis project"`
- `/teaching:rubric "research paper" 100`

## What type of assignment needs a rubric?

Provide the assignment type and optionally the total points.

<system>
This command generates detailed grading rubrics with:
- Clear criteria for each performance level
- Point allocations
- Multiple assessment dimensions
- Objective and subjective criteria balanced

## Implementation

The command should:

1. **Gather Information** - Ask user for:
   - Assignment type (homework, project, paper, presentation, exam)
   - Total points
   - Key criteria to assess
   - Number of performance levels (3-5 typical)
   - Emphasis areas (technical skills, communication, creativity, etc.)

2. **Generate Rubric Structure**:

   **Format 1: Traditional Grid Rubric**
   ```markdown
   # Grading Rubric: [Assignment Name]

   **Total Points:** [X]

   ## Rubric

   | Criterion | Excellent (A) | Proficient (B) | Developing (C) | Needs Work (D) | Points |
   |-----------|---------------|----------------|----------------|----------------|--------|
   | [Criterion 1] | [A descriptor] | [B descriptor] | [C descriptor] | [D descriptor] | X pts |
   | [Criterion 2] | [A descriptor] | [B descriptor] | [C descriptor] | [D descriptor] | X pts |
   ...

   ## Criterion Descriptions

   ### [Criterion 1] ([Points] points)
   - **Excellent (90-100%):** [Detailed description]
   - **Proficient (80-89%):** [Detailed description]
   - **Developing (70-79%):** [Detailed description]
   - **Needs Work (<70%):** [Detailed description]
   ```

   **Format 2: Analytic Rubric with Point Ranges**
   ```markdown
   # Grading Rubric: [Assignment Name]

   ## [Criterion 1]: [Title] ([Total Points] points)

   ### Outstanding ([X-Y] points)
   - [Specific descriptor 1]
   - [Specific descriptor 2]
   - [Specific descriptor 3]

   ### Good ([X-Y] points)
   - [Specific descriptor 1]
   - [Specific descriptor 2]

   ### Satisfactory ([X-Y] points)
   - [Specific descriptor 1]
   - [Specific descriptor 2]

   ### Needs Improvement ([X-Y] points)
   - [Specific descriptor]

   ---

   ## [Criterion 2]: [Title] ([Total Points] points)
   ...
   ```

3. **Common Assessment Criteria by Assignment Type**:

   **Data Analysis Project:**
   - Code quality and organization (reproducibility, comments, efficiency)
   - Statistical methodology (appropriate methods, assumptions checked)
   - Interpretation and communication (correct interpretation, clear writing)
   - Visualizations (appropriate plots, clear labels, publication-quality)
   - Technical accuracy (correct calculations, proper tests)

   **Research Paper:**
   - Introduction and motivation (clear research question, lit review)
   - Methodology (appropriate methods, well-described procedures)
   - Results and analysis (thorough analysis, appropriate presentation)
   - Discussion and conclusions (interpretation, limitations, implications)
   - Writing quality (organization, clarity, grammar, citations)

   **Presentation:**
   - Content knowledge (accuracy, depth, coverage)
   - Organization and structure (logical flow, clear introduction/conclusion)
   - Delivery (clarity, pace, eye contact, confidence)
   - Visual aids (quality of slides, effective use of graphics)
   - Audience engagement (handles questions, interactive elements)

   **Problem Set:**
   - Correctness (accurate solutions, appropriate methods)
   - Work shown (clear steps, justification of approach)
   - Interpretation (correct interpretation of results)
   - Presentation (organized, readable, professional)

4. **Point Allocation Guidance**:
   - **Technical correctness:** 40-50% (for quantitative work)
   - **Communication/presentation:** 20-30%
   - **Analysis/interpretation:** 20-30%
   - **Creativity/originality:** 5-10% (if applicable)

## Follow-up Actions

After generating the rubric, offer to:
- Create a companion assignment prompt using the rubric criteria
- Generate a self-assessment checklist for students
- Create a peer review form based on the rubric
- Provide example work at each performance level
- Export to spreadsheet for gradebook integration

## Output Format

Generate as formatted markdown table that can be:
- Shared with students before assignment
- Used for grading (print or digital)
- Imported to LMS rubric tools
- Converted to PDF

## Best Practices

Include:
- ✅ Clear, observable criteria (not vague)
- ✅ Consistent point ranges across performance levels
- ✅ Both objective and subjective measures appropriately weighted
- ✅ Sufficient differentiation between levels
- ✅ Aligned with assignment learning objectives
- ✅ Criteria students can assess before submission

Avoid:
- ❌ Vague descriptors ("good", "excellent" without specifics)
- ❌ Too many criteria (overwhelming to grade, focus on key skills)
- ❌ Unequal point distributions that don't reflect importance
- ❌ Overlapping criterion definitions
- ❌ Criteria that can't be objectively assessed
- ❌ Performance levels that don't clearly distinguish quality

## Performance Level Descriptors

**Strong descriptors are:**
- Observable and measurable
- Use action verbs
- Specific to the criterion
- Distinguish clearly between levels

**Example - Weak vs. Strong:**

❌ Weak: "Good analysis"
✅ Strong: "Applies appropriate statistical methods, checks all assumptions, correctly interprets p-values and confidence intervals in context"

❌ Weak: "Nice visualizations"
✅ Strong: "Creates publication-quality plots with clear axis labels, appropriate plot types for data, and effective use of color/legends"

## Rubric Quality Checklist

Before finalizing, verify:
- [ ] Each criterion has clear descriptors for all performance levels
- [ ] Point allocations add up to total
- [ ] Most important skills have appropriate weight
- [ ] Students can understand what's expected
- [ ] Criteria are assessable given the assignment scope
- [ ] Rubric can be applied consistently across students
</system>
