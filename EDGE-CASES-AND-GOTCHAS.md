# Edge Cases & Gotchas - Claude Code Plugins

**Last Updated:** 2024-12-24
**Context:** Lessons learned from RForge plugin consolidation and marketplace debugging

---

## Plugin Installation & Discovery

### Edge Case 1: Marketplace Cache Persistence

**Symptom:**
```bash
/plugin install rforge@local-plugins
# Returns: Plugin "rforge" not found in any marketplace
```

**Root Cause:**
Claude Code caches marketplace plugins in `~/.claude/plugins/cache/`. When you rename a plugin, the old name remains in the cache even after updating the marketplace.json.

**Location:**
```
~/.claude/plugins/cache/local-plugins/
├── old-plugin-name/     # ← Stale cache!
└── other-plugin/
```

**Solution:**
```bash
# Remove the old cached plugin
rm -rf ~/.claude/plugins/cache/local-plugins/old-plugin-name

# Then reinstall
/plugin marketplace remove local-plugins
/plugin marketplace add ~/.claude/local-marketplace
/plugin install new-plugin-name@local-plugins
```

**Prevention:**
Always clear the cache when renaming plugins:
```bash
rm -rf ~/.claude/plugins/cache/local-plugins/[old-name]
```

---

### Edge Case 2: Marketplace Schema Validation

**Symptom:**
```bash
/plugin marketplace add ~/.claude/local-marketplace
# Returns: Invalid schema: plugins.0.source: Invalid input: must start with "./"
```

**Root Cause:**
Marketplace schema requires `source` paths to start with `./` - relative paths like `../../plugins/name` are rejected.

**Wrong:**
```json
{
  "plugins": [{
    "source": "../../plugins/rforge"  // ❌ Fails validation
  }]
}
```

**Correct:**
```json
{
  "plugins": [{
    "source": "./rforge"  // ✅ Passes validation
  }]
}
```

**Solution:**
Use symlinks to make paths relative to marketplace directory:
```bash
cd ~/.claude/local-marketplace
ln -s ../plugins/rforge ./rforge
```

**Schema Rule:**
```javascript
{
  "source": {
    "pattern": "^\\./"  // Must start with "./"
  }
}
```

---

### Edge Case 3: Plugin Not Loading After Installation

**Symptom:**
Plugin installs successfully but commands don't appear after restart.

**Checklist:**
1. ✅ Check `plugin.json` exists in `.claude-plugin/`
2. ✅ Verify `name` field in plugin.json matches directory name
3. ✅ Check command files have frontmatter with `name:` field
4. ✅ Verify `package.json` exists at plugin root
5. ✅ Ensure marketplace symlink resolves correctly

**Most Common Causes:**
- Missing `package.json` (plugin won't load at all)
- Missing `name:` in command frontmatter (commands won't register)
- Mismatched plugin name in plugin.json vs directory

**Debug:**
```bash
# Verify plugin structure
ls -la ~/.claude/plugins/plugin-name/
# Should show:
# .claude-plugin/plugin.json  ✅
# package.json                ✅
# commands/*.md               ✅

# Check frontmatter
head -n 3 ~/.claude/plugins/plugin-name/commands/cmd.md
# Should show:
# ---
# name: plugin:command
# ---
```

---

### Edge Case 4: Marketplace Discovery Race Condition

**Symptom:**
Marketplace added successfully but plugins still not found.

**Root Cause:**
Claude Code may not immediately refresh marketplace plugin list after adding marketplace.

**Workaround:**
```bash
# Remove and re-add marketplace to force refresh
/plugin marketplace remove local-plugins
/plugin marketplace add ~/.claude/local-marketplace

# Now install should work
/plugin install plugin-name@local-plugins
```

**Alternative:**
Restart Claude Code after adding marketplace (not just after installing plugin).

---

## Plugin Structure & Naming

### Edge Case 5: Command Name Collisions

**Symptom:**
Two plugins have commands with the same name - only one loads.

**Example:**
```
workflow/commands/next.md        name: next
rforge/commands/next.md          name: next
```

**Result:**
Only one `/next` command will be available (last loaded wins).

**Solution:**
Use plugin-namespaced commands:
```
workflow/commands/next.md        name: workflow:next
rforge/commands/next.md          name: rforge:next
```

**Best Practice:**
Always namespace commands with plugin name:
- ✅ `/rforge:analyze`
- ✅ `/research:arxiv`
- ❌ `/analyze` (too generic)

---

### Edge Case 6: Frontmatter Parsing Sensitivity

**Symptom:**
Command file exists but command doesn't register.

**Cause:**
Frontmatter must be:
- At the very start of file (no blank lines before)
- Delimited by exactly `---` (three hyphens)
- Valid YAML syntax
- Contains required `name:` field

**Wrong:**
```markdown

---  ← Blank line before
name: cmd
---
```

**Wrong:**
```markdown
----  ← Four hyphens
name: cmd
----
```

**Correct:**
```markdown
---
name: plugin:cmd
description: Does something
---

# Command content
```

**Validation:**
```bash
# Check frontmatter
head -n 5 command.md | grep -A 2 "^---"
```

---

## Documentation Generation

### Edge Case 7: MkDocs Strict Mode Link Validation

**Symptom:**
```
Aborted with 33 warnings in strict mode!
```

**Root Cause:**
MkDocs `--strict` flag treats warnings as errors. Links to files outside `docs/` directory fail validation.

**Failed Links:**
- `../plugin-name/README.md` (outside docs/)
- `scripts/README.md` (not in docs/)
- Root-level files (LICENSE, etc.)

**Solution:**
Convert all external links to GitHub URLs:
```markdown
<!-- Wrong -->
[Plugin README](../plugin-name/README.md)

<!-- Correct -->
[Plugin README](https://github.com/owner/repo/blob/main/plugin-name/README.md)
```

**Auto-fix:**
Update documentation generators to use GitHub URLs for source links.

---

### Edge Case 8: Command Reference Relative Paths

**Symptom:**
Command reference shows broken links to source files.

**Cause:**
Generator creates relative links (`../plugin/commands/cmd.md`) which MkDocs can't resolve.

**Solution:**
Use GitHub URLs in generator:
```python
# Before
rel_path = cmd.file_path.relative_to(self.repo_root)
lines.append(f"**Source:** [`{rel_path}`](../{rel_path})")

# After
rel_path = cmd.file_path.relative_to(self.repo_root)
github_url = f"{self.github_repo_url}/blob/main/{rel_path}"
lines.append(f"**Source:** [`{rel_path}`]({github_url})")
```

---

### Edge Case 9: Navigation Auto-Discovery Scope

**Symptom:**
Navigation includes files that shouldn't be in menu.

**Cause:**
Auto-discovery finds all markdown files, including those meant to be excluded.

**Solution:**
Explicitly define navigation structure and skip external files:
```python
# Skip these
skip_files = {
    'README.md', 'LICENSE', 'INSTALL.md',
    'TESTING.md', 'DEVELOPMENT.md'
}

# Only include files in docs/
if not file_path.is_relative_to(docs_dir):
    continue
```

---

## Git & Version Control

### Edge Case 10: Git Rename Detection

**Symptom:**
Git treats directory rename as delete + add instead of rename.

**Cause:**
Git's rename detection threshold not met, or files changed significantly.

**Result:**
```
D  old-plugin/file.md
A  new-plugin/file.md
```

**Preferred:**
```
R  old-plugin/file.md -> new-plugin/file.md
```

**Solution:**
```bash
# Use git mv for renames
git mv old-plugin new-plugin

# If already moved, adjust similarity threshold
git add -A
git status  # Should show renames (R)
```

**Threshold:**
Git detects renames when files are >50% similar. Modify threshold:
```bash
git diff --find-renames=40%  # More aggressive
```

---

## CI/CD & Automation

### Edge Case 11: GitHub Pages Build Delay

**Symptom:**
CI/CD succeeds but site still shows old content.

**Cause:**
GitHub Pages has deployment delay after gh-pages branch update:
- Branch updated: Immediate
- Site deployed: 30 seconds - 2 minutes
- CDN cache: May take 5-10 minutes

**Timeline:**
```
Push → GitHub Actions (2 min) → gh-pages updated → GitHub Pages build (1 min) → CDN cache (5 min)
Total: 3-8 minutes
```

**Solution:**
Wait 5 minutes after CI/CD completes before checking site.

**Force refresh:**
```bash
# Hard refresh browser
Cmd+Shift+R (Mac)
Ctrl+F5 (Windows)

# Or add cache-busting query
https://site.com/?v=123
```

---

### Edge Case 12: Workflow Path Triggers

**Symptom:**
Documentation workflow doesn't trigger on plugin changes.

**Cause:**
Path filters in workflow don't match changed files.

**Example:**
```yaml
# Won't trigger for rforge/ if it says rforge-orchestrator/
on:
  push:
    paths:
      - 'rforge-orchestrator/commands/**'  # ❌ Old name
```

**Solution:**
Update workflow paths when renaming:
```yaml
on:
  push:
    paths:
      - 'rforge/commands/**'  # ✅ New name
      - 'statistical-research/commands/**'
      - 'workflow/commands/**'
```

---

## Cross-Platform Issues

### Edge Case 13: Symlink Compatibility

**Symptom:**
Symlinks work on Mac/Linux but fail on Windows.

**Cause:**
Windows requires special permissions for symlinks, or doesn't support them at all.

**Impact:**
Local marketplace approach (using symlinks) may not work on Windows.

**Workaround (Windows):**
```bash
# Instead of symlinks, copy files
cp -r ~/.claude/plugins/rforge ~/.claude/local-marketplace/rforge
```

**Better Solution:**
Use Git submodules or junction points:
```bash
# Windows junction (like symlink)
mklink /J ~/.claude/local-marketplace/rforge ~/.claude/plugins/rforge
```

---

## Performance & Scalability

### Edge Case 14: Large Plugin Count

**Symptom:**
Slow startup when loading many plugins.

**Cause:**
Claude Code scans all plugins at startup. 50+ plugins = noticeable delay.

**Mitigation:**
- Use `--plugin-dir` for testing (loads only specified plugins)
- Keep installed plugin count reasonable (< 20)
- Uninstall unused plugins

**Benchmark:**
- 1-5 plugins: < 1 second
- 10-15 plugins: 1-2 seconds
- 20-30 plugins: 2-5 seconds
- 50+ plugins: 5-10 seconds

---

### Edge Case 15: Command Autocomplete Performance

**Symptom:**
Typing `/` has lag when showing command list.

**Cause:**
Too many commands (100+) slows down autocomplete.

**Current:**
- 17 commands: Instant
- 50 commands: Slight delay
- 100+ commands: Noticeable lag

**Optimization:**
- Group commands by plugin
- Use subcommands (e.g., `/rforge deps` instead of `/rforge:deps`)
- Cache command list

---

## Security & Permissions

### Edge Case 16: Plugin Directory Permissions

**Symptom:**
```
Error: Permission denied when accessing ~/.claude/plugins/
```

**Cause:**
Directory permissions too restrictive.

**Check:**
```bash
ls -la ~/.claude/plugins/
# Should be readable by user
```

**Fix:**
```bash
chmod 755 ~/.claude/plugins/
chmod 644 ~/.claude/plugins/*/plugin.json
```

---

### Edge Case 17: Script Execution Permissions

**Symptom:**
Plugin scripts fail to execute.

**Cause:**
Scripts need execute permission:
```bash
./scripts/install.sh
# bash: permission denied
```

**Fix:**
```bash
chmod +x scripts/*.sh
```

**Prevention:**
Add to git:
```bash
git add --chmod=+x scripts/*.sh
```

---

## Best Practices to Avoid Edge Cases

### Plugin Development

1. **Always namespace commands**
   - Use `plugin:command` format
   - Prevents collisions

2. **Test installation before committing**
   - Install via marketplace locally
   - Verify commands appear
   - Test on fresh environment

3. **Use consistent naming**
   - Plugin directory = plugin name in plugin.json
   - No special characters
   - Lowercase with hyphens

4. **Validate before publishing**
   - Run validation scripts
   - Check frontmatter
   - Test all commands

### Marketplace Management

1. **Clear cache when renaming**
   ```bash
   rm -rf ~/.claude/plugins/cache/local-plugins/old-name
   ```

2. **Use `./` prefix in source paths**
   ```json
   "source": "./plugin-name"
   ```

3. **Test marketplace discovery**
   ```bash
   /plugin marketplace remove local-plugins
   /plugin marketplace add ~/.claude/local-marketplace
   /plugin install plugin-name@local-plugins
   ```

### Documentation

1. **Use GitHub URLs for external links**
   - Not relative paths
   - Prevents MkDocs strict mode failures

2. **Keep docs in docs/ directory**
   - Avoids link resolution issues
   - Simplifies navigation

3. **Test build locally**
   ```bash
   mkdocs build --strict
   ```

### CI/CD

1. **Update workflow paths when renaming**
   - Check all path filters
   - Test workflow triggers

2. **Allow time for deployment**
   - Don't check site immediately
   - Wait 5 minutes for CDN

---

## Debugging Checklist

When a plugin isn't working:

### Installation
- [ ] Cache cleared for old plugin name?
- [ ] Marketplace source path starts with `./`?
- [ ] Symlink resolves correctly?
- [ ] Marketplace added successfully?

### Plugin Structure
- [ ] `.claude-plugin/plugin.json` exists?
- [ ] `package.json` exists at root?
- [ ] `name` in plugin.json matches directory?
- [ ] Command files have frontmatter with `name:`?

### Commands
- [ ] Commands namespaced (e.g., `plugin:cmd`)?
- [ ] Frontmatter at start of file (no blank lines)?
- [ ] Valid YAML syntax?
- [ ] No name collisions with other plugins?

### Documentation
- [ ] External links use GitHub URLs?
- [ ] No links to files outside docs/?
- [ ] MkDocs builds without errors?
- [ ] Navigation structure correct?

### Git
- [ ] Renamed with `git mv`?
- [ ] Commit includes all changes?
- [ ] Workflow paths updated?

---

## Getting Help

If you encounter an edge case not listed here:

1. **Check Claude Code logs**
   ```bash
   tail -f ~/Library/Logs/Claude/mcp*.log
   ```

2. **Validate plugin structure**
   ```bash
   python3 scripts/validate-all-plugins.py
   ```

3. **Test with `--plugin-dir`**
   ```bash
   claude --plugin-dir /path/to/plugin
   ```

4. **Compare with working plugin**
   - Use statistical-research or workflow as reference
   - Check structure, naming, frontmatter

---

**This document will be updated as new edge cases are discovered.**
