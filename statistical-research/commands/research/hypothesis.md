---
name: research:hypothesis
description: Generate statistical research hypotheses
---

# Generate Research Hypotheses

I'll help you formulate clear, testable statistical research hypotheses.

**Usage:** `/research:hypothesis <topic>` or `/research:hypothesis`

**Examples:**
- `/research:hypothesis "bootstrap mediation intervals"`
- `/research:hypothesis "robust estimation under contamination"`

## Let's formulate your hypotheses

I'll guide you through developing rigorous statistical hypotheses.

<system>
This command helps generate and refine statistical research hypotheses.

## Process

1. **Research Context**
   - What's the methodological question?
   - What do you expect to find?
   - Why is this interesting?

2. **Activate Skills**
   Automatically engages:
   - `mathematical-foundations` skill (mathematical/mathematical-foundations.md)
   - `asymptotic-theory` skill (mathematical/asymptotic-theory.md)
   - `cross-disciplinary-ideation` skill (research/cross-disciplinary-ideation.md)

3. **Hypothesis Formulation**
   Structure hypotheses:
   - Clearly stated
   - Mathematically precise
   - Empirically testable
   - Theoretically motivated

4. **Validation**
   Check that hypotheses are:
   - Novel (not obvious or already proven)
   - Specific (falsifiable)
   - Relevant (addresses real problem)
   - Feasible (can be tested)

## Types of Statistical Hypotheses

### 1. Theoretical Properties

**Form:** "Under conditions X, estimator θ̂ has property Y"

**Examples:**
- Consistency: θ̂ → θ as n → ∞
- Asymptotic normality: √n(θ̂ - θ) →_d N(0, σ²)
- Efficiency: θ̂ achieves Cramér-Rao lower bound
- Robustness: Breakdown point > 0.5

**Template:**
```
H: Under [regularity conditions], [estimator] is [property]
   with [rate of convergence] under [data-generating process]

Example:
H: Under standard regularity conditions, the bootstrap indirect
   effect estimator is consistent and asymptotically normal with
   convergence rate √n under non-normality.
```

### 2. Comparative Hypotheses

**Form:** "Method A performs better than Method B in terms of criterion C under condition D"

**Examples:**
- Bootstrap has better coverage than delta method under non-normality
- Robust estimator has lower MSE under contamination
- Bayesian approach has better small-sample properties
- Permutation test has higher power under specific alternatives

**Template:**
```
H: [Method A] will show [better performance] than [Method B]
   in terms of [metric] under [conditions]

Example:
H: The percentile bootstrap will achieve nominal coverage
   while the delta method will undercover when the indirect
   effect distribution is skewed.
```

### 3. Generalization Hypotheses

**Form:** "Property that holds under condition X also holds under weaker condition Y"

**Examples:**
- Asymptotic normality extends to dependent data
- Consistency holds under weaker moment conditions
- Method works with discrete outcomes
- Approach generalizes to high dimensions

**Template:**
```
H: [Known property] for [method] under [strong conditions]
   will continue to hold under [weaker conditions]

Example:
H: Consistency of the bootstrap indirect effect, proven
   for continuous mediators, will extend to discrete
   mediators under appropriate regularity conditions.
```

### 4. Computational Hypotheses

**Form:** "Algorithm A is faster/more stable than algorithm B"

**Examples:**
- New algorithm has O(n log n) instead of O(n²)
- Iterative method converges in fewer steps
- Numerical stability is improved
- Parallelization reduces runtime

**Template:**
```
H: [Algorithm A] will achieve [computational goal] while
   maintaining [accuracy requirement] compared to [Algorithm B]

Example:
H: The proposed EM algorithm will converge in 50% fewer
   iterations than standard EM while maintaining numerical
   accuracy within 10⁻⁶.
```

## Hypothesis Quality Checklist

### ✓ Clear and Precise
- [ ] All terms defined
- [ ] Mathematical notation specified
- [ ] Conditions stated explicitly
- [ ] No ambiguous language

### ✓ Testable
- [ ] Can design study to test it
- [ ] Observable quantities involved
- [ ] Can be falsified
- [ ] Success criteria defined

### ✓ Novel
- [ ] Not already proven
- [ ] Extends existing knowledge
- [ ] Non-trivial claim
- [ ] Interesting if true

### ✓ Motivated
- [ ] Clear rationale
- [ ] Addresses real problem
- [ ] Connected to literature
- [ ] Theoretical grounding

## Multiple Hypotheses

For comprehensive research, generate:

### Primary Hypothesis
The main claim you're investigating

### Secondary Hypotheses
Supporting or related claims:
- Robustness checks
- Extensions
- Boundary conditions
- Mechanism exploration

### Example Structure

```
Primary:
H₁: The bias-corrected bootstrap achieves second-order
    accuracy for indirect effects

Secondary:
H₁a: Bias correction reduces actual bias by O(n⁻¹)
H₁b: Coverage probability error is O(n⁻²)
H₁c: Improvement is maintained under non-normality

Boundary:
H₁d: Improvement diminishes when skewness > 3
H₁e: Small samples (n < 50) show minimal improvement
```

## Output Format

### Hypothesis Document

```markdown
# Research Hypotheses: [Topic]

## Background
[Brief context for the hypotheses]

## Primary Hypothesis

**Statement:**
[Precise formal statement]

**Notation:**
- θ: [parameter of interest]
- θ̂: [estimator]
- [other notation]

**Conditions:**
1. [Regularity condition 1]
2. [Regularity condition 2]

**Rationale:**
[Why you expect this to be true]

**Implications:**
[What it means if true]

## Secondary Hypotheses

### H₁a: [Title]
[Same structure]

### H₁b: [Title]
[Same structure]

## Testing Strategy

**Approach:**
[How you'll test these - simulation, theory, application]

**Success Criteria:**
[What constitutes support for hypotheses]

**Potential Falsification:**
[What evidence would reject them]

## Next Steps
1. [Immediate action]
2. [Follow-up]
```

## Common Pitfalls

**Avoid:**
- Vague hypotheses ("Method A is better")
- Tautologies ("The estimator estimates the parameter")
- Untestable claims ("In all possible scenarios...")
- Trivial statements ("With infinite data, estimate is perfect")

**Instead:**
- Be specific about conditions and criteria
- State non-obvious claims
- Make testable predictions
- Focus on realistic, informative scenarios

## Integration

Works well with:
- `/research:lit-gap` - Generate hypotheses from gaps
- `/research:simulation:design` - Design study to test hypotheses
- `/research:analysis-plan` - Plan empirical testing

## Example Interaction

User: `/research:hypothesis "bootstrap mediation intervals"`