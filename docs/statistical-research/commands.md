# Statistical Research Commands

Complete reference for all 14 statistical research commands organized by category.

## Command Categories

- [Literature Management](#literature-management) (4 commands)
- [Manuscript Writing](#manuscript-writing) (4 commands)
- [Simulation Studies](#simulation-studies) (2 commands)
- [Research Planning](#research-planning) (4 commands)

## Literature Management

### /research:arxiv
Search arXiv for statistical papers.

```bash
/research:arxiv "causal mediation analysis"
/research:arxiv "bootstrap confidence intervals"
```

**Features:**
- Full-text search across arXiv stat category
- Returns title, authors, abstract, PDF link
- Date filtering available

### /research:doi
Look up paper metadata by DOI.

```bash
/research:doi "10.1080/01621459.2020.1765785"
```

**Returns:**
- Full citation
- BibTeX entry
- Abstract
- Publication details

### /research:bib:search
Search BibTeX files for entries.

```bash
/research:bib:search "Pearl" references.bib
/research:bib:search "mediation" *.bib
```

### /research:bib:add
Add BibTeX entry to bibliography.

```bash
/research:bib:add entry.bib references.bib
```

## Manuscript Writing

### /research:manuscript:methods
Write methods sections with statistical rigor.

```bash
/research:manuscript:methods "Describe the bootstrap mediation analysis"
```

**Generates:**
- Statistical methodology
- Proper notation
- Parameter definitions
- Estimation procedures

### /research:manuscript:results
Generate results sections with proper reporting.

```bash
/research:manuscript:results "Report simulation study findings"
```

**Includes:**
- Statistical test results
- Effect sizes with CI
- Table formatting guidance
- Figure descriptions

### /research:manuscript:reviewer
Generate responses to reviewer comments.

```bash
/research:manuscript:reviewer "Reviewer 2 questions significance testing"
```

**Provides:**
- Respectful, professional responses
- Statistical justification
- Additional analysis suggestions
- Revision guidance

### /research:manuscript:proof
Review mathematical proofs for correctness.

```bash
/research:manuscript:proof "Check identifiability proof in Appendix A"
```

**Validates:**
- Logical flow
- Mathematical rigor
- Assumptions stated
- Completeness

## Simulation Studies

### /research:simulation:design
Design Monte Carlo simulation studies.

```bash
/research:simulation:design "Compare bootstrap methods for mediation"
```

**Provides:**
- Simulation parameters
- Sample size considerations
- Number of replications
- Performance metrics
- Analysis plan

### /research:simulation:analysis
Analyze simulation results.

```bash
/research:simulation:analysis results/simulation.csv
```

**Generates:**
- Performance summaries
- Bias and MSE calculations
- Coverage rate analysis
- Visualization code

## Research Planning

### /research:lit-gap
Identify literature gaps.

```bash
/research:lit-gap "mediation analysis with unmeasured confounding"
```

**Identifies:**
- Methodological gaps
- Application areas
- Research opportunities
- Novel contributions

### /research:hypothesis
Generate testable hypotheses.

```bash
/research:hypothesis "treatment effect heterogeneity"
```

**Produces:**
- Formal statistical hypotheses
- Null and alternative
- Test procedures
- Power considerations

### /research:analysis-plan
Create statistical analysis plans.

```bash
/research:analysis-plan "randomized trial with mediation"
```

**Includes:**
- Primary analysis
- Secondary analyses
- Sensitivity analyses
- Multiple testing procedures

### /research:method-scout
Scout statistical methods for problems.

```bash
/research:method-scout "high-dimensional mediation"
```

**Suggests:**
- Relevant methods
- R packages
- Key papers
- Implementation guidance

## See Also

- **[Skills Guide](skills.md)** - 17 research skills
- **[API Wrappers](api-wrappers.md)** - Shell-based APIs
- **[Examples](examples.md)** - Usage examples

---

**Last Updated:** 2026-01-09
**Document Version:** v1.1.0
**Status:** ✅ Production ready - Complete reference for 14 research commands
