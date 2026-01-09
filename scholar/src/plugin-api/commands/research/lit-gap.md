---
name: research:lit-gap
description: Identify research gaps in literature
---

# Find Literature Gaps

I'll help you identify research gaps and opportunities in your area of statistical research.

**Usage:** `/research:lit-gap <topic>` or `/research:lit-gap`

**Examples:**
- `/research:lit-gap "causal mediation analysis"`
- `/research:lit-gap "bootstrap inference for structural equation models"`

## Let's find research gaps

I'll analyze the current literature to identify unexplored areas and opportunities.

<system>
This command helps identify research gaps in statistical literature.

## Process

1. **Understand Topic**
   - What area of statistical methodology?
   - What specific problem domain?
   - What has been done already?

2. **Activate Skills**
   Automatically engages:
   - `literature-gap-finder` skill (research/literature-gap-finder.md)
   - `cross-disciplinary-ideation` skill (research/cross-disciplinary-ideation.md)
   - `method-transfer-engine` skill (research/method-transfer-engine.md)

3. **Literature Analysis**
   Can integrate with:
   ```bash
   # Search recent literature
   source "${CLAUDE_PLUGIN_ROOT}/lib/arxiv-api.sh"
   arxiv_search "$TOPIC" 20

   # Search Crossref
   source "${CLAUDE_PLUGIN_ROOT}/lib/crossref-api.sh"
   crossref_search "$TOPIC" 20
   ```

4. **Gap Identification**
   Analyze across dimensions:
   - Methodological gaps
   - Application domains
   - Theoretical foundations
   - Computational approaches
   - Assumption relaxation

## Gap Analysis Framework

### 1. Methodological Gaps

**Questions:**
- What methods exist for this problem?
- What assumptions do they require?
- What conditions haven't been addressed?
- What extensions are possible?

**Common Gaps:**
- Small sample behavior
- Robustness to violations
- Efficiency improvements
- Computational scalability
- Multiple testing corrections
- High-dimensional settings

### 2. Application Gaps

**Questions:**
- Where has this method been applied?
- What domains are underserved?
- What data structures haven't been considered?

**Common Gaps:**
- New application domains
- Complex data structures
- Modern data types (text, images, networks)
- Real-time/streaming data
- Missing data patterns

### 3. Theoretical Gaps

**Questions:**
- What theoretical properties are known?
- What remains to be proven?
- Under what conditions does it work?
- What are the limitations?

**Common Gaps:**
- Asymptotic theory under weaker conditions
- Finite-sample properties
- Consistency proofs
- Optimality results
- Robustness theory

### 4. Computational Gaps

**Questions:**
- How is it currently computed?
- What are computational bottlenecks?
- Could it be more efficient?
- Are there implementation gaps?

**Common Gaps:**
- Faster algorithms
- Parallel/distributed implementation
- Memory-efficient versions
- Software availability
- User-friendly packages

## Output Structure

### Research Gap Report

```markdown
# Literature Gaps: [Topic]

## Summary
[1-2 sentence overview of the area and key gaps]

## Current State of Literature

### Well-Developed Areas
1. [What's been thoroughly studied]
2. [What works well]
3. [What's settled]

### Active Research Areas
1. [What people are currently working on]
2. [Recent developments]
3. [Trends]

## Identified Gaps

### Gap 1: [Title]
**Type:** Methodological / Applied / Theoretical / Computational

**Description:** [What's missing]

**Importance:** [Why it matters]

**Feasibility:** High / Medium / Low

**Potential Impact:** High / Medium / Low

**Related Work:** [What exists nearby]

**Possible Approaches:** [How it could be tackled]

### Gap 2: [Title]
[Same structure]

...

## Promising Research Directions

### Direction 1: [Title]
**Combines:** [Gap 1] + [Gap 2]

**Novel Contribution:** [What would be new]

**Expected Outcomes:**
- [Result 1]
- [Result 2]

**Challenges:**
- [Obstacle 1]
- [Obstacle 2]

**First Steps:**
1. [Concrete action]
2. [Concrete action]

## Cross-Disciplinary Opportunities

[Connections to other fields that might offer solutions]

## Recommended Next Steps

1. [Immediate action]
2. [Literature review focus]
3. [Collaboration opportunities]
```

## Search Strategies

### Literature Search

1. **Recent Reviews:**
   - Find recent review papers
   - Identify "future research" sections
   - Note open questions

2. **Citation Analysis:**
   - Highly cited papers (established areas)
   - Rarely cited topics (potential gaps)
   - Recent papers citing classics (new developments)

3. **Method Families:**
   - Compare related methods
   - Look for untried combinations
   - Identify assumption variations

### Gap Indicators

- **Explicit mentions:** "Future research should..."
- **Limitation sections:** "Our method assumes..."
- **Unanswered questions:** "It remains to be shown..."
- **Negative results:** "This approach does not work when..."
- **Computational complaints:** "The method is too slow for..."

## Evaluation Criteria

### Is This Gap Worth Pursuing?

**Impact:**
- Solves a real problem?
- Advances methodology?
- Enables new applications?

**Feasibility:**
- Can it be done with current tools?
- Is it tractable theoretically?
- Can it be implemented computationally?

**Novelty:**
- Truly unexplored?
- Substantive advance?
- Not just incremental?

**Fit:**
- Matches your expertise?
- Available resources?
- Reasonable timeline?

## Integration

Works well with:
- `/research:arxiv` - Search recent papers
- `/research:hypothesis` - Generate hypotheses from gaps
- `/research:analysis-plan` - Plan study to fill gap

## Example Interaction

User: `/research:lit-gap "causal mediation analysis"`