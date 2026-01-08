# Publishing Guide

How to publish Claude Code plugins from this monorepo to npm and create GitHub releases.

---

## Prerequisites

- npm account: https://www.npmjs.com/signup
- npm authentication: `npm login`
- Git repository access
- Plugin tested and ready

---

## Publishing Checklist

Before publishing, ensure:

### Code Quality

- [ ] All tests passing
- [ ] No lint errors
- [ ] Documentation complete
- [ ] README.md comprehensive
- [ ] Examples working

### Package Files

- [ ] `package.json` version correct
- [ ] `package.json` files array includes all needed files
- [ ] LICENSE file present (MIT)
- [ ] `.gitignore` excludes node_modules, etc.
- [ ] No sensitive data in code

### Installation

- [ ] `./scripts/install.sh` works (production mode)
- [ ] `./scripts/install.sh --dev` works (dev mode)
- [ ] `./scripts/uninstall.sh` works
- [ ] Plugin functions after installation

### Version

- [ ] Version follows semver (X.Y.Z)
- [ ] CHANGELOG.md updated
- [ ] Git tag doesn't exist yet

---

## Publishing Workflow

### Step 1: Prepare Release

#### 1.1 Update Version

```bash
cd ~/projects/dev-tools/claude-plugins/my-plugin

# Edit package.json
# Change version: "1.0.0" → "1.1.0"

# Or use npm version
npm version minor  # 1.0.0 → 1.1.0
npm version patch  # 1.0.0 → 1.0.1
npm version major  # 1.0.0 → 2.0.0
```

#### 1.2 Update CHANGELOG.md

```markdown
# Changelog

## [1.1.0] - 2025-01-15

### Added
- New feature X
- New command Y

### Fixed
- Bug Z

### Changed
- Improved error messages
```

#### 1.3 Test Package Contents

```bash
# See what will be published
npm pack --dry-run

# Create tarball
npm pack
# Creates: my-plugin-1.1.0.tgz

# Inspect contents
tar -tzf my-plugin-1.1.0.tgz

# Test installation from tarball
npm install -g ./my-plugin-1.1.0.tgz
```

### Step 2: Commit and Tag

```bash
# Commit changes
git add package.json CHANGELOG.md
git commit -m "chore(my-plugin): release v1.1.0"

# Create tag
git tag my-plugin-v1.1.0

# Push commits and tags
git push origin main
git push origin my-plugin-v1.1.0
```

**Note:** Use plugin-specific tags (`my-plugin-v1.1.0`) to avoid conflicts in monorepo.

### Step 3: Publish to npm

```bash
# Login to npm (if not already)
npm login

# Publish (from plugin directory)
cd ~/projects/dev-tools/claude-plugins/my-plugin
npm publish --access public

# Verify publication
npm view @data-wise/my-plugin
```

#### First-Time Publishing

For first-time publish of a plugin:

```bash
# May need to create organization first
npm access grant read-write data-wise:developers @data-wise/my-plugin

# Then publish
npm publish --access public
```

### Step 4: Create GitHub Release

```bash
# Create release from tag
gh release create my-plugin-v1.1.0 \
  --title "My Plugin v1.1.0" \
  --notes-file CHANGELOG.md

# Or with manual notes
gh release create my-plugin-v1.1.0 \
  --title "My Plugin v1.1.0" \
  --notes "Release notes here..."

# Attach tarball (optional)
gh release upload my-plugin-v1.1.0 my-plugin-1.1.0.tgz
```

---

## Versioning Strategy

Follow [Semantic Versioning](https://semver.org/):

### Major Version (X.0.0)

**When:** Breaking changes

**Examples:**
- Removing commands
- Changing command syntax
- Removing skills
- Incompatible API changes

```bash
npm version major  # 1.2.3 → 2.0.0
```

### Minor Version (1.X.0)

**When:** New features, backward compatible

**Examples:**
- Adding new commands
- Adding new skills
- New functionality
- Performance improvements

```bash
npm version minor  # 1.2.3 → 1.3.0
```

### Patch Version (1.0.X)

**When:** Bug fixes, backward compatible

**Examples:**
- Fixing bugs
- Improving error messages
- Documentation fixes
- Minor improvements

```bash
npm version patch  # 1.2.3 → 1.2.4
```

---

## Package.json Best Practices

### Minimal package.json

```json
{
  "name": "@data-wise/my-plugin",
  "version": "1.0.0",
  "description": "Brief description",
  "type": "module",
  "main": "index.js",
  "bin": {
    "my-plugin": "./scripts/install.sh"
  },
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
  "keywords": [
    "claude",
    "claude-code",
    "plugin",
    "your-domain"
  ],
  "author": "Data-Wise",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/Data-Wise/claude-plugins.git",
    "directory": "my-plugin"
  },
  "bugs": {
    "url": "https://github.com/Data-Wise/claude-plugins/issues"
  },
  "homepage": "https://github.com/Data-Wise/claude-plugins/tree/main/my-plugin#readme"
}
```

### Important Fields

**files:** Controls what gets published
```json
{
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

**repository.directory:** Points to plugin in monorepo
```json
{
  "repository": {
    "type": "git",
    "url": "https://github.com/Data-Wise/claude-plugins.git",
    "directory": "my-plugin"
  }
}
```

---

## npm Commands Reference

```bash
# View package info
npm view @data-wise/my-plugin

# View specific field
npm view @data-wise/my-plugin version
npm view @data-wise/my-plugin dist.tarball

# List published versions
npm view @data-wise/my-plugin versions

# Check package contents (before publishing)
npm pack --dry-run

# Publish
npm publish --access public

# Unpublish (within 72 hours, use cautiously!)
npm unpublish @data-wise/my-plugin@1.0.0

# Deprecate version
npm deprecate @data-wise/my-plugin@1.0.0 "Use version 1.1.0 instead"
```

---

## Monorepo Publishing Pattern

Since this is a monorepo, each plugin publishes independently:

### Directory Structure After Publishing

```
~/projects/dev-tools/claude-plugins/
├── plugin-a/
│   ├── package.json          # version: 1.2.0
│   └── ...
├── plugin-b/
│   ├── package.json          # version: 2.0.0
│   └── ...
└── plugin-c/
    ├── package.json          # version: 1.0.5
    └── ...
```

Each plugin has its own:
- Version number
- npm package
- Git tags
- Release notes

### Git Tags Pattern

Use plugin-specific prefixes:

```bash
# Plugin A releases
git tag plugin-a-v1.0.0
git tag plugin-a-v1.1.0
git tag plugin-a-v1.2.0

# Plugin B releases
git tag plugin-b-v1.0.0
git tag plugin-b-v2.0.0

# List tags for specific plugin
git tag -l "plugin-a-*"
```

---

## Continuous Publishing (Optional)

### GitHub Actions for npm Publishing

Create `.github/workflows/publish-plugin.yml`:

```yaml
name: Publish Plugin

on:
  push:
    tags:
      - '*-v*'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: actions/setup-node@v3
        with:
          node-version: '18'
          registry-url: 'https://registry.npmjs.org'

      - name: Extract plugin name
        id: plugin
        run: |
          TAG=${GITHUB_REF#refs/tags/}
          PLUGIN=${TAG%-v*}
          echo "name=$PLUGIN" >> $GITHUB_OUTPUT

      - name: Publish to npm
        run: |
          cd ${{ steps.plugin.outputs.name }}
          npm publish --access public
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

**Setup:**
1. Create npm token: https://www.npmjs.com/settings/your-username/tokens
2. Add to GitHub secrets: Settings → Secrets → NPM_TOKEN
3. Push tag triggers publish

---

## Troubleshooting

### Issue: "You do not have permission to publish"

**Cause:** Not logged in or wrong organization

**Fix:**
```bash
npm login
npm whoami  # Verify logged in

# For organization packages
npm access grant read-write data-wise:developers @data-wise/my-plugin
```

### Issue: "Package already exists"

**Cause:** Version already published

**Fix:**
```bash
# Increment version
npm version patch
npm publish --access public
```

### Issue: "File not found in package"

**Cause:** File not listed in `files` array

**Fix:** Add to package.json:
```json
{
  "files": [
    "missing-file.js"
  ]
}
```

### Issue: Tag already exists

**Cause:** Git tag conflicts

**Fix:**
```bash
# Delete local tag
git tag -d my-plugin-v1.0.0

# Delete remote tag
git push origin :refs/tags/my-plugin-v1.0.0

# Create correct tag
git tag my-plugin-v1.0.1
git push origin my-plugin-v1.0.1
```

---

## Best Practices

1. **Test before publishing**
   - Always `npm pack` and test tarball
   - Install from tarball and verify

2. **Semantic versioning**
   - Follow semver strictly
   - Major for breaking, minor for features, patch for fixes

3. **Changelog maintenance**
   - Update CHANGELOG.md before each release
   - List all changes clearly

4. **Tag naming**
   - Use plugin-specific prefixes
   - Format: `plugin-name-v1.0.0`

5. **Git hygiene**
   - Commit before tagging
   - Push commits and tags together

6. **npm package size**
   - Keep package small
   - Exclude dev files (tests, docs)
   - Use `.npmignore` if needed

7. **Documentation**
   - README.md is the first thing users see
   - Include examples and quick start

---

## Post-Publishing

After publishing:

1. **Announce release**
   - Update main README.md
   - Post in discussions
   - Tweet/share if desired

2. **Monitor issues**
   - Watch for bug reports
   - Respond to questions
   - Plan next version

3. **Update documentation**
   - Keep docs in sync with code
   - Add new examples

4. **Track usage**
   - npm download stats
   - GitHub stars/forks
   - User feedback

---

## Example: Complete Release Workflow

```bash
# 1. Prepare release
cd ~/projects/dev-tools/claude-plugins/statistical-research

# 2. Update version
npm version minor  # 1.0.0 → 1.1.0

# 3. Update changelog
echo "## [1.1.0] - $(date +%Y-%m-%d)" >> CHANGELOG.md
echo "### Added" >> CHANGELOG.md
echo "- New feature X" >> CHANGELOG.md

# 4. Test package
npm pack
npm install -g ./statistical-research-plugin-1.1.0.tgz
# Test it works...

# 5. Commit
git add package.json CHANGELOG.md
git commit -m "chore(statistical-research): release v1.1.0"

# 6. Tag
git tag statistical-research-v1.1.0

# 7. Push
git push origin main
git push origin statistical-research-v1.1.0

# 8. Publish to npm
npm publish --access public

# 9. Create GitHub release
gh release create statistical-research-v1.1.0 \
  --title "Statistical Research Plugin v1.1.0" \
  --notes "See CHANGELOG.md for details"

# Done!
```

---

See also:
- [npm Documentation](https://docs.npmjs.com/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github)
