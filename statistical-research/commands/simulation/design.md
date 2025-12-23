---
name: research:simulation:design
description: Design Monte Carlo simulation study
---

# Design Simulation Study

I'll help you design a rigorous Monte Carlo simulation study for your statistical research.

**Usage:** `/research:simulation:design` or `/research:simulation:design <topic>`

**Examples:**
- `/research:simulation:design`
- `/research:simulation:design "bootstrap mediation CI coverage"`

## Let's design your simulation

I'll guide you through planning a comprehensive simulation study.

<system>
This command helps design Monte Carlo simulation studies for statistical research.

## Process

1. **Research Question**
   - What statistical property are you investigating?
   - What methods are you comparing?
   - What is the target estimand?

2. **Activate Skills**
   Automatically engages:
   - `simulation-architect` skill (implementation/simulation-architect.md)
   - `algorithm-designer` skill (implementation/algorithm-designer.md)
   - `numerical-methods` skill (implementation/numerical-methods.md)

3. **Design Dimensions**
   Create factorial design across:
   - Sample sizes
   - Effect sizes
   - Data-generating conditions
   - Distributional assumptions
   - Missing data patterns (if applicable)

4. **Performance Metrics**
   Define what to measure:
   - Bias
   - Standard error
   - RMSE
   - Coverage probability
   - Power
   - Type I error rate

## Key Design Elements

### 1. Data-Generating Mechanism

**Model:**
```
Define the population model with parameters:
- Population parameters (true values)
- Distributional assumptions
- Dependency structures
```

**Factors to Vary:**
- Sample size (n): e.g., 50, 100, 200, 500
- Effect size (δ): e.g., 0, 0.1, 0.3, 0.5
- Model complexity
- Violation conditions

### 2. Methods to Compare

For each method specify:
- Estimation procedure
- Inference approach (Wald, bootstrap, permutation, etc.)
- Software implementation
- Tuning parameters

### 3. Performance Measures

**For Point Estimates:**
- Bias: E(θ̂) - θ
- Standard error: SD(θ̂)
- RMSE: sqrt(bias² + variance)
- Relative efficiency

**For Interval Estimates:**
- Coverage probability: P(θ ∈ CI)
- Average width
- Balance (left vs right tail error)

**For Hypothesis Tests:**
- Type I error rate (α)
- Power (1 - β)
- Rejection rate across conditions

### 4. Simulation Parameters

**Iterations:**
- Pilot study: 1,000-5,000 iterations
- Final study: 10,000+ iterations
- Adjust based on variance of estimates

**Random Seeds:**
- Set seeds for reproducibility
- Document seed values
- Consider multiple seed sets for robustness

### 5. Computational Considerations

**Resources:**
- Estimated runtime
- Memory requirements
- Parallel computing strategy
- Storage for results

**Implementation:**
- Programming language (R, Python, Julia)
- Key packages/libraries
- Code organization
- Result storage format

## Simulation Study Plan Template

Generate a comprehensive plan:

```
# Simulation Study Plan

## Research Question
[Clear statement of what you're investigating]

## Methods Being Compared
1. Method 1: [Description]
2. Method 2: [Description]
...

## Data-Generating Conditions

### Fixed Parameters
- [List parameters held constant]

### Varied Factors (Factorial Design)
1. Sample size (n): [values]
2. Effect size (δ): [values]
3. [Other factors]

Total conditions: [product of levels]

## Performance Metrics
1. [Metric 1 with formula]
2. [Metric 2 with formula]
...

## Implementation Plan

### Software
- Language: [R/Python/Julia]
- Key packages: [list]

### Computational Resources
- Iterations: [number]
- Estimated runtime: [time]
- Parallelization: [strategy]

### Code Structure
- data_generation.R
- estimation.R
- summarize_results.R

### Output
- Results format: [CSV/RData/etc]
- Visualization: [planned plots]

## Quality Checks
- Pilot run: [small scale test]
- Diagnostics: [what to check]
- Validation: [known results to compare]

## Timeline
- Design: [time]
- Implementation: [time]
- Pilot run: [time]
- Full run: [time]
- Analysis: [time]
```

## Best Practices

1. **Start Small:** Pilot with few iterations and conditions
2. **Check Implementation:** Verify with known results
3. **Monitor Convergence:** Check Monte Carlo error
4. **Save Everything:** Raw results, seeds, code versions
5. **Document Thoroughly:** Methods, conditions, software versions

## Common Pitfalls

- Too few iterations (high Monte Carlo error)
- Too many conditions (unfocused, hard to interpret)
- Unrealistic data-generating mechanisms
- Forgetting to set seeds
- Not checking implementation against known results

## Example Interaction

User: `/research:simulation:design "bootstrap mediation CI coverage"`