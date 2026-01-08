# Craft Skills & Agents

Craft includes 17 auto-activating skills and 7 specialized agents for comprehensive development support.

## Skills

Skills automatically activate based on conversation context, providing just-in-time expertise.

### 17 Built-in Skills

**Backend Development (3)**
- `api-architect` - REST/GraphQL API design, authentication, data modeling
- `database-architect` - Schema design, query optimization, indexing
- `backend-patterns` - Clean architecture, microservices, event-driven systems

**Frontend Development (2)**
- `frontend-architect` - Component design, state management, performance
- `ux-designer` - User experience, accessibility, responsive design

**DevOps & Infrastructure (3)**
- `devops-engineer` - CI/CD, Docker, Kubernetes, cloud infrastructure
- `performance-engineer` - Profiling, optimization, load testing
- `security-specialist` - OWASP, authentication, secure coding

**Code Quality (3)**
- `code-reviewer` - Code review, best practices, clean code
- `testing-specialist` - Test strategy, TDD/BDD, coverage
- `refactoring-expert` - Code smells, design patterns, technical debt

**Documentation & Communication (3)**
- `documentation-writer` - API docs, README, architecture docs
- `technical-writer` - Clear communication, tutorials, guides
- `api-documenter` - OpenAPI, interactive docs, SDK generation

**Leadership & Strategy (3)**
- `tech-lead` - Architecture decisions, technical strategy, team coordination
- `product-strategist` - Feature prioritization, roadmapping, user research
- `agile-coach` - Sprint planning, retrospectives, team dynamics

### Skill Activation

Skills trigger automatically based on keywords:

**Example:**
```
User: "How should I design the authentication API?"
→ Activates: api-architect, security-specialist
→ Provides: API design patterns, OAuth2 guidance, security best practices
```

## Agents

Specialized agents can be invoked explicitly or delegated to by the orchestrator.

### 7 Specialized Agents

#### backend-architect
**Purpose:** Server-side design, API architecture, database design

**Use cases:**
- Designing RESTful or GraphQL APIs
- Database schema optimization
- Authentication/authorization systems
- Scalable backend architecture

**Invoke:**
```bash
# Via orchestrator
/craft:orchestrate "design authentication API" optimize

# Via Task tool (background)
@backend-architect "design user authentication system"
```

#### performance-engineer
**Purpose:** Application performance optimization

**Use cases:**
- Identifying bottlenecks
- Load testing strategies
- Caching implementation
- Query optimization

**Invoke:**
```bash
/craft:orchestrate "optimize database queries" optimize
```

#### testing-specialist
**Purpose:** Comprehensive testing strategies

**Use cases:**
- Test strategy development
- Unit/integration/e2e testing
- Test coverage improvement
- TDD/BDD implementation

**Invoke:**
```bash
/craft:orchestrate "improve test coverage" release
```

#### security-specialist
**Purpose:** Security audits and secure coding

**Use cases:**
- OWASP vulnerability assessment
- Authentication/authorization review
- Secure coding practices
- Security audit preparation

**Invoke:**
```bash
/craft:orchestrate "security audit" release
```

#### devops-engineer
**Purpose:** CI/CD and deployment automation

**Use cases:**
- Pipeline setup and optimization
- Docker/Kubernetes configuration
- Cloud infrastructure (AWS/GCP/Azure)
- Deployment strategies

**Invoke:**
```bash
/craft:orchestrate "setup CI/CD pipeline" optimize
```

#### tech-lead
**Purpose:** Technical leadership and coordination

**Use cases:**
- Architectural decisions
- Technical strategy
- Team coordination
- Technical debt management

**Invoke:**
```bash
/craft:orchestrate "plan technical roadmap" release
```

#### code-quality-reviewer
**Purpose:** Code quality standards and best practices

**Use cases:**
- Code review automation
- Refactoring guidance
- Design pattern application
- Clean code principles

**Invoke:**
```bash
/craft:orchestrate "code review" debug
```

## Orchestrator Integration

The orchestrator intelligently selects and coordinates agents based on task requirements.

### Multi-Agent Coordination

**Example workflow:**
```
User: "Prepare application for production release"

Orchestrator analyzes request
→ Pattern: PRODUCTION_RELEASE
→ Mode: release (comprehensive)

Launches agents in parallel:
1. security-specialist    - Security audit
2. performance-engineer   - Performance check
3. testing-specialist     - Full test suite
4. devops-engineer        - Deployment readiness

Waits for all agents to complete (5-10 minutes)

Synthesizes results:
✅ Security: No critical vulnerabilities
⚠️  Performance: 2 slow queries identified
✅ Tests: 245/245 passing, 85% coverage
✅ DevOps: CI/CD pipeline ready

Recommendations:
1. Optimize identified slow queries (priority)
2. Increase test coverage to 90% (recommended)
3. Ready for production deployment
```

### Agent Communication

Agents can communicate and coordinate:

```
security-specialist: "Found potential SQL injection in login endpoint"
→ Notifies backend-architect
→ backend-architect: "Refactoring with parameterized queries"
→ Notifies testing-specialist
→ testing-specialist: "Adding security test cases"
```

## Mode-Aware Behavior

Agents adapt their behavior based on mode:

| Mode | Agent Behavior |
|------|----------------|
| **default** | Quick analysis, high-level recommendations |
| **debug** | Verbose output, detailed traces, step-by-step |
| **optimize** | Parallel execution, focus on performance |
| **release** | Comprehensive audit, production-ready checks |

**Example:**
```bash
# Quick check
/craft:orchestrate "check code quality"
→ Agents: [code-quality-reviewer]
→ Time: <10s
→ Output: High-level summary

# Comprehensive audit
/craft:orchestrate "check code quality" release
→ Agents: [code-quality-reviewer, security-specialist, performance-engineer]
→ Time: <5 minutes
→ Output: Detailed report with actionable items
```

## Best Practices

### When to Use Skills vs Agents

**Use Skills (automatic):**
- Conversational guidance
- Just-in-time expertise
- No explicit invocation needed

**Use Agents (explicit):**
- Complex multi-step tasks
- Background processing
- Coordinated multi-agent workflows
- Production-ready deliverables

### Combining Skills and Agents

**Optimal workflow:**
1. Start conversation (skills activate automatically)
2. Get general guidance from skills
3. When ready to implement, invoke agents via orchestrator
4. Agents execute in parallel with skills providing context

### Agent Selection Tips

- **Single focus:** Use specific agent (`@backend-architect`)
- **Multiple concerns:** Use orchestrator to coordinate agents
- **Quick tasks:** Let orchestrator choose (default mode)
- **Complex projects:** Specify release mode for comprehensive coverage

## See Also

- **[Commands Reference](commands.md)** - All 67 commands
- **[Architecture Guide](architecture.md)** - How Craft works
- **[Orchestrator Guide](orchestrator.md)** - Multi-agent coordination
