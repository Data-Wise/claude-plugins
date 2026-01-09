---
name: teaching:exam
description: Create comprehensive exams for course assessments
---

# Create Exam

I'll help you create a comprehensive exam with multiple question types, clear instructions, and a detailed grading rubric.

**Usage:** `/teaching:exam <exam-type> <topics>` or `/teaching:exam <exam-type> <topics> <duration-minutes>`

**Examples:**
- `/teaching:exam midterm "Chapters 1-5"`
- `/teaching:exam final "All course material" 120`
- `/teaching:exam quiz "Regression and ANOVA" 50`
- `/teaching:exam cumulative "Semester topics" 180 --format latex`

<system>
## Implementation

Generate comprehensive exam with:
1. **Cover page** - Course info, instructions, academic integrity statement
2. **Multiple sections** - Organized by question type or topic
3. **Varied question types** - Multiple choice, short answer, problems, essay
4. **Point allocation** - Clear points for each question
5. **Time guidance** - Suggested time per section
6. **Space for answers** - Adequate room for student work
7. **Grading rubric** - Detailed scoring guide

### Exam Structure Template

```markdown
# [Exam Type]: [Course Name]

**Name:** _______________________________
**Date:** [Date]
**Total Points:** [X] points
**Time:** [X] minutes

---

## Instructions

- This exam has [X] questions worth [X] total points
- Read each question carefully before answering
- Show all work for calculation problems
- Partial credit may be awarded
- No notes, books, or electronic devices allowed (or specify what's allowed)
- You have [X] minutes to complete the exam

**Academic Integrity Statement:**
By signing below, you affirm that this work is your own and that you have neither given nor received unauthorized assistance.

Signature: _________________________ Date: __________

---

## Section 1: Multiple Choice (X points)

**Instructions:** Select the best answer for each question. Each question is worth [X] points.

**1.** [Question text]

A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]

[Space for multiple choice questions]

---

## Section 2: True/False (X points)

**Instructions:** Mark T for True or F for False. Each question is worth [X] points.

**[N].** _____ [Statement to evaluate]

[Space for T/F questions]

---

## Section 3: Short Answer (X points)

**Instructions:** Answer each question in 2-3 complete sentences. Each question is worth [X] points.

**[N].** [Question requiring brief written response]

[Space for answer - approximately 4-5 lines]

**[N+1].** [Next question]

[Space for answer]

---

## Section 4: Calculation Problems (X points)

**Instructions:** Show all work for full credit. Clearly label your final answer. Partial credit will be awarded.

**[N].** [Problem statement] ([X] points)

[Space for work - approximately 1/2 page]

Final Answer: ________________

**[N+1].** [Next problem] ([X] points)

[Space for work]

---

## Section 5: Essay/Long Answer (X points)

**Instructions:** Provide a comprehensive answer to the following question. Your answer should be well-organized with clear arguments supported by evidence from course material.

**[N].** [Essay question] ([X] points)

[Space for essay - approximately 1 full page]

---

## Formula Sheet (if applicable)

[Relevant formulas provided for reference]

---

## Scratch Work (optional)

[Additional blank pages for scratch work - not graded]
```

### Exam Type Guidelines

**Quiz (20-30 minutes):**
- 10-15 questions
- Focus on recent material
- Mostly multiple choice and short answer
- 25-50 points total

**Midterm (60-90 minutes):**
- 25-40 questions across multiple sections
- Covers first half of course
- Mix of question types
- 100-150 points total
- Include formula sheet if quantitative

**Final Exam (120-180 minutes):**
- 40-60 questions
- Comprehensive or cumulative
- All question types
- 150-300 points total
- Multiple sections by topic or question type

**Practical Exam:**
- Hands-on problems (coding, data analysis, lab work)
- Focus on application and skills
- Provide necessary resources (data files, equipment)

### Point Allocation Strategy

Distribute points to reflect question difficulty and importance:

- **Multiple Choice:** 2-5 points each (higher for complex questions)
- **True/False:** 1-2 points each
- **Short Answer:** 5-10 points each
- **Calculation Problems:** 10-20 points each (with partial credit breakdown)
- **Essay Questions:** 15-30 points each

**Recommended distribution:**
- 40% Recognition (MC, T/F) - Test knowledge
- 30% Application (problems, short answer) - Test understanding
- 30% Analysis/Synthesis (essay, complex problems) - Test mastery

### Difficulty Balance

Create balanced difficulty:
- **30% Easy** - All students should get these
- **50% Medium** - Average students should get most
- **20% Hard** - Challenge top students

Place easier questions first to build confidence.

### Time Management Guide

Provide timing guidance within exam:
- List suggested time per section
- Help students pace themselves
- Total should be 80% of available time (buffer for review)

Example:
```
Suggested Time Allocation:
- Section 1 (MC): 20 minutes
- Section 2 (Short Answer): 25 minutes
- Section 3 (Problems): 30 minutes
- Review: 15 minutes
```

### Grading Rubric

Include detailed rubric for each section:

**Multiple Choice/True-False:**
```
Correct answer: Full points
Incorrect/Blank: 0 points
```

**Short Answer:**
```
Excellent (Full points): Complete answer with all key elements
Good (80%): Most elements present, minor gaps
Satisfactory (60%): Basic understanding, missing details
Poor (30%): Incomplete or partially incorrect
Incorrect (0%): Major misunderstanding
```

**Calculation Problems:**
```
Full credit: Correct setup, work, and answer
Partial credit breakdown:
- Correct setup/approach: 40%
- Correct intermediate steps: 40%
- Correct final answer: 20%
```

**Essay Questions:**
```
A (90-100%): Comprehensive, well-organized, strong evidence
B (80-89%): Good understanding, organized, adequate support
C (70-79%): Basic understanding, some gaps
D (60-69%): Minimal understanding
F (<60%): Inadequate or incorrect
```

### Format Options

Support multiple exam formats:
- **LaTeX** - Professional typesetting with exam class
- **Word/Markdown** - Editable document format
- **PDF** - Print-ready with proper spacing
- **Canvas/Moodle** - LMS-ready format for online exams
- **Scantron** - Bubble sheet compatible

### Academic Integrity Features

Include appropriate safeguards:
- Academic integrity statement and signature line
- Version indicators (for multiple versions)
- Clear policy on allowed resources
- Statement about partial credit and showing work
- Instructions about what to do if you have questions

### Accessibility Considerations

Ensure exam is accessible:
- Clear, readable font (12pt minimum)
- Adequate spacing between questions
- High contrast text
- Logical organization
- Extra time versions available
- Provide accommodations as needed

## Follow-up Actions

After generating exam, offer:
- Create answer key with full solutions
- Generate multiple exam versions (same difficulty, different questions)
- Create separate grading rubric document
- Generate study guide or practice exam
- Create online version for LMS
- Generate Scantron-compatible version
- Create accommodated versions (extended time, large print)

## Related Commands

- `/teaching:quiz` - Create shorter quizzes
- `/teaching:rubric` - Generate detailed grading rubrics
- `/teaching:slides` - Create review lecture slides
- `/teaching:assignment` - Create homework assignments
</system>
