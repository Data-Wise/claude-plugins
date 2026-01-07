# Claude Plugins - Knowledge Base

**Generated:** 2025-12-23
**Purpose:** Comprehensive architecture, patterns, and best practices for Claude Code plugin development

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Plugin Types and Patterns](#plugin-types-and-patterns)
3. [Directory Structure Standards](#directory-structure-standards)
4. [Command Development](#command-development)
5. [Skill Development](#skill-development)
6. [Installation Patterns](#installation-patterns)
7. [Testing Strategies](#testing-strategies)
8. [Publishing Workflows](#publishing-workflows)
9. [Common Pitfalls](#common-pitfalls)
10. [Design Patterns](#design-patterns)

---

## Architecture Overview

### What is a Claude Code Plugin?

A Claude Code plugin extends Claude's capabilities through:
- **Slash commands** - User-invocable commands (e.g., `/research:arxiv`)
- **Skills** - Auto-activating expertise (e.g., `proof-architect`)
- **Agents** - Autonomous task executors
- **Hooks** - Event-driven automations

### Plugin vs. MCP Server

| Aspect | Plugin | MCP Server |
|--------|--------|------------|
| **Purpose** | Extend Claude UI/UX | Provide tools/resources |
| **Architecture** | Markdown + shell scripts | TypeScript + MCP protocol |
| **Installation** | Copy to `~/.claude/plugins/` | Configure in settings.json |
| **Activation** | User command or context | Tool calls from Claude |
| **Dependencies** | None (self-contained) | Requires MCP runtime |
| **Best for** | Workflows, commands, skills | Data access, computations |

**When to Use Each:**
- **Plugin:** User-facing workflows, research processes, writing assistance
- **MCP:** Data sources, computational engines, external APIs

**Can Combine:** Plugins can delegate to MCP servers (e.g., rforge-orchestrator delegates to RForge MCP)

---

## Plugin Types and Patterns

### 1. Pure Plugin Pattern ⭐ RECOMMENDED for Most Cases

**Example:** `statistical-research`

**Characteristics:**
- ✅ No MCP dependencies
- ✅ Shell-based APIs (arXiv, Crossref, BibTeX)
- ✅ Self-contained and portable
- ✅ Fast (no server startup)
- ✅ Easy installation

**Structure:**
```
statistical-research/
├── commands/          # Slash commands
├── skills/            # A-grade skills
├── lib/               # Shell API wrappers
└── scripts/           # Install/uninstall
```

**Use When:**
- Building workflow tools
- Providing research/writing assistance
- Creating command libraries
- No heavy computation needed

### 2. Orchestrator Plugin Pattern

**Example:** `rforge-orchestrator`

**Characteristics:**
- 🔌 Delegates to MCP server
- 🧠 Pattern recognition
- ⚡ Parallel execution
- 📊 Result synthesis

**Structure:**
```
rforge-orchestrator/
├── commands/          # User commands
├── agents/            # Orchestration logic
└── (delegates to RForge MCP)
```

**Use When:**
- Coordinating multiple MCP tools
- Need intelligent delegation
- Combining tool results
- Workflow optimization

### 3. Hybrid Pattern

**Characteristics:**
- 📦 Plugin provides UI/UX
- 🔧 MCP provides heavy lifting
- 🔄 Two-way communication

**Use When:**
- Complex computations needed
- Large data processing
- External service integration
- Want best of both worlds

---

## Directory Structure Standards

### Minimal Plugin

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json           # Required: Plugin metadata
├── scripts/
│   ├── install.sh            # Required: Installation
│   └── uninstall.sh          # Required: Uninstallation
├── package.json              # Required: npm metadata
├── README.md                 # Required: Documentation
└── LICENSE                   # Required: MIT license
```

### Full-Featured Plugin

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json
├── commands/                  # Slash commands
│   ├── category1/
│   │   ├── command1.md
│   │   └── command2.md
│   └── category2/
│       └── command3.md
├── skills/                    # Auto-activating skills
│   ├── domain1/
│   │   ├── skill1/
│   │   │   └── skill.md
│   │   └── skill2/
│   │       └── SKILL.md
│   └── domain2/
│       └── skill3/
│           └── skill.md
├── agents/                    # Autonomous agents
│   └── agent1.md
├── lib/                       # Utilities and APIs
│   ├── api-wrapper1.sh
│   └── api-wrapper2.sh
├── scripts/
│   ├── install.sh
│   ├── uninstall.sh
│   └── validate.sh
├── tests/                     # Tests
│   ├── commands/
│   └── skills/
├── docs/                      # Additional documentation
│   ├── architecture.md
│   └── examples.md
├── package.json
├── README.md
├── LICENSE
└── .gitignore
```

---

## Command Development

### Command File Structure

```markdown
---
name: namespace:command-name
description: Brief description (appears in autocomplete)
---

# User-Facing Title

User-facing content that Claude shows to the user.

**Usage:** `/namespace:command <args>`

**Examples:**
- `/namespace:command "example 1"`
- `/namespace:command arg1 arg2`

## Section

More user-facing content...

<system>
Implementation details that Claude uses but user doesn't see.

## Implementation

Use shell commands, call APIs, activate skills, etc.

```bash
# Example shell code
source "${CLAUDE_PLUGIN_ROOT}/lib/api.sh"
api_call "$1"
```

## Follow-up Actions

After execution, offer to:
- Do related task A
- Do related task B
</system>
```

### Best Practices

**1. Clear Usage Examples**
```markdown
**Usage:** `/research:arxiv <query> [limit]`

**Examples:**
- `/research:arxiv "mediation analysis"`
- `/research:arxiv "bootstrap inference" 20`
```

**2. Graceful Error Handling**
```bash
# In <system> block
if [[ -z "$QUERY" ]]; then
    echo "Error: Search query required"
    exit 1
fi
```

**3. Follow-up Suggestions**
```markdown
## Follow-up Actions

After showing results, offer to:
- Get full paper details (provide arXiv ID)
- Download PDF
- Add to bibliography
```

**4. Use ${CLAUDE_PLUGIN_ROOT}**
```bash
# Source API wrappers using plugin root
source "${CLAUDE_PLUGIN_ROOT}/lib/arxiv-api.sh"
```

---

## Skill Development

### Skill File Structure

```markdown
---
name: skill-name
description: What this skill does
trigger: When to activate this skill
---

# Skill Name

You are an expert in [domain]. You excel at [capabilities].

## Expertise

- **Strength 1:** [Description]
- **Strength 2:** [Description]
- **Strength 3:** [Description]

## Activation Conditions

This skill activates when:
1. User requests [specific task]
2. Context involves [domain keywords]
3. Task requires [particular expertise]

## Approach

When activated:

1. **Understand** - [First step]
2. **Analyze** - [Second step]
3. **Deliver** - [Third step]

## Quality Standards

Always ensure:
- ✅ [Standard 1]
- ✅ [Standard 2]
- ✅ [Standard 3]

## Example Interactions

### Example 1
User: [Request]
You: [Response approach]

### Example 2
User: [Request]
You: [Response approach]
```

### Skill Quality Tiers

**A-Grade Skills** (🥇):
- Comprehensive expertise definition
- Clear activation conditions
- Detailed approach/methodology
- Multiple examples
- Quality standards

**B-Grade Skills** (🥈):
- Good expertise definition
- Basic activation conditions
- General approach
- At least one example

**C-Grade Skills** (🥉):
- Minimal expertise definition
- Works but lacks depth

---

## Installation Patterns

### Development Mode (Symlink)

**Purpose:** Edit source files, changes immediately reflected

```bash
#!/bin/bash
# install.sh with --dev flag

DEV_MODE=false
if [[ "${1:-}" == "--dev" ]]; then
    DEV_MODE=true
fi

if [[ "$DEV_MODE" == true ]]; then
    ln -s "$SOURCE_DIR" "$TARGET_DIR"
else
    cp -r "$SOURCE_DIR" "$TARGET_DIR"
fi
```

**Benefits:**
- ✅ Instant feedback during development
- ✅ No reinstallation needed
- ✅ Source and installed are same files

**Use:** During plugin development

### Production Mode (Copy)

**Purpose:** Stable installation independent of source

```bash
cp -r "$SOURCE_DIR" "$TARGET_DIR"
```

**Benefits:**
- ✅ Source can be deleted
- ✅ No symlink issues
- ✅ Standard for distribution

**Use:** For end users

---

## Testing Strategies

### Manual Testing

**1. Installation Test**
```bash
cd plugin-name
./scripts/install.sh --dev
ls -la ~/.claude/plugins/plugin-name
```

**2. Command Test**
```
# In Claude Code
/namespace:command "test input"
```

**3. Skill Activation Test**
- Trigger skill activation condition
- Verify skill activates
- Check quality of output

### Automated Testing

**Directory Structure:**
```
tests/
├── commands/
│   ├── test-command1.sh
│   └── test-command2.sh
├── skills/
│   └── test-skill-activation.sh
└── integration/
    └── test-full-workflow.sh
```

**Example Test:**
```bash
#!/bin/bash
# tests/commands/test-arxiv.sh

source "../lib/arxiv-api.sh"

# Test search
result=$(arxiv_search "test" 5)

if [[ -z "$result" ]]; then
    echo "FAIL: arxiv_search returned empty"
    exit 1
fi

echo "PASS: arxiv_search works"
```

### Validation Script

```bash
#!/bin/bash
# scripts/validate.sh

# Check required files
required_files=(
    ".claude-plugin/plugin.json"
    "package.json"
    "README.md"
    "LICENSE"
    "scripts/install.sh"
    "scripts/uninstall.sh"
)

for file in "${required_files[@]}"; do
    if [[ ! -f "$file" ]]; then
        echo "ERROR: Missing required file: $file"
        exit 1
    fi
done

echo "✓ Plugin structure valid"
```

---

## Publishing Workflows

### npm Publishing

**1. Prepare package.json**
```json
{
  "name": "@data-wise/plugin-name",
  "version": "1.0.0",
  "description": "...",
  "files": [
    "commands/",
    "skills/",
    "lib/",
    ".claude-plugin/",
    "scripts/",
    "README.md",
    "LICENSE"
  ]
}
```

**2. Test locally**
```bash
npm pack
# Creates plugin-name-1.0.0.tgz

# Test installation from tarball
npm install -g ./plugin-name-1.0.0.tgz
```

**3. Publish**
```bash
npm login
npm publish --access public
```

### GitHub Release

**1. Tag version**
```bash
git tag v1.0.0
git push origin v1.0.0
```

**2. Create release**
```bash
gh release create v1.0.0 \
  --title "Plugin Name v1.0.0" \
  --notes "Release notes..."
```

**3. Attach assets (optional)**
```bash
gh release upload v1.0.0 plugin-name-1.0.0.tgz
```

---

## Common Pitfalls

### 1. Hardcoded Paths

❌ **Wrong:**
```bash
source "/Users/dt/.claude/plugins/my-plugin/lib/api.sh"
```

✅ **Right:**
```bash
source "${CLAUDE_PLUGIN_ROOT}/lib/api.sh"
```

### 2. Missing Error Handling

❌ **Wrong:**
```bash
result=$(api_call "$1")
echo "$result"
```

✅ **Right:**
```bash
if [[ -z "$1" ]]; then
    echo "Error: Argument required"
    exit 1
fi

result=$(api_call "$1")
if [[ $? -ne 0 ]]; then
    echo "Error: API call failed"
    exit 1
fi

echo "$result"
```

### 3. Forgetting Installation Scripts

❌ **Wrong:** No install.sh/uninstall.sh

✅ **Right:** Always provide both scripts with --dev mode

### 4. Unclear Command Names

❌ **Wrong:** `/cmd`, `/do`, `/run`

✅ **Right:** `/research:arxiv`, `/manuscript:methods`

### 5. Skills Too Generic

❌ **Wrong:** "You are helpful"

✅ **Right:** "You are an expert in statistical proof construction with expertise in asymptotic theory, measure theory, and rigorous mathematical argumentation."

---

## Design Patterns

### Pattern 1: API Wrapper Library

**Use Case:** Integrate external APIs (arXiv, Crossref, etc.)

**Structure:**
```
lib/
├── arxiv-api.sh
├── crossref-api.sh
└── utils.sh

commands/
└── literature/
    ├── arxiv.md          # Calls lib/arxiv-api.sh
    └── doi.md            # Calls lib/crossref-api.sh
```

**Benefits:**
- Reusable API functions
- Testable independently
- Multiple commands share API

### Pattern 2: Skill Cascade

**Use Case:** Complex tasks require multiple skills

**Structure:**
```
skills/
├── primary-skill/
│   └── skill.md        # Main skill, may invoke...
├── supporting-skill-1/
│   └── skill.md        # Supporting skill 1
└── supporting-skill-2/
    └── skill.md        # Supporting skill 2
```

**Example:** `manuscript:methods` activates `methods-paper-writer` which may invoke `mathematical-foundations`

### Pattern 3: Progressive Commands

**Use Case:** Multi-step workflows

**Structure:**
```
commands/
└── workflow/
    ├── step1.md       # Initial command
    ├── step2.md       # Follow-up (references step1)
    └── step3.md       # Final (references step1+2)
```

**Example:** Literature search → Get details → Add to bibliography

### Pattern 4: Orchestrator-MCP

**Use Case:** Coordinate multiple MCP tools

**Structure:**
```
Plugin (orchestrator):
- Pattern recognition
- Tool selection
- Parallel execution
- Result synthesis

MCP Server (tools):
- Individual specialized tools
- Data processing
- Computations
```

**Example:** `rforge-orchestrator` → `rforge-mcp` tools

---

## Versioning Strategy

### Semantic Versioning

- **Major (X.0.0):** Breaking changes
- **Minor (1.X.0):** New features, backward compatible
- **Patch (1.0.X):** Bug fixes

### Changelog

Maintain `CHANGELOG.md`:
```markdown
# Changelog

## [1.1.0] - 2025-01-15

### Added
- New command: `/research:meta-analysis`
- Skill: `meta-analyst`

### Fixed
- arXiv API timeout handling

### Changed
- Improved error messages
```

---

## Monorepo Organization

### Plugin Independence

Each plugin is independent:
- Own package.json
- Own npm publish
- Own git history
- Own version

### Shared Resources

Use `shared/` directory for:
- Test utilities
- Lint configurations
- Documentation templates
- Common scripts

**Don't share plugin code** - plugins should be self-contained

---

## Future Directions

### Plugin CLI (Planned)

```bash
claude-plugin create my-plugin
claude-plugin validate my-plugin
claude-plugin test my-plugin
claude-plugin publish my-plugin
```

### Plugin Registry (Planned)

Central catalog of plugins:
- Searchable by category
- User ratings/reviews
- Automated quality checks
- Install from registry

---

**This document is living** - Update as patterns evolve and new best practices emerge.

---

## Recent Updates

### 2026-01-07: CLAUDE.md Developer Guide

**Added:**
- Comprehensive CLAUDE.md file (401 lines) with developer guidance
- Development commands for testing, validation, documentation
- Architecture patterns and plugin structure standards
- CI/CD workflows and quality standards documentation
- Plugin-specific notes for all 4 plugins

**Integration:**
- Added to repository root for local development access
- Linked in main README navigation bar (🛠️ Developer Guide)
- Integrated with MkDocs documentation site
- Referenced in all plugin-specific READMEs (statistical-research, craft, workflow, rforge)

**Purpose:**
Future Claude Code instances now have immediate access to:
- How to build, test, and validate plugins
- Architecture patterns and design principles
- CI/CD workflows and automation
- Common tasks and troubleshooting
- Plugin standards and quality criteria

**Files Updated:**
- `CLAUDE.md` - New comprehensive developer guide
- `README.md` - Added Developer Guide link
- `docs/CLAUDE.md` - Copy for MkDocs site
- `mkdocs.yml` - Added to navigation
- `.STATUS` - Updated with documentation completion
- All plugin READMEs - Added CLAUDE.md references

---

**Last Updated:** 2026-01-07
**Contributors:** Data-Wise Team
