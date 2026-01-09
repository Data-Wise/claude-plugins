---
name: teaching:syllabus
description: Generate a comprehensive course syllabus
---

# Create Course Syllabus

I'll help you create a comprehensive course syllabus with all necessary components.

**Usage:** `/teaching:syllabus <course-name>` or `/teaching:syllabus <course-name> <semester>`

**Examples:**
- `/teaching:syllabus "Introduction to Statistics"`
- `/teaching:syllabus "Regression Analysis" "Fall 2026"`

## What course would you like to create a syllabus for?

Provide the course name and optionally the semester/term.

<system>
This command generates a comprehensive course syllabus including:
- Course information (title, number, credits, meeting times)
- Instructor information
- Course description and objectives
- Learning outcomes
- Required materials
- Grading policy
- Course schedule/calendar
- Policies (attendance, academic integrity, accommodations)

## Implementation

The command should:

1. **Gather Information** - Ask user for:
   - Course title and number
   - Meeting times and location
   - Prerequisites (if any)
   - Course level (undergraduate/graduate)
   - Textbook/materials
   - Number of weeks/sessions

2. **Generate Syllabus Structure**:
   ```markdown
   # [COURSE TITLE] - [COURSE NUMBER]

   ## Course Information
   - Instructor: [Name]
   - Semester: [Term Year]
   - Meeting Times: [Days/Times]
   - Location: [Room]
   - Office Hours: [Times]
   - Email: [Email]

   ## Course Description
   [Generated based on course level and topic]

   ## Learning Objectives
   By the end of this course, students will be able to:
   1. [Objective 1]
   2. [Objective 2]
   ...

   ## Required Materials
   - Textbook: [Title] by [Author]
   - Software: [If applicable]

   ## Grading Policy
   - Assignments: X%
   - Exams: X%
   - Project: X%
   - Participation: X%

   ## Course Schedule
   [Week-by-week breakdown]

   ## Course Policies
   [Attendance, late work, academic integrity, accessibility]
   ```

3. **Customize for Subject** - Adapt content based on:
   - Statistics courses → Include software requirements (R, Python)
   - Math courses → Include proof-writing expectations
   - Research methods → Include IRB/ethics training

## Follow-up Actions

After generating the syllabus, offer to:
- Create the first week's lecture outline
- Generate assignment prompts for the course
- Create a grading rubric for major assignments
- Export to PDF or Word format
- Add calendar events for all class sessions

## Output Format

Generate as formatted markdown that can be:
- Converted to PDF via Pandoc
- Imported to LMS (Canvas, Blackboard)
- Shared with students via course website

## Best Practices

Include:
- ✅ Clear learning objectives (measurable, actionable)
- ✅ Detailed grading breakdown
- ✅ Academic integrity statement
- ✅ Accessibility/accommodations statement
- ✅ Weekly schedule with topics
- ✅ Key dates (exams, project deadlines)

Avoid:
- ❌ Vague objectives ("understand" → use "apply", "analyze", "evaluate")
- ❌ Missing prerequisite information
- ❌ Unclear grading criteria
- ❌ No contact information or office hours
</system>
