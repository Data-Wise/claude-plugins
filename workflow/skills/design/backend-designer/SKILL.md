---
name: backend-designer
description: This skill should be used when the user asks to "design an API", "plan backend architecture", "design a database schema", "set up authentication", "implement rate limiting", or "plan a caching strategy", or discusses REST, GraphQL, session management, or backend performance. Provides pragmatic backend design guidance following solid indie principles with delegation to specialist agents.
triggers:
  - API design
  - backend architecture
  - database schema
  - authentication
  - REST API
  - GraphQL
  - authentication flow
  - session management
  - rate limiting
  - caching strategy
---

# Backend Designer Skill

**Auto-activated when:** User discusses backend architecture, API design, database decisions, or authentication patterns.

## Core Capabilities

### 1. API Design Patterns
- RESTful API structure (resources, endpoints, versioning)
- GraphQL schema design
- API authentication (JWT, OAuth, API keys)
- Rate limiting and throttling strategies
- Error handling and status codes

### 2. Database Design
- Schema design (normalized vs denormalized)
- Index strategies for performance
- Migration planning
- ORM vs raw SQL trade-offs
- Connection pooling

### 3. Authentication & Authorization
- Session management (JWT vs session cookies)
- OAuth flows (authorization code, client credentials)
- Permission models (RBAC, ABAC)
- Secure token storage
- Password hashing (bcrypt, argon2)

### 4. Performance Patterns
- Caching strategies (Redis, in-memory, CDN)
- Query optimization
- Background jobs (Celery, Bull, Temporal)
- Horizontal scaling considerations
- Database read replicas

## Design Philosophy: Solid Indie

**Ship Fast Principles:**
- Start with monolith, extract services only when needed
- Use proven patterns, avoid trendy frameworks
- Prefer boring technology that works
- Document trade-offs, not just decisions

**Anti-Patterns to Avoid:**
- ❌ Microservices for < 5 person teams
- ❌ Over-abstraction (generic repositories, factories)
- ❌ Premature optimization
- ❌ Complex caching before measuring

## Delegation Strategy

When analysis is needed, I will:
1. **Analyze current state** - Review existing code/architecture
2. **Delegate to agents** when feasible:
   - `backend-architect` agent for deep architectural analysis
   - `database-architect` agent for schema optimization
   - `security-specialist` agent for auth review
3. **Run in background** - Use Task tool with `run_in_background: true`
4. **Synthesize results** - Combine agent outputs into actionable recommendations

## Example Activation

```
User: "I need to design an API for user authentication with social login"

Skill activates and provides:
1. Quick assessment of requirements
2. Recommends OAuth 2.0 flow (authorization code + PKCE)
3. Suggests passport.js or similar proven library
4. Outlines token storage strategy
5. Delegates security review to security-specialist agent (background)
6. Returns with comprehensive auth implementation plan
```

## Output Format

When activated, I provide:

### Immediate Response
- **Pattern Recognition**: Identify the design problem category
- **Quick Recommendation**: Suggest proven pattern
- **Trade-offs**: List pros/cons of approach

### Delegated Analysis (Background)
- Launch appropriate agent for deep analysis
- Provide progress updates
- Synthesize agent findings into actionable plan

### Final Output
- **Recommended approach** with rationale
- **Implementation steps** (numbered, concrete)
- **Code examples** (if requested)
- **Next steps** (what to build first)

## Integration with Existing Workflow

- Complements `/brainstorm` command (auto-activates during brainstorm sessions)
- Works with `/next` (suggests backend implementation steps)
- Integrates with `/done` (captures backend design decisions)

---

**Remember:** This skill auto-activates based on keywords. No explicit invocation needed. Keep responses focused, actionable, and indie-friendly (no corporate over-engineering).
