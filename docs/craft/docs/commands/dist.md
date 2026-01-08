# Distribution Commands

⏱️ **10 minutes** • 🟡 Intermediate • ✓ Multi-platform packaging

> **TL;DR** (30 seconds)
> - **What:** 3 commands for packaging and distributing your project (Homebrew, PyPI, curl installer)
> - **Why:** Automate release workflows and make your project easy to install across platforms
> - **How:** Use `/craft:dist:homebrew setup` for macOS, `/craft:dist:pypi` for Python packages
> - **Next:** Try `/craft:dist:homebrew setup` to create automated Homebrew releases

Craft's distribution commands automate packaging and distribution across Homebrew, PyPI, and curl installers.

---

## Commands Overview

| Command | Purpose | Platforms |
|---------|---------|-----------|
| `/craft:dist:homebrew` | Homebrew formula automation | macOS, Linux |
| `/craft:dist:pypi` | PyPI package publishing | Python (all platforms) |
| `/craft:dist:curl-install` | Curl-based installer script | All platforms |

---

## `/craft:dist:homebrew` - Homebrew Automation

Complete Homebrew formula management with automated GitHub Actions workflows.

### Quick Start

```bash
# Full setup wizard (recommended)
/craft:dist:homebrew setup

# Generate formula only
/craft:dist:homebrew formula

# Generate GitHub Actions workflow
/craft:dist:homebrew workflow

# Validate formula
/craft:dist:homebrew validate
```

### Subcommands

| Subcommand | Purpose |
|------------|---------|
| `formula` | Generate or update Homebrew formula |
| `workflow` | Create GitHub Actions release automation |
| `validate` | Run `brew audit` validation |
| `token` | Guide for setting up tap access token |
| `setup` | Full wizard (formula + workflow + token) |
| `update-resources` | Fix stale PyPI resource URLs |

### Example: Full Setup

```bash
/craft:dist:homebrew setup
```

**Output:**
```
╔═══════════════════════════════════════════════════════════╗
║       HOMEBREW AUTOMATION SETUP WIZARD                     ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  ✓ Detected: Python (pyproject.toml)                      ║
║  ✓ Name: aiterm | Version: 0.6.0                         ║
║  ✓ Created: Formula/aiterm.rb                            ║
║  ✓ Validated: brew audit passed                          ║
║  ✓ Created: .github/workflows/homebrew-release.yml       ║
║  ✓ Configured for: Data-Wise/homebrew-tap               ║
║                                                           ║
║  ⚠ HOMEBREW_TAP_GITHUB_TOKEN not found                   ║
║  Run: gh secret set HOMEBREW_TAP_GITHUB_TOKEN            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

### Supported Project Types

| Type | Detection | Formula Pattern |
|------|-----------|-----------------|
| Python | `pyproject.toml` | `Language::Python::Virtualenv` |
| Node.js | `package.json` | npm install |
| Go | `go.mod` | go build |
| Rust | `Cargo.toml` | cargo install |
| Shell | `*.sh` scripts | bin.install |

### Automated Workflow

Creates `.github/workflows/homebrew-release.yml`:

- **Triggers:** On GitHub release published or manual dispatch
- **Auto-merge:** Optional PR auto-merge
- **Multi-source:** Supports GitHub releases or PyPI packages
- **Token-based:** Uses fine-grained GitHub token

### Update Stale Resources (Python)

PyPI occasionally changes URLs for packages. Fix automatically:

```bash
/craft:dist:homebrew update-resources aiterm
```

**Output:**
```
Checking 5 resources...
  ✓ click: 8.0.0 → 8.1.7 (URL updated)
  ✓ rich: 13.0.0 → 13.7.0 (URL updated)
  - typer: 0.9.0 (no changes)

Updated 2 resources in Formula/aiterm.rb
Running brew audit... ✓ passed
```

---

## `/craft:dist:pypi` - PyPI Publishing

Publish Python packages to PyPI with automated workflows and trusted publishing.

### Quick Start

```bash
# Full PyPI setup
/craft:dist:pypi setup

# Publish current version
/craft:dist:pypi publish

# Check PyPI status
/craft:dist:pypi status

# Generate GitHub Actions workflow
/craft:dist:pypi workflow
```

### Subcommands

| Subcommand | Purpose |
|------------|---------|
| `setup` | Configure PyPI publishing (pyproject.toml, workflows) |
| `publish` | Build and upload to PyPI |
| `status` | Check package status on PyPI |
| `workflow` | Generate GitHub Actions for trusted publishing |
| `validate` | Validate package metadata |

### Trusted Publishing (Recommended)

Uses OpenID Connect (OIDC) for secure, token-free publishing:

**Setup:**

1. **Add pending publisher on PyPI:**
   - Go to: https://pypi.org/manage/account/publishing/
   - Project: `your-package`
   - Owner: `your-org`
   - Repository: `your-repo`
   - Workflow: `publish.yml`
   - Environment: `pypi`

2. **Generate workflow:**

   ```bash
   /craft:dist:pypi workflow
   ```

3. **Create release:**

   ```bash
   gh release create v1.0.0
   ```

### Example Workflow

Creates `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: pypi  # Required for trusted publishing
    permissions:
      id-token: write  # Required for OIDC
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Build package
        run: |
          python -m pip install build
          python -m build
      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
```

### Validation

```bash
/craft:dist:pypi validate
```

**Checks:**
- `pyproject.toml` completeness
- Version format (SemVer)
- README presence
- License file
- Classifiers validity
- Build configuration

---

## `/craft:dist:curl-install` - Universal Installer

Create a curl-based installer script for easy one-line installation.

### Quick Start

```bash
# Generate installer
/craft:dist:curl-install

# Generate with custom URL
/craft:dist:curl-install --repo user/repo

# Add to README
/craft:dist:curl-install --add-readme
```

### What It Creates

Generates `install.sh`:

```bash
#!/bin/bash
# Quick installer for myapp

set -e

# Detect platform
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS - use Homebrew
  brew install user/tap/myapp
elif command -v pip &> /dev/null; then
  # Python available - use PyPI
  pip install myapp
else
  # Fallback - download binary
  curl -sSL https://github.com/user/repo/releases/latest/download/myapp > /usr/local/bin/myapp
  chmod +x /usr/local/bin/myapp
fi
```

### Features

- **Platform detection:** macOS (Homebrew) / Linux (PyPI or binary)
- **Fallback chain:** Homebrew → PyPI → Direct download
- **Error handling:** Checks for dependencies
- **Version pinning:** Optional specific version

### Usage in README

```bash
# Quick install (auto-detects best method)
curl -fsSL https://raw.githubusercontent.com/user/repo/main/install.sh | bash

# Install specific version
curl -fsSL https://raw.githubusercontent.com/user/repo/main/install.sh | bash -s -- v1.0.0
```

### Options

```bash
/craft:dist:curl-install --methods homebrew,pypi    # Specify methods
/craft:dist:curl-install --add-readme               # Append to README
/craft:dist:curl-install --verify-sig               # Add GPG signature verification
```

---

## Common Workflows

### Workflow 1: New Project Distribution Setup

```bash
# Step 1: Set up all distribution channels
/craft:dist:homebrew setup
/craft:dist:pypi setup
/craft:dist:curl-install --add-readme

# Step 2: Validate everything
/craft:dist:homebrew validate
/craft:dist:pypi validate

# Step 3: Create first release
git tag -a v1.0.0 -m "Initial release"
git push --tags

# Step 4: Verify automation
gh run list --workflow homebrew-release
gh run list --workflow publish
```

### Workflow 2: Update Existing Distribution

```bash
# Update version in code
# Commit changes

# Create new release
gh release create v1.1.0 --generate-notes

# Monitor automation
gh run watch
```

### Workflow 3: Fix Stale Homebrew Resources

```bash
# Fix PyPI resource URLs
/craft:dist:homebrew update-resources myapp

# Validate
/craft:dist:homebrew validate --strict --online

# Commit and push to tap
cd ~/homebrew-tap
git add Formula/myapp.rb
git commit -m "fix(myapp): update PyPI resource URLs"
git push
```

---

## Integration with Other Commands

| Command | Use Case |
|---------|----------|
| `/craft:check --for release` | Pre-release validation before distribution |
| `/craft:git:recap` | Create version tags for releases |
| `/craft:docs:changelog` | Generate changelog for release notes |
| `/craft:ci:generate` | Full CI/CD setup including distribution |
| `/craft:code:release` | Complete release checklist |

---

## Skills Used

- `distribution-strategist` - Multi-channel distribution planning
- `homebrew-formula-expert` - Homebrew formula syntax
- `homebrew-workflow-expert` - GitHub Actions automation
- `homebrew-setup-wizard` - Setup wizard implementation

---

## Tips

!!! tip "Start with Setup Wizards"
    Use `/craft:dist:homebrew setup` and `/craft:dist:pypi setup` for guided configuration.

!!! success "Use Trusted Publishing"
    PyPI's trusted publishing (OIDC) is more secure than API tokens - no secrets to manage!

!!! tip "Test Locally First"
    Test Homebrew formulas before release: `brew install --build-from-source ./Formula/myapp.rb`

!!! warning "Token Rotation"
    Set a 90-day reminder to rotate Homebrew tap tokens.

---

## Troubleshooting

### Homebrew Formula Issues

**Problem:** `brew audit` fails with "Description too long"
**Solution:** Keep description under 80 characters, no "A/An" prefix

**Problem:** SHA256 mismatch
**Solution:** Recalculate: `curl -sL <url> | shasum -a 256`

**Problem:** Stale PyPI resource URLs
**Solution:** Run `/craft:dist:homebrew update-resources`

### PyPI Publishing Issues

**Problem:** `invalid-publisher` error
**Solution:** Verify workflow name matches exactly in PyPI config

**Problem:** Missing `environment: pypi`
**Solution:** Add environment to workflow job

**Problem:** Permission denied
**Solution:** Ensure `id-token: write` permission in workflow

### Curl Installer Issues

**Problem:** Installer fails on Linux
**Solution:** Add Python/binary fallback for non-macOS platforms

---

## Learn More

- [Architecture Commands](arch.md) - System design for distribution
- [CI Commands](git.md#ci-commands) - Automated testing before release
- [Visual Workflows](../workflows/index.md) - See distribution in action
