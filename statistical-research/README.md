# Statistical Research Plugin

> **Statistical research workflows for Claude Code** - Literature management, manuscript writing, simulation studies, and 17 A-grade research skills

A comprehensive Claude Code plugin for statistical research workflows. Pure plugin architecture (no MCP dependencies) with slash commands, research skills, and shell-based API wrappers for arXiv, Crossref, and BibTeX.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/Data-Wise/statistical-research-plugin)

---

## Features

### 📚 14 Slash Commands

**Literature Management (4 commands)**
- `/research:arxiv` - Search arXiv for statistical papers
- `/research:doi` - Look up paper metadata by DOI
- `/research:bib:search` - Search BibTeX files for entries
- `/research:bib:add` - Add BibTeX entries to bibliography

**Manuscript Writing (4 commands)**
- `/research:manuscript:methods` - Write methods sections
- `/research:manuscript:results` - Write results sections
- `/research:manuscript:reviewer` - Generate reviewer responses
- `/research:manuscript:proof` - Review mathematical proofs

**Simulation Studies (2 commands)**
- `/research:simulation:design` - Design Monte Carlo studies
- `/research:simulation:analysis` - Analyze simulation results

**Research Planning (4 commands)**
- `/research:lit-gap` - Identify literature gaps
- `/research:hypothesis` - Generate research hypotheses
- `/research:analysis-plan` - Create statistical analysis plans
- `/research:method-scout` - Scout statistical methods for a problem

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

---

## Installation

### From Source (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/Data-Wise/statistical-research-plugin.git
cd statistical-research-plugin

# Install in development mode (symlink - changes reflected immediately)
./scripts/install.sh --dev

# Or install in production mode (copy)
./scripts/install.sh
```

### From npm (Coming Soon)

```bash
npm install -g @data-wise/statistical-research-plugin
```

### From Claude Code Plugin Registry (Future)

```bash
claude plugin install statistical-research
```

---

## Quick Start

### 1. Search Literature

```
/research:arxiv "bootstrap mediation analysis"
```

Searches arXiv and displays:
- Title, authors, arXiv ID
- Publication date
- Abstract preview

### 2. Write Methods Section

```
/research:manuscript:methods "bootstrap mediation"
```

Activates `methods-paper-writer` and `methods-communicator` skills to guide you through writing a rigorous methods section with:
- Clear model specification
- Estimation procedures
- Software implementation details
- Reproducibility information

### 3. Design Simulation Study

```
/research:simulation:design "bootstrap CI coverage"
```

Activates `simulation-architect` skill to help plan:
- Data-generating mechanisms
- Factorial design dimensions
- Performance metrics
- Computational strategy

### 4. Identify Research Gaps

```
/research:lit-gap "causal mediation"
```

Activates `literature-gap-finder` and `cross-disciplinary-ideation` skills to:
- Analyze current literature
- Identify methodological gaps
- Suggest promising research directions
- Find cross-disciplinary opportunities

---

## Command Reference

### Literature Commands

#### `/research:arxiv <query> [limit]`

Search arXiv for papers.

**Arguments:**
- `query` (required): Search terms
- `limit` (optional): Number of results (default: 10)

**Examples:**
```
/research:arxiv "causal inference mediation"
/research:arxiv "bootstrap standard errors" 20
```

**Output:** Title, authors, arXiv ID, date, abstract preview

#### `/research:doi <doi>`

Look up paper metadata by DOI.

**Arguments:**
- `doi` (required): Digital Object Identifier (e.g., 10.1037/met0000310)

**Examples:**
```
/research:doi 10.1037/met0000310
/research:doi 10.1080/00273171.2017.1354758
```

**Output:** Complete metadata (title, authors, journal, year, volume, pages)

**Follow-up:** Can get BibTeX citation or check citation count

#### `/research:bib:search <query> [file]`

Search BibTeX files for entries.

**Arguments:**
- `query` (required): Search terms
- `file` (optional): Specific .bib file (otherwise searches common locations)

**Examples:**
```
/research:bib:search "MacKinnon"
/research:bib:search "mediation" ~/Documents/refs.bib
```

**Search locations (if no file specified):**
1. `$HOME/Zotero/bibtex/`
2. `$HOME/Documents/references/`
3. Current working directory

#### `/research:bib:add <file>`

Add BibTeX entry to bibliography file.

**Arguments:**
- `file` (required): Path to .bib file

**Examples:**
```
/research:bib:add ~/Documents/references/mediation.bib
```

**Features:**
- Creates file if it doesn't exist
- Checks for duplicate cite keys
- Prompts to overwrite duplicates

### Manuscript Commands

#### `/research:manuscript:methods [topic]`

Write methods section for statistical manuscript.

**Activates:**
- `methods-paper-writer` skill
- `methods-communicator` skill

**Guides through:**
- Data description
- Statistical model specification
- Estimation procedure
- Software and implementation
- Assumptions and diagnostics

#### `/research:manuscript:results [topic]`

Write results section for statistical manuscript.

**Activates:**
- `methods-paper-writer` skill
- `methods-communicator` skill
- `publication-strategist` skill

**Covers:**
- Descriptive statistics
- Primary analysis results
- Model assessment
- Sensitivity analyses

#### `/research:manuscript:reviewer [review-file]`

Generate professional response to reviewer comments.

**Arguments:**
- `review-file` (optional): Path to reviewer comments file

**Activates:**
- `methods-paper-writer` skill
- `methods-communicator` skill
- `publication-strategist` skill

**Generates:**
- Structured response for each comment
- Acknowledgment and explanation
- Specific changes made
- Professional, courteous tone

#### `/research:manuscript:proof [proof-file]`

Review mathematical proofs for rigor and clarity.

**Arguments:**
- `proof-file` (optional): Path to proof file

**Activates:**
- `proof-architect` skill
- `mathematical-foundations` skill
- Relevant theory skills

**Reviews:**
- Logical structure
- Mathematical rigor
- Completeness
- Notation consistency
- Common statistical proof issues

### Simulation Commands

#### `/research:simulation:design [topic]`

Design rigorous Monte Carlo simulation study.

**Activates:**
- `simulation-architect` skill
- `algorithm-designer` skill
- `numerical-methods` skill

**Creates plan for:**
- Data-generating mechanisms
- Factorial design across conditions
- Performance metrics (bias, SE, coverage, power)
- Computational resources
- Implementation strategy

#### `/research:simulation:analysis [results-file]`

Analyze Monte Carlo simulation results.

**Arguments:**
- `results-file` (optional): Path to results file

**Activates:**
- `simulation-architect` skill
- `computational-inference` skill
- `statistical-software-qa` skill

**Produces:**
- Performance metric calculations
- Summary tables
- Publication-quality figures
- Interpretation and recommendations

### Research Commands

#### `/research:lit-gap <topic>`

Identify research gaps in literature.

**Arguments:**
- `topic` (required): Research area

**Activates:**
- `literature-gap-finder` skill
- `cross-disciplinary-ideation` skill
- `method-transfer-engine` skill

**Analyzes:**
- Methodological gaps
- Application domains
- Theoretical foundations
- Computational approaches

**Outputs:**
- Gap identification report
- Promising research directions
- Cross-disciplinary opportunities

#### `/research:hypothesis [topic]`

Generate statistical research hypotheses.

**Arguments:**
- `topic` (optional): Research focus

**Activates:**
- `mathematical-foundations` skill
- `asymptotic-theory` skill
- `cross-disciplinary-ideation` skill

**Generates:**
- Primary hypothesis (mathematically precise)
- Secondary hypotheses
- Testing strategy
- Success criteria

#### `/research:analysis-plan [description]`

Create comprehensive statistical analysis plan.

**Arguments:**
- `description` (optional): Study description

**Activates:**
- `mathematical-foundations` skill
- `sensitivity-analyst` skill
- `computational-inference` skill

**Produces:**
- Pre-registration ready document
- Complete methods specification
- Missing data handling
- Sensitivity analyses
- Software/implementation details

#### `/research:method-scout <problem>`

Scout statistical methods for a research problem.

**Arguments:**
- `problem` (required): Research problem description

**Activates:**
- `cross-disciplinary-ideation` skill
- `method-transfer-engine` skill
- `mathematical-foundations` skill

**Process:**
1. Understand research question and data structure
2. Search for methods across disciplines
3. Identify candidate methods
4. Evaluate assumptions and requirements
5. Compare trade-offs (complexity, interpretability, power)
6. Recommend best options with justification

**Produces:**
- Candidate methods with descriptions
- Assumption requirements for each
- Comparison table across criteria
- Justified recommendation
- Key references and software

---

## Skills Guide

Skills automatically activate based on context. No need to manually invoke them.

### When Skills Activate

**Mathematical Skills:**
- Writing proofs → `proof-architect`
- Theoretical derivations → `mathematical-foundations`
- Parameter identifiability → `identification-theory`
- Asymptotic properties → `asymptotic-theory`

**Implementation Skills:**
- Simulation design → `simulation-architect`
- Algorithm development → `algorithm-designer`
- Numerical issues → `numerical-methods`
- Computational inference → `computational-inference`
- Software testing → `statistical-software-qa`

**Writing Skills:**
- Methods sections → `methods-paper-writer`
- Journal positioning → `publication-strategist`
- Explaining statistics → `methods-communicator`

**Research Skills:**
- Finding gaps → `literature-gap-finder`
- Cross-field ideas → `cross-disciplinary-ideation`
- Method adaptation → `method-transfer-engine`
- Mediation meta-analysis → `mediation-meta-analyst`
- Sensitivity analysis → `sensitivity-analyst`

---

## Development

### Project Structure

```
statistical-research/
├── .claude-plugin/
│   └── plugin.json           # Plugin metadata
├── commands/                  # Slash commands
│   ├── literature/           # 4 literature commands
│   ├── manuscript/           # 4 manuscript commands
│   ├── simulation/           # 2 simulation commands
│   └── research/             # 4 research commands
├── skills/                    # 17 A-grade skills
│   ├── mathematical/         # 4 mathematical skills
│   ├── implementation/       # 5 implementation skills
│   ├── writing/              # 3 writing skills
│   └── research/             # 5 research skills
├── lib/                       # Shell API wrappers
│   ├── arxiv-api.sh          # arXiv API
│   ├── crossref-api.sh       # Crossref API
│   └── bibtex-utils.sh       # BibTeX utilities
├── scripts/                   # Installation scripts
│   ├── install.sh            # Install (--dev for symlink)
│   └── uninstall.sh          # Uninstall
├── package.json              # npm package config
└── README.md                 # This file
```

### Development Mode

Install in development mode to edit source files and see changes immediately:

```bash
cd ~/projects/dev-tools/claude-plugins/statistical-research
./scripts/install.sh --dev
```

This creates a symlink from `~/.claude/plugins/statistical-research/` to your source directory.

### Testing Changes

After editing source files:
1. Changes are immediately available (dev mode)
2. Test commands in Claude Code
3. Check skill activation
4. Verify shell API wrappers work

### Adding New Commands

1. Create markdown file in appropriate `commands/` subdirectory
2. Follow existing command structure:
   ```markdown
   ---
   name: research:command-name
   description: Brief description
   ---

   # Command Title

   [User-facing content]

   <system>
   [Implementation details]
   </system>
   ```
3. Update `.claude-plugin/plugin.json` to register command
4. Test installation and usage

### Adding New Skills

1. Create skill file in appropriate `skills/` subdirectory
2. Follow A-grade skill template (see existing skills)
3. Include clear activation conditions
4. Test automatic activation

---

## API Integration

### arXiv API

The `arxiv-api.sh` wrapper provides:

**Functions:**
- `arxiv_search "query" [limit]` - Search papers
- `arxiv_get_paper "arxiv_id"` - Get paper details
- `arxiv_download_pdf "arxiv_id" [dir]` - Download PDF

**Example:**
```bash
source "${CLAUDE_PLUGIN_ROOT}/lib/arxiv-api.sh"
arxiv_search "mediation analysis" 10
```

### Crossref API

The `crossref-api.sh` wrapper provides:

**Functions:**
- `crossref_lookup_doi "doi"` - Look up metadata
- `crossref_get_bibtex "doi"` - Get BibTeX
- `crossref_search "query" [limit]` - Search papers
- `crossref_citation_count "doi"` - Get citation count

**Example:**
```bash
source "${CLAUDE_PLUGIN_ROOT}/lib/crossref-api.sh"
crossref_lookup_doi "10.1037/met0000310"
```

### BibTeX Utilities

The `bibtex-utils.sh` wrapper provides:

**Functions:**
- `bib_search "query" [file]` - Search entries
- `bib_add "file" "entry"` - Add entry
- `bib_format "file"` - Format and sort
- `bib_list [file]` - List all entries

**Example:**
```bash
source "${CLAUDE_PLUGIN_ROOT}/lib/bibtex-utils.sh"
bib_search "MacKinnon" ~/Documents/refs.bib
```

---

## Troubleshooting

### Plugin Not Found

**Problem:** Commands not available after installation

**Solution:**
```bash
# Verify installation
ls -la ~/.claude/plugins/statistical-research

# Reinstall
cd ~/projects/dev-tools/claude-plugins/statistical-research
./scripts/install.sh --dev
```

### Shell Scripts Permission Denied

**Problem:** `Permission denied` when running API wrappers

**Solution:**
```bash
chmod +x ~/.claude/plugins/statistical-research/lib/*.sh
```

### Skills Not Activating

**Problem:** Skills don't seem to activate automatically

**Check:**
1. Skill files are in correct location (`skills/` subdirectories)
2. Skill markdown files have proper structure
3. Context matches skill activation conditions

### API Calls Failing

**Problem:** arXiv/Crossref searches return errors

**Check:**
1. Internet connection
2. API rate limits (Crossref requires User-Agent, set in `crossref-api.sh`)
3. Firewall/proxy settings

---

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

**Areas for Contribution:**
- Additional slash commands (e.g., `/research:meta-analysis`)
- More research skills
- New API wrappers (e.g., PubMed, Google Scholar)
- Documentation improvements
- Bug fixes

---

## License

MIT License - see [LICENSE](LICENSE) file

---

## Citation

If you use this plugin in your research workflow, please cite:

```bibtex
@software{statistical_research_plugin,
  author = {Data-Wise},
  title = {Statistical Research Plugin for Claude Code},
  year = {2025},
  url = {https://github.com/Data-Wise/statistical-research-plugin}
}
```

---

## Acknowledgments

Built with:
- [Claude Code](https://code.claude.com/) - AI-powered development environment
- [arXiv API](https://arxiv.org/help/api/) - Open access to e-prints
- [Crossref API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) - DOI resolution
- Pure plugin architecture (no external dependencies)

Inspired by the needs of statistical researchers working on mediation analysis, causal inference, and statistical methodology.

---

## Development

**For plugin development and contributions:**

- 📖 **[Developer Guide (CLAUDE.md)](../CLAUDE.md)** - Comprehensive guide for working with this monorepo
- Development commands (testing, validation, documentation)
- Architecture patterns and plugin structure
- CI/CD workflows and quality standards
- Common tasks and troubleshooting

See the root-level [CLAUDE.md](../CLAUDE.md) for detailed guidance on plugin development.

---

## Support

- **Issues:** [GitHub Issues](https://github.com/Data-Wise/statistical-research-plugin/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Data-Wise/statistical-research-plugin/discussions)
- **Documentation:** [Wiki](https://github.com/Data-Wise/statistical-research-plugin/wiki)

---

**Ready to use!** Try `/research:arxiv "your research topic"` to get started.
