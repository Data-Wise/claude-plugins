# Craft Site Commands - Complete Redesign Proposal

**Generated:** 2025-12-27
**Focus:** Comprehensive site management with consistent UI/design standards
**Current:** 6 commands → Proposed: 10-12 commands

---

## Executive Summary

The current `/craft:site:*` commands handle basic site lifecycle but lack:
- **Design consistency** - No standards for site UI, menus, branding
- **Content updates** - No way to refresh site content from code
- **Status visibility** - No dashboard or health checks
- **Creation workflow** - Init is basic, no templates or presets

**Goal:** Make site commands the complete solution for documentation websites with consistent, professional design standards.

---

## Current State

### Existing Commands (6)

| Command | Purpose | Gaps |
|---------|---------|------|
| `site:init` | Create mkdocs.yml + structure | No templates, no starter content |
| `site:build` | Build static site | No caching, no incremental |
| `site:preview` | Local server | No hot reload config |
| `site:check` | Validate links/structure | Overlaps with docs:validate |
| `site:deploy` | GitHub Pages | No other targets |
| `site:frameworks` | Compare options | Informational only |

### Missing Capabilities

- [ ] Full creation wizard with design choices
- [ ] Design system / theme management
- [ ] Content updates from code changes
- [ ] Site status dashboard
- [ ] Page/section addition with nav sync
- [ ] Multi-target deployment (Netlify, Vercel, etc.)

---

## Design Standards System

### The Problem

Every project's documentation site looks different. No consistent:
- Color palette
- Navigation structure
- Page layouts
- Component usage
- Branding elements

### The Solution: Design Presets

```yaml
# .craft/site-design.yaml
preset: "data-wise"  # or "minimal", "corporate", "open-source"

branding:
  logo: "assets/logo.png"
  favicon: "assets/favicon.ico"
  name: "AITerm"
  tagline: "AI Terminal Optimizer"

colors:
  primary: "#1a73e8"
  accent: "#ff6b35"
  scheme: "auto"  # light/dark/auto

navigation:
  style: "tabs"  # tabs, sidebar, hybrid
  sections:
    - name: "Getting Started"
      icon: "rocket"
      priority: 1
    - name: "Guide"
      icon: "book"
      priority: 2
    - name: "Reference"
      icon: "code"
      priority: 3

pages:
  required:
    - index.md
    - QUICK-START.md
    - REFCARD.md
  optional:
    - CHANGELOG.md (linked from index)
    - CONTRIBUTING.md

components:
  search: true
  dark_mode: true
  code_copy: true
  edit_on_github: true
  version_selector: false
```

### Design Presets Available

| Preset | Description | Best For |
|--------|-------------|----------|
| `minimal` | Clean, simple, fast | Small projects |
| `data-wise` | DT's standard (Material + custom) | All DT projects |
| `open-source` | Community-friendly, badges | Public repos |
| `corporate` | Professional, formal | Enterprise |
| `academic` | Citation-friendly, formal | Research |

---

## Proposed Command Structure

### Plan A: Comprehensive (12 commands)

```
/craft:site:create    # NEW - Full wizard with design choices
/craft:site:design    # NEW - Manage design/theme settings
/craft:site:update    # NEW - Update content from code changes
/craft:site:status    # NEW - Dashboard and health check
/craft:site:add       # NEW - Add pages/sections with nav sync
/craft:site:init      # KEEP - Basic init (create calls this)
/craft:site:build     # KEEP - Build static site
/craft:site:preview   # KEEP - Local preview
/craft:site:check     # ENHANCED - Comprehensive validation
/craft:site:deploy    # ENHANCED - Multi-target deployment
/craft:site:theme     # NEW - Quick theme changes
/craft:site:migrate   # NEW - Framework migration (future)
```

### Plan B: Focused (9 commands)

```
/craft:site:create    # Full wizard (combines init + design)
/craft:site:update    # Update content + validate
/craft:site:status    # Dashboard
/craft:site:add       # Add pages
/craft:site:build     # Build
/craft:site:preview   # Preview
/craft:site:check     # Validate
/craft:site:deploy    # Deploy
/craft:site:theme     # Theme changes
```

### Plan C: Minimal (7 commands)

```
/craft:site:create    # Full wizard
/craft:site:update    # Update + validate
/craft:site:build     # Build
/craft:site:preview   # Preview
/craft:site:deploy    # Deploy
/craft:site:theme     # Theme
/craft:site:status    # Status
```

---

## Command Specifications

### 1. `/craft:site:create` - Full Creation Wizard ⭐

**Purpose:** One command to go from zero to deployed site with consistent design.

**Usage:**
```bash
/craft:site:create                      # Interactive wizard
/craft:site:create --preset data-wise   # Use preset
/craft:site:create --quick              # Minimal prompts
/craft:site:create --from template      # From template repo
```

**Wizard Flow:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:create                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 🚀 DOCUMENTATION SITE WIZARD                                │
│                                                             │
│ Step 1/5: Project Detection                                 │
│   Detected: Python Package (aiterm-dev)                     │
│   Framework: MkDocs with Material theme                     │
│                                                             │
│ Step 2/5: Design Preset                                     │
│   [1] data-wise - DT's standard (Recommended)               │
│   [2] minimal - Clean and simple                            │
│   [3] open-source - Community-friendly                      │
│   [4] custom - Configure manually                           │
│                                                             │
│ Step 3/5: Branding                                          │
│   Site name: AITerm                                         │
│   Tagline: AI Terminal Optimizer                            │
│   Logo: (none, will use text)                               │
│                                                             │
│ Step 4/5: Navigation Structure                              │
│   [x] Getting Started (Quick Start, Installation)           │
│   [x] User Guide (Features, Workflows)                      │
│   [x] Reference (Commands, API, Config)                     │
│   [ ] API Documentation (auto-generated)                    │
│   [ ] Tutorials (step-by-step guides)                       │
│                                                             │
│ Step 5/5: Deployment                                        │
│   Target: GitHub Pages                                      │
│   URL: https://data-wise.github.io/aiterm/                  │
│   Auto-deploy on push: Yes                                  │
│                                                             │
│ Creating site...                                            │
└─────────────────────────────────────────────────────────────┘
```

**Creates:**

```
project/
├── mkdocs.yml                    # Full config with design settings
├── docs/
│   ├── index.md                  # Home with badges, features
│   ├── QUICK-START.md            # 30-second start guide
│   ├── REFCARD.md                # Quick reference card
│   ├── getting-started/
│   │   ├── installation.md       # Install instructions
│   │   └── first-steps.md        # Getting started guide
│   ├── guide/
│   │   └── overview.md           # Feature overview
│   ├── reference/
│   │   ├── commands.md           # CLI reference
│   │   └── configuration.md      # Config reference
│   └── assets/
│       ├── stylesheets/
│       │   └── custom.css        # Custom styles
│       └── images/               # Image assets
├── .craft/
│   └── site-design.yaml          # Design configuration
└── .github/
    └── workflows/
        └── docs.yml              # Auto-deploy workflow
```

---

### 2. `/craft:site:design` - Design System Management ⭐

**Purpose:** Manage design tokens, theme, branding consistently.

**Usage:**
```bash
/craft:site:design                      # Show current design
/craft:site:design --preset data-wise   # Apply preset
/craft:site:design --colors             # Color configuration
/craft:site:design --nav                # Navigation structure
/craft:site:design --export             # Export design config
```

**Interactive Mode:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:design                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 🎨 SITE DESIGN CONFIGURATION                                │
│                                                             │
│ Current Preset: data-wise                                   │
│                                                             │
│ Colors:                                                     │
│   Primary:  #1a73e8 ████                                    │
│   Accent:   #ff6b35 ████                                    │
│   Scheme:   auto (light/dark)                               │
│                                                             │
│ Typography:                                                 │
│   Font: Roboto (system fallback)                            │
│   Code: JetBrains Mono                                      │
│                                                             │
│ Navigation:                                                 │
│   Style: Tabs + Sidebar                                     │
│   Sections: 4 (Getting Started, Guide, Reference, API)      │
│                                                             │
│ Components:                                                 │
│   ✓ Search                                                  │
│   ✓ Dark mode toggle                                        │
│   ✓ Code copy button                                        │
│   ✓ Edit on GitHub                                          │
│   ○ Version selector                                        │
│                                                             │
│ Actions:                                                    │
│   [1] Change colors                                         │
│   [2] Update navigation                                     │
│   [3] Toggle components                                     │
│   [4] Apply different preset                                │
│   [5] Export configuration                                  │
└─────────────────────────────────────────────────────────────┘
```

**Design Standards Enforced:**

| Element | Standard | Rationale |
|---------|----------|-----------|
| Logo position | Top-left | Consistency |
| Search | Top-right | User expectation |
| Dark mode | Header toggle | Accessibility |
| Nav tabs | Max 5-6 items | Cognitive load |
| Sidebar | Collapsible sections | ADHD-friendly |
| Code blocks | Copy button | Developer UX |
| Links | Open same tab (internal) | Navigation flow |

---

### 3. `/craft:site:update` - Content Updater ⭐

**Purpose:** Update site content based on code changes (mirrors docs:update for site).

**Usage:**
```bash
/craft:site:update                      # Smart update
/craft:site:update --full               # Full refresh
/craft:site:update --badges             # Just badges
/craft:site:update --nav                # Just navigation
/craft:site:update --content            # Just content pages
```

**What It Updates:**

| Content | Smart Mode | Full Mode | Trigger |
|---------|------------|-----------|---------|
| Version badges | ✓ | ✓ | Version changed |
| mkdocs.yml nav | ✓ | ✓ | Orphan files exist |
| index.md features | ✓ | ✓ | New features |
| REFCARD.md | ✓ | ✓ | Commands changed |
| API reference | ○ | ✓ | Code changed |
| requirements.txt | ○ | ✓ | Deps outdated |
| Custom CSS | ○ | ✓ | Design changed |

**Output:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:update                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Analyzing site content...                                   │
│                                                             │
│ Changes detected:                                           │
│   • Version: 0.3.6 → 0.3.7 (update badges)                  │
│   • 2 orphan files (add to nav)                             │
│   • 3 new CLI commands (update reference)                   │
│                                                             │
│ Updates applied:                                            │
│   ✓ docs/index.md - Updated version badge                   │
│   ✓ mkdocs.yml - Added 2 files to nav                       │
│   ✓ docs/reference/commands.md - Added 3 commands           │
│   ✓ docs/REFCARD.md - Synced with commands                  │
│                                                             │
│ Validation:                                                 │
│   ✓ mkdocs build --strict passed                            │
│   ✓ All links valid                                         │
│                                                             │
│ ✅ Site updated successfully!                               │
│                                                             │
│ Next: /craft:site:preview or /craft:site:deploy             │
└─────────────────────────────────────────────────────────────┘
```

---

### 4. `/craft:site:status` - Dashboard

**Purpose:** Quick overview of site health and status.

**Usage:**
```bash
/craft:site:status                      # Full dashboard
/craft:site:status --json               # JSON output
```

**Output:**

```
┌─────────────────────────────────────────────────────────────┐
│ 📊 SITE STATUS                                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Framework: MkDocs 1.6.0 (Material 9.5.3)                    │
│ Design: data-wise preset                                    │
│                                                             │
│ Content:                                                    │
│   • 26 pages (32,322 lines)                                 │
│   • 45 code examples                                        │
│   • 12 images                                               │
│                                                             │
│ Health:                                                     │
│   ✓ Build: Clean (2.1s)                                     │
│   ✓ Links: 156 valid, 0 broken                              │
│   ✓ Nav: Complete (0 orphans)                               │
│   ⚠ Freshness: 3 pages > 30 days old                        │
│                                                             │
│ Deployment:                                                 │
│   • URL: https://data-wise.github.io/aiterm/                │
│   • Last deploy: 2 hours ago                                │
│   • Auto-deploy: Enabled (on push to main)                  │
│                                                             │
│ Suggestions:                                                │
│   → Review stale pages: guide/overview.md (45 days)         │
└─────────────────────────────────────────────────────────────┘
```

---

### 5. `/craft:site:add` - Add Pages/Sections

**Purpose:** Add new pages with automatic nav sync.

**Usage:**
```bash
/craft:site:add guide "Session Management"    # Add to Guide
/craft:site:add reference "CLI Commands"      # Add to Reference
/craft:site:add tutorial "First Steps"        # Add tutorial
/craft:site:add section "API"                 # Add new section
```

**Output:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:add guide "Session Management"                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Creating new guide page...                                  │
│                                                             │
│ Created: docs/guide/session-management.md                   │
│                                                             │
│ Template applied:                                           │
│   • Title: Session Management                               │
│   • Section: Guide                                          │
│   • Template: guide-page                                    │
│                                                             │
│ Navigation updated:                                         │
│   Guide:                                                    │
│     - Overview: guide/overview.md                           │
│     - Session Management: guide/session-management.md  ← NEW│
│     - Workflows: guide/workflows.md                         │
│                                                             │
│ ✅ Page added and nav synced!                               │
│                                                             │
│ Next: Edit docs/guide/session-management.md                 │
└─────────────────────────────────────────────────────────────┘
```

---

### 6. `/craft:site:theme` - Quick Theme Changes

**Purpose:** Quick theme adjustments without full design config.

**Usage:**
```bash
/craft:site:theme                           # Show current
/craft:site:theme --primary "#1a73e8"       # Change primary color
/craft:site:theme --palette ocean           # Apply color palette
/craft:site:theme --dark                    # Force dark mode
/craft:site:theme --font "Inter"            # Change font
```

---

## Page Templates

### Standard Page Types

Each page type has a template with consistent structure:

#### 1. Index Page Template

```markdown
# {PROJECT_NAME}

{BADGES}

{TAGLINE}

## Features

{FEATURE_GRID}

## Quick Start

```bash
{INSTALL_COMMAND}
```

## Documentation

- [Quick Start](QUICK-START.md) - Get started in 30 seconds
- [Reference Card](REFCARD.md) - Quick command reference
- [Full Guide](guide/overview.md) - Complete documentation

## Links

- [GitHub]({REPO_URL})
- [PyPI]({PYPI_URL})
- [Changelog](CHANGELOG.md)
```

#### 2. QUICK-START Template

```markdown
# Quick Start

Get up and running in 30 seconds.

## Install

{INSTALL_OPTIONS}

## Verify

```bash
{VERIFY_COMMAND}
```

## First Command

```bash
{FIRST_COMMAND}
```

## Next Steps

- [Full Guide](guide/overview.md)
- [Reference Card](REFCARD.md)
```

#### 3. REFCARD Template

```markdown
# Quick Reference

{ASCII_BOX_HEADER}

## Essential Commands

| Command | Description |
|---------|-------------|
{COMMAND_TABLE}

## Common Workflows

{WORKFLOW_EXAMPLES}

## Troubleshooting

{TROUBLESHOOTING_TABLE}
```

#### 4. Guide Page Template

```markdown
# {TITLE}

{OVERVIEW_PARAGRAPH}

## Prerequisites

{PREREQUISITES}

## {MAIN_SECTION}

{CONTENT}

## Examples

{EXAMPLES}

## Related

- [Link 1](path1.md)
- [Link 2](path2.md)
```

---

## Navigation Standards

### Standard Structure

```yaml
nav:
  - Home: index.md
  - Quick Start: QUICK-START.md
  - Reference Card: REFCARD.md

  - Getting Started:
    - Installation: getting-started/installation.md
    - Configuration: getting-started/configuration.md
    - First Steps: getting-started/first-steps.md

  - Guide:
    - Overview: guide/overview.md
    - {FEATURE_PAGES}

  - Reference:
    - Commands: reference/commands.md
    - Configuration: reference/configuration.md
    - API: reference/api.md

  - Troubleshooting: troubleshooting.md
```

### Navigation Rules

| Rule | Standard |
|------|----------|
| Max top-level items | 5-6 |
| Max depth | 3 levels |
| Section ordering | Getting Started → Guide → Reference |
| Required pages | index, QUICK-START, REFCARD |
| Capitalization | Title Case for sections |

---

## Implementation Plan

### Phase 1: Core Commands (2-3 hours)

| Command | Priority | Effort |
|---------|----------|--------|
| `/craft:site:create` | P1 | 1.5 hr |
| `/craft:site:update` | P1 | 45 min |
| `/craft:site:status` | P1 | 30 min |

### Phase 2: Design System (2 hours)

| Command | Priority | Effort |
|---------|----------|--------|
| `/craft:site:design` | P2 | 1 hr |
| `/craft:site:theme` | P2 | 30 min |
| Design presets | P2 | 30 min |

### Phase 3: Content Management (1.5 hours)

| Command | Priority | Effort |
|---------|----------|--------|
| `/craft:site:add` | P2 | 45 min |
| Page templates | P2 | 45 min |

### Phase 4: Enhancements (Future)

| Command | Priority | Effort |
|---------|----------|--------|
| `/craft:site:migrate` | P3 | 2 hr |
| Multi-target deploy | P3 | 1 hr |
| Version selector | P3 | 1 hr |

---

## Decision Matrix

### Plan Comparison

| Feature | Plan A (Full) | Plan B (Focused) | Plan C (Minimal) |
|---------|---------------|------------------|------------------|
| Commands | 12 | 9 | 7 |
| Design system | Full | Basic | None |
| Page templates | Yes | Yes | No |
| Creation wizard | Full | Quick | Basic |
| Status dashboard | Yes | Yes | Yes |
| Effort | 8 hrs | 5 hrs | 3 hrs |

### Recommendation

**Plan B (Focused)** is recommended:
- Covers essential functionality
- Includes design system basics
- Reasonable effort (5 hours)
- Can expand to Plan A later

---

## Files to Create

```
craft/commands/site/
├── create.md          # Full creation wizard
├── design.md          # Design system management
├── update.md          # Content updater
├── status.md          # Dashboard
├── add.md             # Add pages
├── theme.md           # Quick theme changes
├── build.md           # (existing, enhance)
├── preview.md         # (existing)
├── check.md           # (existing, enhance)
└── deploy.md          # (existing, enhance)

craft/templates/site/
├── presets/
│   ├── data-wise.yaml
│   ├── minimal.yaml
│   ├── open-source.yaml
│   └── corporate.yaml
├── pages/
│   ├── index.md
│   ├── quick-start.md
│   ├── refcard.md
│   ├── guide-page.md
│   └── reference-page.md
└── mkdocs/
    ├── mkdocs-material.yml
    └── custom.css
```

---

## Summary

| Decision | Options |
|----------|---------|
| **Plan** | A (Full 12), B (Focused 9), C (Minimal 7) |
| **Priority** | create → update → status → design → add |
| **Design System** | Presets + customization |
| **Templates** | 4 page types, 4 presets |
| **Effort** | 3-8 hours depending on plan |

---

**Ready for Review**

Which plan would you like to implement?
- **A** - Full (12 commands, complete design system)
- **B** - Focused (9 commands, essential design) ⭐ Recommended
- **C** - Minimal (7 commands, basic functionality)

