# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **monorepo for Claude Code plugins** developed by Data-Wise. Each plugin is independently versioned and published to npm but shares common standards, tooling, and documentation infrastructure.

**4 Active Plugins:**
- **craft** (v1.16.0) - Full-stack developer toolkit (74 commands, 8 agents, 21 skills)
- **statistical-research** (v1.1.0) - Statistical research workflows (14 commands, 17 skills)
- **workflow** (v2.3.0) - ADHD-friendly workflow automation (12 commands)
- **rforge** - R package ecosystem orchestrator

## Development Commands

### Testing

```bash
# Run all tests across plugins
pytest

# Test specific plugin
cd craft && pytest tests/
cd statistical-research && bash tests/test-plugin-structure.sh

# Run with coverage
pytest --cov=rforge --cov-report=html

# Run specific test markers
pytest -m unit              # Unit tests only
pytest -m integration       # Integration tests
pytest -m backward_compat   # Backward compatibility
pytest -m mode_system       # Mode system tests
```

### Validation

```bash
# Validate all plugins (structure, JSON, commands)
python3 scripts/validate-all-plugins.py

# Pre-commit checks (run before commits)
pre-commit run --all-files

# Validate specific plugin structure
cd <plugin-name>
test -f .claude-plugin/plugin.json || echo "Missing plugin.json"
test -f package.json || echo "Missing package.json"
```

### Documentation

```bash
# Build documentation site
mkdocs build

# Serve documentation locally
mkdocs serve
# Opens at http://127.0.0.1:8000

# Generate command reference
python3 scripts/generate-command-reference.py

# Update navigation automatically
python3 scripts/update-mkdocs-nav.py

# Generate architecture diagrams (Mermaid)
python3 scripts/generate-architecture-diagrams.py
```

### Plugin Installation

```bash
# Install plugin in development mode (symlink - changes reflected immediately)
cd <plugin-name>
./scripts/install.sh --dev

# Install in production mode (copy)
./scripts/install.sh

# Uninstall
./scripts/uninstall.sh

# Verify installation
ls -la ~/.claude/plugins/<plugin-name>
```

## Architecture Patterns

### Plugin Structure Standard

Every plugin follows this structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required: name, version, description
├── commands/                  # Slash commands (optional)
│   ├── category1/
│   │   └── command.md        # Frontmatter: name, description
│   └── category2/
│       └── command.md
├── skills/                    # Auto-activating skills (optional)
│   └── domain/
│       └── skill-name/
│           └── skill.md      # Frontmatter: name, description, trigger
├── agents/                    # Autonomous agents (optional)
│   └── agent.md
├── lib/                       # Utilities/API wrappers (optional)
│   └── api-wrapper.sh
├── scripts/
│   ├── install.sh            # Required: supports --dev flag
│   └── uninstall.sh          # Required
├── tests/                     # Tests (recommended)
├── package.json              # Required: npm metadata
├── README.md                 # Required
└── LICENSE                   # Required: MIT
```

### Command File Format

```markdown
---
name: namespace:command-name
description: Brief description
---

# User-Facing Title

User-facing documentation here.

**Usage:** `/namespace:command <args>`

<system>
Implementation details for Claude (not shown to user).

## Implementation
Shell scripts, API calls, etc.

## Follow-up Actions
Offer related tasks after execution.
</system>
```

### Skill File Format

```markdown
---
name: skill-name
description: What this skill does
trigger: When to activate
---

# Skill Name

You are an expert in [domain]. You excel at [capabilities].

## Expertise
- Strength 1
- Strength 2

## Activation Conditions
This skill activates when:
1. User requests [specific task]
2. Context involves [keywords]

## Approach
Steps to execute when activated.
```

### Installation Patterns

**Development Mode (Symlink):**
- Use `./scripts/install.sh --dev` during plugin development
- Changes to source files immediately reflected
- No reinstallation needed

**Production Mode (Copy):**
- Use `./scripts/install.sh` for stable installation
- Source can be deleted after install
- Standard for end users

## Key Design Principles

### 1. Pure Plugin Pattern (Recommended)

**Example:** `statistical-research`

- No MCP dependencies
- Shell-based APIs (arXiv, Crossref, BibTeX)
- Self-contained and portable
- Fast startup, easy installation

**When to Use:**
- Building workflow tools
- Providing research/writing assistance
- Creating command libraries
- No heavy computation needed

### 2. Orchestrator Pattern

**Example:** `rforge`

- Delegates to MCP server tools
- Pattern recognition and intelligent delegation
- Parallel execution and result synthesis

**When to Use:**
- Coordinating multiple MCP tools
- Need intelligent delegation
- Combining tool results

### 3. Use ${CLAUDE_PLUGIN_ROOT}

Never hardcode paths. Always use the environment variable:

```bash
# ✅ Correct
source "${CLAUDE_PLUGIN_ROOT}/lib/api.sh"

# ❌ Wrong
source "/Users/dt/.claude/plugins/my-plugin/lib/api.sh"
```

## CI/CD Workflows

### GitHub Actions

**`.github/workflows/validate-plugins.yml`**
- Runs on push/PR to main/dev
- Matrix validation across all 4 plugins
- Checks: required files, valid JSON, command structure, no hardcoded paths

**`.github/workflows/docs.yml`**
- Auto-deploys documentation to GitHub Pages
- Runs on push to main
- Validates MkDocs build (strict mode, zero warnings)

**`.github/workflows/craft-ci.yml`**
- Craft plugin-specific CI
- Python 3.9-3.12 matrix testing
- Performance benchmarks

### Pre-commit Hooks

Install: `pre-commit install`

**Automated Checks:**
- JSON/YAML validation
- Plugin structure validation
- Command frontmatter verification
- package.json and plugin.json validation
- Whitespace/EOF fixes

## Common Tasks

### Adding a New Command

1. Create markdown file in `<plugin>/commands/<category>/<command>.md`
2. Add frontmatter with `name:` and `description:`
3. Write user-facing documentation
4. Add `<system>` block with implementation
5. Test: `/namespace:command "test input"`

### Adding a New Skill

1. Create directory `<plugin>/skills/<domain>/<skill-name>/`
2. Add `skill.md` with frontmatter
3. Define expertise, activation conditions, approach
4. Test by triggering activation condition

### Publishing a Plugin Update

```bash
cd <plugin-name>

# 1. Update version in package.json and .claude-plugin/plugin.json
# 2. Update CHANGELOG.md
# 3. Commit changes
git add .
git commit -m "chore: release v1.2.0"

# 4. Create git tag
git tag v1.2.0
git push origin v1.2.0

# 5. Create GitHub release
gh release create v1.2.0 --title "Plugin Name v1.2.0" --notes "Release notes..."

# 6. Publish to npm (when ready)
npm publish --access public
```

## Repository-Level Scripts

**`scripts/validate-all-plugins.py`**
- Validates structure of all plugins
- Checks required files, valid JSON, naming conventions
- Used by pre-commit and CI

**`scripts/generate-command-reference.py`**
- Extracts commands from all plugins
- Generates markdown reference docs
- Auto-updates `docs/COMMAND-REFERENCE.md`

**`scripts/generate-architecture-diagrams.py`**
- Creates Mermaid diagrams for each plugin
- Flow diagrams and structure diagrams
- Outputs to `docs/diagrams/`

**`scripts/update-mkdocs-nav.py`**
- Scans docs directory
- Auto-generates navigation in `mkdocs.yml`
- Maintains consistent nav structure

## Plugin-Specific Notes

### craft Plugin

- **Largest plugin**: 74 commands across 13 categories
- **Orchestrator**: v2 orchestrator with subagent monitoring
- **Testing**: Python-based tests, `pytest tests/`
- **Categories**: arch, ci, code, dist, docs, git, plan, site, test

### statistical-research Plugin

- **Pure plugin**: No MCP dependencies
- **Shell APIs**: `lib/arxiv-api.sh`, `lib/crossref-api.sh`, `lib/bibtex-utils.sh`
- **17 A-grade skills**: Mathematical, implementation, writing, research domains
- **Command categories**: literature, manuscript, simulation, research

### workflow Plugin

- **ADHD-friendly**: Designed for focus and task management
- **Commands**: brainstorm, spec-review, focus, next, done, recap, stuck
- **Features**: 3-layer arguments, spec capture, "Ask More" functionality

### rforge Plugin

- **Mode system**: default (<10s), debug (<120s), optimize (<180s), release (<300s)
- **Format options**: terminal, json, markdown
- **Python-based**: Uses pytest for testing
- **Commands**: analyze, status, detect, cascade, impact, release, deps

## Quality Standards

### A-Grade Plugin Checklist

- ✅ Comprehensive README with examples
- ✅ All required files present
- ✅ Installation scripts support --dev mode
- ✅ Commands have clear documentation and examples
- ✅ Skills have detailed activation conditions
- ✅ No hardcoded paths (use ${CLAUDE_PLUGIN_ROOT})
- ✅ Tests for critical functionality
- ✅ MIT license
- ✅ Semantic versioning

### Command Quality

- Clear usage examples
- Graceful error handling
- Follow-up action suggestions
- Use plugin root variable for paths

### Skill Quality

- Comprehensive expertise definition
- Clear activation conditions
- Detailed approach/methodology
- Multiple examples
- Quality standards section

## Common Pitfalls to Avoid

1. **Hardcoded Paths**: Always use `${CLAUDE_PLUGIN_ROOT}`
2. **Missing Error Handling**: Check for required arguments, handle API failures
3. **Unclear Command Names**: Use descriptive namespace:command format
4. **Generic Skills**: Be specific about expertise and activation
5. **Forgetting --dev Mode**: Always support development mode in install scripts
6. **No Tests**: Add tests for critical functionality
7. **Inconsistent Versions**: Keep package.json and plugin.json versions in sync

## Documentation Site

Built with MkDocs Material theme.

**Structure:**
- Home: Overview and introduction
- Getting Started: Installation and quick start
- Mode System: Usage guides (rforge-specific)
- Command Reference: Auto-generated from all plugins
- Plugin Development: How to create new plugins
- Publishing: npm and GitHub release workflows
- Architecture: Mermaid diagrams for each plugin

**Deployment:**
- Hosted on GitHub Pages
- Auto-deployed on push to main
- URL: https://data-wise.github.io/claude-plugins/

## Support and Resources

- **GitHub Issues**: https://github.com/Data-Wise/claude-plugins/issues
- **Knowledge Base**: `KNOWLEDGE.md` - comprehensive architecture guide
- **Status**: `.STATUS` - current development status and progress
- **npm Organization**: https://www.npmjs.com/org/data-wise
