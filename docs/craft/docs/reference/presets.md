# Design Presets

Craft provides 8 design presets for documentation sites, including 4 ADHD-friendly options.

## Standard Presets

### data-wise (Default)

DT's standard design with Material theme.

**Colors:**
- Primary: Blue (#1a73e8)
- Accent: Orange (#ff6b35)
- Scheme: Auto (light/dark)

**Features:**
- Navigation tabs
- Dark mode toggle
- Code copy buttons
- Edit on GitHub
- Instant navigation

**Best for:** Technical projects, developer tools, CLIs

### minimal

Clean and simple, fast loading.

**Colors:**
- Primary: Neutral gray (#424242)
- Accent: Blue (#1976d2)
- Scheme: Light only

**Features:** Search, code copy (essential only)

**Best for:** Simple projects, quick documentation

### open-source

Community-friendly with badges and contributor focus.

**Colors:**
- Primary: GitHub blue (#0366d6)
- Accent: Green (#28a745)
- Scheme: Auto

**Features:** All features enabled, badges, version selector

**Best for:** Open source projects, community-driven tools

### corporate

Professional and formal.

**Colors:**
- Primary: Navy (#003366)
- Accent: Corporate blue (#0066cc)
- Scheme: Light only

**Features:** Version selector, announcement bar, formal styling

**Best for:** Enterprise documentation, corporate tools

## ADHD-Friendly Presets

### adhd-focus

Calm forest green, minimal distractions.

**Colors:**
- Primary: Forest green (#2d6a4f)
- Accent: Sage (#a4c3b2)
- Scheme: Auto

**Features:**
- Reduced animations
- Clear heading hierarchy
- Calm color palette
- Visual breathing room

**Best for:** Complex technical docs, long-form content

### adhd-calm

Warm earth tones, cozy reading experience.

**Colors:**
- Primary: Warm brown (#8b5a2b)
- Accent: Terracotta (#d4a574)
- Scheme: Auto

**Features:**
- Cream backgrounds
- Soft contrasts
- Warm undertones
- Comfortable reading

**Best for:** Tutorials, learning materials, guides

### adhd-dark

Dark-first, reduced eye strain.

**Colors:**
- Primary: Muted sage (#7c9885)
- Accent: Soft gold (#d4af37)
- Scheme: Dark only (no light mode)

**Features:**
- Night reading optimized
- No harsh whites
- Reduced blue light
- Eye-strain reduction

**Best for:** Late-night coding, extended reading sessions

### adhd-light

Warm light, never harsh white.

**Colors:**
- Primary: Blue-gray (#5a6e78)
- Accent: Warm orange (#ff8c42)
- Scheme: Light only (warm)

**Features:**
- Soft shadows
- Sepia undertones
- No pure white backgrounds
- Comfortable daylight reading

**Best for:** Daytime reading, print-style documentation

## Using Presets

```bash
# Interactive selection
/craft:site:create

# Direct preset selection
/craft:site:create --preset adhd-focus

# Quick mode with auto-detection
/craft:site:create --quick
```

## Customizing Presets

Edit `.craft/site-design.yaml` to customize:

```yaml
preset: "adhd-focus"

# Override specific colors
colors:
  primary: "#custom-color"
  accent: "#custom-accent"

# Override features
features:
  search: true
  dark_mode: false  # Force single mode
```

Then regenerate with:

```bash
/craft:site:update
```

## Next Steps

- [Configuration](configuration.md) - Full configuration reference
- [Site Commands](../commands/site.md) - Site management
