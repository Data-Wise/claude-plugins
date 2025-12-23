---
name: research:manuscript:results
description: Write results section for statistical manuscript
---

# Write Results Section

I'll help you write a clear and comprehensive results section for your statistical manuscript.

**Usage:** `/research:manuscript:results` or `/research:manuscript:results <topic>`

**Examples:**
- `/research:manuscript:results`
- `/research:manuscript:results "mediation analysis findings"`

## Let's present your results

I'll guide you through presenting your statistical findings clearly and accurately.

<system>
This command helps write results sections for statistical manuscripts.

## Process

1. **Gather Results**
   - What analyses did you run?
   - What are the key findings?
   - What tables/figures do you have?

2. **Structure Organization**
   Organize results by:
   - Primary analysis first
   - Secondary analyses
   - Sensitivity analyses
   - Model diagnostics

3. **Activate Skills**
   Automatically engages:
   - `methods-paper-writer` skill (writing/methods-paper-writer.md)
   - `methods-communicator` skill (writing/methods-communicator.md)
   - `publication-strategist` skill (writing/publication-strategist.md)

4. **Generate Content**
   Write each section with:
   - Clear presentation of estimates
   - Appropriate uncertainty measures
   - References to tables/figures
   - Statistical and practical significance

## Key Sections

### Descriptive Statistics
- Sample characteristics
- Variable distributions
- Missingness patterns

### Primary Analysis
- Main parameter estimates
- Standard errors / confidence intervals
- p-values (with interpretation guidance)
- Effect sizes

### Model Assessment
- Model fit statistics
- Assumption checks
- Diagnostic plots

### Sensitivity Analyses
- Robustness to assumptions
- Alternative specifications
- Subgroup analyses

## Best Practices

1. **Reporting Standards**
   - Report estimates with appropriate precision
   - Always include uncertainty measures
   - State effect sizes in context
   - Avoid p-value dichotomies

2. **Tables and Figures**
   - Reference all tables/figures
   - Use tables for precise values
   - Use figures for patterns/relationships
   - Follow journal guidelines

3. **Statistical Significance**
   - Report exact p-values (not just p < 0.05)
   - Interpret confidence intervals
   - Discuss practical significance
   - Avoid "trending toward significance"

4. **Clarity**
   - Define all notation
   - Explain technical terms
   - Use plain language where possible
   - Separate results from interpretation

## Common Pitfalls to Avoid

- Mixing results and discussion
- Over-interpreting non-significant findings
- Reporting too many decimal places
- Forgetting to report sample sizes
- Inconsistent notation between methods and results

## Integration

Can be used with:
- `/research:manuscript:methods` - Ensure consistency
- R output from analysis scripts
- Table/figure drafts

## Example Interaction

User: `/research:manuscript:results "mediation analysis findings"`