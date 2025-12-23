---
name: research:simulation:analysis
description: Analyze Monte Carlo simulation results
---

# Analyze Simulation Results

I'll help you analyze and visualize your Monte Carlo simulation results.

**Usage:** `/research:simulation:analysis` or `/research:simulation:analysis <results-file>`

**Examples:**
- `/research:simulation:analysis`
- `/research:simulation:analysis ~/projects/simulations/mediation-bootstrap/results.RData`

## Let's analyze your simulation results

I'll guide you through computing performance metrics and creating effective visualizations.

<system>
This command helps analyze Monte Carlo simulation study results.

## Process

1. **Load Results**
   If results file provided:
   ```bash
   # Read results file
   RESULTS_FILE="$1"
   if [[ -f "$RESULTS_FILE" ]]; then
       echo "=== SIMULATION RESULTS ==="
       echo "File: $RESULTS_FILE"
       echo ""
   fi
   ```

2. **Activate Skills**
   Automatically engages:
   - `simulation-architect` skill (implementation/simulation-architect.md)
   - `computational-inference` skill (implementation/computational-inference.md)
   - `statistical-software-qa` skill (implementation/statistical-software-qa.md)

3. **Compute Performance Metrics**
   Calculate across all conditions:
   - Bias
   - Standard errors
   - RMSE
   - Coverage rates
   - Power/Type I error

4. **Create Visualizations**
   Generate publication-quality plots

## Analysis Workflow

### 1. Load and Inspect Data

**Check:**
- All conditions represented
- Expected number of iterations
- No missing values (or handle appropriately)
- Convergence issues flagged
- Outliers identified

### 2. Calculate Performance Metrics

**For Point Estimates:**

```r
# Bias
bias <- mean(estimates) - true_value

# Monte Carlo standard error of bias
mc_se_bias <- sd(estimates) / sqrt(n_iterations)

# Standard error (empirical)
se_empirical <- sd(estimates)

# RMSE
rmse <- sqrt(mean((estimates - true_value)^2))
```

**For Confidence Intervals:**

```r
# Coverage probability
coverage <- mean(ci_lower <= true_value & ci_upper >= true_value)

# Monte Carlo SE of coverage
mc_se_coverage <- sqrt(coverage * (1 - coverage) / n_iterations)

# Average width
avg_width <- mean(ci_upper - ci_lower)

# Left/right tail error
left_error <- mean(ci_lower > true_value)
right_error <- mean(ci_upper < true_value)
```

**For Hypothesis Tests:**

```r
# Under null (effect = 0)
type1_error <- mean(p_values < alpha)

# Under alternative (effect != 0)
power <- mean(p_values < alpha)
```

### 3. Summarize Across Conditions

Create summary tables:
- Rows: Methods being compared
- Columns: Performance metrics
- Panels: Different conditions (sample size, effect size)

### 4. Visualization

**Recommended Plots:**

1. **Bias Plots**
   - Bias vs. sample size (faceted by effect size)
   - Include confidence bands for Monte Carlo error
   - Horizontal line at 0

2. **Coverage Plots**
   - Coverage probability vs. sample size
   - Horizontal line at nominal level (0.95)
   - Confidence bands for Monte Carlo error

3. **Power Curves**
   - Power vs. effect size
   - Separate curves for different sample sizes
   - Horizontal line at α level

4. **RMSE Comparison**
   - RMSE vs. sample size
   - Separate lines for each method
   - Log scale often helpful

### 5. Quality Checks

**Monte Carlo Error:**
```r
# For coverage probability
mc_error_coverage <- 1.96 * sqrt(coverage * (1-coverage) / n_iterations)

# Rule of thumb: MC error << variability across conditions
```

**Convergence:**
- Check for outliers or failed iterations
- Examine distribution of estimates
- Look for patterns in residuals

## Output Format

Generate comprehensive report:

### Tables

```
Table 1: Bias and Empirical SE by Condition
+--------+---------+----------+-------------+---------------+
| Method | n       | Effect   | Bias        | SE            |
+--------+---------+----------+-------------+---------------+
| Boot   | 100     | 0.3      | -0.002      | 0.051         |
| Delta  | 100     | 0.3      | 0.015       | 0.048         |
| ...
+--------+---------+----------+-------------+---------------+

Table 2: CI Coverage by Condition
+--------+---------+----------+----------+----------+
| Method | n       | Effect   | Coverage | Width    |
+--------+---------+----------+----------+----------+
| Boot   | 100     | 0.3      | 0.947    | 0.198    |
| Delta  | 100     | 0.3      | 0.922    | 0.187    |
| ...
+--------+---------+----------+----------+----------+
```

### Figures

Save publication-ready plots:
- figure1_bias.pdf
- figure2_coverage.pdf
- figure3_power.pdf
- figure4_rmse.pdf

### Interpretation

Provide narrative summary:
- Main findings across conditions
- Method comparisons
- Recommendations
- Limitations and caveats

## Best Practices

1. **Report Monte Carlo Error**
   - Always include MC SE for coverage rates
   - Acknowledge MC uncertainty

2. **Multiple Comparisons**
   - Be cautious with many pairwise comparisons
   - Focus on substantive differences

3. **Practical Significance**
   - Small statistical differences may not matter
   - Consider effect size and sample size

4. **Reproducibility**
   - Save all analysis code
   - Document software versions
   - Include random seeds used

## Integration

Works with:
- `/research:simulation:design` - Ensure metrics match design
- R/Python scripts for detailed analysis
- Manuscript figure creation

## Example Interaction

User: `/research:simulation:analysis ~/simulations/results.RData`