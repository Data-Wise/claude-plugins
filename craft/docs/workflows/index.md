# Visual Workflows

⏱️ **5 minutes** • 🟢 Beginner • ✓ See the big picture

> **TL;DR** (30 seconds)
> - **What:** 5 visual workflow diagrams showing how craft commands work together
> - **Why:** Understand the complete flow from start to finish for common tasks
> - **How:** Click any diagram to see the step-by-step process
> - **Next:** Try the [Documentation Workflow](#documentation-workflow) to automate your docs

Visual guides to craft's most common workflows - see how commands, skills, and agents work together.

!!! tip "Pro Tip: Start with Documentation"
    New to craft? The Documentation Workflow is the easiest starting point - just run `/craft:docs:update` and watch it detect and fix everything automatically.

---

## Documentation Workflow

**From code changes to deployed docs in one command.**

```mermaid
flowchart TD
    START([Code Changes]) --> UPDATE["/craft:docs:update"]

    UPDATE --> DETECT{Detect Changes}
    DETECT -->|CLI changes| CLI["Update CLI help epilogs"]
    DETECT -->|New features| FEAT["Generate feature guides"]
    DETECT -->|API changes| API["Update API reference"]

    CLI --> REFCARD["Update REFCARD.md"]
    FEAT --> REFCARD
    API --> REFCARD

    REFCARD --> CHECK["/craft:docs:check"]
    CHECK --> LINKS{Validate Links}
    LINKS -->|Broken| FIX["Auto-fix links"]
    LINKS -->|Valid| NAV["Check navigation"]
    FIX --> NAV

    NAV --> CHANGELOG["/craft:docs:changelog"]
    CHANGELOG --> DEPLOY["/craft:site:deploy"]
    DEPLOY --> DONE([Docs Live])

    click UPDATE "../commands/docs#craftdocsupdate" "Click to see full documentation"
    click CHECK "../commands/docs#craftdocscheck" "Click to see validation options"
    click CHANGELOG "../commands/docs#craftdocschangelog" "Click to see changelog generation"
    click DEPLOY "../commands/site#craftcreatecraftsitedeploy" "Click to see deployment options"

    style UPDATE fill:#e3f2fd
    style CHECK fill:#fff3e0
    style DEPLOY fill:#e8f5e9
```

**Key Commands:**
- `/craft:docs:update` - Smart detection → full execution
- `/craft:docs:check` - Validation with auto-fixes
- `/craft:docs:changelog` - Generate changelog from commits
- `/craft:site:deploy` - Deploy to GitHub Pages

**ADHD-Friendly:** Complete workflow in one command, clear progress at each step.

!!! success "Quick Win"
    Run `/craft:docs:update` right now - it takes < 30 seconds and shows instant results. No configuration needed!

---

## Site Creation Workflow

**Zero to deployed documentation site in under 5 minutes.**

```mermaid
flowchart LR
    START([Need Docs Site]) --> CREATE["/craft:site:create"]

    CREATE --> DETECT["Detect project type"]
    DETECT --> WIZARD{Interactive Wizard}

    WIZARD -->|Preset| PRESET["Choose from 8 presets"]
    WIZARD -->|Branding| BRAND["Set name & tagline"]
    WIZARD -->|Nav| NAV["Pick nav structure"]

    PRESET --> GEN["Generate files"]
    BRAND --> GEN
    NAV --> GEN

    GEN --> FILES["mkdocs.yml<br/>docs/index.md<br/>docs/QUICK-START.md<br/>.github/workflows/docs.yml"]

    FILES --> BUILD["/craft:site:build"]
    BUILD --> PREVIEW["/craft:site:preview"]
    PREVIEW --> REVIEW{Looks good?}

    REVIEW -->|No| THEME["/craft:site:theme"]
    THEME --> BUILD
    REVIEW -->|Yes| DEPLOY["/craft:site:deploy"]

    DEPLOY --> DONE([Site Live])

    click CREATE "../commands/site#craftcreate" "Click to see site creation wizard"
    click THEME "../commands/site#craftcreatecraftsitetheme" "Click to see theme options"
    click DEPLOY "../commands/site#craftcreatecraftsitedeploy" "Click to see deployment options"
    click PRESET "../reference/presets" "Click to see all 8 presets"

    style CREATE fill:#e3f2fd
    style WIZARD fill:#fff3e0
    style DEPLOY fill:#e8f5e9
```

**8 ADHD-Friendly Presets:**
- `adhd-focus` - Calm forest green
- `adhd-calm` - Warm earth tones
- `adhd-dark` - Dark-first mode
- `adhd-light` - Warm off-white
- `data-wise` - DT's standard (blue/orange)
- `minimal` - Clean and simple
- `open-source` - Community-friendly
- `corporate` - Professional

**Time to Deploy:** < 5 minutes with `--quick` flag

!!! tip "Pro Tip: Use --quick for Zero Prompts"
    Add `--quick` to skip all wizard prompts and use smart defaults: `/craft:site:create --preset adhd-focus --quick`

---

## Release Workflow

**From pre-release checks to published release.**

```mermaid
flowchart TD
    START([Ready to Release]) --> CHECK["/craft:check --for release"]

    CHECK --> AUDIT{Full Audit}
    AUDIT -->|Tests| TESTS["Run test suite"]
    AUDIT -->|Lint| LINT["Code quality checks"]
    AUDIT -->|Docs| DOCS["Docs validation"]
    AUDIT -->|Git| GIT["Git status clean"]

    TESTS --> RESULTS{All Pass?}
    LINT --> RESULTS
    DOCS --> RESULTS
    GIT --> RESULTS

    RESULTS -->|No| FIX["Fix issues"]
    FIX --> CHECK

    RESULTS -->|Yes| CHANGELOG["/craft:docs:changelog"]
    CHANGELOG --> VERSION["Update version"]
    VERSION --> TAG["Create git tag"]
    TAG --> PUSH["Push to remote"]

    PUSH --> GHRELEASE["GitHub Release triggers"]
    GHRELEASE --> PYPI["PyPI publish"]
    GHRELEASE --> BREW["Homebrew formula update"]
    GHRELEASE --> PAGES["GitHub Pages deploy"]

    PYPI --> DONE([Released])
    BREW --> DONE
    PAGES --> DONE

    style CHECK fill:#e3f2fd
    style RESULTS fill:#fff3e0
    style DONE fill:#e8f5e9
```

**Automation:**
- GitHub Actions triggers PyPI publish (trusted publisher)
- Homebrew formula updates via PR
- Docs deploy to GitHub Pages
- All from one release creation

**Safety:** Multiple validation gates prevent bad releases

!!! warning "Release Safety"
    `/craft:check --for release` will fail if tests fail, docs are stale, or git status is dirty. This prevents releasing broken code - fix issues before retrying.

---

## Development Workflow

**Feature branch to merged PR with git worktrees.**

```mermaid
flowchart TD
    START([New Feature]) --> WORKTREE["/craft:git:worktree add feature-name"]

    WORKTREE --> CLONE["Create worktree<br/>~/.git-wt/project/feature-name"]
    CLONE --> SWITCH["Switch terminal<br/>to worktree"]

    SWITCH --> DEV{Development}
    DEV -->|Write code| CODE["Implement feature"]
    DEV -->|Run tests| TEST["/craft:test:run debug"]
    DEV -->|Lint| LINT["/craft:code:lint optimize"]

    CODE --> CHECK["/craft:check"]
    TEST --> CHECK
    LINT --> CHECK

    CHECK --> VALID{Passes?}
    VALID -->|No| DEV
    VALID -->|Yes| DOCS["/craft:docs:update"]

    DOCS --> COMMIT["Git commit + push"]
    COMMIT --> PR["Create PR via gh"]
    PR --> REVIEW{Code Review}

    REVIEW -->|Changes| DEV
    REVIEW -->|Approved| MERGE["Merge PR"]

    MERGE --> CLEANUP["/craft:git:worktree remove"]
    CLEANUP --> DONE([Feature Complete])

    style WORKTREE fill:#e3f2fd
    style CHECK fill:#fff3e0
    style DONE fill:#e8f5e9
```

**Worktree Benefits:**
- Work on multiple features in parallel
- Keep main branch clean
- Instant context switching
- No stashing required

**Commands:**
- `/craft:git:worktree add` - Create feature worktree
- `/craft:git:worktree list` - See all worktrees
- `/craft:git:worktree remove` - Clean up after merge

---

## AI Routing Workflow

**How /craft:do routes tasks to the right tools.**

```mermaid
flowchart TD
    START(["/craft:do 'add auth'"]) --> ANALYZE["task-analyzer skill"]

    ANALYZE --> CLASSIFY{Task Type?}

    CLASSIFY -->|Backend work| BACKEND["backend-designer skill"]
    CLASSIFY -->|Testing needed| TEST["test-strategist skill"]
    CLASSIFY -->|Docs work| DOCS["Docs commands"]
    CLASSIFY -->|Complex| ORCHESTRATE["Orchestrator"]

    BACKEND --> ROUTE1{Choose Tool}
    ROUTE1 -->|Simple| CMD1["Direct command"]
    ROUTE1 -->|Complex| AGENT1["backend-architect agent"]

    TEST --> ROUTE2{Choose Tool}
    ROUTE2 -->|Unit tests| CMD2["/craft:test:run"]
    ROUTE2 -->|Strategy| AGENT2["test-strategist skill"]

    DOCS --> ROUTE3{Choose Tool}
    ROUTE3 -->|Update| CMD3["/craft:docs:update"]
    ROUTE3 -->|Site| CMD4["/craft:site:create"]

    ORCHESTRATE --> PARALLEL["Run in parallel"]
    PARALLEL --> SUB1["Backend agent"]
    PARALLEL --> SUB2["Test agent"]
    PARALLEL --> SUB3["Docs agent"]

    CMD1 --> DONE([Task Complete])
    AGENT1 --> DONE
    CMD2 --> DONE
    AGENT2 --> DONE
    CMD3 --> DONE
    CMD4 --> DONE
    SUB1 --> DONE
    SUB2 --> DONE
    SUB3 --> DONE

    click START "../commands/smart#craftdo" "Click to see universal command docs"
    click ORCHESTRATE "../guide/orchestrator" "Click to learn about orchestrator"
    click CMD3 "../commands/docs#craftdocsupdate" "Click to see docs automation"
    click CMD4 "../commands/site#craftcreate" "Click to see site creation"

    style ANALYZE fill:#e3f2fd
    style CLASSIFY fill:#fff3e0
    style ORCHESTRATE fill:#ffe0b2
    style DONE fill:#e8f5e9
```

**Three Layers:**

1. **Skills** (17 total) - Auto-triggered expertise
   - `task-analyzer` - Routes to appropriate tools
   - `backend-designer` - API/database/auth patterns
   - `test-strategist` - Test strategy recommendations

2. **Commands** (69 total) - Direct actions
   - `/craft:docs:update` - Documentation automation
   - `/craft:test:run` - Test execution
   - `/craft:code:lint` - Code quality checks

3. **Agents** (7 specialized) - Long-running complex tasks
   - `backend-architect` - Scalable API design
   - `docs-architect` - Comprehensive documentation
   - `api-documenter` - OpenAPI spec generation

**Mode System:**
- `default` (<10s) - Quick tasks, 2 agents max
- `debug` (<120s) - Verbose output, 1 agent (sequential)
- `optimize` (<180s) - 4 agents max, parallel execution
- `release` (<300s) - Thorough validation, full reports

**ADHD-Friendly:** One command handles routing, you don't need to remember which tool to use.

---

## Quick Reference

| Workflow | Start Command | Time | ADHD Score |
|----------|--------------|------|------------|
| Documentation | `/craft:docs:update` | < 30s | ⭐⭐⭐⭐⭐ |
| Site Creation | `/craft:site:create --quick` | < 5m | ⭐⭐⭐⭐⭐ |
| Release | `/craft:check --for release` | < 2m | ⭐⭐⭐⭐ |
| Development | `/craft:git:worktree add name` | varies | ⭐⭐⭐⭐ |
| AI Routing | `/craft:do "task"` | varies | ⭐⭐⭐⭐⭐ |

## Next Steps

- **Try a workflow:** Pick one diagram above and run the first command
- **Combine workflows:** Use `/craft:orchestrate` to run multiple workflows
- **Learn more:** Read the [Orchestrator Guide](../guide/orchestrator.md)
- **Reference:** Check the [Quick Reference Card](../REFCARD.md)
