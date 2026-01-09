---
name: scholar:method-scout
description: Scout and evaluate statistical methods for research problems
---

# Scout Methods

Find and evaluate statistical or analytical methods for a research problem.

## Purpose

Discover appropriate methods by:
- Searching across disciplines for relevant techniques
- Identifying method assumptions and requirements
- Comparing alternative approaches
- Finding seminal papers and tutorials

## Required Input

- **Research problem**: What you're trying to analyze or test
- **Data characteristics**: Sample size, variable types, structure
- **Constraints**: Software availability, audience familiarity
- **Goal**: Estimation, inference, prediction, description

## Process

1. Understand the research question and data structure
2. Search for methods used in similar contexts
3. Identify candidate methods from multiple disciplines
4. Evaluate assumptions and requirements for each
5. Compare trade-offs (complexity, interpretability, power)
6. Recommend best options with justification

## MCP Integration

Uses these tools when available:
- `arxiv_search` - Find recent methodological papers
- `crossref_lookup` - Get citation information
- Cross-disciplinary skills for method transfer

## Output Format

```markdown
## Method Scout Report

### Research Problem
[Restated problem and goals]

### Data Characteristics
- Sample size: N = X
- Variables: [types and structure]
- Special features: [clustering, missingness, etc.]

### Candidate Methods

#### Method 1: [Name]
- **Description**: [Brief explanation]
- **Assumptions**: [Key requirements]
- **Strengths**: [Advantages]
- **Limitations**: [Drawbacks]
- **Software**: [R packages, etc.]
- **Key reference**: [Citation]

#### Method 2: [Name]
[Same structure]

### Comparison

| Criterion | Method 1 | Method 2 | Method 3 |
|-----------|----------|----------|----------|
| Assumptions | | | |
| Complexity | | | |
| Interpretability | | | |
| Power/Efficiency | | | |

### Recommendation
[Justified recommendation with context]

### Next Steps
1. [Suggested action]
2. [Suggested action]
```

## Search Strategies

- **Within-discipline**: Standard methods in your field
- **Cross-discipline**: Methods from other fields that apply
- **Recent advances**: New methods from last 3-5 years
- **Classic approaches**: Well-established, widely understood

## Examples

**Request**: "Find methods for analyzing mediation with binary outcomes and clustered data"

**Request**: "What methods exist for causal inference with time-varying confounders?"

**Request**: "Scout methods for handling missing data in longitudinal studies"

**Request**: "Find alternatives to ANOVA when assumptions are violated"

## Tips

- Consider your audience's familiarity with methods
- Balance novelty with practicality
- Check software availability early
- Look for tutorial papers, not just methodological ones
