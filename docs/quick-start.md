# Quick Start Guide

Get started with Claude Code plugins in 5 minutes.

---

## Installation (2 minutes)

```bash
# Clone repository
git clone https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins

# Install a plugin
./scripts/install-plugin.sh workflow

# Restart Claude Code
```

**That's it!** After restart, commands will be available.

---

## First Commands

### Workflow Plugin

```bash
# Enhanced brainstorming
/brainstorm "API design for user authentication"
```

**Output:**
- Multiple design approaches
- Trade-offs for each option
- Recommended next steps
- Auto-delegates to specialized agents

### RForge Orchestrator (Requires RForge MCP)

```bash
# Quick R package analysis
/rforge:quick

# Balanced analysis with recommendations
/rforge:analyze "Update bootstrap algorithm"

# Comprehensive analysis (2-5 minutes)
/rforge:thorough "Prepare for CRAN"
```

### Statistical Research (Requires Research MCP)

```bash
# Search arXiv
/research:arxiv "mediation analysis"

# Generate methods section
/research:manuscript:methods

# Find literature gaps
/research:lit-gap "causal inference"
```

---

## Common Workflows

### 1. Brainstorming a Feature

```bash
# Start with brainstorming
/brainstorm "Add dark mode to settings page"

# Get structured output:
# - Quick wins
# - Medium effort tasks
# - Long-term improvements
# - Recommended first step
```

### 2. R Package Development

```bash
# Quick health check
/rforge:quick

# Before making changes
/rforge:analyze "Add new statistical test"

# Before CRAN submission
/rforge:thorough "Prepare for CRAN release"
```

### 3. Research Writing

```bash
# Find relevant papers
/research:arxiv "bootstrap methods mediation"

# Write methods section
/research:manuscript:methods

# Respond to reviewers
/research:manuscript:reviewer
```

---

## Understanding Output

### Command Response Structure

Most commands provide:

1. **Summary** - Quick overview of results
2. **Details** - Specific findings or analysis
3. **Recommendations** - Actionable next steps
4. **Options** - What to do next

**Example:**

```
✅ Analysis complete! (10.2 seconds)

🎯 IMPACT: MEDIUM
  • 2 packages affected (mediate, sensitivity)
  • Estimated cascade: 4 hours over 2 days

✅ QUALITY: EXCELLENT
  • Tests: 187/187 passing (94% coverage)
  • CRAN: Clean, no warnings

📋 RECOMMENDED NEXT STEPS:
  1. Implement changes (3 hours)
  2. Auto-fix documentation
  3. Run cascade plan

What would you like to do next?
[1] Generate implementation plan
[2] Auto-fix documentation
[3] Show cascade sequence
[4] Something else
```

---

## Tips & Tricks

### 1. Use Auto-Complete

Type `/` to see available commands:
```bash
/rf<TAB>     # Shows /rforge:* commands
/res<TAB>    # Shows /research:* commands
/bra<TAB>    # Shows /brainstorm
```

### 2. Add Context

Many commands accept optional context:
```bash
/rforge:analyze "Update mediation formula"
/brainstorm "API design" --technical
```

### 3. Follow-Up Questions

After a command completes, you can ask follow-up questions:
```
/rforge:quick

> "Show me the test coverage details"
> "What's the dependency impact?"
> "Generate an implementation plan"
```

### 4. Chain Commands

Use multiple commands for complex workflows:
```bash
# 1. Quick check
/rforge:quick

# 2. If good, detailed analysis
/rforge:analyze "Prepare for release"

# 3. Before release, comprehensive check
/rforge:thorough
```

---

## Command Categories

### Quick Analysis (< 10 seconds)

- `/rforge:quick` - Fast R package check

### Balanced Analysis (< 30 seconds)

- `/rforge:analyze` - Recommended for daily development

### Deep Analysis (2-5 minutes)

- `/rforge:thorough` - Pre-release validation

### Literature & Research

- `/research:arxiv` - Search papers
- `/research:doi` - Look up by DOI
- `/research:bib:search` - Search local bibliography

### Writing

- `/research:manuscript:methods` - Methods section
- `/research:manuscript:results` - Results section
- `/research:manuscript:reviewer` - Reviewer responses

### Workflow

- `/brainstorm` - Enhanced brainstorming with auto-delegation

---

## ADHD-Friendly Features

All plugins are designed with ADHD in mind:

✅ **Fast feedback** - Results in seconds, not minutes
✅ **Clear structure** - Consistent output format
✅ **Visual hierarchy** - Emojis, headers, bullets
✅ **Actionable** - Always suggests next steps
✅ **Interruptible** - Can stop anytime (Ctrl+C)
✅ **Scannable** - Easy to skim and find key info

---

## Next Steps

### Learn More

- **[Command Reference](COMMAND-REFERENCE.md)** - All commands documented
- **[Architecture](diagrams/ECOSYSTEM.md)** - How plugins work
- **[Installation Guide](installation.md)** - Advanced setup

### Get Help

- **Issues:** [GitHub Issues](https://github.com/Data-Wise/claude-plugins/issues)
- **Documentation:** [Full docs](https://data-wise.github.io/claude-plugins/)

### Contribute

- **Validate plugins:** `python3 scripts/validate-all-plugins.py`
- **Generate docs:** `./scripts/generate-docs.sh`
- **Submit PR:** [Contributing guide](https://github.com/Data-Wise/claude-plugins/tree/main/scripts)

---

## Troubleshooting

### Commands Don't Appear

1. Check installation:

   ```bash
   ls -la ~/.claude/plugins/
   ```

2. Restart Claude Code (REQUIRED!)

3. Try again

### Command Fails

1. Check if MCP server is configured (for rforge/research plugins)
2. Verify dependencies installed (R, Node.js)
3. Check Claude Code logs for errors

### Need Help?

- See [Installation Troubleshooting](installation.md#troubleshooting)
- Report issue on [GitHub](https://github.com/Data-Wise/claude-plugins/issues)

---

**Ready to dive in?** Start with `/brainstorm` - it works without any MCP setup!
