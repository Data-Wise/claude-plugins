---
description: Complete Homebrew automation - formulas, workflows, tokens, and validation
arguments:
  - name: subcommand
    description: "Subcommand: formula|workflow|validate|token|setup"
    required: false
    default: formula
  - name: tap
    description: Homebrew tap repository (e.g., user/tap)
    required: false
  - name: version
    description: Specific version to use (default: latest tag)
    required: false
---

# /craft:dist:homebrew - Homebrew Automation Hub

Complete Homebrew formula management with automated workflows.

## Subcommands

| Command | Purpose |
|---------|---------|
| `formula` | Generate or update formula (default) |
| `workflow` | Generate GitHub Actions release workflow |
| `validate` | Run `brew audit` validation |
| `token` | Guide for setting up tap access token |
| `setup` | Full setup wizard (formula + workflow + token) |
| `update-resources` | Fix stale PyPI resource URLs |

## Quick Start

```bash
# Generate formula for current project
/craft:dist:homebrew

# Full automated setup (recommended for new projects)
/craft:dist:homebrew setup

# Generate release workflow
/craft:dist:homebrew workflow

# Validate formula before release
/craft:dist:homebrew validate
```

---

## /craft:dist:homebrew formula

Generate or update a Homebrew formula.

### Usage

```bash
/craft:dist:homebrew formula                    # Auto-detect and create
/craft:dist:homebrew formula --tap user/tap     # Specify target tap
/craft:dist:homebrew formula --version 1.2.3    # Use specific version
```

### Auto-Detection

Detects project type and generates appropriate formula:

| Project Type | Detection | Formula Pattern |
|--------------|-----------|-----------------|
| Python | `pyproject.toml` | `Language::Python::Virtualenv` |
| Node.js | `package.json` | npm install pattern |
| Go | `go.mod` | go build pattern |
| Rust | `Cargo.toml` | cargo install pattern |
| Shell | `*.sh` scripts | bin.install pattern |

### Example Output

```
✓ Detected: Python project (pyproject.toml)
✓ Found version: 0.3.5 (from git tag)
✓ Calculated SHA256: abc123...
✓ Generated: Formula/myapp.rb

Formula saved to: ./Formula/myapp.rb
```

---

## /craft:dist:homebrew workflow

Generate GitHub Actions workflow for automated Homebrew releases.

### Usage

```bash
/craft:dist:homebrew workflow                   # Generate caller workflow
/craft:dist:homebrew workflow --tap user/tap    # Specify tap repository
```

### Output Files

Creates `.github/workflows/homebrew-release.yml`:

```yaml
name: Homebrew Release

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to release'
        required: true
      auto_merge:
        description: 'Auto-merge the PR'
        type: boolean
        default: true

jobs:
  prepare:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.version.outputs.version }}
      sha256: ${{ steps.sha256.outputs.sha256 }}
    steps:
      - name: Get version
        id: version
        run: |
          if [ "${{ github.event_name }}" = "release" ]; then
            VERSION="${{ github.event.release.tag_name }}"
            VERSION="${VERSION#v}"
          else
            VERSION="${{ github.event.inputs.version }}"
          fi
          echo "version=$VERSION" >> $GITHUB_OUTPUT

      - name: Calculate SHA256
        id: sha256
        run: |
          TARBALL_URL="https://github.com/${{ github.repository }}/archive/refs/tags/v${{ steps.version.outputs.version }}.tar.gz"
          SHA256=$(curl -sL "$TARBALL_URL" | shasum -a 256 | cut -d' ' -f1)
          echo "sha256=$SHA256" >> $GITHUB_OUTPUT

  update-homebrew:
    needs: prepare
    uses: YOUR-ORG/homebrew-tap/.github/workflows/update-formula.yml@main
    with:
      formula_name: YOUR-FORMULA-NAME
      version: ${{ needs.prepare.outputs.version }}
      sha256: ${{ needs.prepare.outputs.sha256 }}
      source_type: github
      auto_merge: ${{ github.event.inputs.auto_merge == 'true' || github.event_name == 'release' }}
    secrets:
      tap_token: ${{ secrets.HOMEBREW_TAP_GITHUB_TOKEN }}
```

### Workflow Types

| Source | When to Use |
|--------|-------------|
| GitHub | Projects with GitHub releases |
| PyPI | Python packages published to PyPI |

For PyPI source, use:
```bash
/craft:dist:homebrew workflow --source pypi
```

---

## /craft:dist:homebrew validate

Validate formula before release using `brew audit`.

### Usage

```bash
/craft:dist:homebrew validate                   # Validate local formula
/craft:dist:homebrew validate --strict          # Strict mode (extra checks)
/craft:dist:homebrew validate --online          # Online checks (URL validation)
```

### Checks Performed

| Check | Description |
|-------|-------------|
| Syntax | Ruby syntax validation |
| `desc` | < 80 chars, no 'A/An' prefix |
| `license` | Valid SPDX identifier |
| `url` | Accessible (with --online) |
| `sha256` | Matches URL content |
| `test` | Test block present |
| Dependencies | All deps available |

### Example Output

```
Running: brew audit --strict --online Formula/myapp.rb

✓ Formula syntax valid
✓ Description format correct
✓ License is valid SPDX identifier
✓ URL accessible and matches SHA256
✓ Test block present
✓ All dependencies available

Formula is ready for release!
```

### Common Fixes

```ruby
# Fix: Description too long or starts with article
desc "AI terminal optimizer"  # Not "A terminal optimizer..."

# Fix: Invalid license
license "MIT"  # Use SPDX identifier

# Fix: Missing test block
test do
  assert_match version.to_s, shell_output("#{bin}/myapp --version")
end
```

---

## /craft:dist:homebrew token

Guide for setting up the Homebrew tap access token.

### Usage

```bash
/craft:dist:homebrew token                      # Show token setup guide
/craft:dist:homebrew token --check              # Check if token is configured
/craft:dist:homebrew token --repos              # Show repos needing token
```

### Token Requirements

Create a **Fine-Grained Personal Access Token**:

| Setting | Value |
|---------|-------|
| **Name** | `homebrew-tap-updater` |
| **Expiration** | 90 days (set rotation reminder) |
| **Repository access** | Only select repositories |
| **Selected repositories** | `YOUR-ORG/homebrew-tap` |
| **Permissions** | |
| - Contents | Read and write |
| - Pull requests | Read and write |

### Setup Steps

1. **Create Token**
   - Go to: https://github.com/settings/tokens?type=beta
   - Click "Generate new token"
   - Configure as above
   - Copy the token immediately

2. **Add to Repository**
   ```bash
   gh secret set HOMEBREW_TAP_GITHUB_TOKEN --repo YOUR-ORG/your-repo
   # Paste token when prompted
   ```

3. **Verify**
   ```bash
   gh secret list --repo YOUR-ORG/your-repo
   # Should show: HOMEBREW_TAP_GITHUB_TOKEN
   ```

### Token Rotation

Set a calendar reminder for 80 days after creation:
1. Create new token with same settings
2. Update in all repos: `gh secret set HOMEBREW_TAP_GITHUB_TOKEN --repo ...`
3. Delete old token from GitHub settings

---

## /craft:dist:homebrew setup

Full guided setup for Homebrew automation.

### Usage

```bash
/craft:dist:homebrew setup                      # Interactive wizard
/craft:dist:homebrew setup --tap user/tap       # Specify tap
```

### Setup Flow

```
╔═══════════════════════════════════════════════════════════════╗
║           HOMEBREW AUTOMATION SETUP WIZARD                     ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Step 1: Detect Project Type                                  ║
║  ───────────────────────────────────────                      ║
║  ✓ Detected: Python (pyproject.toml)                          ║
║  ✓ Name: myapp                                                ║
║  ✓ Version: 0.3.5                                             ║
║                                                               ║
║  Step 2: Generate Formula                                     ║
║  ───────────────────────────────────────                      ║
║  ✓ Created: Formula/myapp.rb                                  ║
║  ✓ Validated: brew audit passed                               ║
║                                                               ║
║  Step 3: Generate Workflow                                    ║
║  ───────────────────────────────────────                      ║
║  ✓ Created: .github/workflows/homebrew-release.yml            ║
║  ✓ Configured for: Data-Wise/homebrew-tap                     ║
║                                                               ║
║  Step 4: Token Check                                          ║
║  ───────────────────────────────────────                      ║
║  ⚠ HOMEBREW_TAP_GITHUB_TOKEN not found                        ║
║                                                               ║
║  Run: gh secret set HOMEBREW_TAP_GITHUB_TOKEN                 ║
║  (See /craft:dist:homebrew token for guide)                   ║
║                                                               ║
║  Step 5: Commit Changes                                       ║
║  ───────────────────────────────────────                      ║
║  ✓ Staged: Formula/myapp.rb                                   ║
║  ✓ Staged: .github/workflows/homebrew-release.yml             ║
║                                                               ║
║  Ready to commit? (y/n)                                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

### What It Does

1. **Detects** project type and metadata
2. **Generates** Homebrew formula
3. **Validates** formula with `brew audit`
4. **Creates** GitHub Actions workflow
5. **Checks** if token is configured
6. **Commits** all changes (with confirmation)

### Post-Setup

After setup completes:

```bash
# Create first release
git tag -a v0.3.5 -m "Release v0.3.5"
git push --tags

# Or trigger manually
gh workflow run homebrew-release.yml -f version=0.3.5
```

---

## Formula Templates

### Python (virtualenv)

```ruby
class MyApp < Formula
  include Language::Python::Virtualenv

  desc "Description from pyproject.toml"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/myapp --version")
  end
end
```

### Node.js

```ruby
class MyApp < Formula
  desc "Description from package.json"
  homepage "https://github.com/user/repo"
  url "https://registry.npmjs.org/myapp/-/myapp-1.0.0.tgz"
  sha256 "..."
  license "MIT"

  depends_on "node"

  def install
    system "npm", "install", *std_npm_args
    bin.install_symlink Dir["#{libexec}/bin/*"]
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/myapp --version")
  end
end
```

### Go

```ruby
class MyApp < Formula
  desc "Description"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "go" => :build

  def install
    system "go", "build", *std_go_args(ldflags: "-s -w -X main.version=#{version}")
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/myapp --version")
  end
end
```

### Rust

```ruby
class MyApp < Formula
  desc "Description from Cargo.toml"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "rust" => :build

  def install
    system "cargo", "install", *std_cargo_args
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/myapp --version")
  end
end
```

---

## /craft:dist:homebrew update-resources

Fix stale PyPI resource URLs in formulas automatically.

### The Problem

PyPI occasionally changes the directory structure for package downloads, causing formulas with `resource` blocks to break:

```
Error: Failed to download resource "click"
expected sha256 checksum <old>, got <new>
```

### Usage

```bash
/craft:dist:homebrew update-resources myapp        # Update specific formula
/craft:dist:homebrew update-resources --all        # Update all formulas
/craft:dist:homebrew update-resources --dry-run    # Preview changes only
```

### How It Works

1. **Parse Formula** - Extract all `resource` blocks
2. **Query PyPI API** - Get current URLs and checksums for each package
3. **Update Formula** - Replace stale URLs and SHA256 values
4. **Validate** - Run `brew audit` on updated formula

### Example

**Before (stale):**
```ruby
resource "click" do
  url "https://files.pythonhosted.org/packages/old/path/click-8.0.0.tar.gz"
  sha256 "abc123..."
end
```

**After (updated):**
```ruby
resource "click" do
  url "https://files.pythonhosted.org/packages/source/c/click/click-8.1.7.tar.gz"
  sha256 "def456..."
end
```

### PyPI API Integration

```bash
# Fetch package info
curl -s "https://pypi.org/pypi/click/json" | jq '{
  name: .info.name,
  version: .info.version,
  url: .urls[] | select(.packagetype == "sdist") | .url,
  sha256: .urls[] | select(.packagetype == "sdist") | .digests.sha256
}'
```

### Output

```
Updating resources for: nexus-cli

Checking 5 resources...
  ✓ click: 8.0.0 → 8.1.7 (URL updated)
  ✓ rich: 13.0.0 → 13.7.0 (URL updated)
  - typer: 0.9.0 (no changes)
  - httpx: 0.24.0 (no changes)
  ✓ pydantic: 2.0.0 → 2.5.3 (URL updated)

Updated 3 resources in Formula/nexus-cli.rb
Running brew audit... ✓ passed
```

### Options

| Option | Description |
|--------|-------------|
| `--dry-run` | Show what would change without modifying |
| `--all` | Update all formulas in tap |
| `--pin` | Don't upgrade versions, only fix URLs |
| `--commit` | Auto-commit changes |

### Common Issues

**Issue: Package renamed on PyPI**
```
Warning: Package 'old-name' not found on PyPI
Hint: Check if package was renamed or deprecated
```

**Issue: Source distribution not available**
```
Warning: No sdist found for 'package-name'
Only wheel distributions available
```

---

## Integration

| Command | Use With |
|---------|----------|
| `/craft:check --for release` | Pre-release validation |
| `/craft:git:tag` | Create version tag |
| `/craft:docs:changelog` | Update changelog |
| `/craft:ci:generate` | Full CI/CD setup |

## Skills Used

- `homebrew-formula-expert` - Formula syntax and patterns
- `homebrew-workflow-expert` - GitHub Actions automation
- `homebrew-setup-wizard` - Setup wizard implementation
- `distribution-strategist` - Multi-channel distribution

---

## Tips

- Always run `validate` before creating releases
- Use semantic versioning for clean formulas
- Set token rotation reminders (90-day expiry recommended)
- Test locally: `brew install --build-from-source ./Formula/myapp.rb`
- Auto-merge is safe for personal taps; disable for team taps
