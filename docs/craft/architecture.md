# Craft Architecture

Craft is a comprehensive full-stack development toolkit built on intelligent orchestration, mode-aware execution, and multi-agent coordination.

## Architecture Overview

```mermaid
graph TB
    User[User Request] --> Router{Smart Router<br/>/craft:do}

    Router --> |Auth| PatternA[Authentication Pattern]
    Router --> |Perf| PatternP[Performance Pattern]
    Router --> |Release| PatternR[Release Pattern]
    Router --> |Custom| PatternC[Custom Pattern]

    PatternA --> Orch[Orchestrator v2]
    PatternP --> Orch
    PatternR --> Orch
    PatternC --> Orch

    Orch --> Mode{Execution Mode}

    Mode --> |default <10s| Mode1[Quick Checks]
    Mode --> |debug <120s| Mode2[Verbose Output]
    Mode --> |optimize <180s| Mode3[Max Parallel]
    Mode --> |release <300s| Mode4[Full Audit]

    Mode1 --> Agents
    Mode2 --> Agents
    Mode3 --> Agents
    Mode4 --> Agents

    Agents[Agent Pool] --> |Parallel| A1[backend-architect]
    Agents --> |Parallel| A2[frontend-specialist]
    Agents --> |Parallel| A3[database-architect]
    Agents --> |Parallel| A4[security-specialist]
    Agents --> |Parallel| A5[performance-engineer]
    Agents --> |Parallel| A6[devops-engineer]
    Agents --> |Parallel| A7[ux-ui-designer]

    A1 --> Synthesis[Result Synthesis]
    A2 --> Synthesis
    A3 --> Synthesis
    A4 --> Synthesis
    A5 --> Synthesis
    A6 --> Synthesis
    A7 --> Synthesis

    Synthesis --> Output[User-Friendly Output]

    style User fill:#e1f5ff
    style Router fill:#ffe1f5
    style Orch fill:#fff4e1
    style Mode fill:#e1ffe1
    style Agents fill:#f0e1ff
    style Synthesis fill:#ffe1e1
    style Output fill:#e1f5ff
```

## Core Components

### 1. Smart Routing System

The `/craft:do` command uses AI to route tasks to appropriate workflows:

```
"add authentication" → backend-architect + security-specialist
"optimize queries" → performance-engineer + database-architect
"prepare release" → orchestrator (release mode, all agents)
```

### 2. Orchestrator v2

Enhanced multi-agent orchestration with:
- **Mode-aware execution** - Adapts behavior based on mode
- **Context tracking** - Monitors token usage and budget
- **Timeline view** - Visualizes agent execution
- **Subagent monitoring** - Tracks agent progress
- **Result synthesis** - Combines agent outputs

### 3. Mode System

Four execution modes control depth and time:

| Mode | Time | Agents | Use Case |
|------|------|--------|----------|
| default | <10s | 1-2 | Quick checks |
| debug | <120s | 2-3 | Verbose diagnostics |
| optimize | <180s | 3-4 | Parallel performance |
| release | <300s | 4+ | Comprehensive audit |

### 4. Agent Coordination

Agents execute in parallel with automatic coordination:

```python
async def orchestrate(task, mode):
    # Pattern recognition
    pattern = recognize_pattern(task)

    # Agent selection
    agents = select_agents(pattern, mode)

    # Parallel execution
    results = await Promise.all([
        agent1.execute(),
        agent2.execute(),
        agent3.execute()
    ])

    # Synthesis
    return synthesize(results)
```

## Command Organization

Commands organized in 13 categories:

```
craft/commands/
├── arch/          # Architecture analysis
├── ci/            # CI/CD automation
├── code/          # Code quality
├── dist/          # Distribution
├── docs/          # Documentation
├── git/           # Git operations
├── plan/          # Planning
├── site/          # Static sites
├── test/          # Testing
├── check.md       # Pre-flight checks
├── do.md          # Smart routing
├── hub.md         # Discovery
└── orchestrate.md # Orchestration
```

## Python Testing Framework

Craft includes comprehensive Python-based testing:

```
tests/
├── unit/              # Unit tests
├── integration/       # Integration tests
├── performance/       # Performance benchmarks
└── test_craft.py      # Main test suite
```

**Run tests:**
```bash
cd craft
pytest tests/
pytest tests/ --cov=craft
```

## Performance

- **Parallel execution:** 3-4× faster than sequential
- **Smart caching:** Reduces redundant operations
- **Incremental analysis:** Only checks changed code
- **Token-efficient:** Optimized prompts and context

## Extensibility

Craft is designed for easy extension:

1. **Add commands:** Create markdown in `commands/category/`
2. **Add skills:** Create skill definitions in `skills/domain/`
3. **Add agents:** Define agents in `agents/`
4. **Add modes:** Extend mode system with custom time budgets

## See Also

- **[Commands Reference](commands.md)** - All commands
- **[Skills & Agents](skills-agents.md)** - 17 skills, 7 agents
- **[Orchestrator Guide](orchestrator.md)** - Coordination details

---

**Last Updated:** 2026-01-09
**Document Version:** v1.10.0
**Status:** ✅ Production ready - Smart routing and delegation patterns
