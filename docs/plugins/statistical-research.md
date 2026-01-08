# Statistical Research - Research Toolkit

**Version:** 1.1.0 | **Status:** Production-Ready

Comprehensive Claude Code plugin for statistical research workflows. Pure plugin architecture (no MCP dependencies) with literature management, manuscript writing, simulation studies, and 17 A-grade research skills.

## Overview

Statistical Research is a specialized toolkit for statistical researchers and methodologists. It provides intelligent workflows for literature review, manuscript writing, simulation study design, and research planning through slash commands and auto-activating skills.

**Key Innovation:** Pure plugin architecture with lightweight shell-based API wrappers, eliminating MCP dependencies while providing full research workflow support.

## Key Features

### 📚 Literature Management
Four commands for efficient literature discovery and management:
- Search arXiv for statistical papers
- Look up paper metadata by DOI
- Search and add BibTeX entries
- Automated bibliography management

### ✍️ Manuscript Writing
Four specialized commands for academic writing:
- Write methods sections with statistical rigor
- Generate results sections with proper reporting
- Respond to reviewer comments
- Review mathematical proofs for correctness

### 🎲 Simulation Studies
Two commands for Monte Carlo simulation workflows:
- Design comprehensive simulation studies
- Analyze and visualize simulation results

### 🔬 Research Planning
Four commands for research strategy:
- Identify literature gaps
- Generate testable hypotheses
- Create statistical analysis plans
- Scout methods for specific problems

### 🎯 17 A-Grade Skills
Auto-activating skills across 4 domains:
- **Mathematical** (4 skills) - Proof construction, theory, identifiability
- **Implementation** (5 skills) - Algorithms, numerical methods, software QA
- **Writing** (3 skills) - Methods papers, publication strategy, communication
- **Research** (5 skills) - Literature gaps, cross-disciplinary ideation, sensitivity analysis

## Installation

### From Source

```bash
# Clone repository
git clone https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins/statistical-research

# Development mode (symlink)
./scripts/install.sh --dev

# Production mode (copy)
./scripts/install.sh
```

### From npm

```bash
npm install -g @data-wise/statistical-research-plugin
```

### Verify Installation

```bash
# Restart Claude Code, then test
/research:arxiv "mediation analysis bootstrap"
```

## Quick Start

### Literature Search

```bash
# Search arXiv
/research:arxiv "causal mediation analysis"

# Look up paper by DOI
/research:doi "10.1080/01621459.2020.1765785"

# Search BibTeX files
/research:bib:search "Pearl" references.bib

# Add BibTeX entry
/research:bib:add entry.bib references.bib
```

### Manuscript Writing

```bash
# Write methods section
/research:manuscript:methods "Describe the bootstrap mediation analysis"

# Generate results section
/research:manuscript:results "Report simulation study findings"

# Respond to reviewers
/research:manuscript:reviewer "Reviewer 2 questions significance testing"

# Review mathematical proof
/research:manuscript:proof "Check identifiability proof in Appendix A"
```

### Simulation Studies

```bash
# Design Monte Carlo study
/research:simulation:design "Compare bootstrap methods for mediation"

# Analyze results
/research:simulation:analysis results.csv
```

### Research Planning

```bash
# Identify literature gaps
/research:lit-gap "mediation analysis with unmeasured confounding"

# Generate hypotheses
/research:hypothesis "treatment effect heterogeneity"

# Create analysis plan
/research:analysis-plan "randomized trial with mediation"

# Scout methods
/research:method-scout "high-dimensional mediation"
```

## Core Commands

### Literature Management (4 commands)
- **`/research:arxiv`** - Search arXiv for statistical papers
- **`/research:doi`** - Look up paper metadata by DOI
- **`/research:bib:search`** - Search BibTeX files for entries
- **`/research:bib:add`** - Add BibTeX entries to bibliography

### Manuscript Writing (4 commands)
- **`/research:manuscript:methods`** - Write methods sections
- **`/research:manuscript:results`** - Write results sections
- **`/research:manuscript:reviewer`** - Generate reviewer responses
- **`/research:manuscript:proof`** - Review mathematical proofs

### Simulation Studies (2 commands)
- **`/research:simulation:design`** - Design Monte Carlo studies
- **`/research:simulation:analysis`** - Analyze simulation results

### Research Planning (4 commands)
- **`/research:lit-gap`** - Identify literature gaps
- **`/research:hypothesis`** - Generate research hypotheses
- **`/research:analysis-plan`** - Create statistical analysis plans
- **`/research:method-scout`** - Scout statistical methods

## Skills

### Mathematical Skills (4)

**proof-architect**
- Rigorous proof construction and validation
- Theorem-lemma structure
- Mathematical completeness checks

**mathematical-foundations**
- Statistical theory foundations
- Probability theory
- Measure-theoretic statistics

**identification-theory**
- Parameter identifiability analysis
- Causal identification strategies
- Non-parametric identification

**asymptotic-theory**
- Large-sample theory
- Consistency and asymptotic normality
- Weak convergence

### Implementation Skills (5)

**simulation-architect**
- Monte Carlo study design
- Simulation experiment planning
- Results synthesis

**algorithm-designer**
- Statistical algorithm development
- Computational efficiency
- Numerical stability

**numerical-methods**
- Numerical optimization
- Root finding
- Integration

**computational-inference**
- Computational statistical inference
- Bootstrap and resampling
- MCMC methods

**statistical-software-qa**
- Software quality assurance
- Unit testing for statistical code
- Validation studies

### Writing Skills (3)

**methods-paper-writer**
- Statistical methods manuscripts
- Theory-methods-simulation structure
- Clear exposition

**publication-strategist**
- Journal selection and positioning
- Impact factor considerations
- Target audience identification

**methods-communicator**
- Clear statistical communication
- Non-technical summaries
- Visual presentation

### Research Skills (5)

**literature-gap-finder**
- Research gap identification
- Systematic literature review
- Novelty assessment

**cross-disciplinary-ideation**
- Cross-field method transfer
- Interdisciplinary innovation
- Domain adaptation

**method-transfer-engine**
- Adapting methods across domains
- Generalization strategies
- Application examples

**mediation-meta-analyst**
- Mediation analysis meta-analysis
- Effect size synthesis
- Heterogeneity assessment

**sensitivity-analyst**
- Sensitivity analysis design
- Robustness checks
- Assumption validation

## Architecture

### Pure Plugin Pattern

Statistical Research uses a **pure plugin architecture** with no MCP dependencies:

```
statistical-research/
├── commands/              # 14 slash commands
│   ├── literature/        # arXiv, DOI, BibTeX
│   ├── manuscript/        # Methods, results, reviewer
│   ├── simulation/        # Design, analysis
│   └── research/          # Planning, gaps, hypotheses
├── skills/                # 17 A-grade skills
│   ├── mathematical/      # 4 mathematical skills
│   ├── implementation/    # 5 implementation skills
│   ├── writing/           # 3 writing skills
│   └── research/          # 5 research skills
├── lib/                   # Shell API wrappers
│   ├── arxiv-api.sh       # arXiv search
│   ├── crossref-api.sh    # DOI lookup
│   └── bibtex-utils.sh    # BibTeX management
└── tests/                 # Test suite
```

### Shell API Wrappers

Lightweight, portable, and fast:

**arxiv-api.sh**
- Search arXiv API
- Download PDF papers
- Parse metadata

**crossref-api.sh**
- DOI resolution
- BibTeX retrieval
- Metadata formatting

**bibtex-utils.sh**
- Search BibTeX files
- Add entries
- Format validation

**Benefits:**
- No MCP server overhead
- Fast startup (<100ms)
- Easy to maintain and extend
- Shell-scriptable workflows

## Use Cases

### Literature Review

```bash
# Find recent papers on your topic
/research:arxiv "causal mediation bootstrap"

# Add to bibliography
/research:bib:add paper.bib references.bib

# Identify research gaps
/research:lit-gap "mediation with unmeasured confounding"
```

### Manuscript Writing

```bash
# Draft methods section
/research:manuscript:methods "Explain the bootstrap procedure"

# Generate results
/research:manuscript:results "Report coverage rates from simulation"

# Respond to reviewers
/research:manuscript:reviewer "Address concerns about sample size"
```

### Simulation Studies

```bash
# Design comprehensive study
/research:simulation:design "Compare 3 bootstrap methods"

# Analyze results
/research:simulation:analysis results/simulation.csv
```

### Method Development

```bash
# Scout existing methods
/research:method-scout "high-dimensional mediation"

# Generate hypotheses
/research:hypothesis "sensitivity to unmeasured confounding"

# Create analysis plan
/research:analysis-plan "randomized trial with multiple mediators"
```

## Documentation

- **[Commands Reference](../statistical-research/docs/commands.md)** - All 14 commands with usage examples
- **[Skills Guide](../statistical-research/docs/skills.md)** - 17 A-grade research skills
- **[API Wrappers](../statistical-research/docs/api-wrappers.md)** - Shell-based APIs (arXiv, Crossref, BibTeX)
- **[Examples](../statistical-research/docs/examples.md)** - Complete research workflows

## Related

- **[Plugin Development](../PLUGIN-DEVELOPMENT.md)** - Creating research plugins
- **[Workflow Plugin](workflow.md)** - ADHD-friendly task management

## Support

- **GitHub Issues:** [https://github.com/Data-Wise/claude-plugins/issues](https://github.com/Data-Wise/claude-plugins/issues)
- **npm Package:** [https://www.npmjs.com/package/@data-wise/statistical-research-plugin](https://www.npmjs.com/package/@data-wise/statistical-research-plugin)
- **Documentation Site:** [https://data-wise.github.io/claude-plugins](https://data-wise.github.io/claude-plugins)

## Status

### Production-Ready Features
- ✅ 14 slash commands fully functional
- ✅ 17 A-grade skills implemented
- ✅ 3 shell API wrappers tested
- ✅ Pure plugin (no MCP dependencies)
- ✅ Comprehensive test coverage
- ✅ MIT licensed

### Future Enhancements
- 🔄 Additional statistical methods (Bayesian, ML)
- 🔄 Integration with Zotero
- 🔄 LaTeX template generation
- 🔄 Collaborative writing tools
