---
name: teaching:assignment
description: Create homework assignments and problem sets
---

# Create Course Assignment

I'll help you create a well-structured homework assignment or problem set with clear instructions and learning objectives.

**Usage:** `/teaching:assignment <topic>` or `/teaching:assignment <topic> <difficulty>`

**Examples:**
- `/teaching:assignment "Linear Regression"`
- `/teaching:assignment "Hypothesis Testing" "intermediate"`

## What assignment would you like to create?

Provide the topic and optionally the difficulty level (introductory/intermediate/advanced).

<system>
This command generates homework assignments or problem sets with:
- Clear learning objectives
- Detailed instructions
- Multiple problem types (conceptual, computational, applied)
- Rubric alignment
- Submission requirements

## Implementation

The command should:

1. **Gather Information** - Ask user for:
   - Course level (undergraduate/graduate)
   - Topic/concept being assessed
   - Number of problems desired
   - Problem types: conceptual, computational, proof-based, applied/data analysis
   - Software requirements (R, Python, etc.)
   - Due date

2. **Generate Assignment Structure**:
   ```markdown
   # Assignment [Number]: [Topic]

   **Course:** [Course Name]
   **Due Date:** [Date and Time]
   **Points:** [Total Points]
   **Submission:** [Format and method]

   ## Learning Objectives
   This assignment assesses your ability to:
   1. [Objective 1]
   2. [Objective 2]

   ## Instructions
   - [General instructions]
   - [Collaboration policy]
   - [Software/tools requirements]
   - [Submission format]

   ## Problems

   ### Problem 1: [Title] ([Points] points)
   [Problem statement with clear instructions]

   **What to submit:**
   - [Specific deliverables]

   **Hints:**
   - [Optional hints if appropriate]

   ### Problem 2: [Title] ([Points] points)
   ...

   ## Submission Requirements
   - Format: [PDF, R Markdown, Jupyter Notebook, etc.]
   - File naming: [Convention]
   - Where to submit: [LMS, email, etc.]

   ## Grading Criteria
   - Correctness: X points
   - Code quality: X points
   - Interpretation: X points
   - Presentation: X points

   ## Resources
   - [Textbook sections]
   - [Lecture notes]
   - [Software documentation]
   ```

3. **Problem Type Templates**:

   **Conceptual:**
   - Explain why/how concepts work
   - Compare/contrast methods
   - Interpret results in context

   **Computational:**
   - Step-by-step calculations
   - Implement algorithms
   - Verify results

   **Applied/Data Analysis:**
   - Real dataset analysis
   - Report findings
   - Justify methodological choices

   **Proof-Based (if applicable):**
   - Prove theoretical results
   - Show mathematical derivations

4. **Adaptive Difficulty**:
   - **Introductory:** Focus on fundamentals, provide more scaffolding
   - **Intermediate:** Mix of guided and open-ended problems
   - **Advanced:** Complex scenarios, require synthesis of multiple concepts

## Follow-up Actions

After generating the assignment, offer to:
- Create a detailed grading rubric
- Generate a solution key
- Create sample data for analysis problems
- Suggest related practice problems
- Generate peer review guidelines

## Output Format

Generate as formatted markdown that includes:
- Clear point values for each problem
- Explicit submission requirements
- Aligned with course learning objectives

## Best Practices

Include:
- ✅ Variety of problem types (assess different skills)
- ✅ Clear point allocation
- ✅ Explicit instructions and deliverables
- ✅ Reasonable workload (2-4 hours for weekly assignment)
- ✅ Connection to real-world applications
- ✅ Resources for students who need help

Avoid:
- ❌ Ambiguous problem statements
- ❌ Unrealistic time expectations
- ❌ Problems requiring tools not covered in class
- ❌ Unclear collaboration policy
- ❌ Missing submission details

## Subject-Specific Considerations

**Statistics/Data Analysis:**
- Provide datasets or data generation code
- Require code + interpretation
- Include model diagnostics

**Mathematics:**
- Balance computational and proof problems
- Include examples before harder problems
- Specify notation conventions

**Research Methods:**
- Include literature review components
- Require methodological justification
- Emphasize ethical considerations
</system>
