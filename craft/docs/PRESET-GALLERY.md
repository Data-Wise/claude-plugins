# Design Preset Gallery

Quick visual reference for all 8 design presets available in `/craft:site:create` and `/craft:site:theme`.

---

## Standard Presets

### 1. data-wise (Default)

**DT's standard documentation style**

```
┌─────────────────────────────────────────┐
│ ████████ Header (Blue #1a73e8)          │
├─────────────────────────────────────────┤
│ Home | Quick Start | Guide | Reference  │ ← Tabs
├─────────────────────────────────────────┤
│                                         │
│ # Welcome                               │
│                                         │
│ Links are [orange](#ff6b35)             │
│ Dark mode toggle: ✅                    │
│                                         │
└─────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Primary | `#1a73e8` (Google Blue) |
| Accent | `#ff6b35` (Vibrant Orange) |
| Font | Roboto / Roboto Mono |
| Nav Style | Tabs |
| Dark Mode | Auto (toggle) |

**Best for:** All DT projects, modern SaaS docs

---

### 2. minimal

**Clean and simple**

```
┌─────────────────────────────────────────┐
│ ████████ Header (Gray #424242)          │
├─────────────────────────────────────────┤
│ │ Home                                  │
│ │ Docs         ← Sidebar                │
│ │ Reference                             │
├─────────────────────────────────────────┤
│ # Title                                 │
│                                         │
│ Simple, fast, no frills.                │
│                                         │
└─────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Primary | `#424242` (Neutral Gray) |
| Accent | `#1976d2` (Subtle Blue) |
| Font | System fonts |
| Nav Style | Sidebar |
| Dark Mode | Light only |

**Best for:** Small projects, personal docs, fast loading

---

### 3. open-source

**Community-friendly**

```
┌─────────────────────────────────────────┐
│ ████████ Header (GitHub Blue #0366d6)   │
├─────────────────────────────────────────┤
│ Home | Getting Started | API | Contrib  │
├─────────────────────────────────────────┤
│ # Project Name                          │
│ [PyPI] [License] [Tests] [Coverage]     │ ← Badges
│                                         │
│ Links are [green](#28a745)              │
│                                         │
└─────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Primary | `#0366d6` (GitHub Blue) |
| Accent | `#28a745` (GitHub Green) |
| Font | Roboto / Fira Code |
| Nav Style | Tabs |
| Dark Mode | Auto |

**Best for:** Public repos, community projects

---

### 4. corporate

**Professional and formal**

```
┌─────────────────────────────────────────┐
│ ████████ Header (Navy #003366)          │
│ [v2.0] ← Version selector               │
├─────────────────────────────────────────┤
│ Overview | User Guide | API | Support   │
├─────────────────────────────────────────┤
│ # Enterprise Documentation              │
│                                         │
│ Formal, professional appearance.        │
│ Footer: © 2025 Company Name             │
│                                         │
└─────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Primary | `#003366` (Deep Navy) |
| Accent | `#0066cc` (Corporate Blue) |
| Font | Open Sans / Source Code Pro |
| Nav Style | Tabs |
| Dark Mode | Light only |

**Best for:** Enterprise docs, commercial products

---

## ADHD-Friendly Presets

All ADHD presets include:
- Reduced animations (0.1s max)
- Larger click targets
- Narrower content width (750-850px)
- Clear heading hierarchy
- Softer color contrasts

---

### 5. adhd-focus

**Calm, focused, minimal distractions**

```
┌─────────────────────────────────────────┐
│ ████████ Header (Forest Green #2d6a4f)  │
├─────────────────────────────────────────┤
│ │ Start Here                            │
│ │ Guide           ← Sidebar (2 levels)  │
│ │ Reference                             │
├─────────────────────────────────────────┤
│ # Welcome                               │
│ ────────────────── ← Clear h2 separator │
│                                         │
│ Calm green links, warm background.      │
│ No visual noise.                        │
│                                         │
└─────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Primary | `#2d6a4f` (Forest Green) |
| Accent | `#40916c` (Sage) |
| Font | Inter / JetBrains Mono |
| Nav Style | Sidebar |
| Dark Mode | Auto |
| Background | `#fafafa` (warm) / `#1a1a2e` (dark) |

**Best for:** Focus-intensive reading, sustained attention tasks

---

### 6. adhd-calm

**Warm, cozy, anxiety-reducing**

```
┌─────────────────────────────────────────┐
│ ████████ Header (Warm Brown #8b5a2b)    │
├─────────────────────────────────────────┤
│ │ Welcome                               │
│ │ Learn            ← Friendly labels    │
│ │ Reference                             │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ # Content                           │ │ ← Card-like
│ │                                     │ │
│ │ Cream background like parchment.    │ │
│ │ Warm, inviting, cozy.               │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Primary | `#8b5a2b` (Warm Brown) |
| Accent | `#d4a373` (Terracotta) |
| Font | Merriweather Sans |
| Nav Style | Sidebar |
| Dark Mode | Auto |
| Background | `#faf6f1` (cream) / `#2c2416` (warm dark) |

**Best for:** Reducing reading avoidance, late-night reading

---

### 7. adhd-dark

**Dark-first, reduced eye strain**

```
┌─────────────────────────────────────────┐
│ ████████ Header (gradient dark)         │
│ (No light mode toggle - always dark)    │
├─────────────────────────────────────────┤
│ │ Quick Start                           │
│ │ Guide                                 │
│ │ Reference                             │
├─────────────────────────────────────────┤
│                                         │
│ # Deep blue-black background (#16161e)  │
│                                         │
│ Muted sage green links.                 │
│ Easy on eyes, no glare.                 │
│                                         │
└─────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Primary | `#7c9885` (Muted Sage) |
| Accent | `#a8c5b5` (Light Sage) |
| Font | IBM Plex Sans / IBM Plex Mono |
| Nav Style | Sidebar |
| Dark Mode | Always dark |
| Background | `#16161e` (deep blue-black) |

**Best for:** Light sensitivity, night coding, eye strain

---

### 8. adhd-light

**Warm light, never harsh white**

```
┌─────────────────────────────────────────┐
│ ████████ Header (Blue-gray #5a6e78)     │
│ (No dark mode toggle - always light)    │
├─────────────────────────────────────────┤
│ │ Get Started                           │
│ │ Guide                                 │
│ │ Reference                             │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ # Content                           │ │ ← Soft shadow
│ │                                     │ │
│ │ Off-white background (#f8f6f3)      │ │
│ │ Soft contrasts, sepia undertones.   │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

| Property | Value |
|----------|-------|
| Primary | `#5a6e78` (Blue-Gray) |
| Accent | `#7a9e9f` (Teal-Gray) |
| Font | Source Sans Pro / Source Code Pro |
| Nav Style | Sidebar |
| Dark Mode | Always light |
| Background | `#f8f6f3` (warm off-white) |

**Best for:** Day reading, glare reduction, extended reading sessions

---

## Quick Usage

```bash
# Create new site with preset
/craft:site:create --preset adhd-focus

# Switch existing site to preset
/craft:site:theme --preset adhd-calm

# Show current theme
/craft:site:theme
```

---

## Customizing Presets

After applying a preset, customize via:

```bash
# Change colors
/craft:site:theme --primary "#your-color"

# Switch palette
/craft:site:theme --palette ocean

# Full custom design
/craft:site:create --preset custom
```

---

## Files Updated

When applying a preset:

| File | Changes |
|------|---------|
| `.craft/site-design.yaml` | Design configuration |
| `mkdocs.yml` | Theme, colors, fonts |
| `docs/stylesheets/extra.css` | CSS variables, custom styles |
