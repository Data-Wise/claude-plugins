---
name: teaching:quiz
description: Create quiz questions for course material
---

# Create Quiz

I'll help you create comprehensive quiz questions for your course material.

**Usage:** `/teaching:quiz <topic>` or `/teaching:quiz <topic> <num-questions>`

**Examples:**
- `/teaching:quiz "Linear Regression"`
- `/teaching:quiz "Confidence Intervals" 10`
- `/teaching:quiz "ANOVA" 15 --difficulty mixed`
- `/teaching:quiz "Sampling" 8 --format canvas`

<system>
## Implementation

Generate quiz questions with:
1. **Multiple choice questions** (primary format)
2. **True/False questions** (quick checks)
3. **Short answer questions** (for deeper understanding)
4. **Calculation problems** (for quantitative topics)
5. **Answer key** with explanations
6. **Learning objective tags** (map to course objectives)

### Question Structure Template

```markdown
# Quiz: [Topic Name]

**Instructions:** Select the best answer for each question.

---

## Question 1 (Multiple Choice)

[Question text with clear stem]

A) [Distractor 1]
B) [Correct answer]
C) [Distractor 2]
D) [Distractor 3]

**Answer:** B
**Explanation:** [Why B is correct and others are wrong]
**Learning Objective:** [LO reference]
**Difficulty:** [Easy/Medium/Hard]

---

## Question 2 (True/False)

[Statement to evaluate]

**Answer:** True
**Explanation:** [Reasoning]

---

## Question 3 (Short Answer)

[Question requiring written response]

**Sample Answer:** [Expected response with key points]
**Grading Rubric:**
- Full credit (2 pts): [Criteria]
- Partial credit (1 pt): [Criteria]

---

## Question 4 (Calculation)

[Problem with numerical answer]

**Answer:** [Numerical result]
**Solution Steps:**
1. [Step 1]
2. [Step 2]
3. [Final answer]
```

### Question Type Distribution

Default mix for a 10-question quiz:
- **6 Multiple Choice** (60%) - Test conceptual understanding
- **2 True/False** (20%) - Quick fact checks
- **1 Short Answer** (10%) - Deeper understanding
- **1 Calculation** (10%) - Applied problem solving

Adjust based on topic and course level.

### Difficulty Levels

**Easy (Knowledge):**
- Recall definitions
- Identify examples
- State facts

**Medium (Comprehension/Application):**
- Explain concepts
- Apply formulas
- Interpret results
- Compare/contrast

**Hard (Analysis/Synthesis):**
- Analyze scenarios
- Design studies
- Critique approaches
- Create solutions

Default: 40% easy, 40% medium, 20% hard

### Distractor Design (Multiple Choice)

Create effective distractors:
1. **Plausible but incorrect** - Not obviously wrong
2. **Common misconceptions** - Address typical errors
3. **Partial understanding** - For students who know some material
4. **Similar wording** - Test careful reading

Avoid:
- "All of the above" or "None of the above"
- Obvious patterns in answer keys (e.g., all B's)
- Trick questions with subtle wording traps

### Format Options

Support multiple quiz formats:
- **Markdown** (default) - Human-readable, version-controllable
- **Canvas LMS** - Canvas quiz import format (QTI)
- **Moodle** - Moodle XML format
- **Google Forms** - Structured format for Google Forms
- **PDF** - Printable format with answer key separate
- **LaTeX** - Exam document class

### Best Practices

1. **Clear questions**: Avoid ambiguous wording
2. **One correct answer**: No debatable "best" answers
3. **Consistent difficulty**: Mix throughout quiz
4. **Fair distractors**: All options should seem reasonable
5. **Explanations**: Include reasoning for correct answers
6. **Time estimate**: 1-2 minutes per question
7. **Alignment**: Map questions to learning objectives

### Question Bank Features

Optionally generate:
- **Question pool** - More questions than needed for randomization
- **Difficulty ratings** - Tag each question
- **Topic tags** - For filtering and selection
- **Version variants** - Multiple versions of same quiz

## Follow-up Actions

After generating quiz, offer:
- Create answer key (separate document)
- Generate quiz variants (different question order)
- Create study guide based on quiz topics
- Generate similar practice questions
- Export to specific LMS format
- Create rubric for short answer questions

## Related Commands

- `/teaching:exam` - Create comprehensive exams
- `/teaching:rubric` - Generate grading rubrics
- `/teaching:slides` - Create lecture slides
- `/teaching:feedback` - Generate student feedback
</system>
