---
description: Generate Mermaid diagram templates for documentation
arguments:
  - name: type
    description: Template type (dependency|workflow|architecture|comparison|sequence|state|all)
    required: false
    default: all
  - name: output
    description: Output file path (optional, defaults to stdout)
    required: false
---

# /craft:docs:mermaid - Mermaid Diagram Templates

Generate production-ready Mermaid diagram templates following best practices.

## Why Templates?

- **Consistent styling** across all documentation
- **Proper text lengths** to prevent overflow
- **Tested patterns** that render correctly
- **Quick start** for common diagram types

## Usage

```bash
/craft:docs:mermaid                    # Show all templates
/craft:docs:mermaid dependency         # Dependency graph template
/craft:docs:mermaid workflow           # Workflow/process template
/craft:docs:mermaid architecture       # System architecture template
/craft:docs:mermaid comparison         # Side-by-side comparison
/craft:docs:mermaid sequence           # Sequence diagram template
/craft:docs:mermaid state              # State machine template
/craft:docs:mermaid all --output docs/diagrams/templates.md
```

## Templates

### dependency - Dependency Graph

Shows relationships between components, packages, or systems.

```mermaid
graph LR
    subgraph CORE["Core Layer"]
        A["Component A"]
        B["Component B"]
    end

    subgraph UTILS["Utilities"]
        C["Helper C"]
        D["Helper D"]
    end

    subgraph EXTERNAL["External"]
        E["Library E"]
    end

    A --> C
    A --> D
    B --> C
    C --> E
    D --> E
```

**Use for:**
- Package dependencies
- Module relationships
- Service connections
- Import hierarchies

**Customization points:**
- Replace subgraph names with your layers
- Add/remove nodes as needed
- Change arrow directions for data flow

---

### workflow - Process Flow

Shows step-by-step processes with decisions.

```mermaid
flowchart TD
    START([Start]) --> STEP1[Step 1: Input]
    STEP1 --> CHECK{Decision?}

    CHECK -->|Yes| PATH_A[Path A]
    CHECK -->|No| PATH_B[Path B]

    PATH_A --> PROCESS[Process]
    PATH_B --> PROCESS

    PROCESS --> RESULT[Result]
    RESULT --> DONE([End])
```

**Use for:**
- User workflows
- CI/CD pipelines
- Decision trees
- Installation steps

**Node shapes:**
- `([text])` - Start/End (stadium)
- `[text]` - Process (rectangle)
- `{text}` - Decision (diamond)
- `[[text]]` - Subroutine

---

### architecture - System Architecture

Shows system components and their interactions.

```mermaid
graph TB
    subgraph CLIENT["Client Layer"]
        UI["Web UI"]
        CLI["CLI Tool"]
        API_CLIENT["API Client"]
    end

    subgraph SERVER["Server Layer"]
        GW["API Gateway"]
        AUTH["Auth Service"]
        CORE["Core Service"]
    end

    subgraph DATA["Data Layer"]
        DB[(Database)]
        CACHE[(Cache)]
    end

    UI --> GW
    CLI --> GW
    API_CLIENT --> GW

    GW --> AUTH
    GW --> CORE

    AUTH --> DB
    CORE --> DB
    CORE --> CACHE
```

**Use for:**
- System overviews
- Microservices
- Infrastructure diagrams
- Component relationships

**Node shapes:**
- `[(text)]` - Database (cylinder)
- `[text]` - Service (rectangle)
- `((text))` - Circle (for actors)

---

### comparison - Side-by-Side

Shows two approaches or states for comparison.

```mermaid
graph LR
    subgraph BEFORE["Before"]
        B1["Manual process"]
        B2["Error prone"]
        B3["Slow"]
    end

    subgraph AFTER["After"]
        A1["Automated"]
        A2["Reliable"]
        A3["Fast"]
    end

    BEFORE -->|Transform| AFTER
```

**Alternative: Two-column comparison**

```mermaid
graph TB
    subgraph LEFT["Option A"]
        direction TB
        L1["Pro: Simple"]
        L2["Pro: Fast"]
        L3["Con: Limited"]
    end

    subgraph RIGHT["Option B"]
        direction TB
        R1["Pro: Flexible"]
        R2["Pro: Scalable"]
        R3["Con: Complex"]
    end
```

**Use for:**
- Before/After states
- Feature comparisons
- Trade-off analysis
- Migration plans

---

### sequence - Sequence Diagram

Shows interactions between components over time.

```mermaid
sequenceDiagram
    participant U as User
    participant C as Client
    participant S as Server
    participant D as Database

    U->>C: Action
    activate C
    C->>S: Request
    activate S
    S->>D: Query
    activate D
    D-->>S: Result
    deactivate D
    S-->>C: Response
    deactivate S
    C-->>U: Display
    deactivate C
```

**Use for:**
- API interactions
- Authentication flows
- Message passing
- Protocol documentation

**Arrow types:**
- `->>` Solid with arrowhead
- `-->>` Dotted with arrowhead
- `-x` Solid with X (async)
- `--x` Dotted with X

---

### state - State Machine

Shows states and transitions.

```mermaid
stateDiagram-v2
    [*] --> Idle

    Idle --> Loading: Start
    Loading --> Ready: Success
    Loading --> Error: Failure

    Ready --> Processing: Submit
    Processing --> Ready: Complete
    Processing --> Error: Failure

    Error --> Idle: Reset
    Ready --> Idle: Cancel
```

**Use for:**
- UI states
- Order workflows
- Session lifecycles
- Connection states

---

## Best Practices (Built Into Templates)

### Text Length Rules

| Element | Max | Example |
|---------|-----|---------|
| Node labels | 15 chars | `"Auth Service"` |
| Edge labels | 10 chars | `"creates"` |
| Subgraph titles | 20 chars | `"Client Layer"` |

### Abbreviation Patterns

```mermaid
%% BAD - Too long
graph LR
    A["~/projects/dev-tools/aiterm/feature-branch/"]

%% GOOD - Abbreviated
graph LR
    A["~/.../feature-branch"]
```

### Common Abbreviations

| Full | Abbreviated |
|------|-------------|
| `~/projects/dev-tools/` | `~/...dev-tools/` |
| `~/.git-worktrees/project/branch` | `~/.git-wt/.../branch` |
| `Authentication Service` | `Auth Service` |
| `Configuration Manager` | `Config Mgr` |
| `automatically creates` | `creates` |

---

## Output Format

When running without `--output`:

```
╭─ Mermaid Templates ─────────────────────────────────╮
│                                                     │
│ Available templates:                                │
│   • dependency  - Package/module relationships      │
│   • workflow    - Process flows with decisions      │
│   • architecture - System component diagrams        │
│   • comparison  - Before/after, option A vs B       │
│   • sequence    - Time-based interactions           │
│   • state       - State machine transitions         │
│                                                     │
│ Usage:                                              │
│   /craft:docs:mermaid <type>                        │
│   /craft:docs:mermaid all --output docs/templates.md│
│                                                     │
╰─────────────────────────────────────────────────────╯
```

When running with a type:

```
╭─ Dependency Graph Template ─────────────────────────╮
│                                                     │
│ Copy this template and customize:                   │
│                                                     │
│ ```mermaid                                          │
│ graph LR                                            │
│     subgraph CORE["Core Layer"]                     │
│         A["Component A"]                            │
│         B["Component B"]                            │
│     end                                             │
│     ...                                             │
│ ```                                                 │
│                                                     │
│ Customization tips:                                 │
│   • Replace subgraph names with your layers         │
│   • Keep node labels under 15 characters            │
│   • Use LR for wide, TB for tall diagrams           │
│                                                     │
╰─────────────────────────────────────────────────────╯
```

---

## Project-Specific Templates

### R Package Ecosystem

```mermaid
graph TB
    subgraph CORE["Core Package"]
        A["rmediation"]
    end

    subgraph EXTENSIONS["Extensions"]
        B["mediationverse"]
        C["medfit"]
    end

    subgraph DEPS["Dependencies"]
        D["lavaan"]
        E["ggplot2"]
    end

    B --> A
    C --> A
    A --> D
    A --> E
```

### CLI Tool Architecture

```mermaid
graph TB
    subgraph CLI["CLI Layer"]
        MAIN["main.py"]
        CMDS["commands/"]
    end

    subgraph CORE["Core"]
        CTX["context/"]
        TERM["terminal/"]
    end

    subgraph CONFIG["Config"]
        SETTINGS["settings.py"]
        PROFILES["profiles/"]
    end

    MAIN --> CMDS
    CMDS --> CTX
    CMDS --> TERM
    CTX --> SETTINGS
    TERM --> PROFILES
```

### Git Worktree Structure

```mermaid
graph TB
    subgraph MAIN["Main Repo"]
        M["~/projects/app"]
        MB["Branch: main"]
    end

    subgraph WT["Worktrees"]
        W1["~/.git-wt/app/feat-a"]
        W1B["Branch: feat-a"]
        W2["~/.git-wt/app/feat-b"]
        W2B["Branch: feat-b"]
    end

    M --- W1
    M --- W2
```

---

## Integration

**Related commands:**
- `/craft:docs:generate diagram` - Routes to mermaid-expert agent
- `/craft:site:status` - Validates Mermaid configuration

**Uses skill:**
- `mermaid-linter` - Validates diagram syntax and text length

**mkdocs.yml requirements:**
```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format

extra_javascript:
  - https://unpkg.com/mermaid@10/dist/mermaid.min.js
```

---

## Quick Reference

| Template | Direction | Best For |
|----------|-----------|----------|
| `dependency` | LR | Package relationships |
| `workflow` | TD | Process flows |
| `architecture` | TB | System diagrams |
| `comparison` | LR | Before/after |
| `sequence` | - | API interactions |
| `state` | - | State machines |

**Direction keywords:**
- `LR` - Left to Right (wide)
- `RL` - Right to Left
- `TB` or `TD` - Top to Bottom (tall)
- `BT` - Bottom to Top
