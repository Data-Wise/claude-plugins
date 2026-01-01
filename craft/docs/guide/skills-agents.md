# Skills & Agents

⏱️ **6 minutes** • 🟡 Intermediate • ✓ Understanding AI automation

> **TL;DR** (30 seconds)
> - **What:** 21 auto-triggered skills + 8 specialized agents for backend, docs, testing, and architecture
> - **Why:** AI automatically selects the right expertise for your task without manual intervention
> - **How:** Skills trigger on context (e.g., "API" → backend-designer), agents handle long-running tasks
> - **Next:** Read [Orchestrator](orchestrator.md) to learn how they work together

## Skills (21 total)

Skills are auto-triggered expertise modules that activate based on context.

### Design Skills

- **backend-designer** - Triggers: API, database, auth
- **frontend-designer** - Triggers: UI/UX, components
- **system-architect** - Triggers: System design

### Testing Skills

- **test-strategist** - Triggers: Test strategy
- **cli-test-strategist** - Triggers: CLI testing

### Development Skills

- **devops-helper** - Triggers: CI/CD, deployment
- **project-planner** - Triggers: Feature planning
- **mode-controller** - Manages mode behavior
- **task-analyzer** - Routes tasks to appropriate tools

### Documentation Skills

- **changelog-automation** - Patterns for changelogs
- **architecture-decision-records** - ADR generation
- **doc-classifier** - Documentation type detection (guide, reference, tutorial, etc.)
- **mermaid-linter** - Mermaid diagram syntax validation and fixing

### Distribution Skills

- **distribution-strategist** - Multi-channel distribution planning (Homebrew, PyPI, npm)
- **homebrew-formula-expert** - Homebrew formula syntax and best practices
- **homebrew-workflow-expert** - GitHub Actions automation for tap releases
- **homebrew-setup-wizard** - Guided Homebrew setup implementation
- **homebrew-multi-formula** - Managing multiple formulas in a tap

### Infrastructure Skills

- **session-state** - Orchestrator state tracking and session management
- **project-detector** - Auto-detect project type (Python, Node, R, Rust, Go, etc.)

## Agents (8 specialized)

Agents are long-running AI assistants for complex tasks.

### Backend Development

**backend-architect**
- Scalable API design
- Microservices architecture
- REST/GraphQL/gRPC patterns

### Documentation

**docs-architect**
- Comprehensive technical documentation
- Long-form technical manuals
- Architecture guides

**api-documenter**
- OpenAPI 3.1 documentation
- SDK generation
- Developer portal creation

**tutorial-engineer**
- Step-by-step tutorials
- Progressive learning experiences
- Hands-on examples

**reference-builder**
- API references
- Configuration guides
- Searchable documentation

### Visualization

**mermaid-expert**
- Flowcharts, sequence diagrams
- ERDs, architecture diagrams
- All Mermaid diagram types

**demo-engineer**
- VHS tape file generation
- Terminal recording scripts
- GIF demonstration creation

### Orchestration

**orchestrator-v2**
- Multi-agent task decomposition
- Parallel execution with monitoring
- Context compression and session management
- ADHD-friendly status tracking

*Note: The original `orchestrator` agent still exists for backward compatibility but orchestrator-v2 is the recommended version with enhanced features (v1.1.0+).*

## How They Work Together

When you run `/craft:do "add authentication"`:

1. **task-analyzer** skill routes the task
2. **backend-designer** skill provides expertise
3. **backend-architect** agent (if needed) implements
4. **test-strategist** skill suggests testing approach

## Triggering Specific Agents

Use the Task tool directly:

```bash
# In your prompt to Claude
"Use the backend-architect agent to design the API"
```

## Next Steps

- [Orchestrator](orchestrator.md) - Advanced orchestration
- [Getting Started](getting-started.md) - Basic usage
