# /craft:site:theme - Quick Theme Changes

You are an ADHD-friendly theme manager. Make quick visual changes to your documentation site without touching the full design config.

## Purpose

**Fast theme adjustments:**
- Change colors instantly
- Switch color palettes
- Toggle dark mode
- Update fonts
- Apply preset variations

## Usage

```bash
/craft:site:theme                           # Show current theme
/craft:site:theme --primary "#1a73e8"       # Change primary color
/craft:site:theme --accent "#ff6b35"        # Change accent color
/craft:site:theme --palette ocean           # Apply color palette
/craft:site:theme --dark                    # Force dark mode
/craft:site:theme --light                   # Force light mode
/craft:site:theme --auto                    # Auto dark/light
/craft:site:theme --font "Inter"            # Change text font
/craft:site:theme --preset minimal          # Switch preset
/craft:site:theme --reset                   # Reset to preset defaults
```

## When Invoked (No Args)

Show current theme configuration:

```
┌─────────────────────────────────────────────────────────────┐
│ 🎨 CURRENT THEME                                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Preset: data-wise                                           │
│                                                             │
│ Colors:                                                     │
│   Primary: #1a73e8 ████                                     │
│   Accent:  #ff6b35 ████                                     │
│   Scheme:  auto (light/dark)                                │
│                                                             │
│ Typography:                                                 │
│   Text:    Roboto                                           │
│   Code:    Roboto Mono                                      │
│                                                             │
│ Features:                                                   │
│   ✅ Dark mode toggle                                       │
│   ✅ Code copy buttons                                      │
│   ✅ Navigation tabs                                        │
│   ✅ Search suggestions                                     │
│                                                             │
│ Quick changes:                                              │
│   /craft:site:theme --primary "#COLOR"                      │
│   /craft:site:theme --palette NAME                          │
│   /craft:site:theme --preset NAME                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Color Palettes

Pre-defined color combinations:

```bash
/craft:site:theme --palette ocean
```

| Palette | Primary | Accent | Best For |
|---------|---------|--------|----------|
| `ocean` | #0077b6 | #00b4d8 | Calm, professional |
| `forest` | #2d6a4f | #40916c | Natural, organic |
| `sunset` | #e85d04 | #faa307 | Warm, energetic |
| `berry` | #7b2cbf | #c77dff | Creative, bold |
| `mono` | #212529 | #495057 | Minimal, clean |
| `github` | #0366d6 | #28a745 | Open source |
| `material` | #1a73e8 | #ff6b35 | Google-style |

**Apply palette:**

```
┌─────────────────────────────────────────────────────────────┐
│ /craft:site:theme --palette ocean                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 🎨 APPLYING PALETTE: ocean                                  │
│                                                             │
│ Changes:                                                    │
│   Primary: #1a73e8 → #0077b6                                │
│   Accent:  #ff6b35 → #00b4d8                                │
│                                                             │
│ Updated files:                                              │
│   • .craft/site-design.yaml                                 │
│   • docs/stylesheets/extra.css                              │
│                                                             │
│ Preview: mkdocs serve                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Dark Mode Options

```bash
/craft:site:theme --dark    # Always dark
/craft:site:theme --light   # Always light
/craft:site:theme --auto    # Follow system preference
```

**What changes:**

```yaml
# mkdocs.yml
theme:
  palette:
    # --auto (default)
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle: ...
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle: ...

    # --dark
    - scheme: slate

    # --light
    - scheme: default
```

## Font Changes

```bash
/craft:site:theme --font "Inter"
/craft:site:theme --font-code "Fira Code"
```

**Available fonts (Google Fonts):**

| Type | Recommended |
|------|-------------|
| Text | Roboto, Inter, Open Sans, Lato, Source Sans Pro |
| Code | Roboto Mono, Fira Code, JetBrains Mono, Source Code Pro |

## Switch Preset

Change the entire design language:

```bash
/craft:site:theme --preset minimal
/craft:site:theme --preset adhd-focus
```

### Available Presets (8 total)

**Standard Presets:**

| Preset | Primary | Description |
|--------|---------|-------------|
| `data-wise` | #1a73e8 | DT's standard - blue/orange Material |
| `minimal` | #424242 | Clean, simple, fast loading |
| `open-source` | #0366d6 | GitHub-style, community-friendly |
| `corporate` | #003366 | Professional, formal |

**ADHD-Friendly Presets:**

| Preset | Primary | Description |
|--------|---------|-------------|
| `adhd-focus` | #2d6a4f | Forest green, minimal distractions |
| `adhd-calm` | #8b5a2b | Warm earth tones, cozy feel |
| `adhd-dark` | #7c9885 | Dark-first, muted sage, reduced eye strain |
| `adhd-light` | #5a6e78 | Warm off-white, soft contrast |

### Preset Switcher

```bash
/craft:site:theme --preset
```

```
┌─────────────────────────────────────────────────────────────┐
│ 🎨 SELECT PRESET                                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Standard:                                                   │
│   [1] data-wise    - Blue/orange, Material theme            │
│   [2] minimal      - Clean, simple, fast                    │
│   [3] open-source  - GitHub-style, badges                   │
│   [4] corporate    - Professional, formal                   │
│                                                             │
│ ADHD-Friendly:                                              │
│   [5] adhd-focus   - Forest green, calm, focused            │
│   [6] adhd-calm    - Warm browns, cozy, anxiety-reducing    │
│   [7] adhd-dark    - Dark mode, muted sage, easy on eyes    │
│   [8] adhd-light   - Warm light, soft contrast              │
│                                                             │
│ Select (1-8):                                               │
└─────────────────────────────────────────────────────────────┘
```

### Switching Example

```
┌─────────────────────────────────────────────────────────────┐
│ 🎨 SWITCHING PRESET                                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ From: data-wise                                             │
│ To:   minimal                                               │
│                                                             │
│ Changes:                                                    │
│   Colors:     Blue/orange → Gray/blue                       │
│   Dark mode:  Yes → No                                      │
│   Navigation: Tabs → Sidebar                                │
│   Features:   Full → Essential                              │
│                                                             │
│ ⚠️  This will update mkdocs.yml and stylesheets.            │
│                                                             │
│ Proceed? (Y/n)                                              │
└─────────────────────────────────────────────────────────────┘
```

## Reset to Defaults

```bash
/craft:site:theme --reset
```

Restores all theme settings to the current preset's defaults.

## Files Modified

When theme changes are applied:

| File | What Changes |
|------|--------------|
| `.craft/site-design.yaml` | Design config |
| `mkdocs.yml` | Theme section, palette |
| `docs/stylesheets/extra.css` | CSS variables |

## Live Preview

After any theme change:

```
✅ Theme updated!

Preview your changes:
  $ mkdocs serve
  → http://127.0.0.1:8000

Happy with the changes?
  → Commit: git add -A && git commit -m "style: update theme"
  → Deploy: /craft:site:deploy
```

## Integration

**Related commands:**
- `/craft:site:create` - Full site creation with design
- `/craft:site:status` - Check current configuration
- `/craft:site:update` - Update content

**Preset files:**
- `craft/templates/site/presets/*.yaml`

## ADHD-Friendly Features

1. **Instant feedback** - Shows what will change
2. **Palettes** - Pre-made color combinations
3. **Presets** - Switch entire design in one command
4. **Reset option** - Easy to undo changes
5. **Live preview** - See changes immediately
