---
name: teaching:slides
description: Generate lecture slides for a course topic
---

# Create Lecture Slides

I'll help you create comprehensive lecture slides for your course topic.

**Usage:** `/teaching:slides <topic>` or `/teaching:slides <topic> <duration-minutes>`

**Examples:**
- `/teaching:slides "Multiple Regression"`
- `/teaching:slides "Hypothesis Testing" 75`
- `/teaching:slides "ANOVA" 50 --format reveal.js`

<system>
## Implementation

Generate lecture slides with:
1. **Title slide** with topic and instructor placeholders
2. **Learning objectives** (3-5 clear outcomes)
3. **Content slides** organized by subtopics
4. **Examples and visualizations** where appropriate
5. **Practice problems** for student engagement
6. **Summary slide** with key takeaways
7. **References** (if needed)

### Slide Structure Template

```markdown
# [Topic Name]
## [Course Name] | [Date]

---

## Learning Objectives

By the end of this lecture, you will be able to:
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

---

## Introduction

[Context and motivation for the topic]

---

## [Subtopic 1]

### Key Concept
[Explanation]

### Example
[Concrete example]

---

## [Subtopic 2]

[Content with appropriate depth]

---

## Practice Problem

[Guided practice question]

---

## Summary

**Key Takeaways:**
- [Point 1]
- [Point 2]
- [Point 3]

**Next Time:** [Preview of next lecture]

---

## Questions?

[Contact information placeholders]
```

### Format Options

Support multiple slide formats:
- **Markdown** (default) - Pandoc-compatible with `---` slide breaks
- **reveal.js** - HTML5 presentation framework
- **Beamer** - LaTeX slides for academic presentations
- **PowerPoint** - PPTX outline format
- **Google Slides** - Structured outline for Google Slides

### Timing Guidelines

Estimate slide count based on duration:
- **50-minute lecture**: 20-25 slides (2-2.5 min per slide)
- **75-minute lecture**: 30-35 slides
- **90-minute lecture**: 35-40 slides

Include more practice/discussion slides for longer sessions.

### Content Depth by Level

- **Undergraduate**: Focus on intuition, examples, visual explanations
- **Graduate**: Include proofs, advanced theory, research connections
- **Intro course**: More examples, less theory
- **Advanced course**: Assume prerequisites, go deeper

### Best Practices

1. **Visual hierarchy**: Use headers, bullets, emphasis appropriately
2. **One concept per slide**: Don't overcrowd
3. **Examples are essential**: Include 1-2 examples per major concept
4. **Interactivity**: Add discussion prompts or quick checks
5. **Pacing**: Mix content slides with practice/discussion
6. **Accessibility**: High contrast, large fonts, alt text for images

## Follow-up Actions

After generating slides, offer:
- Generate speaker notes for each slide
- Create accompanying handout (PDF version)
- Generate practice problems for students
- Create quiz questions based on slides
- Suggest interactive activities

## Related Commands

- `/teaching:assignment` - Create homework assignments
- `/teaching:quiz` - Generate quiz questions
- `/teaching:exam` - Create comprehensive exams
</system>
