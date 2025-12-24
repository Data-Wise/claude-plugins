# Plugin Development Guide

Quick guide to creating new Claude Code plugins in this monorepo.

---

## Quick Start

### 1. Create Plugin Structure

```bash
cd ~/projects/dev-tools/claude-plugins

# Create plugin directory
mkdir -p my-plugin/{.claude-plugin,commands,skills,lib,scripts,tests}

# Navigate to plugin
cd my-plugin
```

### 2. Create Required Files

#### `.claude-plugin/plugin.json`

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief description of what your plugin does",
  "author": "Data-Wise",
  "commands": {
    "category": {
      "command-name": "commands/category/command-name.md"
    }
  },
  "skills": {
    "domain": [
      "skills/domain/skill-name.md"
    ]
  }
}
```

#### `package.json`

```json
{
  "name": "@data-wise/my-plugin",
  "version": "1.0.0",
  "description": "Your plugin description",
  "type": "module",
  "main": "index.js",
  "files": [
    "commands/",
    "skills/",
    "lib/",
    ".claude-plugin/",
    "scripts/",
    "README.md",
    "LICENSE"
  ],
  "scripts": {
    "install": "./scripts/install.sh",
    "uninstall": "./scripts/uninstall.sh"
  },
  "keywords": ["claude", "claude-code", "plugin"],
  "author": "Data-Wise",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/Data-Wise/claude-plugins.git",
    "directory": "my-plugin"
  }
}
```

#### `scripts/install.sh`

Copy from `../statistical-research/scripts/install.sh` and update `PLUGIN_NAME`.

#### `scripts/uninstall.sh`

Copy from `../statistical-research/scripts/uninstall.sh` and update `PLUGIN_NAME`.

#### `LICENSE`

```
MIT License

Copyright (c) 2025 Data-Wise

[Full MIT license text - copy from another plugin]
```

#### `README.md`

```markdown
# My Plugin

Brief description of your plugin.

## Features

- Feature 1
- Feature 2

## Installation

[Installation instructions]

## Usage

[Usage examples]
```

### 3. Create Commands

Create `commands/category/command-name.md`:

```markdown
---
name: namespace:command-name
description: Brief description
---

# Command Title

User-facing instructions.

<system>
Implementation details.
</system>
```

### 4. Create Skills

Create `skills/domain/skill-name/skill.md`:

```markdown
---
name: skill-name
description: What this skill does
trigger: When to activate
---

# Skill Name

You are an expert in [domain].

## Expertise

- Strength 1
- Strength 2

## Activation Conditions

This skill activates when:
1. [Condition 1]
2. [Condition 2]
```

### 5. Make Scripts Executable

```bash
chmod +x scripts/install.sh scripts/uninstall.sh
```

### 6. Test Installation

```bash
./scripts/install.sh --dev
ls -la ~/.claude/plugins/my-plugin

# Test in Claude Code
/namespace:command-name "test"
```

---

## Command Development

### Command Template

```markdown
---
name: namespace:command
description: One-line description
---

# User-Facing Title

**Usage:** `/namespace:command <args>`

**Examples:**
- `/namespace:command "example 1"`
- `/namespace:command arg1 arg2`

## Description

What this command does...

<system>
## Implementation

```bash
# Shell code here
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT}"
source "$PLUGIN_ROOT/lib/utils.sh"

ARG1="$1"
if [[ -z "$ARG1" ]]; then
    echo "Error: Argument required"
    exit 1
fi

# Do the work
process_arg "$ARG1"
```

## Follow-up Actions

After execution, offer to:
- Related task A
- Related task B
</system>
```

### Best Practices

1. **Clear usage** - Show exact command format
2. **Examples** - Provide 2-3 concrete examples
3. **Error handling** - Check arguments, handle failures
4. **Follow-ups** - Suggest next steps
5. **Use ${CLAUDE_PLUGIN_ROOT}** - For portable paths

---

## Skill Development

### Skill Template

```markdown
---
name: skill-name
description: Expert in [domain]
trigger: [When to activate]
---

# Skill Name

You are an expert in [specific domain] with deep knowledge of [key areas].

## Core Expertise

- **Area 1:** [Specific capability]
- **Area 2:** [Specific capability]
- **Area 3:** [Specific capability]

## Activation Conditions

This skill automatically activates when:

1. User requests [specific task type]
2. Context involves [domain keywords]
3. Task requires [particular expertise]

## Methodology

When this skill activates:

### 1. Understand Context
- Analyze user's need
- Identify key requirements
- Clarify ambiguities

### 2. Apply Expertise
- Use [specific approach]
- Follow [best practices]
- Ensure [quality standards]

### 3. Deliver Results
- Provide [specific output]
- Explain [reasoning]
- Suggest [next steps]

## Quality Standards

All outputs must:
- ✅ [Standard 1]
- ✅ [Standard 2]
- ✅ [Standard 3]

## Example Scenarios

### Scenario 1: [Common Use Case]
User asks: "[Typical request]"
Approach: [How you'd respond]

### Scenario 2: [Edge Case]
User asks: "[Unusual request]"
Approach: [How you'd handle it]
```

### Skill Quality Levels

**A-Grade (🥇):**
- Comprehensive expertise definition
- Clear activation conditions
- Detailed methodology
- Multiple examples
- Quality standards

**B-Grade (🥈):**
- Good expertise definition
- Basic activation conditions
- General methodology
- At least one example

**Aim for A-Grade!**

---

## Testing Your Plugin

### 1. Validation

```bash
# Check structure
ls -R | head -30

# Required files present?
test -f .claude-plugin/plugin.json && echo "✓ plugin.json"
test -f package.json && echo "✓ package.json"
test -f README.md && echo "✓ README.md"
test -f LICENSE && echo "✓ LICENSE"
test -x scripts/install.sh && echo "✓ install.sh (executable)"
test -x scripts/uninstall.sh && echo "✓ uninstall.sh (executable)"
```

### 2. Installation Test

```bash
# Install in dev mode
./scripts/install.sh --dev

# Verify symlink
ls -la ~/.claude/plugins/my-plugin

# Should show:
# lrwxr-xr-x ... my-plugin -> /path/to/claude-plugins/my-plugin
```

### 3. Command Test

In Claude Code:
```
/namespace:command "test input"
```

Expected:
- Command executes
- Output is correct
- No errors

### 4. Skill Test

Trigger skill activation:
- Use keywords from activation conditions
- Request relevant task
- Verify skill activates
- Check output quality

### 5. Uninstallation Test

```bash
./scripts/uninstall.sh
ls ~/.claude/plugins/my-plugin
# Should not exist
```

---

## Publishing Checklist

Before publishing:

- [ ] All required files present
- [ ] README.md is comprehensive
- [ ] Commands have clear examples
- [ ] Skills have activation conditions
- [ ] Scripts are executable
- [ ] LICENSE is MIT
- [ ] package.json version is correct
- [ ] Tested installation (dev mode)
- [ ] Tested installation (production mode)
- [ ] All commands work
- [ ] All skills activate correctly
- [ ] No hardcoded paths

---

## Common Issues

### Issue: Command not found

**Cause:** `plugin.json` doesn't list command

**Fix:** Add to plugin.json:
```json
{
  "commands": {
    "category": {
      "command-name": "commands/category/command-name.md"
    }
  }
}
```

### Issue: Skill doesn't activate

**Cause:** Activation conditions too specific or missing

**Fix:** Broaden conditions in skill frontmatter:
```markdown
---
trigger: User requests [domain] tasks, asks about [topic], needs [expertise]
---
```

### Issue: Scripts not executable

**Cause:** Permissions not set

**Fix:**
```bash
chmod +x scripts/install.sh scripts/uninstall.sh
```

### Issue: Shell API not found

**Cause:** Not using ${CLAUDE_PLUGIN_ROOT}

**Fix:**
```bash
# Wrong
source "/absolute/path/to/lib/api.sh"

# Right
source "${CLAUDE_PLUGIN_ROOT}/lib/api.sh"
```

---

## Next Steps

1. **Develop your plugin** following this guide
2. **Test thoroughly** with installation tests
3. **Review KNOWLEDGE.md** for patterns and best practices
4. **Check PUBLISHING.md** when ready to publish
5. **Submit PR** to add to monorepo

---

See also:
- [KNOWLEDGE.md](https://github.com/Data-Wise/claude-plugins/blob/main/KNOWLEDGE.md) - Architecture and patterns
- [PUBLISHING.md](PUBLISHING.md) - Publishing workflow
- [Existing plugins](https://github.com/Data-Wise/claude-plugins) - Examples to learn from
