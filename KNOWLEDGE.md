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
11. [Git Worktree Workflows](#git-worktree-workflows)

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

## Git Worktree Workflows

### Overview

Git worktrees enable **parallel plugin development without branch switching** by creating multiple working directories for the same repository. This is particularly powerful for plugin development where you might be:

- Experimenting with risky refactors
- Working on multiple plugins simultaneously
- Testing breaking changes in isolation
- Reviewing PRs without disrupting active work

### Why Worktrees for Plugin Development?

**Traditional Branch Workflow Problems:**
```bash
# Working on craft plugin enhancement
git checkout -b feature/craft-mode-system

# Urgent: Need to fix rforge bug!
git stash                          # Save craft work
git checkout main                  # Switch branches
git checkout -b hotfix/rforge-bug  # Create hotfix
# Fix bug, commit, merge...
git checkout feature/craft-mode-system  # Back to craft
git stash pop                      # Restore work
```

**Issues:**
- ⚠️ Lost context when switching between plugins
- ⚠️ Can't test multiple plugins together
- ⚠️ IDE/editor reloads on every branch switch
- ⚠️ Risk of stash conflicts

**Worktree Solution:**
```
~/projects/dev-tools/claude-plugins/              # Main (stable)
~/.git-worktrees/claude-plugins-craft-feature/    # Craft enhancement
~/.git-worktrees/claude-plugins-rforge-hotfix/    # RForge bug fix
~/.git-worktrees/claude-plugins-experiment/       # Risky experiment
```

**Benefits:**
- ✅ Each branch has dedicated directory
- ✅ Test multiple plugins together
- ✅ No context switching
- ✅ Easy cleanup of failed experiments
- ✅ Safe isolation for YOLO mode

### Basic Worktree Commands

**Create Worktree:**
```bash
# Via flow-cli (if using flow-cli)
wt create feature/craft-mode-system

# Or via git directly
git worktree add ~/.git-worktrees/claude-plugins-craft-mode feature/craft-mode-system
```

**List Worktrees:**
```bash
# Via flow-cli
wt list

# Or via git
git worktree list
```

**Output:**
```
/Users/dt/projects/dev-tools/claude-plugins        abc1234 [main]
/Users/dt/.git-worktrees/claude-plugins-craft      def5678 [feature/craft-mode]
/Users/dt/.git-worktrees/claude-plugins-experiment ghi9012 [experiment/refactor]
```

**Remove Worktree:**
```bash
# Via flow-cli
wt remove feature/craft-mode-system

# Or via git
git worktree remove ~/.git-worktrees/claude-plugins-craft-mode
```

### Flow-CLI Integration

If you have flow-cli installed, you get enhanced worktree support with Claude Code integration.

**Unified "Mode First" Pattern:**
```bash
# Pattern: cc [mode] wt <branch>

# Launch Claude in worktree with specific mode
cc yolo wt experiment/plugin-refactor    # YOLO mode
cc plan wt feature/new-plugin            # Plan mode
cc opus wt experiment/architecture       # Opus model

# Pick from existing worktrees
cc wt pick                               # Interactive picker
cc yolo wt pick                          # YOLO mode + picker
```

**Session Tracking:**
```bash
# Show all worktrees with Claude session info
cc wt status

# Output shows:
# 🟢 Recent session (< 24h)
# 🟡 Old session (> 24h)
# ⚪ No session
```

**Aliases:**
```bash
ccw feature/craft-enhancement     # cc wt
ccwy experiment/risky-refactor    # cc wt yolo
ccwp                              # cc wt pick
```

### Plugin Development Workflows

#### Workflow 1: Safe Experimentation with YOLO Mode

**Scenario:** Test radical plugin refactoring without risking main codebase

```bash
# 1. Create experimental worktree with YOLO mode
cc yolo wt experiment/rforge-rewrite

# Claude launches in: ~/.git-worktrees/claude-plugins-experiment-rforge-rewrite/
# With: --dangerously-skip-permissions (fast iteration)

# 2. Give Claude experimental instructions
> Completely refactor rforge plugin to use pure Python instead of shell delegation

# 3. Monitor from main project (separate terminal)
cd ~/projects/dev-tools/claude-plugins
watch -n 2 'git -C ~/.git-worktrees/claude-plugins-experiment-rforge-rewrite diff --stat'

# 4. Review results
cd ~/.git-worktrees/claude-plugins-experiment-rforge-rewrite
git diff --stat
pytest rforge/tests/  # Test in isolation

# 5. Decision point
# Option A: Success! Merge to main
cd ~/projects/dev-tools/claude-plugins
git checkout main
git merge experiment/rforge-rewrite
git push

# Option B: Failed experiment - delete worktree
wt remove experiment/rforge-rewrite
# All changes gone, main repo untouched
```

**Why This Works:**
- ✅ YOLO mode = no permission prompts (fast)
- ✅ Worktree = main repo stays safe
- ✅ Easy cleanup if experiment fails
- ✅ Test changes without affecting main

#### Workflow 2: Parallel Plugin Development

**Scenario:** Working on multiple plugins simultaneously

```bash
# Terminal 1: Enhance craft plugin
cc wt feature/craft-orchestrator-v3
cd ~/.git-worktrees/claude-plugins-craft-orchestrator
# Work on craft with Claude...

# Terminal 2: Update workflow plugin
cc plan wt feature/workflow-brainstorm-v2
cd ~/.git-worktrees/claude-plugins-workflow-brainstorm
# Plan workflow enhancements with Claude...

# Terminal 3: Main repo for testing/review
cd ~/projects/dev-tools/claude-plugins
pytest                        # Run all plugin tests
mkdocs serve                  # Preview docs
python3 scripts/validate-all-plugins.py
```

**Benefits:**
- Each plugin isolated in own directory
- No context switching between terminals
- Test plugins independently
- Main repo available for integration testing

#### Workflow 3: Documentation Updates

**Scenario:** Test documentation changes without disrupting development

```bash
# Create docs worktree
cc wt feature/docs-phase5-gifs

# Work in worktree
cd ~/.git-worktrees/claude-plugins-docs-phase5
# Add GIFs, update markdown...

# Test documentation build in isolation
mkdocs serve
# Preview at localhost:8000

# If satisfied, merge
cd ~/projects/dev-tools/claude-plugins
git merge feature/docs-phase5-gifs

# If not satisfied, delete worktree
wt remove feature/docs-phase5-gifs
```

#### Workflow 4: Plugin Testing with Installation

**Scenario:** Test plugin changes with actual installation

```bash
# Create worktree for plugin testing
cc wt feature/statistical-research-v2

# In worktree: make changes and test installation
cd ~/.git-worktrees/claude-plugins-statistical-research-v2/statistical-research
./scripts/install.sh --dev

# Test in Claude Code
# Use /research:* commands

# If satisfied, merge from main repo
cd ~/projects/dev-tools/claude-plugins
git merge feature/statistical-research-v2

# Uninstall test version
cd ~/.git-worktrees/claude-plugins-statistical-research-v2/statistical-research
./scripts/uninstall.sh
```

#### Workflow 5: Breaking Changes Across Multiple Plugins

**Scenario:** Implementing breaking changes that affect multiple plugins

```bash
# Create worktree for breaking change
cc yolo wt breaking/unified-command-format

# In worktree: update all 4 plugins
cd ~/.git-worktrees/claude-plugins-breaking-unified-format

# Update craft, workflow, statistical-research, rforge
# Run comprehensive tests
pytest
python3 scripts/validate-all-plugins.py

# Update documentation
python3 scripts/generate-command-reference.py
mkdocs build

# If all tests pass, merge
cd ~/projects/dev-tools/claude-plugins
git merge breaking/unified-command-format

# If tests fail, debug in worktree or delete
wt remove breaking/unified-command-format
```

#### Workflow 6: A/B Testing Plugin Architectures

**Scenario:** Compare different architectural approaches

```bash
# Create 3 experimental worktrees
cc wt experiment/approach-a-mcp-delegation
cc wt experiment/approach-b-pure-shell
cc wt experiment/approach-c-hybrid

# Terminal 1: MCP delegation approach
cd ~/.git-worktrees/claude-plugins-experiment-approach-a
cc yolo
> Implement using MCP server delegation pattern

# Terminal 2: Pure shell approach
cd ~/.git-worktrees/claude-plugins-experiment-approach-b
cc yolo
> Implement using shell-based API wrappers

# Terminal 3: Hybrid approach
cd ~/.git-worktrees/claude-plugins-experiment-approach-c
cc yolo
> Implement using hybrid pattern

# Compare results
cd ~/projects/dev-tools/claude-plugins
# Test each approach
pytest ~/.git-worktrees/claude-plugins-experiment-approach-a/
pytest ~/.git-worktrees/claude-plugins-experiment-approach-b/
pytest ~/.git-worktrees/claude-plugins-experiment-approach-c/

# Pick winner, delete losers
git merge experiment/approach-b-pure-shell
wt remove experiment/approach-a-mcp-delegation
wt remove experiment/approach-c-hybrid
```

### Monorepo-Specific Best Practices

#### 1. Plugin Isolation

**Good: Isolate single plugin changes**
```bash
# Only working on craft plugin
cc wt feature/craft-skill-updates
# Changes confined to craft/ directory
```

**Bad: Mixed plugin changes in one worktree**
```bash
# Don't do this
cc wt feature/update-all-plugins
# Mixing craft, workflow, rforge changes
# Hard to test, review, and revert
```

#### 2. Test Independence

**Always test plugins independently:**
```bash
# In worktree
cd ~/.git-worktrees/claude-plugins-feature-craft/craft
pytest tests/                    # Craft tests only
./scripts/install.sh --dev       # Install craft only
# Test with Claude Code
./scripts/uninstall.sh           # Clean up
```

#### 3. Documentation Consistency

**Update docs in same worktree as plugin changes:**
```bash
# In worktree for craft feature
cd ~/.git-worktrees/claude-plugins-craft-feature

# Update plugin files
vim craft/commands/new-command.md

# Update docs in same commit
vim docs/craft/commands.md
python3 scripts/generate-command-reference.py

# Commit together
git add craft/ docs/
git commit -m "feat(craft): add new command with docs"
```

#### 4. CI/CD Testing

**Test CI workflows before merging:**
```bash
# In worktree
cd ~/.git-worktrees/claude-plugins-feature-new-workflow

# Update workflow
vim .github/workflows/validate-plugins.yml

# Test locally
python3 scripts/validate-all-plugins.py

# Push to feature branch, check CI
git push origin feature/new-workflow
gh run watch --repo Data-Wise/claude-plugins
```

### Safety Practices

#### 1. Always Review Before Merging

```bash
# Before merging from worktree
cd ~/.git-worktrees/claude-plugins-feature-craft
git status                       # Check what changed
git diff main                    # Review all changes
git log --oneline                # Review commits

# Run full validation
cd ~/projects/dev-tools/claude-plugins
git diff main..feature/craft     # Review from main
pytest                           # All tests
python3 scripts/validate-all-plugins.py
```

#### 2. Keep Main Clean

**Never use YOLO in main project:**
```bash
# ❌ BAD: YOLO in main project
cd ~/projects/dev-tools/claude-plugins
cc yolo                          # Too risky!

# ✅ GOOD: YOLO in experimental worktree
cc yolo wt experiment/risky-refactor
```

#### 3. Clean Up Regularly

```bash
# List all worktrees
wt list

# Remove completed/abandoned worktrees
wt remove feature/completed-craft-update
wt remove experiment/failed-approach

# Prune stale references
git worktree prune
```

#### 4. Name Worktrees Descriptively

**Good naming conventions:**
```bash
experiment/rforge-pure-python     # Purpose: experiment, plugin: rforge
feature/craft-mode-system         # Purpose: feature, plugin: craft
hotfix/workflow-brainstorm-bug    # Purpose: hotfix, plugin: workflow
docs/add-phase5-gifs              # Purpose: docs update
breaking/unified-command-format   # Purpose: breaking change
```

**Bad naming:**
```bash
test              # Too vague
tmp               # What temporary work?
new               # New what?
fix               # Fix what?
```

### Troubleshooting

#### "Branch already checked out"

**Error:** Can't create worktree because branch already exists

**Solution:**
```bash
# List existing worktrees
wt list

# Remove old worktree if done
wt remove feature/craft-mode

# Or use existing worktree
cd ~/.git-worktrees/claude-plugins-craft-mode
```

#### "Worktree out of sync"

**Problem:** Worktree doesn't have latest changes

**Solution:**
```bash
cd ~/.git-worktrees/claude-plugins-feature-craft
git status
git pull origin feature/craft
```

#### "Disk space issues"

**Problem:** Too many old worktrees

**Solution:**
```bash
# List all worktrees
wt list

# Remove old experiments
wt remove experiment/old-1
wt remove experiment/old-2

# Prune stale references
git worktree prune
```

### Quick Reference

**Create & Launch:**
```bash
cc wt <branch>              # Standard mode
cc yolo wt <branch>         # YOLO mode (fast iteration)
cc plan wt <branch>         # Plan mode
cc opus wt <branch>         # Opus model
```

**Pick Existing:**
```bash
cc wt pick                  # Interactive picker
cc yolo wt pick             # YOLO + picker
```

**Management:**
```bash
cc wt status                # Show all with sessions
wt list                     # List all worktrees
wt remove <branch>          # Delete worktree
git worktree prune          # Clean stale references
```

**Aliases (flow-cli):**
```bash
ccw <branch>                # cc wt
ccwy <branch>               # cc wt yolo
ccwp                        # cc wt pick
```

### When to Use Worktrees

**✅ Use Worktrees For:**
- Experimental plugin refactoring
- Parallel plugin development
- Breaking changes testing
- Long-running feature branches
- A/B testing architectures
- Documentation updates in isolation
- Hotfixes during feature work

**❌ Don't Need Worktrees For:**
- Simple bug fixes
- Minor documentation updates
- Single-file changes
- Quick commits to main

### Summary

Git worktrees enable:
1. ✅ Safe experimentation with YOLO mode
2. ✅ Parallel development across multiple plugins
3. ✅ Easy cleanup of failed experiments
4. ✅ No branch switching disruption
5. ✅ Isolated testing environments

**Best workflow for claude-plugins:**
- Experiments → `cc yolo wt experiment/<name>`
- Features → `cc wt feature/<plugin-name>`
- Hotfixes → `cc wt hotfix/<plugin-issue>`
- Docs → `cc wt docs/<update-name>`

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

### 2026-01-08: Git Worktree Workflows

**Added:**
- Comprehensive Git Worktree Workflows section (550+ lines)
- Adapted flow-cli's worktree patterns for plugin development
- 6 plugin-specific workflows with detailed examples
- Monorepo-specific best practices for plugin isolation
- Safety practices and troubleshooting guide
- Quick reference for common worktree operations

**Key Features:**
- Safe experimentation with YOLO mode in isolated worktrees
- Parallel plugin development without branch switching
- A/B testing plugin architectures
- Documentation updates in isolation
- Breaking changes testing across multiple plugins

**Integration:**
- Flow-CLI CC dispatcher integration (`cc wt`, `cc yolo wt`, `cc plan wt`)
- Session tracking with visual indicators (🟢/🟡/⚪)
- Monorepo-specific naming conventions
- Plugin isolation best practices
- CI/CD testing workflows

**Use Cases:**
- `experiment/rforge-pure-python` - Experimental refactoring
- `feature/craft-mode-system` - Feature development
- `hotfix/workflow-brainstorm-bug` - Urgent fixes
- `docs/add-phase5-gifs` - Documentation updates
- `breaking/unified-command-format` - Breaking changes

**Benefits:**
- ✅ Main repo stays clean and stable
- ✅ Easy cleanup of failed experiments (just delete worktree)
- ✅ No context switching between plugins
- ✅ Isolated testing environments
- ✅ Parallel development across multiple terminals

---

**Last Updated:** 2026-01-08
**Contributors:** Data-Wise Team
