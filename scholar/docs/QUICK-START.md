# Statistical Research Plugin - Quick Start

> **Get up and running in 5 minutes**

---

## Install (2 minutes)

```bash
# Navigate to plugin directory
cd ~/projects/dev-tools/claude-plugins/statistical-research

# Install in development mode (changes apply immediately)
./install-private.sh --dev
```

**Done!** The plugin is now available in Claude Code.

---

## First Commands (1 minute)

Try these three commands to see the plugin in action:

### 1. Search arXiv for Papers

```
/lit:arxiv "mediation analysis"
```

**What it does:** Searches arXiv for statistical papers, returns titles, authors, and abstracts.

### 2. Design a Simulation Study

```
/sim:design
```

**What it does:** Asks questions and helps you design a Monte Carlo simulation study.

### 3. Find Literature Gaps

```
/research:lit-gap "causal mediation with time-varying confounders"
```

**What it does:** Identifies gaps in the literature for your research area.

---

## The 4 Command Categories

**Literature** (`/lit:*`) - Manage papers and citations
```bash
/lit:arxiv "topic"       # Search arXiv
/lit:doi 10.xxxx/yyyy    # Lookup by DOI
/lit:bib-add             # Add to BibTeX
/lit:bib-search "author" # Search your .bib file
```

**Manuscript** (`/ms:*`) - Write and improve papers
```bash
/ms:methods    # Write methods section
/ms:results    # Write results section
/ms:proof      # Review mathematical proofs
/ms:reviewer   # Respond to peer reviews
```

**Simulation** (`/sim:*`) - Monte Carlo studies
```bash
/sim:design    # Design simulation study
/sim:analysis  # Analyze simulation results
```

**Research** (`/research:*`) - Planning and ideation
```bash
/research:hypothesis     # Generate hypotheses
/research:analysis-plan  # Create analysis plan
/research:lit-gap        # Find literature gaps
```

---

## Auto-Activating Skills

You don't need to invoke skills manually - they activate automatically when relevant:

**Working on proofs?** → Proof Architect skill activates
**Designing simulations?** → Simulation Architect skill activates
**Writing methods?** → Methods Paper Writer skill activates

**17 skills total** across 4 categories:
- Mathematical (4 skills)
- Implementation (5 skills)
- Writing (3 skills)
- Research (5 skills)

See full list: `docs/REFCARD.md`

---

## Common Workflows

### Literature Review

```bash
# 1. Search for papers
/lit:arxiv "your topic"

# 2. Look up specific papers
/lit:doi 10.1037/met0000425

# 3. Add to bibliography
/lit:bib-add

# 4. Find gaps
/research:lit-gap "your area"
```

### Writing a Paper

```bash
# 1. Write methods section
/ms:methods

# 2. Write results section
/ms:results

# 3. Review proofs (if applicable)
/ms:proof

# 4. Respond to reviewers (after submission)
/ms:reviewer
```

### Simulation Study

```bash
# 1. Design study
/sim:design

# 2. Run your simulations (outside Claude)

# 3. Analyze results
/sim:analysis
```

---

## Tips for Best Results

1. **Be specific** - Better: `/lit:arxiv "causal mediation bootstrap"` vs `/lit:arxiv "mediation"`

2. **Use natural language** - The skills understand context:
   - "I need to prove this estimator is consistent" → Triggers Asymptotic Theory
   - "Help me design a simulation" → Triggers Simulation Architect

3. **BibTeX commands need .bib files** - Make sure you have a `.bib` file in your project directory

4. **Skills don't need invocation** - Just describe your task naturally and relevant skills activate

---

## What's Next?

- **Full command list:** See `docs/REFCARD.md`
- **Installation details:** See `INSTALL-PRIVATE.md`
- **All skills:** See `skills/README.md`
- **Plugin source:** https://github.com/Data-Wise/claude-plugins

---

## Uninstall

```bash
cd ~/projects/dev-tools/claude-plugins/statistical-research
./uninstall-private.sh
```

---

## Troubleshooting

**Commands not showing up?**
- Restart Claude Code
- Check: `ls ~/.claude/plugins/statistical-research`

**arXiv search not working?**
- Check internet connection
- Try a simpler query

**BibTeX commands fail?**
- Ensure `.bib` file exists in your project
- Check file path in command

---

**You're ready!** Try `/lit:arxiv "your research topic"` to get started.
