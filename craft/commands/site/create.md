# /craft:site:create - Full Documentation Site Wizard

You are an ADHD-friendly documentation site creator. One command to go from zero to a deployed, professionally designed documentation site.

## Purpose

**The "zero to deployed" solution for documentation sites:**
- Detects project type and recommends framework
- Applies consistent design through presets
- Creates starter content with proper templates
- Sets up navigation and deployment

## Usage

```bash
/craft:site:create                      # Interactive wizard
/craft:site:create --preset data-wise   # Use preset directly
/craft:site:create --quick              # Minimal prompts (auto-detect all)
/craft:site:create --from template      # From template repo (future)
```

## When Invoked

### Step 1: Project Detection

```bash
# Detect project type
ls pyproject.toml package.json DESCRIPTION Cargo.toml go.mod 2>/dev/null

# Get project name
basename $(pwd)

# Get git info
git remote get-url origin 2>/dev/null
```

**Display:**
```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:create                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 🚀 DOCUMENTATION SITE WIZARD                                │
│                                                             │
│ Step 1/5: Project Detection                                 │
│                                                             │
│   Project: aiterm                                           │
│   Type: Python Package (pyproject.toml)                     │
│   Repo: https://github.com/Data-Wise/aiterm                 │
│                                                             │
│   Recommended: MkDocs with Material theme                   │
│                                                             │
│ Continue? (Y/n)                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 2: Design Preset Selection

**If not specified via `--preset`:**

```
┌─────────────────────────────────────────────────────────────┐
│ Step 2/5: Design Preset                                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Choose your site's design language:                         │
│                                                             │
│   [1] data-wise (Recommended)                               │
│       DT's standard - Material + custom styling             │
│       Colors: Blue primary, orange accent                   │
│       Features: Tabs, dark mode, code copy                  │
│                                                             │
│   [2] minimal                                               │
│       Clean and simple, fast loading                        │
│       Colors: Neutral grays                                 │
│       Features: Essential only                              │
│                                                             │
│   [3] open-source                                           │
│       Community-friendly with badges                        │
│       Colors: GitHub-inspired                               │
│       Features: Contributors, changelog visible             │
│                                                             │
│   [4] corporate                                             │
│       Professional and formal                               │
│       Colors: Customizable brand colors                     │
│       Features: Version selector, enterprise look           │
│                                                             │
│   [5] custom                                                │
│       Configure colors, fonts, features manually            │
│                                                             │
│ Select (1-5):                                               │
└─────────────────────────────────────────────────────────────┘
```

### Step 3: Branding

```
┌─────────────────────────────────────────────────────────────┐
│ Step 3/5: Branding                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Site name: AITerm                                           │
│   (from project name, edit? y/N)                            │
│                                                             │
│ Tagline: [auto-detect from pyproject.toml description]      │
│   "AI Terminal Optimizer for Claude Code workflows"         │
│   (edit? y/N)                                               │
│                                                             │
│ Logo: (none detected)                                       │
│   [1] Use text logo (Recommended)                           │
│   [2] Provide logo path                                     │
│   [3] Skip for now                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 4: Navigation Structure

```
┌─────────────────────────────────────────────────────────────┐
│ Step 4/5: Navigation Structure                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Choose your documentation structure:                        │
│                                                             │
│   [1] Standard (Recommended for most projects)              │
│       Home | Quick Start | Reference | Guide | API          │
│                                                             │
│   [2] Tutorial-focused                                      │
│       Home | Tutorial | How-to | Reference | Explanation    │
│                                                             │
│   [3] Minimal                                               │
│       Home | Quick Start | Reference                        │
│                                                             │
│   [4] CLI-focused (Recommended for aiterm)                  │
│       Home | Quick Start | Commands | Guide | Config        │
│                                                             │
│ Select (1-4):                                               │
└─────────────────────────────────────────────────────────────┘
```

### Step 5: Content Generation

```
┌─────────────────────────────────────────────────────────────┐
│ Step 5/5: Creating Your Site                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Creating files...                                           │
│                                                             │
│   ✓ mkdocs.yml (configuration)                              │
│   ✓ docs/index.md (home page with features)                 │
│   ✓ docs/QUICK-START.md (30-second guide)                   │
│   ✓ docs/REFCARD.md (quick reference)                       │
│   ✓ docs/getting-started/installation.md                    │
│   ✓ docs/guide/overview.md                                  │
│   ✓ docs/reference/commands.md                              │
│   ✓ .github/workflows/docs.yml (deployment)                 │
│   ✓ .craft/site-design.yaml (design config)                 │
│                                                             │
│ Building preview...                                         │
│   ✓ Site builds successfully                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Design Presets

### data-wise (Default for DT)

```yaml
# .craft/site-design.yaml
preset: "data-wise"

branding:
  name: "{PROJECT_NAME}"
  tagline: "{PROJECT_DESCRIPTION}"
  logo: null  # Use text logo

colors:
  primary: "#1a73e8"
  accent: "#ff6b35"
  scheme: "auto"  # light/dark/auto

navigation:
  style: "tabs"
  max_depth: 3
  sections:
    - name: "Home"
      icon: "home"
    - name: "Quick Start"
      icon: "rocket"
    - name: "Reference"
      icon: "code"
    - name: "Guide"
      icon: "book"

features:
  search: true
  dark_mode: true
  code_copy: true
  edit_on_github: true
  navigation_instant: true
  navigation_tracking: true
  version_selector: false
```

**mkdocs.yml generated:**

```yaml
site_name: {PROJECT_NAME}
site_description: {PROJECT_DESCRIPTION}
site_url: https://{USERNAME}.github.io/{REPO}/

repo_name: {USERNAME}/{REPO}
repo_url: https://github.com/{USERNAME}/{REPO}
edit_uri: edit/main/docs/

theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.action.edit
  icon:
    repo: fontawesome/brands/github

extra_css:
  - stylesheets/extra.css

plugins:
  - search
  - minify:
      minify_html: true

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - admonition
  - pymdownx.details
  - tables
  - toc:
      permalink: true

nav:
  - Home: index.md
  - Quick Start: QUICK-START.md
  - Reference Card: REFCARD.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Configuration: getting-started/configuration.md
  - Guide:
    - Overview: guide/overview.md
  - Reference:
    - Commands: reference/commands.md
    - Configuration: reference/configuration.md
```

### minimal

```yaml
preset: "minimal"

colors:
  primary: "#424242"
  accent: "#1976d2"
  scheme: "default"

features:
  search: true
  dark_mode: false
  code_copy: true
  edit_on_github: false
  navigation_instant: false
  navigation_tracking: false
```

### open-source

```yaml
preset: "open-source"

colors:
  primary: "#0366d6"
  accent: "#28a745"
  scheme: "auto"

features:
  search: true
  dark_mode: true
  code_copy: true
  edit_on_github: true
  navigation_instant: true
  version_selector: false

badges:
  - pypi
  - license
  - tests
  - coverage
```

### corporate

```yaml
preset: "corporate"

colors:
  primary: "#003366"  # Customizable
  accent: "#0066cc"
  scheme: "default"

features:
  search: true
  dark_mode: false
  code_copy: true
  edit_on_github: false
  version_selector: true
  announcement_bar: true
```

## Page Templates

### index.md Template

```markdown
# {PROJECT_NAME}

{BADGES}

> {TAGLINE}

## Features

<div class="grid cards" markdown>

- :rocket: **Quick Setup**

    Get started in 30 seconds with our streamlined installation.

- :sparkles: **Feature 2**

    Description of key feature.

- :zap: **Feature 3**

    Description of key feature.

- :shield: **Feature 4**

    Description of key feature.

</div>

## Quick Start

```bash
{INSTALL_COMMAND}
```

```bash
{FIRST_COMMAND}
```

## Documentation

- **[Quick Start](QUICK-START.md)** - Get running in 30 seconds
- **[Reference Card](REFCARD.md)** - Quick command reference
- **[Full Guide](guide/overview.md)** - Complete documentation

## Links

- [GitHub]({REPO_URL})
- [PyPI]({PYPI_URL})
- [Changelog](CHANGELOG.md)
```

### QUICK-START.md Template

```markdown
# Quick Start

Get up and running in 30 seconds.

## Install

=== "Homebrew (macOS)"

    ```bash
    brew install {HOMEBREW_TAP}/{PROJECT_NAME}
    ```

=== "pip"

    ```bash
    pip install {PYPI_NAME}
    ```

=== "uv"

    ```bash
    uv tool install {PYPI_NAME}
    ```

## Verify

```bash
{PROJECT_NAME} --version
```

## First Command

```bash
{FIRST_COMMAND}
```

Expected output:
```
{EXPECTED_OUTPUT}
```

## Next Steps

- [Full Guide](guide/overview.md) - Complete documentation
- [Reference Card](REFCARD.md) - Quick command reference
- [Configuration](reference/configuration.md) - Customize your setup
```

### REFCARD.md Template

```markdown
# Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│  {PROJECT_NAME} QUICK REFERENCE                             │
├─────────────────────────────────────────────────────────────┤
│  Version: {VERSION}                                         │
│  Docs: {DOCS_URL}                                           │
└─────────────────────────────────────────────────────────────┘
```

## Essential Commands

| Command | Description |
|---------|-------------|
| `{cmd1}` | {desc1} |
| `{cmd2}` | {desc2} |
| `{cmd3}` | {desc3} |

## Common Workflows

### Workflow 1: {Name}

```bash
# Step 1
{command}

# Step 2
{command}
```

### Workflow 2: {Name}

```bash
{command}
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `{setting1}` | `{default1}` | {desc1} |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| {issue1} | {solution1} |

## Links

- [Full Documentation](guide/overview.md)
- [GitHub Issues]({REPO_URL}/issues)
```

## Files Created

```
project/
├── mkdocs.yml                 # Site configuration
├── .craft/
│   └── site-design.yaml       # Design settings
├── docs/
│   ├── index.md               # Home page
│   ├── QUICK-START.md         # 30-second guide
│   ├── REFCARD.md             # Quick reference
│   ├── CHANGELOG.md           # (symlink or copy)
│   ├── getting-started/
│   │   ├── installation.md
│   │   └── configuration.md
│   ├── guide/
│   │   └── overview.md
│   ├── reference/
│   │   ├── commands.md
│   │   └── configuration.md
│   └── stylesheets/
│       └── extra.css          # Custom styles
├── .github/
│   └── workflows/
│       └── docs.yml           # Deployment workflow
└── requirements-docs.txt      # MkDocs dependencies
```

## Output

```
┌─────────────────────────────────────────────────────────────┐
│ ✅ DOCUMENTATION SITE CREATED                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Preset: data-wise                                           │
│ Framework: MkDocs Material                                  │
│                                                             │
│ Created:                                                    │
│   • mkdocs.yml (site configuration)                         │
│   • docs/ (9 pages)                                         │
│   • .github/workflows/docs.yml (deployment)                 │
│   • .craft/site-design.yaml (design settings)               │
│                                                             │
│ Quick commands:                                             │
│   Preview:  mkdocs serve                                    │
│   Build:    mkdocs build                                    │
│   Deploy:   mkdocs gh-deploy                                │
│                                                             │
│ Or use craft commands:                                      │
│   /craft:site:preview                                       │
│   /craft:site:build                                         │
│   /craft:site:deploy                                        │
│                                                             │
│ What's next?                                                │
│   → Edit docs/index.md with your content                    │
│   → Run mkdocs serve to preview                             │
│   → Push to GitHub to auto-deploy                           │
└─────────────────────────────────────────────────────────────┘
```

## Quick Mode (`--quick`)

Skips all prompts and uses detected/default values:

```bash
/craft:site:create --quick
```

Defaults:
- Preset: `data-wise`
- Name: from project config
- Tagline: from project config
- Structure: auto-detected based on project type

## Integration

This command is **Phase 1** of the site command redesign.

**Replaces:** `/craft:site:init` (which remains for basic init only)

**Related commands:**
- `/craft:site:update` - Update content from code changes
- `/craft:site:status` - Dashboard and health check
- `/craft:site:theme` - Quick theme changes
- `/craft:site:deploy` - Deploy to GitHub Pages

## ADHD-Friendly Features

1. **One command** - No need to remember multiple commands
2. **Smart defaults** - Everything auto-detected when possible
3. **Visual wizard** - Clear steps with progress indicator
4. **Immediate result** - Site builds and previews automatically
5. **Next steps** - Always shows what to do next
