# Skills & Agents

⏱️ **6 minutes** • 🟡 Intermediate • ✓ Understanding AI automation

Understanding craft's AI-powered automation system.

## Skills (17 total)

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

## Agents (7 specialized)

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
