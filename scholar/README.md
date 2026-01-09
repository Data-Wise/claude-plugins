# Scholar Plugin

> **Academic workflows for research and teaching** - Literature management, manuscript writing, simulation studies, course material generation, and 17 A-grade research skills

A comprehensive Claude Code plugin for academic workflows combining research and teaching. Features unified Plugin + MCP architecture with 21 slash commands and research skills.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/Data-Wise/claude-plugins)

---

## Features

### 📚 21 Slash Commands

**Literature Management (4 commands)**
- `/arxiv <query>` - Search arXiv for papers (top-level command)
- `/doi <doi>` - Look up paper metadata by DOI (top-level command)
- `/bib:search <query>` - Search BibTeX files for entries
- `/bib:add <file>` - Add BibTeX entries to bibliography

**Manuscript Writing (4 commands)**
- `/manuscript:methods` - Write methods sections
- `/manuscript:results` - Write results sections
- `/manuscript:reviewer` - Generate reviewer responses
- `/manuscript:proof` - Review mathematical proofs

**Simulation Studies (2 commands)**
- `/simulation:design` - Design Monte Carlo studies
- `/simulation:analysis` - Analyze simulation results

**Research Planning (4 commands)**
- `/scholar:lit-gap <topic>` - Identify literature gaps
- `/scholar:hypothesis <topic>` - Generate research hypotheses
- `/scholar:analysis-plan` - Create statistical analysis plans
- `/scholar:method-scout <problem>` - Scout statistical methods for research problems

**Teaching (7 commands - NEW in v1.0.0)**
- `/teaching:syllabus <course>` - Generate comprehensive course syllabus
- `/teaching:assignment <topic>` - Create homework assignments with solutions
- `/teaching:rubric <type>` - Generate detailed grading rubrics
- `/teaching:slides <topic>` - Create lecture slides with examples ⭐ NEW
- `/teaching:quiz <topic>` - Generate quiz questions with answer keys ⭐ NEW
- `/teaching:exam <type>` - Create comprehensive exams with rubrics ⭐ NEW
- `/teaching:feedback <assignment>` - Generate constructive student feedback ⭐ NEW

### 🎯 17 A-Grade Skills

Skills automatically activate when relevant to your work:

**Mathematical (4 skills)**
- `proof-architect` - Rigorous proof construction and validation
- `mathematical-foundations` - Statistical theory foundations
- `identification-theory` - Parameter identifiability analysis
- `asymptotic-theory` - Large-sample theory

**Implementation (5 skills)**
- `simulation-architect` - Monte Carlo study design
- `algorithm-designer` - Statistical algorithm development
- `numerical-methods` - Numerical optimization and computation
- `computational-inference` - Computational statistical inference
- `statistical-software-qa` - Statistical software quality assurance

**Writing (3 skills)**
- `methods-paper-writer` - Statistical methods manuscripts
- `publication-strategist` - Journal selection and positioning
- `methods-communicator` - Clear statistical communication

**Research (5 skills)**
- `literature-gap-finder` - Research gap identification
- `cross-disciplinary-ideation` - Cross-field method transfer
- `method-transfer-engine` - Adapting methods across domains
- `mediation-meta-analyst` - Mediation analysis meta-analysis
- `sensitivity-analyst` - Sensitivity analysis design

### 🔧 Shell API Wrappers

Lightweight shell-based APIs for research tools:
- `arxiv-api.sh` - arXiv paper search and PDF download
- `crossref-api.sh` - DOI lookup and BibTeX retrieval
- `bibtex-utils.sh` - BibTeX file search, add, format

### 🏗️ Architecture

**Unified Plugin + MCP Pattern:**
- `src/core/` - Framework-agnostic business logic
- `src/plugin-api/` - Claude Plugin commands and skills
- `src/mcp-server/` - MCP Protocol tools
- `lib/` - External API wrappers (arXiv, Crossref, BibTeX)

This architecture eliminates IPC overhead by sharing core logic directly between both APIs.

---

## Installation

### From Source (Development)

```bash
# Navigate to claude-plugins monorepo
cd ~/projects/dev-tools/claude-plugins/scholar

# Install in development mode (symlink - changes reflected immediately)
./scripts/install.sh --dev

# Or install in production mode (copy)
./scripts/install.sh
```

### Verify Installation

```bash
# Check plugin is installed
ls -la ~/.claude/plugins/scholar

# Run tests
./tests/test-plugin-structure.sh
```

---

## Quick Start

### Literature Search

```bash
# Search arXiv
/arxiv "bootstrap mediation analysis"

# Look up specific paper
/doi "10.1080/00273171.2014.962683"

# Search your BibTeX files
/bib:search "mediation"
```

### Manuscript Writing

```bash
# Generate methods section
/manuscript:methods

# Write results section with statistical details
/manuscript:results

# Respond to reviewer comments
/manuscript:reviewer
```

### Teaching

```bash
# Create course syllabus
/teaching:syllabus "Introduction to Statistics"

# Generate homework assignment
/teaching:assignment "Linear Regression"

# Create grading rubric
/teaching:rubric "data analysis project"
```

### Research Planning

```bash
# Identify literature gaps
/scholar:lit-gap "causal mediation analysis"

# Generate hypotheses
/scholar:hypothesis "mediation moderation"

# Create analysis plan
/scholar:analysis-plan
```

---

## Command Reference

### Literature Management

#### `/arxiv <query> [limit]`
Search arXiv for papers matching your query.

**Examples:**
```bash
/arxiv "bootstrap mediation"
/arxiv "causal inference" 20
```

**Output:** Title, authors, arXiv ID, publication date, abstract preview

**Follow-up Actions:** Get full details, download PDF, add BibTeX entry

---

#### `/doi <doi>`
Look up paper metadata by DOI using Crossref API.

**Examples:**
```bash
/doi "10.1037/met0000165"
/doi 10.1080/00273171.2014.962683
```

**Output:** Full citation, BibTeX entry, journal information

---

#### `/bib:search <query>`
Search BibTeX files in your project for entries matching keywords.

**Examples:**
```bash
/bib:search "mediation"
/bib:search "Baron Kenny"
```

**Output:** Matching BibTeX entries with citation keys

---

#### `/bib:add <file>`
Add BibTeX entries to your bibliography file.

**Examples:**
```bash
/bib:add references.bib
```

---

### Manuscript Writing

#### `/manuscript:methods`
Generate a methods section for statistical manuscript.

**Includes:**
- Study design description
- Statistical methods with mathematical notation
- Software and implementation details
- Assumptions and diagnostics

---

#### `/manuscript:results`
Write a results section with statistical findings.

**Includes:**
- Descriptive statistics
- Model fit and diagnostics
- Parameter estimates with uncertainty
- Interpretation in context

---

#### `/manuscript:reviewer`
Generate responses to reviewer comments.

**Features:**
- Point-by-point responses
- Additional analyses if requested
- Clarifications and revisions
- Professional academic tone

---

#### `/manuscript:proof`
Review mathematical proofs in manuscript for correctness and clarity.

---

### Simulation Studies

#### `/simulation:design`
Design a Monte Carlo simulation study.

**Includes:**
- Data generation mechanisms
- Estimator implementations
- Performance metrics
- Parallelization strategy

---

#### `/simulation:analysis`
Analyze simulation results and create summary tables.

**Output:**
- Bias, variance, MSE, coverage
- Publication-quality tables
- Convergence diagnostics

---

### Research Planning

#### `/scholar:lit-gap <topic>`
Identify gaps in literature for a research area.

**Output:**
- Current state of literature
- Identified gaps and opportunities
- Potential research questions

---

#### `/scholar:hypothesis <topic>`
Generate testable research hypotheses.

**Output:**
- Theoretical hypotheses
- Statistical hypotheses
- Expected findings

---

#### `/scholar:analysis-plan`
Create a comprehensive statistical analysis plan.

**Includes:**
- Research questions
- Statistical methods
- Sample size justification
- Analysis workflow

---

### Teaching Commands

#### `/teaching:syllabus <course> [semester]`
Generate a comprehensive course syllabus.

**Examples:**
```bash
/teaching:syllabus "Introduction to Statistics"
/teaching:syllabus "Regression Analysis" "Fall 2026"
```

**Includes:**
- Course information and objectives
- Learning outcomes
- Grading policy
- Week-by-week schedule
- Course policies

---

#### `/teaching:assignment <topic> [difficulty]`
Create homework assignments and problem sets.

**Examples:**
```bash
/teaching:assignment "Linear Regression"
/teaching:assignment "Hypothesis Testing" "intermediate"
```

**Includes:**
- Clear learning objectives
- Multiple problem types (conceptual, computational, applied)
- Submission requirements
- Grading criteria

---

#### `/teaching:rubric <assignment-type> [points]`
Generate detailed grading rubrics.

**Examples:**
```bash
/teaching:rubric "data analysis project"
/teaching:rubric "research paper" 100
```

**Includes:**
- Clear criteria for each performance level
- Point allocations
- Observable, measurable descriptors

---

## Skills Reference

Skills automatically activate based on context. See `src/plugin-api/skills/README.md` for detailed documentation of all 17 A-grade skills.

**When do skills activate?**
- Writing methods → `methods-paper-writer`, `methods-communicator`
- Designing simulations → `simulation-architect`, `numerical-methods`
- Mathematical proofs → `proof-architect`, `mathematical-foundations`
- Literature review → `literature-gap-finder`, `cross-disciplinary-ideation`

---

## Architecture Details

### Unified Plugin + MCP Pattern

```
scholar/
├── src/
│   ├── core/              # Business logic (framework-agnostic)
│   │   ├── literature/    # Literature search, metadata
│   │   ├── manuscript/    # Writing assistance
│   │   └── teaching/      # Course material generation
│   ├── plugin-api/        # Claude Plugin commands/skills
│   │   ├── commands/
│   │   └── skills/
│   └── mcp-server/        # MCP Protocol tools (future)
├── lib/                   # External API wrappers
│   ├── arxiv-api.sh
│   ├── crossref-api.sh
│   └── bibtex-utils.sh
├── tests/                 # Test suite
└── scripts/               # Installation scripts
```

**Benefits:**
- No IPC overhead (shared core library)
- Single source of truth for business logic
- Both APIs consume the same tested code
- Easy to maintain and extend

---

## Development

### Running Tests

```bash
cd scholar
./tests/test-plugin-structure.sh
```

**Test Coverage:**
- ✅ Required files present
- ✅ Valid JSON in plugin.json
- ✅ Directory structure
- ✅ 17+ commands exist
- ✅ Teaching commands present
- ✅ 15+ skills exist
- ✅ API wrappers present
- ✅ No hardcoded paths
- ✅ Valid command frontmatter

### Modifying Commands

Commands are in `src/plugin-api/commands/`. Each command is a markdown file with:

1. **YAML frontmatter** (name, description)
2. **User-facing documentation**
3. **`<system>` block** with implementation details

**Example:**
```markdown
---
name: arxiv
description: Search arXiv for papers
---

# Search arXiv

User-facing instructions here...

<system>
Implementation details for Claude...
</system>
```

### Adding New Commands

1. Create `.md` file in appropriate category directory
2. Add frontmatter with `name:` and `description:`
3. Write user-facing documentation
4. Add `<system>` block with implementation
5. Test: `/namespace:command "test input"`

---

## Roadmap

### Phase 1: MVP (Complete)
- ✅ 14 research commands from statistical-research
- ✅ 3 teaching commands (syllabus, assignment, rubric)
- ✅ 17 A-grade skills
- ✅ Shell API wrappers
- ✅ Unified directory structure
- ✅ Installation scripts
- ✅ Test suite

### Phase 2: MCP Server Integration (Future)
- [ ] Implement MCP protocol tools in `src/mcp-server/`
- [ ] Add TypeScript/Zod schemas
- [ ] Test MCP server independently
- [ ] Integrate with Claude Desktop app

### Phase 3: Teaching Expansion (Future)
- [ ] Additional teaching commands (lecture, exam, feedback)
- [ ] LMS integration (Canvas, Blackboard)
- [ ] Export to PDF/Word formats
- [ ] Calendar integration

---

## Contributing

This plugin is part of the [claude-plugins monorepo](https://github.com/Data-Wise/claude-plugins). See the main repository for contribution guidelines.

**Development workflow:**
1. Fork the repository
2. Create a feature branch
3. Make changes in `scholar/` directory
4. Run tests: `./tests/test-plugin-structure.sh`
5. Submit pull request

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Support

- **Issues:** https://github.com/Data-Wise/claude-plugins/issues
- **Documentation:** https://data-wise.github.io/claude-plugins/
- **Monorepo:** https://github.com/Data-Wise/claude-plugins

---

## Related Projects

- **craft** - Full-stack developer toolkit (86 commands)
- **rforge** - R package ecosystem orchestrator
- **workflow** - ADHD-friendly workflow automation (deprecated, merged into craft)
- **statistical-research** - Pure research plugin (deprecated, superseded by scholar)

---

**Ready to use!** Try: `/arxiv "your research topic"`
