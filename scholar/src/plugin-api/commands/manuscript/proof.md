---
name: research:manuscript:proof
description: Review mathematical proofs in manuscript
---

# Review Mathematical Proofs

I'll help you review and refine mathematical proofs in your statistical manuscript.

**Usage:** `/research:manuscript:proof` or `/research:manuscript:proof <proof-file>`

**Examples:**
- `/research:manuscript:proof`
- `/research:manuscript:proof ~/Documents/proofs/theorem1.tex`

## Let's review your proof

I'll check for rigor, clarity, and correctness.

<system>
This command helps review mathematical proofs for statistical manuscripts.

## Process

1. **Read Proof**
   If proof file provided:
   ```bash
   # Read proof file
   PROOF_FILE="$1"
   if [[ -f "$PROOF_FILE" ]]; then
       echo "=== PROOF TO REVIEW ==="
       cat "$PROOF_FILE"
       echo ""
   fi
   ```

2. **Activate Skills**
   Automatically engages:
   - `proof-architect` skill (mathematical/proof-architect.md)
   - `mathematical-foundations` skill (mathematical/mathematical-foundations.md)
   - Relevant theory skills (asymptotic-theory, identification-theory)

3. **Review Checklist**
   - Logical structure
   - Mathematical rigor
   - Completeness
   - Clarity of exposition
   - Notation consistency

4. **Provide Feedback**
   - Identify gaps or unclear steps
   - Suggest improvements
   - Check assumptions
   - Verify references

## Proof Review Checklist

### Logical Structure
- [ ] Clear statement of theorem/proposition
- [ ] Explicit assumptions stated
- [ ] Logical flow from assumptions to conclusion
- [ ] No circular reasoning
- [ ] All cases considered

### Mathematical Rigor
- [ ] All claims justified
- [ ] Technical conditions verified
- [ ] Limits and convergence well-defined
- [ ] Measurability/integrability conditions stated
- [ ] Inequalities valid

### Completeness
- [ ] No missing steps
- [ ] All notation defined
- [ ] References to lemmas/theorems complete
- [ ] Edge cases handled
- [ ] Proof of necessity and sufficiency (if claimed)

### Clarity
- [ ] Proof strategy explained
- [ ] Key insights highlighted
- [ ] Difficult steps elaborated
- [ ] Intuition provided where helpful
- [ ] Notation consistent with manuscript

## Common Issues to Check

### Statistical Proofs
- **Asymptotic theory:** Check regularity conditions, uniform convergence, dominated convergence
- **Probability limits:** Verify ε-δ arguments, weak/strong convergence
- **Consistency:** Check identifiability, parameter space compactness
- **Asymptotic normality:** Verify Lindeberg-Feller conditions, CLT applicability
- **Bootstrap:** Check consistency conditions, Polya's theorem

### Measure Theory
- **Integration:** Verify integrability, dominated convergence theorem applicability
- **Random variables:** Check measurability
- **Convergence:** Distinguish almost sure, in probability, in distribution
- **Expectations:** Verify existence, Fubini's theorem applicability

### Matrix Algebra
- **Inverses:** Check non-singularity conditions
- **Decompositions:** Verify existence conditions (e.g., positive definiteness for Cholesky)
- **Norms:** Check triangle inequality, submultiplicativity
- **Eigenvalues:** Verify spectral properties

## Feedback Format

### For Each Issue Found

**Line/Equation:** [Reference to specific location]

**Issue:** [Description of problem]

**Severity:** Critical / Important / Minor / Suggestion

**Suggested Fix:** [How to address it]

**Explanation:** [Why this matters]

## Improvement Suggestions

### Structure
- Add proof roadmap for long proofs
- Break into lemmas for modularity
- Add intermediate results
- Improve transitions between steps

### Clarity
- Define technical terms
- Add intuition before technical details
- Explain "it follows that" steps
- Reference standard results explicitly

### Rigor
- Strengthen weak arguments
- Add missing conditions
- Verify technical details
- Fix logical gaps

## Example Interaction

User: `/research:manuscript:proof`

[Paste or provide proof]