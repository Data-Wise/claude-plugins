# Installation Guide

Complete guide to installing Claude Code plugins.

---

## Prerequisites

### Required

- **Claude Code CLI** - Install from [claude.ai/code](https://claude.ai/code)
- **Git** - For cloning the repository

### Optional (for development)

- **Python 3.10+** - For running validation and documentation scripts
- **Node.js 18+** - Required by some MCP servers
- **R >= 4.0** - For RForge MCP server (rforge plugin)

---

## Quick Installation

### Option 1: Using Installation Script (Recommended)

```bash
# Clone repository
git clone https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins

# Install a plugin
./scripts/install-plugin.sh rforge

# Restart Claude Code
# Commands will appear after restart
```

### Option 2: Manual Installation

```bash
# Clone repository
git clone https://github.com/Data-Wise/claude-plugins.git

# Copy plugin to Claude's plugin directory
cp -r claude-plugins/rforge ~/.claude/plugins/

# Restart Claude Code
```

---

## Plugin-Specific Setup

### RForge Orchestrator

**Requires:** RForge MCP Server

```bash
# Install RForge MCP server
npm install -g rforge-mcp

# Configure in ~/.claude/settings.json
# (Or use rforge-mcp configure command)
```

**Dependencies:**
- R >= 4.0
- R packages: devtools, testthat, covr

### Statistical Research

**Requires:** Statistical Research MCP Server

```bash
# Install from repository
cd ~/projects/dev-tools/mcp-servers/statistical-research
npm install
npm link

# Configure in ~/.claude/settings.json
```

**Optional:**
- Zotero (for citation management)
- LaTeX (for document generation)

### Workflow

**No additional setup required** - Works out of the box!

---

## Verification

### Check Plugin Installation

```bash
# List installed plugins
ls -la ~/.claude/plugins/

# Should show:
# rforge/
# statistical-research/
# workflow/
```

### Test Commands

After restarting Claude Code, test commands:

```bash
# In Claude Code CLI
/rforge:quick
/research:arxiv "test"
/brainstorm
```

If commands don't appear:
1. Verify plugin is in `~/.claude/plugins/`
2. Check `package.json` and `plugin.json` exist
3. Restart Claude Code again
4. Check Claude Code logs for errors

---

## Updating Plugins

### Update All Plugins

```bash
cd claude-plugins
git pull

# Reinstall (force overwrites existing)
./scripts/install-plugin.sh rforge --force
./scripts/install-plugin.sh statistical-research --force
./scripts/install-plugin.sh workflow --force

# Restart Claude Code
```

### Update Single Plugin

```bash
cd claude-plugins
git pull

./scripts/install-plugin.sh <plugin-name> --force

# Restart Claude Code
```

---

## Uninstallation

### Remove a Plugin

```bash
# Remove from Claude's plugins directory
rm -rf ~/.claude/plugins/<plugin-name>

# Restart Claude Code
```

### Remove All Plugins

```bash
# Remove all plugins (careful!)
rm -rf ~/.claude/plugins/rforge
rm -rf ~/.claude/plugins/statistical-research
rm -rf ~/.claude/plugins/workflow

# Restart Claude Code
```

---

## Troubleshooting

### Plugin Not Appearing

**Problem:** Commands don't show up in Claude Code

**Solutions:**
1. Check plugin directory exists:

   ```bash
   ls -la ~/.claude/plugins/<plugin-name>
   ```

2. Verify required files exist:

   ```bash
   test -f ~/.claude/plugins/<plugin-name>/package.json && echo "OK" || echo "MISSING"
   test -f ~/.claude/plugins/<plugin-name>/.claude-plugin/plugin.json && echo "OK" || echo "MISSING"
   ```

3. Check for errors in plugin files:

   ```bash
   python3 -m json.tool ~/.claude/plugins/<plugin-name>/package.json
   ```

4. Restart Claude Code (IMPORTANT!)

### Commands Missing Name Field

**Problem:** Command appears but errors when used

**Solution:**
```bash
# Check command frontmatter
head -n 5 ~/.claude/plugins/<plugin-name>/commands/<command>.md

# Should show:
# ---
# name: plugin:command
# description: ...
# ---
```

If missing, the command file is corrupted. Reinstall:
```bash
./scripts/install-plugin.sh <plugin-name> --force
```

### MCP Server Not Found

**Problem:** Plugin works but commands fail with "MCP server not found"

**Solution:**
1. Install required MCP server (see plugin-specific setup above)

2. Configure in `~/.claude/settings.json`:

   ```json
   {
     "mcpServers": {
       "rforge-mcp": {
         "command": "npx",
         "args": ["-y", "rforge-mcp"]
       }
     }
   }
   ```

3. Restart Claude Code

### Permission Denied

**Problem:** Can't install plugin due to permissions

**Solution:**
```bash
# Ensure ~/.claude/plugins directory exists and is writable
mkdir -p ~/.claude/plugins
chmod 755 ~/.claude/plugins

# Reinstall
./scripts/install-plugin.sh <plugin-name>
```

---

## Advanced Installation

### For Developers

```bash
# Clone repository
git clone https://github.com/Data-Wise/claude-plugins.git
cd claude-plugins

# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Validate plugins
python3 scripts/validate-all-plugins.py

# Install locally
./scripts/install-plugin.sh <plugin-name> --force

# Generate documentation
./scripts/generate-docs.sh
```

### Using Symlinks (Development)

```bash
# Link instead of copy (changes reflect immediately)
ln -s ~/claude-plugins/rforge ~/.claude/plugins/rforge

# Restart Claude Code after changes
```

**Note:** Symlinks require absolute paths

---

## Next Steps

After installation:

1. **[Quick Start Guide](quick-start.md)** - Learn basic usage
2. **[Command Reference](COMMAND-REFERENCE.md)** - See all available commands
3. **[Architecture](diagrams/ECOSYSTEM.md)** - Understand how plugins work

---

## Getting Help

**Issues?** [Report on GitHub](https://github.com/Data-Wise/claude-plugins/issues)

**Questions?** Check [Common Issues](installation.md#troubleshooting)

**Contributions?** See [Development Guide](https://github.com/Data-Wise/claude-plugins/tree/main/scripts)
