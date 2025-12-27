# /craft:docs:generate - Comprehensive Documentation Generation

You are a documentation generation orchestrator. Generate and maintain all project documentation.

## Purpose

Unified documentation generation that:
- Creates comprehensive technical documentation
- Updates CLAUDE.md with project status
- Syncs website docs with codebase
- Updates planning documents
- Generates diagrams and references
- Adds badges to README/index

## When Invoked

### Without Arguments

Full documentation generation workflow:

```
📚 DOCUMENTATION GENERATION
═══════════════════════════════════════════════════════════════

Select documentation type to generate:

  1. [full]         Full documentation suite
  2. [tutorial]     Step-by-step tutorial
  3. [architecture] Architecture documentation
  4. [reference]    API/CLI reference
  5. [diagram]      Mermaid diagrams
  6. [adr]          Architecture Decision Record
  7. [update]       Update existing docs (CLAUDE.md, website, planning)

Or specify: /craft:docs:generate <type>
```

### With Arguments

```bash
/craft:docs:generate full          # Complete documentation
/craft:docs:generate tutorial      # Create tutorial (uses tutorial-engineer agent)
/craft:docs:generate architecture  # Architecture docs (uses docs-architect agent)
/craft:docs:generate reference     # Technical reference (uses reference-builder agent)
/craft:docs:generate diagram       # Mermaid diagrams (uses mermaid-expert agent)
/craft:docs:generate adr           # Architecture Decision Record
/craft:docs:generate update        # Update CLAUDE.md, website, planning docs
```

## Step-by-Step Process

### Step 1: Project Analysis

```bash
# Detect project type
ls -la
cat pyproject.toml 2>/dev/null || cat package.json 2>/dev/null

# Check existing documentation
ls docs/ 2>/dev/null
cat CLAUDE.md 2>/dev/null | head -50
cat README.md 2>/dev/null | head -30
```

**Analyze:**
- Project type (Python, Node, R, etc.)
- Existing documentation structure
- What needs to be created vs updated

### Step 2: Route to Appropriate Agent

| Type | Agent | Output |
|------|-------|--------|
| `architecture` | docs-architect | Long-form technical manual (10-100+ pages) |
| `tutorial` | tutorial-engineer | Step-by-step learning guide |
| `reference` | reference-builder | Complete API/CLI reference |
| `diagram` | mermaid-expert | Flowcharts, sequences, ERDs |
| `adr` | - | Architecture Decision Record (uses ADR skill) |
| `update` | - | CLAUDE.md + website + planning updates |
| `full` | All agents | Complete documentation suite |

### Step 3: Generate Documentation

For each documentation type:

1. **Read existing code/docs**
2. **Generate content using appropriate agent**
3. **Preview output**
4. **Write to appropriate location**

### Step 4: Update Meta-Documentation

Always update after generating:

```
📝 META-DOCUMENTATION UPDATES

Updating:
  ✅ CLAUDE.md - Project status and structure
  ✅ mkdocs.yml - Navigation for new pages
  ✅ docs/index.md - Badges and overview
  ✅ .STATUS - Progress tracking

Preview changes? (y/n)
```

## Output Format

```
✅ DOCUMENTATION GENERATION COMPLETE
═══════════════════════════════════════════════════════════════

Generated:
  📄 docs/architecture.md (2,450 lines)
  📄 docs/tutorial/getting-started.md (380 lines)
  📄 docs/reference/api.md (1,200 lines)

Updated:
  📝 CLAUDE.md - Added new architecture section
  📝 mkdocs.yml - Added navigation entries
  📝 docs/index.md - Added badges
  📝 .STATUS - Updated progress

Diagrams created:
  🎨 docs/diagrams/architecture.md
  🎨 docs/diagrams/data-flow.md

Next steps:
  1. Review: ls docs/
  2. Preview: mkdocs serve
  3. Commit: git add docs/ CLAUDE.md mkdocs.yml && git commit -m "docs: generate comprehensive documentation"
```

## Full Documentation Mode

When running `full`:

```
📚 FULL DOCUMENTATION GENERATION
═══════════════════════════════════════════════════════════════

Phase 1: Analysis
  • Scanning codebase structure...
  • Identifying key components...
  • Mapping dependencies...

Phase 2: Architecture Documentation
  • Generating system overview...
  • Creating component diagrams...
  • Documenting design decisions...

Phase 3: Reference Documentation
  • Extracting API signatures...
  • Documenting CLI commands...
  • Creating configuration reference...

Phase 4: Tutorials
  • Creating getting started guide...
  • Writing feature tutorials...

Phase 5: Diagrams
  • Architecture diagram...
  • Data flow diagram...
  • Sequence diagrams...

Phase 6: Meta Updates
  • Updating CLAUDE.md...
  • Syncing website docs...
  • Adding badges to README...

Progress: [████████████████████░░░░░░░░░░] 65%
```

## Badge Generation

When updating README or docs/index.md, add relevant badges:

```markdown
<!-- Badges -->
![Version](https://img.shields.io/badge/version-0.3.0-blue)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-green)
![Coverage](https://img.shields.io/badge/coverage-85%25-green)
![Docs](https://img.shields.io/badge/docs-available-blue)

<!-- Or dynamic badges -->
[![PyPI version](https://badge.fury.io/py/package-name.svg)](https://badge.fury.io/py/package-name)
[![GitHub stars](https://img.shields.io/github/stars/org/repo)](https://github.com/org/repo/stargazers)
```

## Integration

Works with existing craft docs commands:
- `/craft:docs:sync` - Called during update phase
- `/craft:docs:changelog` - Update changelog after generation
- `/craft:docs:claude-md` - Update CLAUDE.md
- `/craft:docs:validate` - Validate generated docs
- `/craft:docs:nav-update` - Update mkdocs navigation

Uses agents:
- `docs-architect` - Architecture documentation
- `tutorial-engineer` - Tutorial creation
- `reference-builder` - Reference documentation
- `mermaid-expert` - Diagram generation

Uses skills:
- `architecture-decision-records` - ADR generation
- `changelog-automation` - Changelog patterns
