# Site Management Commands

> **TL;DR** (30 seconds)
> - **What:** 15 commands for complete documentation site lifecycle (create, update, deploy, theme)
> - **Why:** Zero-to-deployed in minutes with 8 ADHD-friendly presets and smart automation
> - **How:** `/craft:site:create --preset adhd-focus` for instant site, `/craft:site:status` for health check
> - **Next:** Explore the 8 design presets below or run `/craft:site:update` for content sync

Full documentation site wizard with 8 ADHD-friendly design presets - 15 commands.

## /craft:site:create

**Purpose:** Zero to deployed documentation site in minutes.

**Features:**
- 8 ADHD-friendly design presets
- Auto project detection
- Smart navigation structure
- GitHub Pages deployment setup

**Usage:**
```bash
/craft:site:create                      # Interactive wizard
/craft:site:create --preset data-wise   # Use preset directly
/craft:site:create --quick              # Minimal prompts (auto-detect)
```

**Presets:**
- `data-wise` - DT's standard (blue/orange)
- `minimal` - Clean and simple
- `open-source` - Community-friendly
- `corporate` - Professional
- `adhd-focus` - Calm forest green
- `adhd-calm` - Warm earth tones
- `adhd-dark` - Dark-first
- `adhd-light` - Warm light

## Navigation & Audit Commands

### /craft:site:nav

Navigation reorganization (ADHD-friendly, max 7 sections)

```bash
/craft:site:nav
```

### /craft:site:audit

Content inventory & audit (outdated, duplicates, gaps)

```bash
/craft:site:audit
```

### /craft:site:consolidate

Merge duplicate/overlapping documentation files

```bash
/craft:site:consolidate
```

## Management Commands

### /craft:site:status

Dashboard and health check

### /craft:site:update

Update site content from code changes

### /craft:site:theme

Quick theme changes (colors, presets, fonts)

### /craft:site:build

Build site

### /craft:site:preview

Preview locally

### /craft:site:deploy

Deploy to GitHub Pages

### /craft:site:init

Basic initialization (use `create` for full wizard)

### /craft:site:add

Add new pages to existing site with proper navigation integration

```bash
/craft:site:add guide/authentication  # Add new page to navigation
```

### /craft:site:check

Validate site configuration, broken links, and deployment readiness

```bash
/craft:site:check           # Full validation
/craft:site:check --links   # Links only
```

## Framework Support

### /craft:site:docs/frameworks

Show supported documentation frameworks and their features

```bash
/craft:site:docs/frameworks
```

**Supported:**
- MkDocs Material (default)
- Docusaurus
- VuePress
- Sphinx
