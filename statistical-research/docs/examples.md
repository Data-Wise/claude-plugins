# Statistical Research Examples

Practical examples demonstrating common research workflows using the Statistical Research plugin.

## Literature Review Workflow

### Finding Relevant Papers

```bash
# Search arXiv for recent papers
/research:arxiv "causal mediation analysis machine learning"

# Get specific paper by DOI
/research:doi "10.1080/01621459.2020.1765785"

# Search local bibliography
/research:bib:search "Pearl" ~/papers/references.bib
```

### Building Bibliography

```bash
# Add new paper to bibliography
/research:bib:add paper.bib ~/papers/references.bib

# Identify research gaps
/research:lit-gap "mediation with unmeasured confounding"
```

## Manuscript Writing Workflow

### Methods Section

```bash
# Generate methods description
/research:manuscript:methods "Describe the bootstrap procedure for testing indirect effects. We use 1000 replications with bias-corrected confidence intervals."
```

**Output includes:**
- Statistical notation
- Parameter definitions
- Estimation procedure
- Bootstrap algorithm

### Results Section

```bash
# Generate results with proper reporting
/research:manuscript:results "Report simulation results: bias 0.001 (SE 0.02), coverage 94.5% (target 95%), power 82% at n=500"
```

**Output includes:**
- Formatted statistics
- Table structure
- Interpretation guidance

### Responding to Reviewers

```bash
# Generate professional response
/research:manuscript:reviewer "Reviewer 2 asks why we didn't use the Sobel test. They suggest it's simpler than bootstrap."
```

**Output includes:**
- Respectful response
- Statistical justification
- References to literature
- Additional analysis suggestions

## Simulation Study Workflow

### Design Phase

```bash
# Design comprehensive simulation
/research:simulation:design "Compare three bootstrap methods (percentile, BCa, studentized) for mediation effects across sample sizes (n=100,200,500) and effect sizes (small, medium, large)"
```

**Output includes:**
- Simulation parameters
- Data generation process
- Performance metrics (bias, MSE, coverage)
- Number of replications
- R code template

### Analysis Phase

```bash
# Analyze results
/research:simulation:analysis results/sim_results.csv
```

**Output includes:**
- Performance summaries
- Statistical comparisons
- Visualization code
- Interpretation

## Method Development Workflow

### Initial Planning

```bash
# Scout existing methods
/research:method-scout "high-dimensional mediation with regularization"

# Identify gaps
/research:lit-gap "high-dimensional mediation"

# Generate hypotheses
/research:hypothesis "sparse mediation with L1 penalty improves estimation"
```

### Implementation

```bash
# Design algorithm (triggers algorithm-designer skill)
"How should I implement coordinate descent for sparse mediation?"

# Plan simulation (triggers simulation-architect skill)
/research:simulation:design "Evaluate sparse mediation estimator"
```

### Validation

```bash
# Design sensitivity analysis
"Design sensitivity analysis for unmeasured confounding in sparse mediation"
# Triggers: sensitivity-analyst skill

# Plan proof
"How do I prove identifiability conditions?"
# Triggers: identification-theory, proof-architect skills
```

## Complete Research Project Example

### Step 1: Literature Review (Week 1)

```bash
# Search recent literature
/research:arxiv "high-dimensional mediation" --recent

# Identify gap
/research:lit-gap "regularization in mediation analysis"

# Build bibliography
/research:bib:add *.bib references.bib
```

### Step 2: Method Development (Weeks 2-4)

```bash
# Develop theory
# Skills auto-activate: mathematical-foundations, identification-theory

# Implement algorithm
# Skills auto-activate: algorithm-designer, numerical-methods

# Create test suite
# Skills auto-activate: statistical-software-qa
```

### Step 3: Simulation Study (Weeks 5-6)

```bash
# Design simulation
/research:simulation:design "Compare proposed method with existing approaches"

# Run simulation (in R)
# ...

# Analyze results
/research:simulation:analysis results/simulation.csv
```

### Step 4: Manuscript Preparation (Weeks 7-8)

```bash
# Write methods
/research:manuscript:methods "Describe the sparse mediation estimator..."

# Write results
/research:manuscript:results "Report simulation findings..."

# Generate analysis plan for real data
/research:analysis-plan "Apply sparse mediation to gene expression study"
```

### Step 5: Submission & Revision (Weeks 9-10)

```bash
# Select journal
# Skills auto-activate: publication-strategist

# Respond to reviewers
/research:manuscript:reviewer "Reviewer comments..."

# Proofread mathematics
/research:manuscript:proof "Check identifiability proof in Appendix"
```

## Advanced Use Cases

### Meta-Analysis of Mediation Studies

```bash
# Search for mediation studies
/research:arxiv "mediation analysis effect size"

# Extract effect sizes
# Skills auto-activate: mediation-meta-analyst

# Synthesize results
"How do I meta-analyze mediation effects with different parameterizations?"
```

### Cross-Disciplinary Method Transfer

```bash
# Find method from other field
/research:method-scout "penalized regression in genomics"

# Adapt to mediation
# Skills auto-activate: method-transfer-engine, cross-disciplinary-ideation

# Validate adaptation
# Skills auto-activate: mathematical-foundations
```

### Teaching & Communication

```bash
# Create accessible explanation
# Skills auto-activate: methods-communicator

# Generate examples
"Create teaching example for causal mediation"

# Design visualizations
"How should I visualize mediation effects for non-statisticians?"
```

## Tips for Effective Use

### Leverage Skills

Skills activate automatically - just ask natural questions:

```bash
# Instead of invoking a command
"How do I prove identifiability?"
# → identification-theory skill provides guidance

# Then use command when ready
/research:manuscript:proof "..."
```

### Combine Commands

Chain commands for complete workflows:

```bash
/research:arxiv "topic" \
  && /research:bib:add paper.bib refs.bib \
  && /research:lit-gap "topic"
```

### Use in R Scripts

Commands work well in research scripts:

```r
# simulation.R
# Design generated by /research:simulation:design

set.seed(123)
n_sim <- 1000
results <- run_simulation(...)

# Analysis by /research:simulation:analysis
write.csv(results, "results/simulation.csv")
```

## See Also

- **[Commands Reference](commands.md)** - All 14 commands
- **[Skills Guide](skills.md)** - 17 research skills
- **[API Wrappers](api-wrappers.md)** - Shell APIs
