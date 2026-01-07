# Workflow Plugin for Claude Code

**Version:** 2.1.0
**Author:** Data-Wise
**License:** MIT

> **ADHD-friendly workflow automation: brainstorm, focus, next, done, recap, stuck, task management, and design patterns**

**🎉 What's New in v2.1:**
- 📦 **10 workflow commands** - Complete ADHD workflow suite
- 🛠️ **Shell scripts** - Automation helpers for documentation updates
- 📚 **ADHD guide** - Best practices for ADHD-friendly development

**What's in v2.0:**
- ⏱️ Performance guarantees (quick <60s, default <5m, thorough <30m)
- 📊 Multiple output formats (terminal, json, markdown)
- 🎯 Explicit time budgets for all modes
- 📈 Backward compatible - all v0.1.0 commands still work!

---

## Overview

The Workflow Plugin enhances your development workflow with:

✨ **Auto-activating skills** - Backend, frontend, and DevOps guidance triggers automatically based on conversation keywords

⚡ **Smart brainstorming** - Enhanced `/brainstorm` command with mode detection and agent delegation

🤖 **Background delegation** - Automatically delegates complex analysis to specialized agents running in parallel

📊 **Result synthesis** - Combines multiple agent outputs into unified, actionable recommendations

🧠 **ADHD-friendly** - Scannable output, quick wins, clear next steps, reduced decision paralysis

---

## Commands (10 total)

### Core Workflow Commands

| Command | Description |
|---------|-------------|
| `/brainstorm` | Smart ideation with auto-delegation |
| `/focus` | Single-task mode with distraction blocking |
| `/next` | Decision support for what to work on next |
| `/done` | Session completion with context capture |
| `/recap` | Context restoration for returning to work |
| `/stuck` | Unblock helper with guided problem solving |
| `/refine` | Prompt optimizer for better AI interactions |

### Task Management Commands

| Command | Description |
|---------|-------------|
| `/task-status` | Check background task progress |
| `/task-output` | View background task results |
| `/task-cancel` | Cancel running background task |

### Documentation

| Resource | Description |
|----------|-------------|
| `/workflow:docs:adhd-guide` | Best practices for ADHD-friendly development |

---

## Features

### 1. Auto-Activating Skills (3 skills)

Skills that automatically provide guidance when relevant topics are discussed:

#### **backend-designer**
- **Triggers:** API design, database schema, authentication, caching
- **Provides:** Pragmatic backend patterns, "solid indie" architecture advice
- **Delegates to:** backend-architect, database-architect, security-specialist agents

#### **frontend-designer**
- **Triggers:** UI/UX design, component architecture, accessibility, responsive design
- **Provides:** ADHD-friendly design patterns, component structure, a11y guidance
- **Delegates to:** ux-ui-designer, frontend-specialist agents

#### **devops-helper**
- **Triggers:** CI/CD, deployment, Docker, infrastructure
- **Provides:** Platform recommendations, cost optimization, indie-friendly DevOps
- **Delegates to:** devops-engineer, performance-engineer agents

### 2. Enhanced Brainstorm Command (v2.0)

**Usage:**
```bash
/brainstorm                          # Auto-detect mode from context
/brainstorm feature                  # Feature brainstorm
/brainstorm architecture             # Architecture design
/brainstorm design                   # UI/UX design
/brainstorm quick                    # Fast ideation (< 1 min, no delegation)
/brainstorm thorough "topic"         # Deep analysis with agents (< 30 min)
/brainstorm --format json            # Output as JSON
/brainstorm --format markdown        # Output as markdown
```

**⏱️ Performance Guarantees (NEW in v2.0):**

| Mode | Time Budget | Delegation | Use When |
|------|-------------|------------|----------|
| **quick** | < 60s (MUST) | None | Fast decisions, familiar topics |
| **default** | < 5m (SHOULD) | Optional | Daily brainstorming needs |
| **thorough** | < 30m (MAX) | 2-4 agents | Architecture decisions, unfamiliar domains |

**Content Modes:**
- **feature** - User value, MVP scope, user stories
- **architecture** - System design, scalability, trade-offs
- **design** - UI/UX, accessibility, user experience
- **backend** - API design, database, auth patterns
- **frontend** - Components, state management, performance
- **devops** - CI/CD, deployment, infrastructure

**📊 Output Formats (NEW in v2.0):**
- **Terminal** (default) - Rich colors, emojis, ADHD-friendly
- **JSON** - Structured output for automation/APIs
- **Markdown** - Documentation-ready format

**Smart Features:**
- Auto-detects mode from conversation context
- Time budget enforcement with completion reports
- Launches 2-4 specialized agents in background (thorough mode)
- Provides immediate ideas while agents work
- Synthesizes agent findings into comprehensive plan
- Saves brainstorms in multiple formats

### 3. Workflow Orchestrator Agent

Manages complex workflows by:
- Analyzing task requirements
- Selecting appropriate specialized agents
- Running multiple agents in parallel (non-blocking)
- Monitoring progress with status updates
- Synthesizing results into unified recommendations

**Example orchestration:**
```
User: "Design user authentication with OAuth"

Orchestrator:
1. Launches 4 agents in parallel:
   - backend-architect (OAuth flow design)
   - security-specialist (security review)
   - ux-ui-designer (login UI design)
   - devops-engineer (secrets management)

2. Provides status updates:
   "✓ Security specialist completed (35s)"
   "✓ DevOps engineer completed (42s)"
   "✓ UX designer completed (58s)"
   "✓ Backend architect completed (1m 24s)"

3. Synthesizes into implementation plan with:
   - Backend setup steps
   - Frontend UI components
   - DevOps secrets configuration
   - Security checklist
   - Next steps (numbered, concrete)

Total time: ~1.5 min (4 agents in parallel, not 4+ min sequential!)
```

---

## Installation

### Option 1: Manual Installation (Recommended for Development)

```bash
cd ~/.claude/plugins
git clone https://github.com/Data-Wise/claude-plugins.git temp
mv temp/workflow .
rm -rf temp
```

### Option 2: Symlink for Development

```bash
cd ~/.claude/plugins
ln -s /path/to/claude-plugins/workflow workflow
```

### Verify Installation

```bash
# Restart Claude Code, then check:
ls ~/.claude/plugins/workflow

# You should see:
# .claude-plugin/
# commands/
# skills/
# agents/
# README.md
```

---

## Quick Start

### 1. Auto-Activating Skills (Zero Setup)

Skills activate automatically when you discuss relevant topics:

```
You: "I need to design a REST API for user management"

→ backend-designer skill auto-activates
→ Provides API design patterns (RESTful resources, auth strategies)
→ May delegate to backend-architect agent for deep analysis
```

No explicit invocation needed!

### 2. Brainstorming

**Quick brainstorm** (5 ideas, no delegation):
```
/brainstorm quick feature user notifications
```

**Thorough brainstorm** (comprehensive analysis with agents):
```
/brainstorm thorough multi-tenant SaaS architecture
```

**Auto-detected mode** (analyzes conversation context):
```
You: "I'm thinking about how to handle user authentication"
/brainstorm

→ Detects backend topic
→ Launches backend-architect + security-specialist agents
→ Generates comprehensive auth implementation plan
```

### 3. Design Philosophy

All guidance follows **"Solid Indie" principles:**

✅ **Ship fast** - Pragmatic solutions over perfect architecture
✅ **Proven patterns** - Boring technology that works
✅ **Right-sized** - Complexity matches team size
✅ **Cost-conscious** - Indie developer budget (~$50/month)

❌ **Avoid over-engineering** - No microservices for small teams
❌ **No premature optimization** - Ship functionality first
❌ **No corporate patterns** - Generic repositories, complex abstractions

---

## Usage Examples

### Example 1: API Design with Auto-Activation

```
You: "I need to add pagination to my API endpoints"

→ backend-designer skill activates
→ Suggests cursor-based vs offset pagination
→ Provides implementation examples
→ Notes trade-offs (cursor = better perf, offset = simpler)
→ Recommends offset for MVP, cursor for scale
```

### Example 2: UI Component Design

```
You: "How should I structure my dashboard components?"

→ frontend-designer skill activates
→ Suggests component composition pattern
→ Recommends card-based layout for scannability
→ Provides accessibility checklist
→ May delegate to ux-ui-designer agent for comprehensive review
```

### Example 3: Deployment Strategy

```
You: "I need to deploy my Next.js app with PostgreSQL"

→ devops-helper skill activates
→ Recommends Vercel (Next.js) + Supabase (PostgreSQL)
→ Estimates cost ($0 for MVP, ~$25/month at scale)
→ Provides CI/CD setup (GitHub Actions + Vercel auto-deploy)
→ Outlines environment variables strategy
```

### Example 4: Comprehensive Feature Brainstorm

```
/brainstorm thorough real-time collaboration feature

Response:
1. Auto-detects architecture + frontend topics
2. Launches 3 agents in parallel:
   - backend-architect (WebSocket vs SSE vs polling)
   - frontend-specialist (state synchronization)
   - performance-engineer (scaling considerations)
3. Provides immediate ideas while agents work
4. After ~2 min, synthesizes comprehensive plan:
   - Technology recommendation (WebSocket via Socket.io)
   - State sync strategy (operational transforms)
   - Scaling approach (Redis pub/sub)
   - Implementation steps (numbered, concrete)
   - Cost estimate (~$15/month for 1K users)
5. Saves to BRAINSTORM-real-time-collaboration-2025-12-23.md
```

---

## Plugin Structure

```
workflow/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── commands/
│   ├── brainstorm.md            # Smart ideation with delegation
│   ├── done.md                  # Session completion & context capture
│   ├── focus.md                 # Single-task mode
│   ├── next.md                  # Decision support
│   ├── recap.md                 # Context restoration
│   ├── refine.md                # Prompt optimizer
│   ├── stuck.md                 # Unblock helper
│   ├── task-cancel.md           # Cancel background tasks
│   ├── task-output.md           # View task results
│   ├── task-status.md           # Check task progress
│   └── docs/
│       └── adhd-guide.md        # ADHD best practices
├── lib/                         # 🆕 Shell automation scripts (v2.1)
│   ├── detect-changelog.sh      # Detect CHANGELOG needs
│   ├── detect-claude-md.sh      # Detect CLAUDE.md needs
│   ├── update-changelog.sh      # Auto-update CHANGELOG
│   ├── update-claude-md.sh      # Auto-update CLAUDE.md
│   ├── update-mkdocs-nav.sh     # Auto-update mkdocs.yml
│   └── run-all-updaters.sh      # Run all updaters
├── skills/
│   └── design/
│       ├── backend-designer.md  # Auto-activating backend skill
│       ├── frontend-designer.md # Auto-activating frontend skill
│       └── devops-helper.md     # Auto-activating DevOps skill
├── agents/
│   └── orchestrator.md          # Workflow orchestrator agent
├── workflow/                    # 🆕 Python package (v2.0)
│   ├── __init__.py              # Package exports
│   ├── mode_parser.py           # Command parsing (270 lines)
│   ├── time_budgets.py          # Time budget system (150 lines)
│   ├── format_handlers.py       # Output formatters (240 lines)
│   └── agent_delegation.py      # Agent selection (240 lines)
├── tests/                       # 🆕 Pytest test suite (v2.0)
│   ├── conftest.py              # Test fixtures (20+)
│   ├── unit/                    # Unit tests (157 tests)
│   │   ├── test_mode_parsing.py
│   │   ├── test_time_budgets.py
│   │   ├── test_format_handling.py
│   │   └── test_agent_delegation.py
│   ├── integration/             # Integration tests (32 tests)
│   │   └── test_brainstorm_workflow.py
│   ├── pytest.ini               # Pytest configuration
│   └── requirements-test.txt    # Test dependencies
├── docs/
│   ├── QUICK-START.md           # 5-minute getting started
│   ├── REFCARD.md               # One-page reference
│   └── README.md                # Documentation hub
├── .STATUS                      # 🆕 Current state tracking (v2.0)
├── TODO.md                      # 🆕 Task management (v2.0)
├── IDEAS.md                     # 🆕 Enhancement backlog (v2.0)
├── CHANGELOG.md                 # 🆕 Version history (v2.0)
├── README.md                    # This file
├── package.json                 # npm metadata
└── LICENSE                      # MIT license
```

---

## Configuration

### No Configuration Required!

The plugin works out of the box with sensible defaults.

### Optional: Customize Agent Behavior

Skills automatically delegate to agents when thorough analysis is needed. You can control delegation by:

**In conversation:**
- Use `/brainstorm quick` to skip agent delegation
- Use `/brainstorm thorough` to force deep analysis

**Agents used:**
- backend-architect (from experienced-engineer plugin)
- ux-ui-designer (from experienced-engineer plugin)
- devops-engineer (from experienced-engineer plugin)
- security-specialist (from experienced-engineer plugin)
- performance-engineer (from experienced-engineer plugin)

*Note: These agents must be installed separately (typically included in Claude Code).*

---

## Design Patterns Library

Skills reference proven patterns for common scenarios:

### Backend Patterns
- **RESTful API design** - Resources, HTTP methods, versioning
- **Authentication flows** - JWT vs sessions, OAuth 2.0, API keys
- **Database design** - Normalization, indexing, migrations
- **Caching strategies** - Redis, in-memory, CDN

### Frontend Patterns
- **Component composition** - Container/presentational, compound components
- **State management** - Context, Redux, Zustand (when to use which)
- **Accessibility** - WCAG checklist, keyboard nav, screen readers
- **Performance** - Code splitting, lazy loading, virtualization

### DevOps Patterns
- **CI/CD pipelines** - GitHub Actions, testing automation
- **Deployment platforms** - Vercel, Render, Fly.io (comparison)
- **Infrastructure** - Docker multi-stage builds, container orchestration
- **Cost optimization** - Free tier strategies, scaling thresholds

### ADHD-Friendly Patterns
- **Progressive disclosure** - Hide complexity behind toggles
- **Immediate feedback** - Loading states, success confirmations
- **Visual hierarchy** - Clear focus states, limited colors
- **Cognitive load reduction** - One action per screen, templates

---

## Troubleshooting

### Skills Not Auto-Activating

**Check:**
1. Plugin installed in `~/.claude/plugins/workflow/`
2. Skills directory present: `~/.claude/plugins/workflow/skills/design/`
3. Restart Claude Code

**Test activation:**
```
You: "I need to design a REST API"

Expected: backend-designer skill should activate and provide guidance
```

### Agent Delegation Not Working

**Possible causes:**
1. Missing experienced-engineer plugin (provides specialized agents)
2. Agent timed out (5 min max per agent)
3. Using quick mode (`/brainstorm quick` skips delegation)

**Check agent availability:**
```
# Should list agents: backend-architect, ux-ui-designer, devops-engineer, etc.
ls ~/.claude/plugins/experienced-engineer/agents/
```

### Brainstorm Files Not Saving

**Check:**
1. Write permissions in current directory
2. Fallback location: `~/brainstorms/` should be writable

**Manual save location:**
```bash
mkdir -p ~/brainstorms
chmod 755 ~/brainstorms
```

---

## Development

### Running Tests (v2.0 - Pytest)

```bash
cd ~/.claude/plugins/workflow

# Run all tests (189 tests)
python3 -m pytest

# Run with verbose output
python3 -m pytest -v

# Run only unit tests
python3 -m pytest -m unit

# Run only integration tests
python3 -m pytest -m integration

# Run with coverage report
python3 -m pytest --cov=workflow --cov-report=html
```

**Test Suite (189 tests, 100% passing):**
- **Unit tests** (157 tests):
  - Mode parsing: 38 tests
  - Time budgets: 40 tests
  - Format handlers: 40 tests
  - Agent delegation: 39 tests
- **Integration tests** (32 tests):
  - End-to-end workflow validation
  - Backward compatibility verification

**Test execution:** < 1 second (0.90s average)

**Test documentation:** See `TESTING-INFRASTRUCTURE.md` for complete guide

### Adding New Skills

1. Create skill file in `skills/[category]/[name].md`
2. Add frontmatter with triggers
3. Document auto-activation behavior
4. Update tests to expect new skill count

### Adding New Commands

1. Create command file in `commands/[name].md`
2. Add frontmatter with arguments
3. Document usage examples
4. Update tests

---

## Roadmap

### v2.0.0 (Current - Dec 24, 2024) 🎉 FULLY IMPLEMENTED
- [x] 3 auto-activating skills (backend, frontend, devops)
- [x] Enhanced /brainstorm command with delegation
- [x] Workflow orchestrator agent
- [x] Comprehensive documentation
- [x] **Time budget system** (quick <60s, default <5m, thorough <30m)
- [x] **Format handlers** (terminal, json, markdown)
- [x] **Performance guarantees** (MUST/SHOULD/MAX)
- [x] **Planning infrastructure** (.STATUS, TODO, IDEAS, CHANGELOG)
- [x] **🧪 Pytest testing infrastructure** (189 tests, 100% passing)
- [x] **📦 Core components implemented** (mode parser, time budgets, format handlers, agent delegation)
- [x] **📚 Comprehensive documentation** (~6,800 lines)
- [x] **✅ 100% backward compatible** with v0.1.0

**Quality Metrics:**
- 189/189 tests passing (100%)
- 0.90 seconds test execution time
- 972 lines of implementation code
- 2,607 lines of test code
- Zero bugs found
- Zero refactoring needed

### v2.1.0 (Next - Q1 2025)
**Deployment & Validation:**
- [ ] Dedicated CI/CD workflow
- [ ] Pre-commit hooks for quality
- [ ] Coverage reporting (Codecov)
- [ ] Performance validation in production
- [ ] User feedback integration

**Enhanced Features:**
- [ ] Mode aliases (/brainstorm:q for quick)
- [ ] Workflow presets
- [ ] Agent result caching

**Optional - New Commands** (validate need with user feedback first):
- [ ] /analyze command (architecture analysis)
- [ ] /review command (code review with quality + security)
- [ ] /optimize command (performance review)

### v3.0.0 (Future - Q2+ 2025)
- [ ] Custom modes in config
- [ ] Result caching for faster repeated queries
- [ ] Brainstorm templates
- [ ] Pattern library expansion (30+ additional patterns)

### v1.0.0 Long-Term Vision
- [ ] Custom skill creation wizard
- [ ] Integration with /done command (capture design decisions)
- [ ] Workflow templates (auth, payment, notifications)
- [ ] MCP server integration for external tools
- [ ] Community pattern sharing

---

## Contributing

This plugin follows "solid indie" principles:

1. **Ship fast** - PR merged quickly for working features
2. **Pragmatic** - Real-world usage over theoretical perfection
3. **ADHD-friendly** - Scannable docs, clear examples, quick wins

**How to contribute:**
1. Test with real projects
2. Share use cases that worked well
3. Suggest patterns that saved time
4. Report what felt over-engineered

**For plugin development:**
- 📖 **[Developer Guide (CLAUDE.md)](../CLAUDE.md)** - Comprehensive guide for working with this monorepo
- Development commands, architecture patterns, CI/CD workflows
- Quality standards and troubleshooting

---

## License

MIT License - see LICENSE file

---

## Links

- **Repository:** https://github.com/Data-Wise/claude-plugins
- **Documentation:** [docs/README.md](docs/README.md)
- **Quick Start:** [docs/QUICK-START.md](docs/QUICK-START.md)
- **Reference Card:** [docs/REFCARD.md](docs/REFCARD.md)

---

**Built with ❤️ for indie developers who ship fast and iterate based on real usage.**
