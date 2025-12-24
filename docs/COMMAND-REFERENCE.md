# Command Reference

**Auto-generated:** 2025-12-23 22:09:57

Complete reference of all commands across all plugins.

## Table of Contents

- [Rforge Orchestrator](#rforge-orchestrator) (3 commands)
- [Statistical Research](#statistical-research) (13 commands)
- [Workflow](#workflow) (1 commands)

---

## Rforge Orchestrator

**Plugin:** `rforge-orchestrator`
**Commands:** 3

| Command | Description | Arguments |
|---------|-------------|-----------|
| `/rforge:analyze` | Quick R package analysis with auto-delegation to RForge MCP tools | Optional context (e.g., "Update bootstrap algorithm") |
| `/rforge:quick` | Ultra-fast analysis using only quick tools (< 10 seconds) | — |
| `/rforge:thorough` | Comprehensive analysis with background R processes (2-5 minutes) | Optional context (e.g., "Prepare for CRAN release") |

### Detailed Descriptions

#### `/rforge:analyze`

**Description:** Quick R package analysis with auto-delegation to RForge MCP tools

**Arguments:** Optional context (e.g., "Update bootstrap algorithm")

**Usage:**

Automatically analyze R package changes with intelligent tool delegation and parallel execution.

**Source:** [`rforge-orchestrator/commands/analyze.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge-orchestrator/commands/analyze.md)

#### `/rforge:quick`

**Description:** Ultra-fast analysis using only quick tools (< 10 seconds)

**Usage:**

Lightning-fast analysis using only quick MCP tools. Results in < 10 seconds guaranteed.

**Source:** [`rforge-orchestrator/commands/quick.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge-orchestrator/commands/quick.md)

#### `/rforge:thorough`

**Description:** Comprehensive analysis with background R processes (2-5 minutes)

**Arguments:** Optional context (e.g., "Prepare for CRAN release")

**Usage:**

Deep, comprehensive analysis using background R processes. Takes 2-5 minutes but provides publication-quality insights.

**Source:** [`rforge-orchestrator/commands/thorough.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge-orchestrator/commands/thorough.md)

---

## Statistical Research

**Plugin:** `statistical-research`
**Commands:** 13

| Command | Description | Arguments |
|---------|-------------|-----------|
| `/research:analysis-plan` | Create comprehensive statistical analysis plan | — |
| `/research:arxiv` | Search arXiv for papers | — |
| `/research:bib:add` | Add BibTeX entry to bibliography file | — |
| `/research:bib:search` | Search BibTeX files for entries | — |
| `/research:doi` | Look up paper metadata by DOI | — |
| `/research:hypothesis` | Generate statistical research hypotheses | — |
| `/research:lit-gap` | Identify research gaps in literature | — |
| `/research:manuscript:methods` | Write methods section for statistical manuscript | — |
| `/research:manuscript:proof` | Review mathematical proofs in manuscript | — |
| `/research:manuscript:results` | Write results section for statistical manuscript | — |
| `/research:manuscript:reviewer` | Generate response to reviewer comments | — |
| `/research:simulation:analysis` | Analyze Monte Carlo simulation results | — |
| `/research:simulation:design` | Design Monte Carlo simulation study | — |

### Detailed Descriptions

#### `/research:analysis-plan`

**Description:** Create comprehensive statistical analysis plan

**Usage:**

I'll help you develop a comprehensive statistical analysis plan for your research study.

**Source:** [`statistical-research/commands/research/analysis-plan.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/research/analysis-plan.md)

#### `/research:arxiv`

**Description:** Search arXiv for papers

**Usage:**

I'll help you search arXiv for relevant papers.

**Source:** [`statistical-research/commands/literature/arxiv.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/literature/arxiv.md)

#### `/research:bib:add`

**Description:** Add BibTeX entry to bibliography file

**Usage:**

I'll help you add a BibTeX entry to your bibliography file.

**Source:** [`statistical-research/commands/literature/bib-add.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/literature/bib-add.md)

#### `/research:bib:search`

**Description:** Search BibTeX files for entries

**Usage:**

I'll search your BibTeX files for entries matching your query.

**Source:** [`statistical-research/commands/literature/bib-search.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/literature/bib-search.md)

#### `/research:doi`

**Description:** Look up paper metadata by DOI

**Usage:**

I'll retrieve metadata for a paper using its DOI (Digital Object Identifier).

**Source:** [`statistical-research/commands/literature/doi.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/literature/doi.md)

#### `/research:hypothesis`

**Description:** Generate statistical research hypotheses

**Usage:**

I'll help you formulate clear, testable statistical research hypotheses.

**Source:** [`statistical-research/commands/research/hypothesis.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/research/hypothesis.md)

#### `/research:lit-gap`

**Description:** Identify research gaps in literature

**Usage:**

I'll help you identify research gaps and opportunities in your area of statistical research.

**Source:** [`statistical-research/commands/research/lit-gap.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/research/lit-gap.md)

#### `/research:manuscript:methods`

**Description:** Write methods section for statistical manuscript

**Usage:**

I'll help you write a comprehensive methods section for your statistical manuscript.

**Source:** [`statistical-research/commands/manuscript/methods.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/manuscript/methods.md)

#### `/research:manuscript:proof`

**Description:** Review mathematical proofs in manuscript

**Usage:**

I'll help you review and refine mathematical proofs in your statistical manuscript.

**Source:** [`statistical-research/commands/manuscript/proof.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/manuscript/proof.md)

#### `/research:manuscript:results`

**Description:** Write results section for statistical manuscript

**Usage:**

I'll help you write a clear and comprehensive results section for your statistical manuscript.

**Source:** [`statistical-research/commands/manuscript/results.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/manuscript/results.md)

#### `/research:manuscript:reviewer`

**Description:** Generate response to reviewer comments

**Usage:**

I'll help you craft professional, thorough responses to reviewer comments on your manuscript.

**Source:** [`statistical-research/commands/manuscript/reviewer.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/manuscript/reviewer.md)

#### `/research:simulation:analysis`

**Description:** Analyze Monte Carlo simulation results

**Usage:**

I'll help you analyze and visualize your Monte Carlo simulation results.

**Source:** [`statistical-research/commands/simulation/analysis.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/simulation/analysis.md)

#### `/research:simulation:design`

**Description:** Design Monte Carlo simulation study

**Usage:**

I'll help you design a rigorous Monte Carlo simulation study for your statistical research.

**Source:** [`statistical-research/commands/simulation/design.md`](https://github.com/Data-Wise/claude-plugins/blob/main/statistical-research/commands/simulation/design.md)

---

## Workflow

**Plugin:** `workflow`
**Commands:** 1

| Command | Description | Arguments |
|---------|-------------|-----------|
| `/brainstorm` | Enhanced brainstorming with smart detection, design modes, and automatic agent delegation for deep analysis | — |

### Detailed Descriptions

#### `/brainstorm`

**Description:** Enhanced brainstorming with smart detection, design modes, and automatic agent delegation for deep analysis

**Usage:**

**Usage:**
```bash
/brainstorm                          # Auto-detect mode from context
/brainstorm feature                  # Feature brainstorm mode
/brainstorm architecture             # Architectu

**Source:** [`workflow/commands/brainstorm.md`](https://github.com/Data-Wise/claude-plugins/blob/main/workflow/commands/brainstorm.md)

---

## How to Use Commands

Commands are invoked in Claude Code using the `/` prefix:

```
/command-name [arguments]
```

**Examples:**
```
/rforge:quick
/rforge:analyze "Update bootstrap algorithm"
/research:arxiv mediation analysis
/brainstorm
```

---

**Note:** This document is auto-generated from command frontmatter.
Do not edit manually - regenerate with `scripts/generate-command-reference.py`
