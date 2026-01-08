# Statistical Research - Research Toolkit

> Statistical research toolkit for literature, manuscripts, and simulations

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

⏱️ **5 minutes** • 🟢 Beginner • For statistical researchers

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

| Command | Purpose |
|---------|---------|
| `/research:arxiv` | Search arXiv for statistical papers |
| `/research:doi` | Look up paper metadata by DOI |
| `/research:bib:search` | Search BibTeX files for entries |
| `/research:bib:add` | Add BibTeX entries to bibliography |

### Manuscript Writing (4 commands)

| Command | Purpose |
|---------|---------|
| `/research:manuscript:methods` | Write methods sections |
| `/research:manuscript:results` | Write results sections |
| `/research:manuscript:reviewer` | Generate reviewer responses |
| `/research:manuscript:proof` | Review mathematical proofs |

### Simulation Studies (2 commands)

| Command | Purpose |
|---------|---------|
| `/research:simulation:design` | Design Monte Carlo studies |
| `/research:simulation:analysis` | Analyze simulation results |

### Research Planning (4 commands)

| Command | Purpose |
|---------|---------|
| `/research:lit-gap` | Identify literature gaps |
| `/research:hypothesis` | Generate research hypotheses |
| `/research:analysis-plan` | Create statistical analysis plans |
| `/research:method-scout` | Scout statistical methods |

## Auto-Activating Skills

Skills automatically trigger based on conversation keywords:

### Mathematical Skills (4)

- **proof-architect** - Rigorous proof construction and validation
- **mathematical-foundations** - Statistical theory foundations
- **identification-theory** - Parameter identifiability analysis
- **asymptotic-theory** - Large-sample theory

### Implementation Skills (5)

- **simulation-architect** - Monte Carlo study design
- **algorithm-designer** - Statistical algorithm development
- **numerical-methods** - Numerical optimization, root finding
- **computational-inference** - Bootstrap, resampling, MCMC
- **statistical-software-qa** - Software quality assurance

### Writing Skills (3)

- **methods-paper-writer** - Statistical methods manuscripts
- **publication-strategist** - Journal selection and positioning
- **methods-communicator** - Clear statistical communication

### Research Skills (5)

- **literature-gap-finder** - Research gap identification
- **cross-disciplinary-ideation** - Cross-field method transfer
- **method-transfer-engine** - Adapting methods across domains
- **mediation-meta-analyst** - Mediation analysis meta-analysis
- **sensitivity-analyst** - Sensitivity analysis design

## Use Cases

### Literature Review Workflow

```bash
# 1. Find recent papers on your topic
/research:arxiv "causal mediation bootstrap"

# 2. Add to bibliography
/research:bib:add paper.bib references.bib

# 3. Identify research gaps
/research:lit-gap "mediation with unmeasured confounding"
```

### Manuscript Writing Workflow

```bash
# 1. Draft methods section
/research:manuscript:methods "Explain the bootstrap procedure"

# 2. Generate results
/research:manuscript:results "Report coverage rates from simulation"

# 3. Respond to reviewers
/research:manuscript:reviewer "Address concerns about sample size"
```

### Simulation Study Workflow

```bash
# 1. Design comprehensive study
/research:simulation:design "Compare 3 bootstrap methods"

# 2. Analyze results
/research:simulation:analysis results/simulation.csv
```

### Method Development Workflow

```bash
# 1. Scout existing methods
/research:method-scout "high-dimensional mediation"

# 2. Generate hypotheses
/research:hypothesis "sensitivity to unmeasured confounding"

# 3. Create analysis plan
/research:analysis-plan "randomized trial with multiple mediators"
```

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

**Benefits:**

- No MCP server overhead
- Fast startup (<100ms)
- Easy to maintain and extend
- Shell-scriptable workflows

## Next Steps

- **[Commands](commands.md)** - All 14 commands with usage examples
- **[Skills](skills.md)** - 17 A-grade research skills
- **[API Wrappers](api-wrappers.md)** - Shell-based APIs (arXiv, Crossref, BibTeX)
- **[Examples](examples.md)** - Complete research workflows

---

**Last Updated:** 2026-01-09
**Document Version:** v1.1.0
**Status:** ✅ Production ready with 14 commands, 17 A-grade skills, pure plugin architecture
