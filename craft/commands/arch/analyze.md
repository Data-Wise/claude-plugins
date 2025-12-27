---
description: Analyze codebase architecture with mode support
arguments:
  - name: mode
    description: Execution mode (default|debug|optimize|release)
    required: false
    default: default
  - name: path
    description: Directory to analyze
    required: false
    default: "."
---

# /craft:arch:analyze - Architecture Analysis

Analyze codebase architecture patterns, dependencies, and structure.

## Modes

| Mode | Time | Focus |
|------|------|-------|
| **default** | < 15s | Quick overview |
| **debug** | < 120s | Deep dive, all patterns |
| **optimize** | < 180s | Performance hotspots |
| **release** | < 300s | Full architectural audit |

## Usage

```bash
/craft:arch:analyze                 # Quick overview (default)
/craft:arch:analyze debug           # Deep pattern analysis
/craft:arch:analyze optimize        # Performance architecture
/craft:arch:analyze release         # Full audit
/craft:arch:analyze debug src/      # Analyze specific directory
```

## Analysis Areas

| Area | What's Analyzed |
|------|-----------------|
| Structure | Directory layout, module organization |
| Dependencies | Import graphs, coupling metrics |
| Patterns | MVC, microservices, layers, etc. |
| Data Flow | How data moves through the system |
| Complexity | Cyclomatic complexity, nesting depth |

## Mode Behaviors

### Default Mode (< 15s)
**Output:**
```
╭─ Architecture Overview ─────────────────────────────╮
│ Project: aiterm | Type: Python CLI                 │
│ Structure: src/aiterm/ (6 modules)                 │
├─────────────────────────────────────────────────────┤
│ cli/ terminal/ context/ claude/ opencode/ utils/   │
├─────────────────────────────────────────────────────┤
│ Health: Good | Dependencies: 4 external, 6 internal│
╰─────────────────────────────────────────────────────╯
```

### Debug Mode (< 120s)
**Output:**
```
╭─ Architecture Analysis (Debug Mode) ────────────────╮
│ STRUCTURE                                           │
│ src/aiterm/                                         │
│ ├── cli/         (entry point, commands)           │
│ ├── terminal/    (backends, detection)             │
│ ├── context/     (project detection)               │
│ └── claude/      (Claude Code integration)         │
│                                                     │
│ PATTERNS DETECTED                                   │
│ ✓ Strategy Pattern - terminal backends             │
│ ✓ Factory Pattern - detector creation              │
│ ⚠ God Class - main.py (consider splitting)         │
│                                                     │
│ DEPENDENCIES                                        │
│ cli/ ──→ terminal/ ──→ context/                    │
│   └──→ claude/                                     │
╰─────────────────────────────────────────────────────╯
```

### Optimize Mode (< 180s)
**Output:**
```
╭─ Architecture Analysis (Optimize Mode) ─────────────╮
│ IMPORT PERFORMANCE                                  │
│   rich          234ms  ████████████████            │
│   typer         156ms  ██████████                  │
│   yaml           89ms  ██████                      │
│                                                     │
│ HOT PATHS                                           │
│ 1. detector.py:detect_context() - 45ms avg         │
│ 2. settings.py:load_settings() - File I/O          │
│                                                     │
│ SUGGESTIONS                                         │
│ • Cache context detection result                   │
│ • Lazy load heavy modules                          │
│ • Estimated startup improvement: 40%               │
╰─────────────────────────────────────────────────────╯
```

### Release Mode (< 300s)
**Output:**
```
╭─ Architecture Audit (Release Mode) ─────────────────╮
│ Status: ⚠ MINOR ISSUES (3)                         │
├─────────────────────────────────────────────────────┤
│ METRICS                                             │
│ Cyclomatic Avg   4.2   < 10    ✓                   │
│ Max Func Size    45    < 50    ✓                   │
│ Test Coverage    83%   > 80%   ✓                   │
│ Circular Deps    0     = 0     ✓                   │
├─────────────────────────────────────────────────────┤
│ ISSUES                                              │
│ ⚠ cli/main.py has 15 functions (split?)           │
│ ⚠ Missing docstrings in utils/ (5 funcs)          │
├─────────────────────────────────────────────────────┤
│ QUALITY SCORE: 91/100                              │
╰─────────────────────────────────────────────────────╯
```

## Options

- `--depth <N>` - Analysis depth (1=shallow, 3=deep)
- `--focus <area>` - Focus on specific area
- `--report` - Generate detailed report
- `--json` - Output as JSON

## Integration

Works with:
- `/craft:arch:plan` - Design planning
- `/craft:arch:review` - Architecture review
- `/craft:arch:diagram` - Generate diagrams
- `/craft:code:refactor` - Implement changes
