# Documentation Commands

> **TL;DR** (30 seconds)
> - **What:** 17 smart documentation commands from generation to ADHD-friendly enhancement
> - **Why:** Automate docs updates, validation, and website optimization with one command
> - **How:** Use `/craft:docs:update` for full smart cycle or `/craft:docs:website` for ADHD enhancements
> - **Next:** Try `/craft:docs:sync` to check for stale docs in under 10 seconds

Smart documentation generation, validation, and enhancement - 17 commands.

## Super Commands

### /craft:docs:update

**Smart-Full cycle:** Detect → Generate all needed → Check → Changelog

```bash
/craft:docs:update                    # Smart detection → full execution
/craft:docs:update "sessions"         # Feature-specific full cycle
```

### /craft:docs:sync

**Detection only:** Classify changes, report stale docs, recommend actions

```bash
/craft:docs:sync                      # Quick: "3 stale, guide recommended"
```

### /craft:docs:check

**Validation:** Links + stale + nav + auto-fix (full by default)

```bash
/craft:docs:check                     # Full check cycle, auto-fixes
/craft:docs:check --report-only       # CI-safe mode (no modifications)
```

## NEW: ADHD-Friendly Website Enhancement

### /craft:docs:website

**Purpose:** One command to make any documentation site ADHD-friendly.

**Features:**
- ADHD scoring algorithm (0-100) across 5 categories
- 3-phase enhancement: Quick Wins, Structure, Polish
- Mermaid syntax error detection and fixing
- TL;DR box generation
- Time estimate addition
- ADHD Quick Start page creation

**Usage:**
```bash
/craft:docs:website                   # Full enhancement (all 3 phases)
/craft:docs:website --analyze         # Show ADHD score only
/craft:docs:website --phase 1         # Quick wins: TL;DR, mermaid fixes
/craft:docs:website --phase 2         # Structure: Visual workflows
/craft:docs:website --phase 3         # Polish: Mobile responsive
/craft:docs:website --dry-run         # Preview changes without writing
```

**ADHD Scoring Categories:**
- Visual Hierarchy (25%): TL;DR boxes, emojis, heading structure
- Time Estimates (20%): Tutorial duration info
- Workflow Diagrams (20%): Mermaid diagrams without errors
- Mobile Responsive (15%): Overflow fixes, touch targets
- Content Density (20%): Paragraph length, callout boxes

## Specialized Commands

### /craft:docs:guide

Feature guide + demo + refcard generator

```bash
/craft:docs:guide "authentication"
```

### /craft:docs:demo

VHS tape generator for GIF demos

```bash
/craft:docs:demo "quick-start"
```

### /craft:docs:mermaid

Mermaid diagram templates (6 types)

```bash
/craft:docs:mermaid flowchart
/craft:docs:mermaid sequence
```

### /craft:docs:api

OpenAPI/Swagger documentation

### /craft:docs:changelog

Auto-update CHANGELOG from commits

### /craft:docs:nav-update

Update mkdocs.yml navigation

### /craft:docs:prompt

Generate reusable maintenance prompts

## Integration Commands

### /craft:docs:site

Site-wide documentation updates (integrates with site commands)

```bash
/craft:docs:site sync    # Sync docs with site structure
```

## Internal Commands

### /craft:docs:claude-md

Update CLAUDE.md (called by other commands)
