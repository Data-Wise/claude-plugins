# Plugin Organization Architecture - Deep Analysis

**Generated:** 2026-01-09
**Mode:** Architecture (deep)
**Context:** claude-plugins mono-repo with 4 plugins (rforge, craft, workflow, statistical-research)

---

## 🎯 Executive Summary

**The Question:**
Should plugins remain in mono-repo (`claude-plugins`) or split into separate repositories? Should each plugin have its own website?

**The Answer (TL;DR):**
**Hybrid Mono-Repo with Plugin-Scoped Documentation** - Keep mono-repo for development velocity and shared infrastructure, but create clear plugin boundaries within the documentation site using MkDocs' multi-site or plugin-specific sections.

**Key Insight:**
Your pain points stem from documentation organization, not code organization. The mono-repo structure actually serves you well (frequent cross-plugin changes, shared tooling, coordinated testing).

---

## 📊 Current State Analysis

### What You Have Now

**Repository Structure:**
```
claude-plugins/                    # Mono-repo root
├── rforge/                        # Plugin 1
│   ├── package.json
│   ├── docs/ (if exists)
│   └── README.md
├── craft/                         # Plugin 2
├── workflow/                      # Plugin 3
├── statistical-research/          # Plugin 4
├── mkdocs.yml                     # SINGLE unified site config
├── docs/                          # Shared mono-repo docs
│   ├── MODE-SYSTEM.md            # Cross-plugin docs
│   ├── CICD.md
│   └── diagrams/
├── .github/workflows/             # 6 CI/CD workflows
│   ├── validate.yml              # Cross-plugin validation
│   ├── craft-ci.yml
│   ├── deploy-docs.yml
│   └── ...
└── README.md                      # Main landing page
```

**Documentation State:**
- **Site:** Single MkDocs site at github.com/Data-Wise/claude-plugins
- **Navigation:** Flat structure mixing mono-repo docs + plugin docs
- **Plugin Docs:** 28 markdown files scattered across plugins
- **Problem:** Hard to find plugin-specific information
- **Workflow:** 6 GitHub Actions workflows (some shared, some plugin-specific)

### Your Constraints (From Questions)

| Factor | Your Answer | Implication |
|--------|-------------|-------------|
| **Pain Point** | All of the above | Need holistic solution |
| **Cross-Plugin Changes** | Frequently (weekly+) | Mono-repo benefits strong |
| **Docs Vision** | Unified site with sections | Don't want separate sites |
| **Priority** | Balanced (DX/UX/Maint) | Can't sacrifice any dimension |
| **Docs Blocker** | Content gaps | Structure is secondary |
| **Code Sharing** | Mix of approaches | Need standardization |
| **Release Cadence** | Independent versions | Need per-plugin versioning |
| **Discoverability** | Important but secondary | Suite-first, plugins discoverable |

---

## 🏗️ Architecture Options

### Option A: Status Quo+ (Hybrid Mono-Repo) ⭐ RECOMMENDED

**Structure:**
```
claude-plugins/                    # Keep mono-repo
├── rforge/
│   ├── docs/                     # Plugin-specific docs
│   ├── mkdocs-plugin.yml         # Plugin config fragment
│   └── README.md
├── craft/
├── workflow/
├── statistical-research/
├── docs/
│   ├── mono-repo/                # Shared infrastructure docs
│   │   ├── MODE-SYSTEM.md
│   │   ├── CICD.md
│   │   └── PUBLISHING.md
│   └── plugins/                  # Plugin landing pages
│       ├── rforge.md
│       ├── craft.md
│       └── ...
├── mkdocs.yml                    # Unified site with clear sections
└── scripts/
    └── merge-plugin-docs.py      # Combine plugin configs
```

**Documentation Strategy:**
- **Single Site:** `data-wise.github.io/claude-plugins/`
- **Navigation:**
  ```yaml
  nav:
    - Home: index.md
    - Getting Started: ...
    - Plugins:
        - Overview: plugins/index.md
        - RForge:
            - Overview: plugins/rforge.md
            - Quick Start: rforge/docs/quickstart.md
            - Commands: rforge/docs/commands.md
            - Architecture: rforge/docs/architecture.md
        - Craft: ...
        - Workflow: ...
        - Statistical Research: ...
    - Shared Infrastructure:
        - Mode System: mono-repo/MODE-SYSTEM.md
        - CI/CD: mono-repo/CICD.md
  ```

**Pros:**
- ✅ Preserves mono-repo velocity (weekly cross-plugin changes)
- ✅ Single CI/CD pipeline, shared tooling
- ✅ Unified documentation site (your preference)
- ✅ Clear plugin boundaries via navigation sections
- ✅ Independent plugin versioning possible
- ✅ Moderate implementation effort (~4-8 hours)

**Cons:**
- ⚠️ Plugins less discoverable as standalone projects
- ⚠️ Can't showcase individual plugins on GitHub
- ⚠️ Shared infrastructure changes affect all plugins

**Best For:**
- Frequent cross-plugin development
- Unified suite branding
- Balanced DX/UX/Maintainability

---

### Option B: Multi-Repo with Mono-Site

**Structure:**
```
# Separate repos
github.com/Data-Wise/rforge
github.com/Data-Wise/craft
github.com/Data-Wise/workflow
github.com/Data-Wise/statistical-research

# Unified docs repo
github.com/Data-Wise/claude-plugins-docs
├── mkdocs.yml
├── docs/
│   ├── rforge/ (git submodule → rforge/docs/)
│   ├── craft/ (git submodule → craft/docs/)
│   └── ...
└── .github/workflows/
    └── deploy-docs.yml (pulls all submodules)
```

**Documentation Strategy:**
- **Single Site:** Unified docs repo aggregates plugin docs via git submodules
- **Plugin Sites:** Each plugin repo has minimal README, link to unified docs
- **Versioning:** Plugin docs versioned with plugin releases

**Pros:**
- ✅ Independent plugin development and releases
- ✅ Plugin discoverability on GitHub (separate repos)
- ✅ Still unified documentation site
- ✅ Clear ownership boundaries

**Cons:**
- ❌ High overhead for cross-plugin changes (weekly!)
- ❌ Git submodule complexity (notorious pain point)
- ❌ CI/CD duplication across repos
- ❌ Shared code management difficult
- ❌ High implementation effort (~20-30 hours)

**Best For:**
- Rare cross-plugin changes
- Strong plugin independence requirements
- Large team with separate plugin owners

**Not Recommended For You:** Conflicts with "Frequently (weekly+)" cross-plugin changes

---

### Option C: Mono-Repo with Per-Plugin Sites

**Structure:**
```
claude-plugins/                    # Keep mono-repo
├── rforge/
│   ├── mkdocs.yml                # Independent site config
│   ├── docs/
│   └── .github/workflows/
│       └── deploy-rforge-docs.yml
├── craft/
│   ├── mkdocs.yml
│   └── ...
├── workflow/
├── statistical-research/
└── docs/                          # Landing page only
    ├── mkdocs.yml                # Suite overview site
    └── index.md (links to plugin sites)
```

**Documentation Strategy:**
- **Multiple Sites:**
  - `data-wise.github.io/claude-plugins/` - Suite landing page
  - `data-wise.github.io/claude-plugins/rforge/` - RForge docs
  - `data-wise.github.io/claude-plugins/craft/` - Craft docs
  - etc.
- **Navigation:** Each plugin site independent

**Pros:**
- ✅ Plugin-specific documentation autonomy
- ✅ Clear separation of concerns
- ✅ Mono-repo development velocity preserved
- ✅ Each plugin can evolve docs independently

**Cons:**
- ⚠️ Shared documentation (MODE-SYSTEM, CICD) duplicated or unclear home
- ⚠️ Multiple MkDocs configs to maintain (4+ sites)
- ⚠️ Navigation fragmentation (users jump between sites)
- ⚠️ Moderate-high implementation effort (~12-16 hours)

**Best For:**
- Mature plugins with distinct audiences
- When plugins need different doc themes/styles
- Documentation autonomy > unified experience

**Trade-off:** You wanted "Unified site with plugin sections" - this contradicts that preference

---

### Option D: Mono-Repo with MkDocs Monorepo Plugin

**Structure:**
```
claude-plugins/
├── rforge/
│   └── mkdocs.yml                # Plugin config (merged)
├── craft/
│   └── mkdocs.yml
├── mkdocs.yml                     # Root config
└── plugins:
    - monorepo                     # mkdocs-monorepo-plugin
```

**Documentation Strategy:**
- **Single Site:** Uses mkdocs-monorepo-plugin to merge configs
- **Plugin Configs:** Each plugin has `mkdocs.yml` defining its section
- **Root Config:** Imports all plugin configs automatically

**Pros:**
- ✅ Best of both worlds: unified site + plugin autonomy
- ✅ Plugin docs live with plugin code
- ✅ Automatic navigation generation
- ✅ Mono-repo velocity preserved

**Cons:**
- ⚠️ Dependency on third-party plugin (mkdocs-monorepo)
- ⚠️ Learning curve for new tooling
- ⚠️ Possible build complexity
- ⚠️ Medium implementation effort (~8-12 hours)

**Best For:**
- Large mono-repos with many plugins
- When you want plugin doc autonomy within unified site
- Modern tooling approach

**Risk:** Third-party dependency stability

---

## 📐 Decision Matrix

| Criteria | Option A (Hybrid Mono) | Option B (Multi-Repo) | Option C (Per-Plugin Sites) | Option D (Monorepo Plugin) |
|----------|------------------------|----------------------|----------------------------|---------------------------|
| **Cross-Plugin Velocity** | ⭐⭐⭐⭐⭐ Excellent | ⭐ Poor | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Excellent |
| **Unified Docs Site** | ⭐⭐⭐⭐⭐ Yes | ⭐⭐⭐⭐ Yes (submodules) | ⭐⭐ No (fragmented) | ⭐⭐⭐⭐⭐ Yes |
| **Plugin Independence** | ⭐⭐⭐ Moderate | ⭐⭐⭐⭐⭐ Full | ⭐⭐⭐⭐ High | ⭐⭐⭐⭐ High |
| **Discoverability** | ⭐⭐ Suite-first | ⭐⭐⭐⭐⭐ Standalone repos | ⭐⭐⭐ Per-plugin sites | ⭐⭐⭐ Suite-first |
| **Implementation Effort** | ⭐⭐⭐⭐ Low (4-8h) | ⭐ Very High (20-30h) | ⭐⭐ High (12-16h) | ⭐⭐⭐ Medium (8-12h) |
| **Maintenance Burden** | ⭐⭐⭐⭐ Low | ⭐ High | ⭐⭐⭐ Moderate | ⭐⭐⭐ Moderate |
| **Aligns with Preferences** | ⭐⭐⭐⭐⭐ Perfect fit | ⭐⭐ Poor fit | ⭐⭐⭐ Partial fit | ⭐⭐⭐⭐ Good fit |

**Winner:** Option A (Hybrid Mono-Repo) or Option D (MkDocs Monorepo Plugin)

---

## 💡 Recommended Path: Option A (Hybrid Mono-Repo)

### Why This Works Best

**Aligns with Your Constraints:**
1. ✅ **Frequent cross-plugin changes** → Mono-repo velocity preserved
2. ✅ **Unified docs site preference** → Single MkDocs site with clear sections
3. ✅ **Independent versioning** → Each plugin has `package.json` with own version
4. ✅ **Balanced priorities** → DX (mono-repo), UX (unified site), Maintainability (low overhead)
5. ✅ **Content gaps blocker** → Focus on content, not restructuring
6. ✅ **Suite-first discovery** → Unified site showcases all plugins

**Solves Your Pain Points:**
| Pain Point | How Hybrid Mono-Repo Solves It |
|------------|-------------------------------|
| Hard to maintain independence | Clear plugin boundaries via docs/ structure + navigation sections |
| Documentation scattered | Reorganize into `docs/plugins/` and `docs/mono-repo/` |
| Release complexity | Keep independent `package.json` versions, coordinate releases in mono-repo |

---

## 🚀 Implementation Plan

### Phase 1: Reorganize Documentation Structure (2-3 hours)

**Goal:** Create clear plugin vs mono-repo doc boundaries

**Actions:**
1. Create new directory structure:
   ```bash
   mkdir -p docs/mono-repo docs/plugins
   ```

2. Move shared infrastructure docs:
   ```bash
   mv docs/MODE-SYSTEM.md docs/mono-repo/
   mv docs/CICD.md docs/mono-repo/
   mv docs/PUBLISHING.md docs/mono-repo/
   ```

3. Create plugin landing pages:
   ```bash
   # docs/plugins/rforge.md
   # docs/plugins/craft.md
   # docs/plugins/workflow.md
   # docs/plugins/statistical-research.md
   ```

4. Move plugin-specific docs to plugin directories:
   ```bash
   # Ensure each plugin has docs/ directory
   # Move plugin-specific content from root docs/
   ```

**Deliverable:** Clear separation of mono-repo vs plugin docs

---

### Phase 2: Update MkDocs Navigation (1-2 hours)

**Goal:** Create intuitive navigation with plugin sections

**Update `mkdocs.yml`:**
```yaml
nav:
  - Home: index.md
  - Getting Started:
      - Installation: installation.md
      - Quick Start: quick-start.md
  - Developer Guide: CLAUDE.md

  # PLUGIN SECTIONS
  - Plugins:
      - Overview: plugins/index.md
      - 'RForge - R Package Ecosystem':
          - Overview: plugins/rforge.md
          - Quick Start: rforge/docs/quickstart.md
          - Commands:
              - Status: rforge/commands/status.md
              - Analyze: rforge/commands/analyze.md
              - Cascade: rforge/commands/cascade.md
          - Architecture: rforge/docs/architecture.md
          - Development: rforge/docs/development.md

      - 'Craft - Workflow Orchestration':
          - Overview: plugins/craft.md
          - Commands: craft/docs/commands.md
          - Architecture: craft/docs/architecture.md

      - 'Workflow - ADHD-Friendly Tools':
          - Overview: plugins/workflow.md
          - Commands: workflow/docs/commands.md

      - 'Statistical Research':
          - Overview: plugins/statistical-research.md
          - Tools: statistical-research/docs/tools.md

  # SHARED INFRASTRUCTURE
  - Shared Infrastructure:
      - Mode System: mono-repo/MODE-SYSTEM.md
      - CI/CD: mono-repo/CICD.md
      - Publishing: mono-repo/PUBLISHING.md
      - Architecture:
          - Dependencies: diagrams/DEPENDENCIES.md
          - Ecosystem: diagrams/ECOSYSTEM.md
```

**Features:**
- Material theme's `navigation.tabs` will show top-level sections as tabs
- Plugin sections clearly grouped
- Shared infrastructure has dedicated section
- Each plugin expandable with subsections

**Deliverable:** Intuitive navigation that matches mental model

---

### Phase 3: Fill Content Gaps (4-6 hours)

**Goal:** Address "content gaps" blocker

**For Each Plugin:**

1. **Create Plugin Landing Page** (`docs/plugins/<plugin>.md`):
   ```markdown
   # <Plugin Name>

   ## Overview
   [2-3 sentence description]

   ## Key Features
   - Feature 1
   - Feature 2

   ## Quick Start
   [Installation + hello world]

   ## Documentation
   - [Quick Start](../<plugin>/docs/quickstart.md)
   - [Commands](../<plugin>/docs/commands.md)
   - [Architecture](../<plugin>/docs/architecture.md)

   ## Installation
   [npm/pip/manual install]

   ## Examples
   [Common use cases]
   ```

2. **Ensure Plugin Has:**
   - `docs/quickstart.md` - 5-minute getting started
   - `docs/commands.md` - Command reference
   - `docs/architecture.md` - How it works
   - `docs/development.md` - Contributing guide

3. **Create Cross-Links:**
   - Link plugin docs to shared infrastructure (e.g., Mode System)
   - Link shared docs to plugin examples

**Priority Order:**
1. RForge (most mature, already has docs)
2. Craft (active development)
3. Workflow (ADHD tools)
4. Statistical Research (research-specific)

**Deliverable:** Complete documentation for all plugins

---

### Phase 4: Automate Navigation Generation (Optional - 2 hours)

**Goal:** Reduce maintenance burden

**Create `scripts/update-mkdocs-nav.py`:**
```python
#!/usr/bin/env python3
"""
Auto-generate MkDocs navigation from plugin structure.

Scans each plugin's docs/ directory and builds navigation
hierarchy automatically.
"""

import os
import yaml
from pathlib import Path

PLUGINS = ['rforge', 'craft', 'workflow', 'statistical-research']

def scan_plugin_docs(plugin_name):
    """Scan plugin docs and return nav structure."""
    plugin_path = Path(plugin_name) / 'docs'
    if not plugin_path.exists():
        return None

    nav = []
    # ... scan *.md files, build hierarchy
    return nav

def generate_nav():
    """Generate full navigation structure."""
    nav = [
        {'Home': 'index.md'},
        {'Getting Started': [
            {'Installation': 'installation.md'},
            {'Quick Start': 'quick-start.md'}
        ]},
        {'Developer Guide': 'CLAUDE.md'}
    ]

    # Add plugin sections
    plugin_nav = {'Plugins': [{'Overview': 'plugins/index.md'}]}
    for plugin in PLUGINS:
        plugin_docs = scan_plugin_docs(plugin)
        if plugin_docs:
            plugin_nav['Plugins'].append(plugin_docs)

    nav.append(plugin_nav)

    # Add shared infrastructure
    nav.append({
        'Shared Infrastructure': [
            {'Mode System': 'mono-repo/MODE-SYSTEM.md'},
            {'CI/CD': 'mono-repo/CICD.md'}
        ]
    })

    return nav

if __name__ == '__main__':
    nav = generate_nav()

    # Update mkdocs.yml
    with open('mkdocs.yml', 'r') as f:
        config = yaml.safe_load(f)

    config['nav'] = nav

    with open('mkdocs.yml', 'w') as f:
        yaml.safe_dump(config, f, default_flow_style=False)

    print("✅ Updated mkdocs.yml navigation")
```

**Usage:**
```bash
python scripts/update-mkdocs-nav.py
```

**Benefit:** Add new plugin docs → run script → navigation updated automatically

**Deliverable:** Automated navigation maintenance

---

### Phase 5: Update CI/CD (1 hour)

**Goal:** Ensure docs deploy correctly

**Update `.github/workflows/deploy-docs.yml`:**
```yaml
name: Deploy Documentation

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - '*/docs/**'
      - 'mkdocs.yml'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install mkdocs-material
          pip install pymdown-extensions

      - name: Build docs
        run: mkdocs build --strict

      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force
```

**Validation:**
- Test build locally: `mkdocs build --strict`
- Check for broken links
- Verify all plugin sections render

**Deliverable:** Automated docs deployment

---

## ⏱️ Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 1: Reorganize Structure | 2-3 hours | Clear doc boundaries |
| Phase 2: Update Navigation | 1-2 hours | Intuitive MkDocs nav |
| Phase 3: Fill Content Gaps | 4-6 hours | Complete plugin docs |
| Phase 4: Automate (Optional) | 2 hours | Nav generation script |
| Phase 5: Update CI/CD | 1 hour | Automated deployment |
| **Total** | **10-14 hours** | **Production-ready unified site** |

**Quick Win Path (Skip Phase 4):** 8-12 hours

---

## 🎯 Quick Wins (< 30 min each)

Before full implementation, try these immediate improvements:

### 1. Create Plugin Landing Pages (20 min)

Create simple `docs/plugins/index.md`:
```markdown
# Plugins

The Claude Code plugin ecosystem provides specialized tools for different workflows.

## Available Plugins

### [RForge - R Package Ecosystem Management](rforge.md)
Comprehensive R package ecosystem orchestrator with dependency analysis and cascade updates.

**Use When:** Managing multiple R packages with complex dependencies

**Quick Start:** [RForge Documentation](../rforge/docs/quickstart.md)

---

### [Craft - Workflow Orchestration](craft.md)
ADHD-friendly workflow orchestration with mode-aware execution and subagent monitoring.

**Use When:** Building complex multi-step workflows

**Quick Start:** [Craft Documentation](../craft/docs/quickstart.md)

---

[Continue for workflow and statistical-research]
```

**Benefit:** Users can discover plugins immediately

---

### 2. Add Plugin Badges to Main README (15 min)

Update root `README.md`:
```markdown
# Claude Code Plugins

## Available Plugins

| Plugin | Version | Status | Docs |
|--------|---------|--------|------|
| [RForge](rforge/) | ![npm](https://img.shields.io/npm/v/rforge) | ✅ Production | [Docs](https://data-wise.github.io/claude-plugins/plugins/rforge/) |
| [Craft](craft/) | ![npm](https://img.shields.io/npm/v/craft) | 🚧 Beta | [Docs](https://data-wise.github.io/claude-plugins/plugins/craft/) |
| [Workflow](workflow/) | ![npm](https://img.shields.io/npm/v/workflow) | ✅ Production | [Docs](https://data-wise.github.io/claude-plugins/plugins/workflow/) |
| [Statistical Research](statistical-research/) | ![npm](https://img.shields.io/npm/v/statistical-research) | ✅ Production | [Docs](https://data-wise.github.io/claude-plugins/plugins/statistical-research/) |
```

**Benefit:** GitHub discoverability improved

---

### 3. Update `mkdocs.yml` with Plugin Section (25 min)

Just add a "Plugins" section to existing nav:
```yaml
nav:
  # ... existing sections

  - Plugins:
      - Overview: plugins/index.md
      - RForge: rforge/README.md
      - Craft: craft/README.md
      - Workflow: workflow/README.md
      - Statistical Research: statistical-research/README.md
```

**Benefit:** Immediate plugin discoverability in docs site

---

## 🔄 Alternative: Quick Hybrid (Option D) Implementation

If you want to try the mkdocs-monorepo-plugin approach:

### Setup (2 hours)

1. **Install plugin:**
   ```bash
   pip install mkdocs-monorepo-plugin
   ```

2. **Update root `mkdocs.yml`:**
   ```yaml
   plugins:
     - search
     - monorepo
   ```

3. **Create plugin configs:**
   ```yaml
   # rforge/mkdocs.yml
   site_name: RForge
   nav:
     - Overview: README.md
     - Quick Start: docs/quickstart.md
     - Commands: docs/commands.md
   ```

4. **Link plugin docs in root nav:**
   ```yaml
   # mkdocs.yml
   nav:
     - Plugins:
         - RForge: '!include ./rforge/mkdocs.yml'
         - Craft: '!include ./craft/mkdocs.yml'
   ```

**Benefit:** Plugin autonomy + unified site
**Risk:** Third-party dependency

---

## 📊 Comparison: Hybrid vs MkDocs Monorepo Plugin

| Aspect | Hybrid Mono-Repo (A) | MkDocs Monorepo (D) |
|--------|----------------------|---------------------|
| **Setup Time** | 4-8 hours | 8-12 hours |
| **Maintenance** | Manual nav updates | Auto-merged configs |
| **Plugin Autonomy** | Moderate (manual linking) | High (plugin owns config) |
| **Dependencies** | None | mkdocs-monorepo-plugin |
| **Complexity** | Low | Medium |
| **Recommended For** | Quick implementation | Scalable long-term |

**Recommendation:**
- Start with **Option A (Hybrid)** for quick wins
- Migrate to **Option D (Monorepo Plugin)** later if plugin count grows (5+)

---

## 🎓 Lessons from Phase 1 (RForge)

Your RForge plugin already has Phase 1 complete (95%). Use it as a template:

**What Works Well:**
- Clear `docs/` directory structure
- Comprehensive MODE-SYSTEM.md documentation
- Strong test coverage (292 tests)
- Production-ready release process

**Apply to Other Plugins:**
1. Create `<plugin>/docs/` directories
2. Copy RForge documentation structure
3. Adapt content to plugin specifics
4. Link to shared MODE-SYSTEM.md for common infrastructure

---

## 🚧 Known Challenges & Solutions

### Challenge 1: Shared Code Management

**Problem:** "Mix of approaches" for code sharing between plugins

**Solution:**
```
claude-plugins/
├── shared/                        # NEW: Shared utilities
│   ├── lib/
│   │   ├── mode-system.ts        # Shared mode system logic
│   │   ├── formatters.ts         # Shared formatters
│   │   └── testing.ts            # Shared test utilities
│   └── package.json              # @claude-plugins/shared
├── rforge/
│   └── package.json              # Depends: @claude-plugins/shared
├── craft/
│   └── package.json              # Depends: @claude-plugins/shared
```

**Implementation:**
- Extract shared code to `shared/` package
- Use npm workspaces for local linking
- Publish `@claude-plugins/shared` to npm (optional)

**Benefit:** DRY, single source of truth for shared logic

---

### Challenge 2: Independent Versioning in Mono-Repo

**Problem:** Each plugin needs independent version, but coordinated releases

**Solution:** Use Lerna or Changesets

**With Changesets:**
```bash
npm install @changesets/cli

# Developer workflow
npx changeset add               # Mark changes for plugin
npx changeset version           # Update versions based on changes
npx changeset publish           # Publish updated plugins
```

**Example:**
```
User updates rforge → adds changeset
User updates craft → adds changeset
Run 'changeset version' → rforge bumps to 1.2.0, craft to 2.1.0
Run 'changeset publish' → publishes both with correct versions
```

**Benefit:** Independent versions, coordinated releases

---

### Challenge 3: Cross-Plugin Breaking Changes

**Problem:** Shared infrastructure change breaks multiple plugins

**Solution:** Feature flags + deprecation warnings

**Example:**
```typescript
// shared/lib/mode-system.ts (v2.0.0)
export function getMode(options: ModeOptions) {
  if (options.deprecatedField) {
    console.warn(
      'DEPRECATION: deprecatedField will be removed in v3.0.0. Use newField instead.'
    );
  }

  // Support both old and new
  return options.newField || options.deprecatedField;
}
```

**Benefit:** Graceful migration path for plugins

---

## 🏆 Success Criteria

How to know if implementation succeeded:

### User Experience (UX)
- [ ] User can find plugin documentation within 30 seconds
- [ ] Plugin landing pages clearly explain purpose and use cases
- [ ] Navigation structure is intuitive (no confusion)
- [ ] Plugin-to-plugin cross-links work correctly

### Developer Experience (DX)
- [ ] Adding new plugin docs takes < 1 hour
- [ ] Cross-plugin changes remain fast (weekly cadence maintained)
- [ ] Documentation builds without errors (`mkdocs build --strict`)
- [ ] CI/CD deploys automatically on merge

### Maintainability
- [ ] Navigation updates are automated (or trivial)
- [ ] Shared code has single source of truth
- [ ] Independent plugin versioning works smoothly
- [ ] Breaking changes have clear migration path

### Discoverability
- [ ] GitHub README clearly lists all plugins
- [ ] Each plugin has status badge (production/beta/alpha)
- [ ] Documentation site appears in Google search for plugin names
- [ ] Plugin landing pages include installation instructions

---

## 📚 Resources & References

**MkDocs Documentation:**
- [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
- [Navigation Tabs](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#navigation-tabs)
- [MkDocs Monorepo Plugin](https://backstage.github.io/mkdocs-monorepo-plugin/)

**Mono-Repo Tools:**
- [Lerna](https://lerna.js.org/) - Multi-package repository management
- [Changesets](https://github.com/changesets/changesets) - Version management
- [npm Workspaces](https://docs.npmjs.com/cli/v7/using-npm/workspaces)

**Inspiration:**
- [Turborepo Docs](https://turbo.build/repo/docs) - Mono-repo with clear plugin sections
- [Nx Documentation](https://nx.dev/) - Multi-package documentation structure
- [Storybook Docs](https://storybook.js.org/docs) - Unified docs for multiple tools

---

## 🔮 Future Considerations

### If Plugin Count Grows (5+ plugins)

**Consider:**
1. **Plugin Registry:** Automated plugin discovery and listing
2. **Plugin Templates:** Scaffolding tool for new plugins
3. **Documentation Linting:** Enforce documentation standards
4. **Multi-Version Docs:** Version each plugin's docs separately

**Tool:** mkdocs-monorepo-plugin becomes more valuable at scale

---

### If Audience Diversifies

**Scenario:** Different plugins target different user types

**Solution:** Audience-specific landing pages
```
docs/
├── for-r-developers/             # RForge, Statistical Research
├── for-workflows/                # Craft, Workflow
└── for-beginners/                # Getting Started guides
```

---

### If Plugins Need Separate Branding

**Scenario:** One plugin becomes flagship product

**Solution:** Hybrid approach
- Flagship plugin gets separate repo + site
- Other plugins remain in mono-repo
- Suite site links to flagship site

**Example:**
- RForge → `github.com/Data-Wise/rforge` (standalone)
- Others → `github.com/Data-Wise/claude-plugins` (mono-repo)

---

## 🎯 Recommended Immediate Action

**This Week (4-6 hours):**

1. **Create Plugin Landing Pages** (1 hour)
   - `docs/plugins/index.md`
   - `docs/plugins/rforge.md`
   - `docs/plugins/craft.md`
   - `docs/plugins/workflow.md`
   - `docs/plugins/statistical-research.md`

2. **Update MkDocs Navigation** (1 hour)
   - Add "Plugins" section
   - Add "Shared Infrastructure" section
   - Link plugin READMEs

3. **Reorganize Root Docs** (1 hour)
   - Move MODE-SYSTEM.md to `docs/mono-repo/`
   - Move CICD.md to `docs/mono-repo/`
   - Update internal links

4. **Test Documentation Build** (30 min)
   - Run `mkdocs build --strict`
   - Fix broken links
   - Test navigation

5. **Deploy and Validate** (30 min)
   - Push changes
   - Verify GitHub Pages deployment
   - Test user flow (find plugin → read docs)

**Next Week (4-6 hours):**

6. **Fill RForge Content Gaps** (2 hours)
   - Expand RForge quickstart
   - Add architecture diagrams
   - Create command reference

7. **Template for Other Plugins** (2 hours)
   - Copy RForge docs structure
   - Adapt for Craft
   - Adapt for Workflow

8. **Automation** (Optional - 2 hours)
   - Create nav generation script
   - Update CI/CD workflow

---

## ✅ Summary

**The Answer:**
**Keep Mono-Repo, Improve Documentation Structure**

**Why:**
- Your frequent cross-plugin changes (weekly+) make mono-repo essential
- You prefer unified documentation site - just needs better organization
- Independent versioning is possible within mono-repo (using Changesets)
- Problem is documentation structure, not code organization

**Implementation:**
1. Reorganize docs into `docs/plugins/` and `docs/mono-repo/`
2. Update MkDocs navigation with clear plugin sections
3. Create plugin landing pages (< 1 hour each)
4. Fill content gaps systematically (RForge first, template for others)
5. Automate navigation generation (optional)

**Timeline:** 10-14 hours for complete implementation

**Quick Wins:** Can see improvements in 4-6 hours (landing pages + navigation)

**Long-Term:** If plugin count grows (5+), consider mkdocs-monorepo-plugin for better scalability

---

**Generated:** 2026-01-09
**Duration:** Deep analysis (8 expert questions)
**Next Step:** Create SPEC.md for implementation
