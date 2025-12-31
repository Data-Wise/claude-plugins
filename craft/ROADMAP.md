# Craft Plugin Roadmap

## Current Version: 1.8.0-dev

**Next Priority:** v1.8.0 - Homebrew Automation 🎯

---

## v1.5.0 - Distribution Commands ✅ RELEASED

### Distribution Commands (All Complete)

#### `/craft:dist:homebrew` - Homebrew Tap Management ✅
- Detect project type (Python, Node, Go, Rust)
- Generate formula file with dependencies
- Calculate SHA256 for release tarballs
- Update existing formula for new versions
- Push to homebrew-tap repository

#### `/craft:dist:curl-install` - Direct GitHub Installation ✅
- Create `install.sh` for direct GitHub downloads
- Support multiple installation methods (binary, source)
- Include version detection and updates
- Add to README installation section

#### Skills Added ✅
- `distribution-strategist` - Distribution channel recommendations
- `homebrew-formula-expert` - Formula best practices

**Stats:** 53 commands, 13 skills, 7 agents

**Dogfooding:** Tested on aiterm v0.3.5
- Generated and validated Homebrew formula
- Created install.sh with smart auto-detection
- Updated README with curl install instructions

---

## v1.4.0 - Orchestrator v2.1 Enhancement ✅ RELEASED

### Orchestrator v2.1 Features (All Complete)

#### Phase 1: Quick Wins ✅

**1. Real Context Tracking** ✅
- Improved heuristics for context usage estimation
- Watch for Claude Code system warnings about context
- Smarter compression triggers based on exchange count + content size
- Per-agent context budget tracking

**2. Mode Integration** ✅
- Orchestrator respects craft mode system
- `default` mode: 2 agents, 70% compression threshold
- `debug` mode: 1 agent (sequential), verbose output, 90% threshold
- `optimize` mode: 4 agents max, aggressive 60% compression
- `release` mode: 4 agents, full reports, 85% threshold

**Usage:**
```bash
/craft:orchestrate "add auth" optimize    # Fast parallel
/craft:orchestrate "prep release" release # Thorough
```

#### Phase 2: State Persistence ✅

**3. Session State File** ✅
- Persist orchestrator state to `.claude/orchestrator-session.json`
- Enable session recovery after disconnects
- Track completed work, active agents, decisions made

**New Commands:**
```bash
/craft:orchestrate continue      # Resume from saved state
/craft:orchestrate save          # Force state save
/craft:orchestrate history       # Show past sessions
```

#### Phase 3: ADHD Enhancements ✅

**4. Timeline View** ✅
- Visual Gantt-style timeline of agent execution
- ETA countdown with progress bars
- Reduces anxiety about "what's happening"

```
TIME     0    1m    2m    3m    4m
─────────┼─────┼─────┼─────┼─────┤
arch-1   ██████░░░░░░░░░░░░░░░░░░ ✅
code-1        ░░░░████████████░░░ 🟡
─────────┼─────┼─────┼─────┼─────┤
                         NOW ▲
```

### Dogfooding Phase (Manual Testing) ✅ COMPLETE

Live validation tests completed on aiterm project:

- [x] **Live orchestrator test** - Added `ait hello` command via `/craft:orchestrate` default mode
- [x] **Stress test** - 4 parallel agents in `optimize` mode added `ait info` + enhanced `--version`
- [x] **Session persistence test** - Added `ait goodbye` via save/resume workflow

**Results:** All tests passed, features shipped in aiterm v0.3.5

---

## v1.6.0 - Docs Workflow Commands 🚧 IN PROGRESS

**Theme:** ADHD-friendly documentation workflows

### New Workflow Commands

| Command | Purpose |
|---------|---------|
| `/craft:docs:update [full]` | Smart update all docs (or force full update) |
| `/craft:docs:feature [name]` | Comprehensive update after adding a feature |
| `/craft:docs:done [summary]` | End-of-session doc updates |
| `/craft:docs:site [--deploy]` | Website-focused updates |

### What `/craft:docs:update full` Updates

- CLI Help epilogs (new/changed commands)
- `docs/reference/commands.md`
- `docs/REFCARD.md` + domain-specific refcards
- `README.md` (features, badges)
- `CLAUDE.md` (status, quick reference)
- `mkdocs.yml` navigation
- Guide docs (feature-specific)

### What `/craft:docs:feature` Does

After implementing a feature, ONE command updates:
1. Detects new commands, modules, files from commits
2. Updates CLI help epilogs
3. Updates commands reference
4. Updates/creates REFCARD entries
5. Suggests tutorial if complex feature
6. Updates README feature list
7. Updates CLAUDE.md "Just Completed"
8. Updates mkdocs navigation

### Workflow Cheat Sheet

```
AFTER FEATURE:     /craft:docs:feature
END OF SESSION:    /craft:docs:done
BEFORE RELEASE:    /craft:docs:changelog → update full
DEPLOY SITE:       /craft:docs:site --deploy
QUICK UPDATE:      /craft:docs:update
```

**Principle:** Workflow commands CALL individual commands. Individual commands remain for granular control.

---

## v1.7.0 - Site Commands Redesign 🚧 IN PROGRESS

**Theme:** Complete documentation site management with design standards

**Plan B (Focused):** 9 commands with essential design system

### Command Structure

| Command | Status | Purpose |
|---------|--------|---------|
| `/craft:site:create` | ✅ DONE | Full wizard (combines init + design) |
| `/craft:site:update` | ✅ DONE | Update content from code + validate |
| `/craft:site:status` | ✅ DONE | Dashboard and health check |
| `/craft:site:add` | ✅ DONE | Add pages/sections with nav sync |
| `/craft:site:theme` | ✅ DONE | Quick theme changes |
| `/craft:site:build` | KEEP | Build static site |
| `/craft:site:preview` | KEEP | Local preview server |
| `/craft:site:check` | KEEP | Comprehensive validation |
| `/craft:site:deploy` | KEEP | Multi-target deployment |

### Design System

**Design Presets (8 total):**

| Preset | Description | Best For |
|--------|-------------|----------|
| `data-wise` | DT's standard (Material + custom) | All DT projects |
| `minimal` | Clean, simple, fast | Small projects |
| `open-source` | Community-friendly, badges | Public repos |
| `corporate` | Professional, formal | Enterprise |

**ADHD-Friendly Presets:**

| Preset | Description | Best For |
|--------|-------------|----------|
| `adhd-focus` | Forest green, minimal distractions | Sustained focus |
| `adhd-calm` | Warm earth tones, cozy feel | Anxiety reduction |
| `adhd-dark` | Dark-first, muted sage | Night reading, light sensitivity |
| `adhd-light` | Warm off-white, soft contrast | Day reading, no glare |

**Config File:** `.craft/site-design.yaml`
```yaml
preset: "data-wise"
branding:
  name: "AITerm"
  tagline: "AI Terminal Optimizer"
colors:
  primary: "#1a73e8"
  accent: "#ff6b35"
navigation:
  style: "tabs"  # tabs, sidebar, hybrid
```

### Page Templates

Standard pages with consistent structure:
- **index.md** - Project overview with feature grid
- **QUICK-START.md** - 30-second setup guide
- **REFCARD.md** - Quick command reference
- **guide-page.md** - Standard guide format

### Navigation Standards

- Max 5-6 top-level sections
- Max 3 levels deep
- Required pages: index, QUICK-START, REFCARD
- Order: Home → Quick Start → Reference → Guides → Reference → API

### Implementation Phases

**Phase 1: Core Commands ✅ COMPLETE**
- [x] `/craft:site:create` - Full wizard
- [x] `/craft:site:update` - Content updater
- [x] `/craft:site:status` - Dashboard

**Phase 2: Design System ✅ COMPLETE**
- [x] `/craft:site:theme` - Quick theme changes
- [x] Design presets (8 presets total)
  - Standard: data-wise, minimal, open-source, corporate
  - ADHD-friendly: adhd-focus, adhd-calm, adhd-dark, adhd-light
- [x] Page templates (index, quick-start, refcard, guide-page)
- [x] MkDocs templates (mkdocs.yml, extra.css)

**Phase 3: Content Management ✅ COMPLETE**
- [x] `/craft:site:add` - Add pages with nav sync
- [ ] Enhanced build/check/deploy (deferred - existing commands work well)

**Dogfooding:** Applied data-wise preset to aiterm docs (Dec 27, 2025)

**Total Effort:** ~4 hours (under estimate!)

**See:** `PROPOSAL-site-commands-2025-12-27.md` for full specifications

---

## v1.8.0 - Homebrew Automation 🎯 TOP PRIORITY

**Theme:** Automated Homebrew formula management with zero manual intervention

**Background:** Built reusable workflow system for Data-Wise tap (Dec 31, 2025)
- Centralized workflow: `homebrew-tap/.github/workflows/update-formula.yml`
- Auto-merge PRs on release
- Multi-source support (GitHub tarballs, PyPI packages)
- Token management with fine-grained PAT

### Phase 1: Quick Wins (This Week)

| Task | Status | Description |
|------|--------|-------------|
| `homebrew-workflow-expert` skill | 🚧 TODO | Generate release workflows for any repo |
| Enhanced `/craft:dist:homebrew` | 🚧 TODO | Add subcommands: `formula`, `workflow`, `token`, `setup` |
| Formula validation | 🚧 TODO | Run `brew audit` before release |

### Phase 2: Setup Wizard (Next Week)

| Task | Status | Description |
|------|--------|-------------|
| `/craft:dist:homebrew setup` | 🚧 TODO | Full guided setup: detect → generate → token → release |
| PyPI resource updater | 🚧 TODO | Fix stale URLs automatically from PyPI API |

### Phase 3: Advanced Features (Future)

| Task | Status | Description |
|------|--------|-------------|
| Multi-formula coordinator | 📋 PLANNED | Batch releases with dependency order |
| Homebrew Cask support | 📋 PLANNED | Desktop apps (DMG/PKG) |
| Cross-platform packages | 📋 PLANNED | apt, chocolatey, scoop |

### New Commands

```bash
# Formula management
/craft:dist:homebrew formula       # Generate formula (existing, enhanced)
/craft:dist:homebrew workflow      # Generate release workflow
/craft:dist:homebrew validate      # Run brew audit
/craft:dist:homebrew setup         # Full setup wizard

# Updates
/craft:dist:homebrew update-resources  # Fix PyPI URLs
/craft:dist:homebrew release-batch     # Multi-formula release
```

### New Skill

**`homebrew-workflow-expert.md`** - Expert knowledge on:
- Reusable workflow patterns
- GitHub Actions for formula updates
- Token setup and management
- PyPI → Homebrew integration
- Auto-merge strategies

### Reusable Workflow Pattern

```yaml
# In any repo's .github/workflows/homebrew-release.yml
uses: Data-Wise/homebrew-tap/.github/workflows/update-formula.yml@main
with:
  formula_name: myapp
  version: ${{ needs.prepare.outputs.version }}
  sha256: ${{ needs.prepare.outputs.sha256 }}
  source_type: github  # or pypi
  auto_merge: true
secrets:
  tap_token: ${{ secrets.HOMEBREW_TAP_GITHUB_TOKEN }}
```

**See:** `BRAINSTORM-homebrew-automation-2025-12-31.md` for full details

---

## v1.9.0 - Release Automation (Future)

- `/craft:dist:pypi` - PyPI publishing workflow
- `/craft:dist:npm` - npm publishing workflow
- `/craft:dist:cargo` - Cargo publishing workflow
- `/craft:dist:release` - Multi-channel release orchestrator
- Agent pool management (max parallel, priority queue, resource budgets)
- Cost tracking per agent

---

## v1.10.0 - CI/CD Integration (Future)

- `/craft:ci:matrix` - Generate test matrix
- `/craft:ci:workflow` - Create GitHub Actions workflows
- `/craft:ci:badge` - Add/update README badges

---

## Ideas Backlog

### Site Commands (Future Enhancements)
- `/craft:site:migrate` - Framework migration (MkDocs ↔ Docusaurus)
- Multi-target deployment (Netlify, Vercel, Cloudflare Pages)
- Version selector for multi-version docs
- Academic preset (citation-friendly)

### Distribution
- Monorepo support for distribution commands
- Version bumping automation
- Changelog-to-release-notes conversion
- Installation verification tests
- Cross-platform binary building
- Agent result caching (reuse recent analysis)
- Cross-session agent continuity

---

## Contributing

To request features, create an issue or add to this roadmap.
