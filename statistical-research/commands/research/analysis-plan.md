---
name: research:analysis-plan
description: Create comprehensive statistical analysis plan
---

# Create Analysis Plan

I'll help you develop a comprehensive statistical analysis plan for your research study.

**Usage:** `/research:analysis-plan <study-description>` or `/research:analysis-plan`

**Examples:**
- `/research:analysis-plan "mediation analysis with binary outcome"`
- `/research:analysis-plan "longitudinal study with missing data"`

## Let's plan your analysis

I'll guide you through creating a rigorous, pre-specified analysis plan.

<system>
This command helps create comprehensive statistical analysis plans (SAPs).

## Process

1. **Study Overview**
   - Research question
   - Study design
   - Data characteristics
   - Sample size

2. **Activate Skills**
   Automatically engages:
   - `mathematical-foundations` skill (mathematical/mathematical-foundations.md)
   - `sensitivity-analyst` skill (research/sensitivity-analyst.md)
   - `computational-inference` skill (implementation/computational-inference.md)

3. **Plan Components**
   Structure comprehensive plan:
   - Objectives
   - Variables and outcomes
   - Statistical methods
   - Missing data handling
   - Sensitivity analyses
   - Software and implementation

4. **Documentation**
   Generate pre-registration ready document

## Analysis Plan Structure

### 1. Study Objectives

**Primary Objective:**
- Main research question
- Primary estimand
- Hypothesis to test

**Secondary Objectives:**
- Supporting questions
- Exploratory analyses
- Subgroup analyses

### 2. Variables

**Outcome Variables:**
- Primary outcome (clearly defined)
- Secondary outcomes
- Measurement scale
- Transformations (if any)

**Predictor Variables:**
- Independent variables
- Covariates/confounders
- Mediators/moderators
- How coded/measured

**Example:**
```
Primary Outcome: Depression score (BDI-II, continuous 0-63)
  - Higher scores indicate more severe depression
  - Measured at baseline and 12 weeks post-treatment

Primary Predictor: Treatment group (binary: 0=control, 1=intervention)

Covariates:
  - Age (continuous, years)
  - Sex (binary: 0=female, 1=male)
  - Baseline depression (BDI-II)
```

### 3. Sample Size and Power

**Justification:**
- Target sample size
- Power calculation
- Expected effect size
- Assumed variance
- Attrition/missing data allowance

**Example:**
```
Target n = 200 (100 per group)

Power: 80% to detect δ = 0.4 standardized mean difference
  - α = 0.05 (two-tailed)
  - Assumed SD = 10
  - Allows for 15% attrition
```

### 4. Statistical Methods

**Primary Analysis:**

Specify completely:
- Statistical test/model
- Assumptions
- Estimation method
- Inference approach
- Software package

**Example:**
```
Linear regression model:
  Y = β₀ + β₁·Treatment + β₂·Age + β₃·Sex + β₄·Baseline + ε

Estimation: Ordinary least squares
Inference: Robust standard errors (HC3)
Software: R (lm function with sandwich package)
Primary test: H₀: β₁ = 0 vs. H₁: β₁ ≠ 0
α-level: 0.05 (two-tailed)
```

**Secondary Analyses:**
- Additional models
- Subgroup analyses
- Mediation/moderation
- Time-varying effects (if longitudinal)

### 5. Missing Data

**Mechanism:**
- Expected pattern (MCAR, MAR, MNAR)
- Variables with missing data
- Proportion expected

**Handling:**
- Primary approach (e.g., multiple imputation)
- Sensitivity analysis for mechanism
- Complete-case as sensitivity

**Example:**
```
Primary: Multiple imputation (m=20 imputations)
  - Method: MICE with predictive mean matching
  - Imputation model includes all analysis variables
    plus auxiliary variables (list)
  - Pool estimates using Rubin's rules

Sensitivity: Complete-case analysis
```

### 6. Assumptions and Diagnostics

**For Each Analysis:**

List assumptions and how you'll check them:

```
Linear Regression Assumptions:

1. Linearity:
   - Check: Residual vs. fitted plots
   - Remedy: Add polynomial terms if needed

2. Normality of residuals:
   - Check: Q-Q plot, Shapiro-Wilk test
   - Remedy: Bootstrap inference if violated

3. Homoscedasticity:
   - Check: Scale-location plot, Breusch-Pagan test
   - Remedy: Robust SEs (HC3)

4. No multicollinearity:
   - Check: VIF < 5
   - Remedy: Remove/combine highly correlated predictors

5. Independence:
   - Check: Durbin-Watson test
   - Remedy: Use clustered SEs if needed
```

### 7. Sensitivity Analyses

**What If Assumptions Fail?**

Pre-specify alternatives:

```
Sensitivity Analysis Plan:

1. Non-normality:
   - Percentile bootstrap (10,000 replicates)
   - Permutation test
   - Rank-based methods

2. Outliers:
   - Rerun excluding outliers (> 3 SD)
   - Robust regression (Huber M-estimator)

3. Missing not at random:
   - Pattern-mixture models
   - Selection models
   - Tipping point analysis

4. Model misspecification:
   - Alternative link functions
   - Interaction terms
   - Non-linear terms
```

### 8. Multiple Testing

**If Multiple Comparisons:**

State adjustment strategy:

```
Multiple Testing:
- 3 primary outcomes → Bonferroni (α = 0.05/3 = 0.0167)
- 5 secondary outcomes → FDR control (Benjamini-Hochberg, α = 0.05)
- Exploratory subgroups → No adjustment, clearly labeled exploratory
```

### 9. Reporting

**What Will Be Reported:**

Pre-specify what goes in the paper:

```
Primary Paper Will Report:
1. Descriptive statistics (Table 1)
2. Primary analysis results (Table 2)
3. Assumption diagnostics (Supplementary)
4. Sensitivity analyses (Table 3)

NOT Report:
- Secondary outcomes not in plan
- Post-hoc subgroup analyses
- Model selection based on data
```

### 10. Software

**Implementation:**

```
Software Environment:
- R version 4.3.0 or later
- Key packages:
  * lm() - base stats
  * sandwich (v3.0+) - robust SEs
  * mice (v3.14+) - multiple imputation
  * boot (v1.3+) - bootstrap

Reproducibility:
- Set seed: 20250101
- Session info will be saved
- Data and code will be archived (OSF/GitHub)
```

## Output Document

### Analysis Plan Template

Generate complete SAP:

```markdown
# Statistical Analysis Plan

**Study:** [Title]
**PI:** [Name]
**Statistician:** [Name]
**Date:** [Date]
**Version:** 1.0

## 1. Study Overview
[Description]

## 2. Objectives
### Primary Objective
[Statement]

### Secondary Objectives
1. [Objective 1]
2. [Objective 2]

## 3. Study Design
- Design: [RCT / Observational / etc.]
- Sample size: [n with justification]
- Duration: [Time period]

## 4. Variables
[Complete list with definitions]

## 5. Sample Size and Power
[Calculations and assumptions]

## 6. Statistical Methods
### Primary Analysis
[Complete specification]

### Secondary Analyses
[List]

## 7. Missing Data
[Plan with sensitivity]

## 8. Assumptions and Diagnostics
[List with remedies]

## 9. Sensitivity Analyses
[Pre-specified alternatives]

## 10. Multiple Testing
[Adjustment strategy]

## 11. Reporting
[What will be reported]

## 12. Software
[Environment and packages]

## Appendix: Analysis Code Template
[Pseudocode or actual code skeleton]
```

## Best Practices

1. **Write Before Seeing Data**
   - Pre-registration reduces bias
   - Shows what was planned vs. exploratory

2. **Be Specific**
   - Not "we'll use regression"
   - "We'll use OLS with HC3 robust SEs"

3. **Plan for Violations**
   - Assumptions will be violated
   - Have backup plans ready

4. **Version Control**
   - Date and version the SAP
   - Track changes if updated

5. **Consult Standards**
   - CONSORT for trials
   - STROBE for observational
   - Journal-specific requirements

## Common Issues

**Too Vague:**
- ❌ "We'll use appropriate tests"
- ✅ "Two-sample t-test with Welch correction"

**Too Rigid:**
- ❌ "Only complete cases, no exceptions"
- ✅ "Complete cases primary, MI sensitivity"

**Post-Hoc Looks Planned:**
- ❌ Writing SAP after seeing data
- ✅ Time-stamped pre-registration

## Integration

Works well with:
- `/research:hypothesis` - Use hypotheses in objectives
- `/research:simulation:design` - Plan sample size
- `/research:manuscript:methods` - Turn SAP into methods section

## Example Interaction

User: `/research:analysis-plan "mediation analysis with binary outcome"`