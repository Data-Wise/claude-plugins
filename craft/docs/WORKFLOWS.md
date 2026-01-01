# Visual Workflows

⏱️ **5 minutes** • 🟢 Beginner • ✓ Understand craft workflows

> **TL;DR** (30 seconds)
>
> - **What:** Visual workflow diagrams showing how craft commands work together
> - **Why:** Quickly understand the flow from task to completion
> - **How:** Follow the mermaid diagrams for your use case
> - **Next:** Pick a workflow and try the commands in sequence

## Documentation Workflow

```mermaid
flowchart TD
    Start([Make code changes]) --> Update[/craft:docs:update/]
    Update --> Analysis{Analyze changes}

    Analysis -->|Stale docs| Generate[Generate new docs]
    Analysis -->|Missing sections| Generate
    Analysis -->|All current| Check

    Generate --> Check[/craft:docs:check/]
    Check --> Validate{Validation}

    Validate -->|Errors found| AutoFix[Auto-fix issues]
    Validate -->|All good| Changelog

    AutoFix --> Changelog[/craft:docs:changelog/]
    Changelog --> Deploy[/craft:site:deploy/]
    Deploy --> Done([Documentation updated!])

    style Start fill:#e8f5e9,stroke:#4caf50
    style Update fill:#fff9c4,stroke:#fbc02d
    style Check fill:#e1bee7,stroke:#8e24aa
    style Deploy fill:#c8e6c9,stroke:#66bb6a
    style Done fill:#a5d6a7,stroke:#4caf50,stroke-width:3px
```

**Commands used:**
1. `/craft:docs:update` - Smart detection and generation
2. `/craft:docs:check` - Validation with auto-fix
3. `/craft:docs:changelog` - Update CHANGELOG.md
4. `/craft:site:deploy` - Deploy to GitHub Pages

---

## Site Creation Workflow

```mermaid
flowchart TD
    Start([New project]) --> Create[/craft:site:create/]
    Create --> Wizard{Choose preset}

    Wizard -->|data-wise| Build[Generate site files]
    Wizard -->|adhd-focus| Build
    Wizard -->|minimal| Build

    Build --> Preview[/craft:site:preview/]
    Preview --> Edit{Need changes?}

    Edit -->|Yes| Theme[/craft:site:theme/]
    Edit -->|No| Deploy[/craft:site:deploy/]

    Theme --> Preview
    Deploy --> Done([Live site!])

    style Start fill:#e8f5e9,stroke:#4caf50
    style Create fill:#fff9c4,stroke:#fbc02d
    style Preview fill:#e1bee7,stroke:#8e24aa
    style Deploy fill:#c8e6c9,stroke:#66bb6a
    style Done fill:#a5d6a7,stroke:#4caf50,stroke-width:3px
```

**Commands used:**
1. `/craft:site:create` - Full wizard with 8 presets
2. `/craft:site:preview` - Local preview
3. `/craft:site:theme` - Adjust colors/fonts
4. `/craft:site:deploy` - Push to GitHub Pages

---

## Testing Workflow

```mermaid
flowchart TD
    Start([Write code]) --> Lint[/craft:code:lint optimize/]
    Lint --> Tests[/craft:test:run debug/]

    Tests --> Results{All pass?}

    Results -->|Failures| Debug[/craft:code:debug/]
    Results -->|Success| Check[/craft:check/]

    Debug --> Fix[Fix issues]
    Fix --> Tests

    Check --> Commit{Ready?}
    Commit -->|Yes| Git[git commit]
    Commit -->|Issues| Review[Review output]

    Review --> Fix2[Address issues]
    Fix2 --> Check

    Git --> Done([Code committed!])

    style Start fill:#e8f5e9,stroke:#4caf50
    style Lint fill:#fff9c4,stroke:#fbc02d
    style Tests fill:#e1bee7,stroke:#8e24aa
    style Check fill:#ffccbc,stroke:#ff5722
    style Done fill:#a5d6a7,stroke:#4caf50,stroke-width:3px
```

**Commands used:**
1. `/craft:code:lint optimize` - Fast parallel linting
2. `/craft:test:run debug` - Verbose test output
3. `/craft:code:debug` - Systematic debugging
4. `/craft:check` - Pre-commit validation

---

## Release Workflow

```mermaid
flowchart TD
    Start([Ready to release]) --> Check[/craft:check --for release/]

    Check --> Audit{Full audit}

    Audit -->|Issues| Fix[Address issues]
    Audit -->|Clean| Docs

    Fix --> Check

    Docs[/craft:docs:update/] --> Changelog[/craft:docs:changelog/]
    Changelog --> Tag[git tag vX.Y.Z]

    Tag --> Deploy[/craft:site:deploy/]
    Deploy --> Push[git push --tags]

    Push --> Done([Released!])

    style Start fill:#e8f5e9,stroke:#4caf50
    style Check fill:#fff9c4,stroke:#fbc02d
    style Docs fill:#e1bee7,stroke:#8e24aa
    style Deploy fill:#c8e6c9,stroke:#66bb6a
    style Done fill:#a5d6a7,stroke:#4caf50,stroke-width:3px
```

**Commands used:**
1. `/craft:check --for release` - Comprehensive audit
2. `/craft:docs:update` - Final docs update
3. `/craft:docs:changelog` - Generate release notes
4. `/craft:site:deploy` - Update documentation site

---

## Git Worktree Workflow

```mermaid
flowchart TD
    Start([Multiple features]) --> Add[/craft:git:worktree add <name>/]

    Add --> Parallel[Create parallel workspaces]

    subgraph work[" "]
        WT1[feature-auth worktree]
        WT2[feature-api worktree]
        WT3[bugfix worktree]
    end

    Parallel --> WT1
    Parallel --> WT2
    Parallel --> WT3

    WT1 --> Merge[Develop & merge to main]
    WT2 --> Merge
    WT3 --> Merge

    Merge --> Clean[/craft:git:clean/]
    Clean --> Done([Worktrees cleaned])

    style Start fill:#e8f5e9,stroke:#4caf50
    style Add fill:#fff9c4,stroke:#fbc02d
    style Clean fill:#c8e6c9,stroke:#66bb6a
    style Done fill:#a5d6a7,stroke:#4caf50,stroke-width:3px
```

**Commands used:**
1. `/craft:git:worktree add <name>` - Create parallel workspace
2. `/craft:git:clean` - Remove merged worktrees

---

## Orchestrator Workflow

```mermaid
flowchart TD
    Start([Complex task]) --> Orch[/craft:orchestrate task mode/]

    Orch --> Analyze[Task analysis]
    Analyze --> Spawn[Spawn subagents]

    Spawn --> Agent1[arch-1: Design]
    Spawn --> Agent2[code-1: Implement]
    Spawn --> Agent3[test-1: Test]

    Agent1 --> Monitor[Monitor progress]
    Agent2 --> Monitor
    Agent3 --> Monitor

    Monitor --> Status{Check status}

    Status -->|In progress| Monitor
    Status -->|Complete| Report[Final report]

    Report --> Done([Task complete!])

    style Start fill:#e8f5e9,stroke:#4caf50
    style Orch fill:#fff9c4,stroke:#fbc02d
    style Monitor fill:#e1bee7,stroke:#8e24aa
    style Report fill:#c8e6c9,stroke:#66bb6a
    style Done fill:#a5d6a7,stroke:#4caf50,stroke-width:3px
```

**Commands used:**
1. `/craft:orchestrate <task> <mode>` - Launch orchestrator
2. `status` - Check agent dashboard during execution
3. `timeline` - View execution timeline

---

## Quick Command Finder

| I want to... | Use this workflow |
|--------------|-------------------|
| Update docs after coding | [Documentation Workflow](#documentation-workflow) |
| Create a new site | [Site Creation Workflow](#site-creation-workflow) |
| Test before committing | [Testing Workflow](#testing-workflow) |
| Prepare a release | [Release Workflow](#release-workflow) |
| Work on multiple features | [Git Worktree Workflow](#git-worktree-workflow) |
| Handle complex tasks | [Orchestrator Workflow](#orchestrator-workflow) |

## Next Steps

- **Try a workflow:** Pick one above and follow the diagram
- **Learn commands:** [Commands Overview](commands/overview.md)
- **Advanced:** [Orchestrator Mode](guide/orchestrator.md)
