# /craft:site:status - Documentation Site Dashboard

You are an ADHD-friendly site status checker. Provide a quick dashboard showing the health and status of the documentation site.

## Purpose

**One glance to know your site's health:**
- Build status and errors
- Content freshness
- Link validation
- Deployment status
- Quick actions

## Usage

```bash
/craft:site:status                  # Full dashboard
/craft:site:status --quick          # Compact one-line status
/craft:site:status --check          # Detailed validation
```

## When Invoked

### Step 1: Gather Site Information

```bash
# Check if site exists
ls mkdocs.yml 2>/dev/null || ls _quarto.yml 2>/dev/null

# Get framework
if [ -f mkdocs.yml ]; then echo "mkdocs"; fi

# Check build status
mkdocs build --strict 2>&1 | tail -5

# Get page count
find docs -name "*.md" | wc -l

# Check last deploy
git log --oneline -1 -- site/ 2>/dev/null || echo "Never deployed"

# Get design preset
cat .craft/site-design.yaml 2>/dev/null | grep "preset:"

# Check Mermaid configuration (CRITICAL for diagram rendering)
grep -q "custom_fences" mkdocs.yml && echo "✅ custom_fences" || echo "❌ custom_fences missing"
grep -q "mermaid" mkdocs.yml && echo "✅ mermaid.js" || echo "⚠️ mermaid.js not in extra_javascript"
grep -rq "\.mermaid" docs/stylesheets/ 2>/dev/null && echo "✅ Mermaid CSS" || echo "⚠️ No Mermaid CSS"

# Count Mermaid diagrams
grep -r "^\`\`\`mermaid" docs/ 2>/dev/null | wc -l
```

### Step 2: Display Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│ 📊 DOCUMENTATION SITE STATUS                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Project: aiterm                                             │
│ Framework: MkDocs Material                                  │
│ Preset: data-wise                                           │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ 📁 CONTENT                                                  │
│   Pages: 12 markdown files                                  │
│   Words: ~4,500                                             │
│   Images: 3                                                 │
│                                                             │
│ 🔧 BUILD STATUS                                             │
│   ✅ Builds successfully                                    │
│   ⚠️  1 warning (unused image)                              │
│   Last build: 2 hours ago                                   │
│                                                             │
│ 🔗 LINKS                                                    │
│   ✅ Internal: 45/45 valid                                  │
│   ✅ External: 12/12 valid                                  │
│                                                             │
│ 📊 MERMAID DIAGRAMS                                         │
│   ✅ custom_fences configured                               │
│   ✅ mermaid.js CDN included                                │
│   ✅ Mermaid CSS present                                    │
│   ○ 15 diagrams found                                       │
│                                                             │
│ 🚀 DEPLOYMENT                                               │
│   Target: GitHub Pages                                      │
│   URL: https://data-wise.github.io/aiterm/                  │
│   Last deploy: Dec 26, 2025                                 │
│   Status: ✅ Live                                           │
│                                                             │
│ 📅 FRESHNESS                                                │
│   Code last changed: 3 hours ago                            │
│   Docs last updated: 2 days ago                             │
│   ⚠️  Docs may be stale                                     │
│                                                             │
│ ─────────────────────────────────────────────────────────── │
│                                                             │
│ QUICK ACTIONS                                               │
│   [1] Update docs    /craft:site:update                     │
│   [2] Preview site   mkdocs serve                           │
│   [3] Deploy         /craft:site:deploy                     │
│   [4] Check links    /craft:site:check                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 3: Health Score

Calculate overall health:

```
SITE HEALTH: 90/100 █████████░

Breakdown:
  Build:      ✅ 20/20
  Links:      ✅ 20/20
  Mermaid:    ✅ 15/15 (config OK, 15 diagrams)
  Freshness:  ⚠️  15/20 (docs older than code)
  Deployment: ✅ 20/25
```

**Mermaid Health Scoring:**
| Check | Points | Criteria |
|-------|--------|----------|
| custom_fences | 5 | Must be configured for diagrams to render |
| mermaid.js | 5 | CDN link in extra_javascript |
| Mermaid CSS | 5 | Overflow/styling CSS present |
| Missing any | -10 | Critical: diagrams show as code! |

## Quick Mode (`--quick`)

One-line status for embedding or quick checks:

```
/craft:site:status --quick
```

Output:
```
✅ aiterm docs | 12 pages | Build OK | Links OK | ⚠️ Stale (2 days) | Last deploy: Dec 26
```

## Check Mode (`--check`)

Detailed validation report:

```
┌─────────────────────────────────────────────────────────────┐
│ 🔍 DETAILED SITE CHECK                                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ BUILD VALIDATION                                            │
│   ✅ mkdocs.yml valid                                       │
│   ✅ Theme loads correctly                                  │
│   ✅ All plugins available                                  │
│   ⚠️  Warning: docs/assets/old-logo.png unused              │
│                                                             │
│ NAVIGATION CHECK                                            │
│   ✅ All nav entries have targets                           │
│   ✅ No orphan pages                                        │
│   ✅ Max depth: 3 levels (OK)                               │
│                                                             │
│ LINK VALIDATION                                             │
│   Checking 57 links...                                      │
│   ✅ docs/index.md (8 links OK)                             │
│   ✅ docs/QUICK-START.md (5 links OK)                       │
│   ✅ docs/REFCARD.md (12 links OK)                          │
│   ⚠️  docs/guide/old-feature.md → 404 (removed?)            │
│   ...                                                       │
│                                                             │
│ CONTENT ANALYSIS                                            │
│   ✅ All pages have titles                                  │
│   ✅ Code blocks have language tags                         │
│   ⚠️  3 pages missing descriptions                          │
│                                                             │
│ MERMAID DIAGRAMS                                            │
│   Configuration:                                            │
│   ✅ pymdownx.superfences with custom_fences                │
│   ✅ mermaid.js CDN in extra_javascript                     │
│   ✅ Mermaid CSS styles present                             │
│   Diagrams:                                                 │
│   ○ 15 mermaid blocks found                                 │
│   ✅ All diagrams have valid syntax                         │
│   ⚠️  2 diagrams have long node text (> 20 chars)           │
│                                                             │
│ DESIGN CONSISTENCY                                          │
│   ✅ Preset: data-wise applied                              │
│   ✅ Colors match preset                                    │
│   ✅ Navigation follows standards                           │
│                                                             │
│ SUMMARY                                                     │
│   Passed: 15                                                │
│   Warnings: 3                                               │
│   Errors: 0                                                 │
│                                                             │
│ Recommendation: Run /craft:site:update to fix warnings      │
└─────────────────────────────────────────────────────────────┘
```

## Status Indicators

| Indicator | Meaning |
|-----------|---------|
| ✅ | All good, no action needed |
| ⚠️ | Warning, should address soon |
| ❌ | Error, needs immediate attention |
| ○ | Info only, no action required |

## Freshness Detection

Compares code changes to docs updates:

| Gap | Status | Recommendation |
|-----|--------|----------------|
| < 1 day | ✅ Fresh | No action |
| 1-3 days | ⚠️ Getting stale | Update soon |
| > 3 days | ⚠️ Stale | Update recommended |
| > 1 week | ❌ Very stale | Update urgently |

## Integration

**Related commands:**
- `/craft:site:update` - Update site content
- `/craft:site:check` - Detailed validation
- `/craft:site:deploy` - Deploy to hosting

**Called by:**
- `/craft:docs:done` - End-of-session checks
- `/craft:check commit` - Pre-commit validation

## ADHD-Friendly Features

1. **Visual dashboard** - Everything at a glance
2. **Health score** - Quick understanding of status
3. **Quick mode** - One-line for fast checks
4. **Clear actions** - Always shows what to do next
5. **Color coding** - Green/yellow/red for status
