# Plugin Development Scripts

This directory contains scripts for developing, testing, and deploying Claude Code plugins.

## Scripts

### 📦 install-plugin.sh

Install plugins from the repository to `~/.claude/plugins/`.

**Usage:**
```bash
# List available plugins
./install-plugin.sh --list

# Install a plugin
./install-plugin.sh rforge-orchestrator

# Force reinstall (replaces existing)
./install-plugin.sh workflow --force

# Show help
./install-plugin.sh --help
```

**Features:**
- Validates plugin structure before installation
- Backs up existing installations
- Shows plugin version and command count
- Reminds to restart Claude Code

**Backup Location:** `~/.claude/plugins/.backups/`

---

### ✅ validate-all-plugins.py

Comprehensive validation of all plugins in the repository.

**Usage:**
```bash
# Validate all plugins
python3 validate-all-plugins.py

# Strict mode (more checks)
python3 validate-all-plugins.py --strict
```

**Checks:**
- Required files (package.json, plugin.json, README, LICENSE)
- JSON validity
- Command frontmatter (name, description fields)
- Version consistency
- Hardcoded paths (in commands, not docs)
- Metadata consistency

**Output:**
- Color-coded results
- Detailed error messages
- Summary of all plugins

**Exit Codes:**
- `0` - All plugins valid
- `1` - Validation errors found
- `2` - Critical errors (missing plugins)

---

### 📚 generate-docs.sh

Master documentation generation script that runs all documentation generators.

**Usage:**
```bash
# Generate documentation only
./generate-docs.sh

# Generate + build with mkdocs
./generate-docs.sh --build

# Generate + deploy to GitHub Pages
./generate-docs.sh --deploy
```

**What it generates:**
1. Command reference (from frontmatter)
2. Architecture diagrams (Mermaid)
3. Updated mkdocs.yml navigation

**Output:**
- `docs/COMMAND-REFERENCE.md` - Complete command reference
- `docs/diagrams/` - 8 architecture diagrams
- `mkdocs.yml` - Auto-updated navigation

**Time:** ~5 seconds for generation

---

### 📝 generate-command-reference.py

Generates command reference documentation from command frontmatter.

**Usage:**
```bash
python3 generate-command-reference.py [--output FILE]
```

**Features:**
- Parses all command .md files
- Extracts name, description, arguments
- Generates markdown tables
- Groups by plugin
- Links to source files

**Output:** `docs/COMMAND-REFERENCE.md` (17 commands documented)

---

### 🏗️ generate-architecture-diagrams.py

Generates Mermaid architecture diagrams from plugin structure.

**Usage:**
```bash
python3 generate-architecture-diagrams.py [--output DIR]
```

**Generates:**
- Plugin structure diagrams (directory tree)
- Command flow diagrams (sequence diagrams)
- Ecosystem diagram (plugin relationships)
- Dependency diagram (requirements)

**Output:** `docs/diagrams/` (8 diagram files)

---

### 📖 update-mkdocs-nav.py

Auto-updates mkdocs.yml navigation from generated docs.

**Usage:**
```bash
python3 update-mkdocs-nav.py [--config FILE]
```

**Updates:**
- Navigation structure
- Command reference section
- Architecture diagrams section
- Plugin documentation links

**Output:** Updates `mkdocs.yml` in place

---

### 🪝 pre-commit-hook.sh

Git pre-commit hook for automated validation.

**Setup:**
```bash
# Install hook
ln -sf ../../scripts/pre-commit-hook.sh .git/hooks/pre-commit

# Or use pre-commit framework
pip install pre-commit
pre-commit install
```

**What it checks:**
- JSON validity (package.json, plugin.json)
- Command frontmatter (name field required)
- Runs full plugin validation
- Only runs if plugin files are staged

**Manual run:**
```bash
./scripts/pre-commit-hook.sh
```

---

## Workflow

### Development Workflow

1. **Make changes** to plugin
2. **Validate locally:**
   ```bash
   python3 scripts/validate-all-plugins.py
   ```
3. **Test installation:**
   ```bash
   ./scripts/install-plugin.sh <plugin-name> --force
   ```
4. **Restart Claude Code** and test commands
5. **Commit changes** (pre-commit hook runs automatically)
6. **Push to GitHub** (CI/CD runs on push)

### CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/validate-plugins.yml`) runs on:
- Push to `main` or `dev` branches
- Pull requests to `main` or `dev`
- Changes to plugin files

**CI checks:**
- Plugin structure validation
- JSON file validation
- Command frontmatter validation
- Hardcoded path detection
- Broken link detection (basic)

---

## Pre-commit Framework

For advanced users, we support the [pre-commit](https://pre-commit.com/) framework.

**Setup:**
```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

**Configuration:** `.pre-commit-config.yaml`

**Hooks:**
- JSON validation
- YAML validation
- Trailing whitespace
- End-of-file fixer
- Plugin structure validation
- Command frontmatter validation

---

## Common Tasks

### Installing a plugin for development
```bash
./scripts/install-plugin.sh <plugin-name> --force
# Restart Claude Code
```

### Validating before commit
```bash
python3 scripts/validate-all-plugins.py
```

### Running all checks
```bash
# JSON validation
find . -name "*.json" -not -path "*/node_modules/*" | xargs -I {} python3 -m json.tool {} > /dev/null

# Plugin validation
python3 scripts/validate-all-plugins.py

# Pre-commit checks
./scripts/pre-commit-hook.sh
```

### Debugging validation errors

If validation fails:

1. **Check error message** - It will tell you which file and what's wrong
2. **Fix the issue:**
   - Missing `name:` field → Add to command frontmatter
   - Invalid JSON → Check syntax with `python3 -m json.tool file.json`
   - Hardcoded paths → Use relative paths or environment variables
3. **Re-run validation:**
   ```bash
   python3 scripts/validate-all-plugins.py
   ```

---

## Quick Reference

| Task | Command |
|------|---------|
| List plugins | `./scripts/install-plugin.sh --list` |
| Install plugin | `./scripts/install-plugin.sh <name>` |
| Validate all | `python3 scripts/validate-all-plugins.py` |
| Run pre-commit | `./scripts/pre-commit-hook.sh` |
| Setup hooks | `pre-commit install` |

---

## Troubleshooting

### "Missing name: field in frontmatter"

Add YAML frontmatter to command files:
```yaml
---
name: plugin:command
description: Command description
---
```

### "Invalid JSON in package.json"

Validate JSON syntax:
```bash
python3 -m json.tool package.json
```

### "Plugin already installed"

Use `--force` to reinstall:
```bash
./scripts/install-plugin.sh <name> --force
```

### "Hardcoded paths detected"

Replace absolute paths with:
- Relative paths: `./commands/file.md`
- Environment variables: `$HOME/.claude/plugins`
- Template variables: `{{PLUGIN_ROOT}}/commands`

---

**Note:** All scripts assume they're run from the repository root (`~/projects/dev-tools/claude-plugins/`).
