# Command Reference

**Auto-generated:** 2025-12-24 11:10:12

Complete reference of all commands across all plugins.

## Table of Contents

- [Rforge](#rforge) (13 commands)
- [Statistical Research](#statistical-research) (13 commands)
- [Workflow](#workflow) (1 commands)

---

## Rforge

**Plugin:** `rforge`
**Commands:** 13

| Command | Description | Arguments |
|---------|-------------|-----------|
| `/rforge:analyze` | Quick R package analysis with auto-delegation to RForge MCP tools | Optional context (e.g., "Update bootstrap algorithm") |
| `/rforge:capture` | Quick capture ideas and tasks for later (with automatic doc cascade detection) | Task description or idea to capture |
| `/rforge:cascade` | Plan coordinated updates across dependent packages | Optional version or change description |
| `/rforge:complete` | Mark tasks complete with automatic documentation cascade | Task ID or description |
| `/rforge:deps` | Build and visualize dependency graph across R package ecosystem | — |
| `/rforge:detect` | Auto-detect R package project structure (single package, ecosystem, or hybrid) | — |
| `/rforge:doc-check` | Check for documentation drift and inconsistencies across packages | — |
| `/rforge:impact` | Analyze change impact across ecosystem packages | Optional description of changes (e.g., "Breaking API change in extract_mediation") |
| `/rforge:next` | Get ecosystem-aware next task recommendation | — |
| `/rforge:quick` | Ultra-fast analysis using only quick tools (< 10 seconds) | — |
| `/rforge:release` | Plan CRAN submission sequence based on dependencies | Optional package name or version |
| `/rforge:status` | Ecosystem-wide status dashboard showing health, tests, and readiness | — |
| `/rforge:thorough` | Comprehensive analysis with background R processes (2-5 minutes) | Optional context (e.g., "Prepare for CRAN release") |

### Detailed Descriptions

#### `/rforge:analyze`

**Description:** Quick R package analysis with auto-delegation to RForge MCP tools

**Arguments:** Optional context (e.g., "Update bootstrap algorithm")

**Usage:**

Automatically analyze R package changes with intelligent tool delegation and parallel execution.

**Source:** [`rforge/commands/analyze.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/analyze.md)

#### `/rforge:capture`

**Description:** Quick capture ideas and tasks for later (with automatic doc cascade detection)

**Arguments:** Task description or idea to capture

**Usage:**

Quickly capture ideas, tasks, and TODOs with automatic context detection.

**Source:** [`rforge/commands/capture.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/capture.md)

#### `/rforge:cascade`

**Description:** Plan coordinated updates across dependent packages

**Arguments:** Optional version or change description

**Usage:**

Plan coordinated updates across your R package ecosystem dependencies.

**Source:** [`rforge/commands/cascade.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/cascade.md)

#### `/rforge:complete`

**Description:** Mark tasks complete with automatic documentation cascade

**Arguments:** Task ID or description

**Usage:**

Mark tasks complete and automatically trigger documentation cascade updates.

**Source:** [`rforge/commands/complete.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/complete.md)

#### `/rforge:deps`

**Description:** Build and visualize dependency graph across R package ecosystem

**Usage:**

Build and visualize dependency relationships in your R package ecosystem.

**Source:** [`rforge/commands/deps.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/deps.md)

#### `/rforge:detect`

**Description:** Auto-detect R package project structure (single package, ecosystem, or hybrid)

**Usage:**

Automatically detect your R package ecosystem structure.

**Source:** [`rforge/commands/detect.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/detect.md)

#### `/rforge:doc-check`

**Description:** Check for documentation drift and inconsistencies across packages

**Usage:**

Check for documentation inconsistencies and drift across your R package ecosystem.

**Source:** [`rforge/commands/doc-check.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/doc-check.md)

#### `/rforge:impact`

**Description:** Analyze change impact across ecosystem packages

**Arguments:** Optional description of changes (e.g., "Breaking API change in extract_mediation")

**Usage:**

Analyze the ripple effects of changes across your R package ecosystem.

**Source:** [`rforge/commands/impact.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/impact.md)

#### `/rforge:next`

**Description:** Get ecosystem-aware next task recommendation

**Usage:**

Get intelligent recommendations for what to work on next based on ecosystem context.

**Source:** [`rforge/commands/next.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/next.md)

#### `/rforge:quick`

**Description:** Ultra-fast analysis using only quick tools (< 10 seconds)

**Usage:**

Lightning-fast analysis using only quick MCP tools. Results in < 10 seconds guaranteed.

**Source:** [`rforge/commands/quick.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/quick.md)

#### `/rforge:release`

**Description:** Plan CRAN submission sequence based on dependencies

**Arguments:** Optional package name or version

**Usage:**

Plan the optimal CRAN submission sequence for your R package ecosystem.

**Source:** [`rforge/commands/release.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/release.md)

#### `/rforge:status`

**Description:** Ecosystem-wide status dashboard showing health, tests, and readiness

**Usage:**

Get a comprehensive status dashboard for your R package ecosystem.

**Source:** [`rforge/commands/status.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/status.md)

#### `/rforge:thorough`

**Description:** Comprehensive analysis with background R processes (2-5 minutes)

**Arguments:** Optional context (e.g., "Prepare for CRAN release")

**Usage:**

Deep, comprehensive analysis using background R processes. Takes 2-5 minutes but provides publication-quality insights.

**Source:** [`rforge/commands/thorough.md`](https://github.com/Data-Wise/claude-plugins/blob/main/rforge/commands/thorough.md)

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
