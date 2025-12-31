---
name: homebrew-setup-wizard
description: Implementation logic for the Homebrew automation setup wizard
version: 1.0.0
category: distribution
triggers:
  - homebrew setup
  - craft:dist:homebrew setup
  - homebrew automation setup
---

# Homebrew Setup Wizard Implementation

Step-by-step implementation guide for `/craft:dist:homebrew setup`.

## Overview

The setup wizard automates complete Homebrew formula automation in one command:

```
detect → generate formula → validate → create workflow → check token → commit
```

## Implementation Steps

### Step 1: Detect Project Type

```bash
# Check for project files in order of specificity
if [ -f "pyproject.toml" ]; then
    PROJECT_TYPE="python"
    # Extract name and version
    NAME=$(grep -E "^name\s*=" pyproject.toml | sed 's/.*=\s*"\([^"]*\)".*/\1/')
    VERSION=$(grep -E "^version\s*=" pyproject.toml | sed 's/.*=\s*"\([^"]*\)".*/\1/')
elif [ -f "package.json" ]; then
    PROJECT_TYPE="node"
    NAME=$(jq -r '.name' package.json)
    VERSION=$(jq -r '.version' package.json)
elif [ -f "go.mod" ]; then
    PROJECT_TYPE="go"
    NAME=$(basename $(head -1 go.mod | awk '{print $2}'))
    VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "0.1.0")
elif [ -f "Cargo.toml" ]; then
    PROJECT_TYPE="rust"
    NAME=$(grep -E "^name\s*=" Cargo.toml | head -1 | sed 's/.*=\s*"\([^"]*\)".*/\1/')
    VERSION=$(grep -E "^version\s*=" Cargo.toml | head -1 | sed 's/.*=\s*"\([^"]*\)".*/\1/')
else
    PROJECT_TYPE="unknown"
fi
```

**Output:**
```
Step 1: Detect Project Type
───────────────────────────────────────
✓ Detected: Python (pyproject.toml)
✓ Name: aiterm
✓ Version: 0.3.8
```

### Step 2: Get Git Remote & Determine Source

```bash
# Get GitHub remote
REMOTE_URL=$(git remote get-url origin 2>/dev/null)
if [[ $REMOTE_URL =~ github.com[:/]([^/]+)/([^/.]+) ]]; then
    GITHUB_ORG="${BASH_REMATCH[1]}"
    GITHUB_REPO="${BASH_REMATCH[2]}"
fi

# Determine source type
if [ "$PROJECT_TYPE" = "python" ]; then
    # Check if published to PyPI
    PYPI_CHECK=$(curl -s "https://pypi.org/pypi/${NAME}/json" | jq -r '.info.name // empty')
    if [ -n "$PYPI_CHECK" ]; then
        SOURCE_TYPE="pypi"
    else
        SOURCE_TYPE="github"
    fi
else
    SOURCE_TYPE="github"
fi
```

**Output:**
```
Step 2: Determine Source
───────────────────────────────────────
✓ GitHub: Data-Wise/aiterm
✓ Source: PyPI (package published)
```

### Step 3: Generate Formula

Based on project type, generate appropriate formula:

#### Python Formula Template

```ruby
class #{ClassName} < Formula
  include Language::Python::Virtualenv

  desc "#{description}"
  homepage "https://github.com/#{org}/#{repo}"
  url "https://github.com/#{org}/#{repo}/archive/refs/tags/v#{version}.tar.gz"
  sha256 "#{sha256}"
  license "#{license}"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/#{binary} --version")
  end
end
```

**Implementation:**

```python
def generate_formula(project_type, name, version, org, repo, description, license):
    # Calculate SHA256
    tarball_url = f"https://github.com/{org}/{repo}/archive/refs/tags/v{version}.tar.gz"
    sha256 = calculate_sha256(tarball_url)

    # Convert name to Ruby class name
    class_name = name.replace("-", "").replace("_", "").title()

    # Get binary name (usually same as package name)
    binary = name.replace("_", "-")

    # Generate formula based on type
    if project_type == "python":
        return PYTHON_TEMPLATE.format(...)
    elif project_type == "node":
        return NODE_TEMPLATE.format(...)
    # etc.
```

**Output:**
```
Step 3: Generate Formula
───────────────────────────────────────
✓ Calculated SHA256: a1b2c3d4...
✓ Generated: Formula/aiterm.rb
```

### Step 4: Validate Formula

```bash
# Run brew audit
brew audit --strict Formula/${NAME}.rb

# Check for common issues
if grep -q "^  desc \"A\|^  desc \"An\|^  desc \"The" Formula/${NAME}.rb; then
    echo "Warning: desc should not start with article"
fi

# Verify URL is accessible
URL=$(grep -E "^\s*url\s+" Formula/${NAME}.rb | sed 's/.*"\([^"]*\)".*/\1/')
if ! curl -sI "$URL" | grep -q "200 OK"; then
    echo "Warning: URL not accessible"
fi
```

**Output:**
```
Step 4: Validate Formula
───────────────────────────────────────
✓ Ruby syntax valid
✓ Description format correct
✓ License is valid SPDX identifier
✓ URL accessible
✓ brew audit passed
```

### Step 5: Generate Workflow

Create `.github/workflows/homebrew-release.yml`:

```yaml
name: Homebrew Release

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to release (e.g., 1.2.3)'
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
          echo "Version: $VERSION"

      - name: Calculate SHA256
        id: sha256
        run: |
          TARBALL_URL="https://github.com/${{ github.repository }}/archive/refs/tags/v${{ steps.version.outputs.version }}.tar.gz"
          SHA256=$(curl -sL "$TARBALL_URL" | shasum -a 256 | cut -d' ' -f1)
          echo "sha256=$SHA256" >> $GITHUB_OUTPUT
          echo "SHA256: $SHA256"

  update-homebrew:
    name: Update Homebrew Formula
    needs: prepare
    uses: ${TAP_ORG}/homebrew-tap/.github/workflows/update-formula.yml@main
    with:
      formula_name: ${FORMULA_NAME}
      version: ${{ needs.prepare.outputs.version }}
      sha256: ${{ needs.prepare.outputs.sha256 }}
      source_type: github
      auto_merge: ${{ github.event.inputs.auto_merge == 'true' || github.event_name == 'release' }}
    secrets:
      tap_token: ${{ secrets.HOMEBREW_TAP_GITHUB_TOKEN }}
```

**Output:**
```
Step 5: Generate Workflow
───────────────────────────────────────
✓ Created: .github/workflows/homebrew-release.yml
✓ Configured for: Data-Wise/homebrew-tap
✓ Triggers: release, workflow_dispatch
```

### Step 6: Check Token

```bash
# Check if token exists in repo secrets
TOKEN_EXISTS=$(gh secret list --repo ${ORG}/${REPO} 2>/dev/null | grep -c "HOMEBREW_TAP_GITHUB_TOKEN" || echo "0")

if [ "$TOKEN_EXISTS" = "0" ]; then
    echo "⚠ HOMEBREW_TAP_GITHUB_TOKEN not found"
    echo ""
    echo "To add the token:"
    echo "  gh secret set HOMEBREW_TAP_GITHUB_TOKEN --repo ${ORG}/${REPO}"
    echo ""
    echo "See: /craft:dist:homebrew token for setup guide"
else
    echo "✓ HOMEBREW_TAP_GITHUB_TOKEN configured"
fi
```

**Output (token missing):**
```
Step 6: Check Token
───────────────────────────────────────
⚠ HOMEBREW_TAP_GITHUB_TOKEN not found

To add the token:
  gh secret set HOMEBREW_TAP_GITHUB_TOKEN --repo Data-Wise/aiterm

See: /craft:dist:homebrew token for setup guide
```

**Output (token present):**
```
Step 6: Check Token
───────────────────────────────────────
✓ HOMEBREW_TAP_GITHUB_TOKEN configured
```

### Step 7: Summary & Commit

```
╔═══════════════════════════════════════════════════════════════╗
║           HOMEBREW AUTOMATION SETUP COMPLETE                   ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Files Created:                                               ║
║  ├── Formula/aiterm.rb                                        ║
║  └── .github/workflows/homebrew-release.yml                   ║
║                                                               ║
║  Configuration:                                               ║
║  ├── Project: aiterm (Python)                                 ║
║  ├── Source: GitHub releases                                  ║
║  ├── Tap: Data-Wise/homebrew-tap                              ║
║  └── Auto-merge: enabled                                      ║
║                                                               ║
║  Token Status: ⚠ Not configured                               ║
║  Run: gh secret set HOMEBREW_TAP_GITHUB_TOKEN                 ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Ready to commit these files? (y/n)                           ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

If user confirms:

```bash
git add Formula/${NAME}.rb .github/workflows/homebrew-release.yml
git commit -m "feat: add Homebrew formula and release workflow

- Add Formula/${NAME}.rb for Homebrew installation
- Add .github/workflows/homebrew-release.yml for automated updates
- Configured for ${TAP_ORG}/homebrew-tap with auto-merge"
```

## Error Handling

### No Git Remote

```
Error: No GitHub remote found
Hint: Run 'git remote add origin https://github.com/org/repo.git'
```

### No Version Tag

```
Warning: No version tag found
Using version from config: 0.1.0
Hint: Create a tag with 'git tag -a v0.1.0 -m "Initial release"'
```

### brew Not Installed

```
Warning: Homebrew not installed, skipping local validation
Formula will be validated when pushed to tap
```

### Existing Formula

```
Found existing Formula/${NAME}.rb
Options:
  1. Update existing formula
  2. Overwrite with new template
  3. Cancel

Choice:
```

## Interactive Prompts

When information can't be auto-detected, prompt user:

```
Tap repository not detected.
Enter tap (e.g., data-wise/tap): _

Source type:
  1. GitHub releases (default)
  2. PyPI package

Binary name (default: aiterm): _
```

## Integration Points

- Uses `homebrew-formula-expert` for formula templates
- Uses `homebrew-workflow-expert` for workflow generation
- Calls `gh secret list` for token verification
- Calls `brew audit` for validation (if available)
