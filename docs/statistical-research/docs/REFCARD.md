# Statistical Research Plugin - Reference Card

> **Version:** 1.0.0 | **Last Updated:** 2025-12-23

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  STATISTICAL RESEARCH PLUGIN REFERENCE                             v1.0.0  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LITERATURE (4 commands)        │  SIMULATION (2 commands)                 │
│  ─────────                       │  ──────────                              │
│  /lit:arxiv                      │  /sim:design                             │
│    Search arXiv papers           │    Design Monte Carlo study             │
│  /lit:doi                        │  /sim:analysis                           │
│    Lookup by DOI                 │    Analyze simulation results           │
│  /lit:bib-add                    │                                          │
│    Add to BibTeX                 │  RESEARCH (3 commands)                   │
│  /lit:bib-search                 │  ────────                                │
│    Search BibTeX library         │  /research:hypothesis                    │
│                                  │    Generate hypotheses                   │
│  MANUSCRIPT (4 commands)         │  /research:analysis-plan                 │
│  ──────────                      │    Create analysis plan                  │
│  /ms:methods                     │  /research:lit-gap                       │
│    Write methods section         │    Find literature gaps                  │
│  /ms:results                     │                                          │
│    Write results section         │                                          │
│  /ms:proof                       │                                          │
│    Review mathematical proof     │                                          │
│  /ms:reviewer                    │                                          │
│    Respond to reviewers          │                                          │
│                                  │                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  AUTO-ACTIVATING SKILLS (17)                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│  MATHEMATICAL (4)                │  WRITING (3)                             │
│  • Asymptotic Theory             │  • Methods Communicator                  │
│  • Identification Theory         │  • Methods Paper Writer                  │
│  • Mathematical Foundations      │  • Publication Strategist                │
│  • Proof Architect               │                                          │
│                                  │  RESEARCH (5)                            │
│  IMPLEMENTATION (5)              │  • Cross-Disciplinary Ideation           │
│  • Algorithm Designer            │  • Literature Gap Finder                 │
│  • Computational Inference       │  • Mediation Meta-Analyst                │
│  • Numerical Methods             │  • Method Transfer Engine                │
│  • Simulation Architect          │  • Sensitivity Analyst                   │
│  • Statistical Software QA       │                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  COMMON WORKFLOWS                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  Literature Review               │  Manuscript Writing                      │
│  1. /lit:arxiv "topic"           │  1. /ms:methods                          │
│  2. /lit:doi 10.xxxx/yyyy        │  2. /ms:results                          │
│  3. /lit:bib-add                 │  3. /ms:proof (if needed)                │
│  4. /research:lit-gap            │  4. /ms:reviewer (after review)          │
│                                  │                                          │
│  Simulation Study                │  Research Planning                       │
│  1. /sim:design                  │  1. /research:lit-gap                    │
│  2. Run simulations              │  2. /research:hypothesis                 │
│  3. /sim:analysis                │  3. /research:analysis-plan              │
├─────────────────────────────────────────────────────────────────────────────┤
│  TIPS                                                                       │
│  • Skills activate automatically - no need to invoke them                   │
│  • Use /lit:arxiv for quick paper searches without leaving Claude           │
│  • /sim:design asks questions to guide Monte Carlo study design             │
│  • /ms:reviewer generates responses based on your paper context             │
│  • BibTeX commands work with local .bib files in your project               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Quick Command Reference

### Literature Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `/lit:arxiv` | Search arXiv | `/lit:arxiv "mediation analysis bootstrap"` |
| `/lit:doi` | Lookup by DOI | `/lit:doi 10.1037/met0000425` |
| `/lit:bib-add` | Add citation | `/lit:bib-add` (interactive) |
| `/lit:bib-search` | Search BibTeX | `/lit:bib-search "MacKinnon"` |

### Manuscript Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/ms:methods` | Write methods | New paper or updating methods section |
| `/ms:results` | Write results | After analysis complete |
| `/ms:proof` | Review proof | Mathematical proofs in paper |
| `/ms:reviewer` | Respond to reviewers | After receiving peer reviews |

### Simulation Commands

| Command | Purpose | Output |
|---------|---------|--------|
| `/sim:design` | Design study | Simulation parameters, estimands, DGP |
| `/sim:analysis` | Analyze results | Bias, coverage, power, recommendations |

### Research Commands

| Command | Purpose | Best For |
|---------|---------|----------|
| `/research:hypothesis` | Generate hypotheses | Early research planning |
| `/research:analysis-plan` | Create analysis plan | Pre-registration, planning |
| `/research:lit-gap` | Find gaps | Literature review, proposal writing |

---

## Skill Activation Triggers

Skills activate automatically when you're working on relevant tasks:

| Skill | Activates When... |
|-------|-------------------|
| **Asymptotic Theory** | Discussing convergence, CLT, consistency |
| **Identification Theory** | Parameter identification, causal inference |
| **Proof Architect** | Writing or reviewing mathematical proofs |
| **Simulation Architect** | Designing Monte Carlo studies |
| **Algorithm Designer** | Developing statistical algorithms |
| **Methods Paper Writer** | Writing methodology papers |
| **Literature Gap Finder** | Conducting literature reviews |
| **Sensitivity Analyst** | Assessing assumption robustness |

---

## Installation

**Private Installation (Personal Use):**

```bash
cd ~/projects/dev-tools/claude-plugins/statistical-research

# Development mode (recommended)
./install-private.sh --dev

# Production mode
./install-private.sh
```

**Uninstall:**

```bash
./uninstall-private.sh
```

---

## File Structure

```
statistical-research/
├── commands/              # 13 slash commands
│   ├── literature/        # 4 commands
│   ├── manuscript/        # 4 commands
│   ├── simulation/        # 2 commands
│   └── research/          # 3 commands
├── skills/                # 17 A-grade skills
│   ├── mathematical/      # 4 skills
│   ├── implementation/    # 5 skills
│   ├── writing/           # 3 skills
│   └── research/          # 5 skills
├── lib/                   # API wrappers
│   ├── arxiv-api.sh
│   ├── crossref-api.sh
│   └── bibtex-utils.sh
└── docs/                  # Documentation
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Commands not showing | Restart Claude Code, check `~/.claude/plugins/` |
| arXiv search fails | Check internet connection, try simpler query |
| BibTeX not found | Ensure `.bib` file in current project directory |
| Skills not activating | They auto-activate - use natural language tasks |

---

## More Documentation

- **Installation Guide:** `INSTALL-PRIVATE.md`
- **Main README:** `README.md`
- **Plugin Repository:** https://github.com/Data-Wise/claude-plugins
- **Skills Guide:** `skills/README.md`

---

**Quick Start:** `/lit:arxiv "your research topic"` → Get started with literature search!
