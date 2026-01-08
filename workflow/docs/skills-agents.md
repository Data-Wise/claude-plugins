# Workflow Skills & Agents

3 auto-activating skills that provide just-in-time expertise for backend, frontend, and DevOps work.

## Auto-Activating Skills

Skills automatically activate based on conversation keywords, providing guidance without explicit invocation.

### backend-designer

**Purpose:** Pragmatic backend architecture and API design

**Triggers on:**
- API design, REST, GraphQL
- Database schema, migrations
- Authentication, authorization, JWT, OAuth
- Caching, Redis, performance
- Microservices, monolith

**Provides:**
- API design patterns
- Database schema recommendations
- Authentication strategies
- Scalability guidance
- "Solid indie" architecture advice (pragmatic over perfect)

**Example activation:**
```
User: "How should I structure the authentication API?"
→ backend-designer activates
→ Provides: REST endpoints, JWT strategy, database schema
```

**Delegates to agents:**
- backend-architect
- database-architect
- security-specialist

### frontend-designer

**Purpose:** ADHD-friendly UI/UX and component architecture

**Triggers on:**
- UI/UX design, interface, layout
- Component architecture, React, Vue, Svelte
- Accessibility, a11y, WCAG
- Responsive design, mobile-first
- State management, Redux, Context

**Provides:**
- ADHD-friendly design patterns
- Component structure recommendations
- Accessibility guidelines (WCAG AA/AAA)
- Responsive design strategies
- State management patterns

**Example activation:**
```
User: "Design the user dashboard component"
→ frontend-designer activates
→ Provides: Component structure, a11y checklist, mobile considerations
```

**Delegates to agents:**
- ux-ui-designer
- frontend-specialist

### devops-helper

**Purpose:** Indie-friendly DevOps and infrastructure

**Triggers on:**
- CI/CD, GitHub Actions, pipelines
- Deployment, hosting, infrastructure
- Docker, containers, Kubernetes
- Cloud, AWS, GCP, Azure, Vercel
- Monitoring, logging, observability

**Provides:**
- Platform recommendations (cost-optimized)
- CI/CD pipeline templates
- Container strategies
- Deployment automation
- Cost optimization tips

**Example activation:**
```
User: "Set up CI/CD for my Node app"
→ devops-helper activates
→ Provides: GitHub Actions workflow, deployment strategy, cost estimate
```

**Delegates to agents:**
- devops-engineer
- performance-engineer

## Agent Delegation

Skills can delegate to specialized agents for complex work:

### Delegation Flow

```
User asks question
    ↓
Skill activates (provides guidance)
    ↓
If task is complex
    ↓
Skill delegates to agent(s)
    ↓
Agent executes in background
    ↓
Results synthesized and returned
```

### Example: Full-Stack Feature

```
User: "Implement user authentication with OAuth"

1. backend-designer activates
   → Provides initial guidance
   → Delegates to: backend-architect + security-specialist

2. frontend-designer activates
   → Provides UI guidance
   → Delegates to: ux-ui-designer

3. devops-helper activates
   → Provides deployment guidance
   → Delegates to: devops-engineer

All agents run in parallel (2-3 minutes)

Results synthesized:
✅ Backend: OAuth2 implementation plan
✅ Frontend: Login component design
✅ DevOps: Deployment configuration
```

## Skill Coordination

Multiple skills work together seamlessly:

### Backend + Frontend Coordination

```
Task: "Add real-time notifications"

backend-designer:
→ WebSocket server design
→ Database schema for notifications
→ API endpoints

frontend-designer:
→ Notification component
→ Real-time UI updates
→ Accessibility for notifications

Results combined into unified plan
```

### Frontend + DevOps Coordination

```
Task: "Deploy React app to production"

frontend-designer:
→ Production build optimization
→ Code splitting strategy
→ Performance checklist

devops-helper:
→ CDN configuration
→ CI/CD for frontend
→ Cache headers

Results: Complete deployment guide
```

## ADHD-Friendly Design

Skills are designed with ADHD considerations:

### Fast Feedback

- Immediate activation (no explicit invocation)
- Quick initial guidance (<10s)
- Background delegation for deep work

### Clear Structure

- Scannable bullet points
- Visual hierarchy (emojis, sections)
- Numbered action items

### Reduced Paralysis

- One clear recommendation
- Escape hatches (alternatives)
- Quick wins highlighted

### Context Preservation

- Skills remember conversation context
- Build on previous guidance
- Connect related concepts

## Practical Usage Tips

### Let Skills Activate Naturally

**Don't:**
```bash
/invoke-skill backend-designer "how do I..."
```

**Do:**
```
"How should I structure the authentication API?"
```
Skills activate automatically based on keywords.

### Use Conversation Flow

**Effective:**
```
1. "Design user authentication system"  # Skills activate
2. Review guidance
3. "Implement OAuth2 flow"             # More specific
4. Review detailed plan
5. "Show me the code"                  # Implementation
```

**Less effective:**
```
"Give me everything about authentication at once"
```

### Combine with Commands

Skills provide guidance, commands execute:

```
1. Ask about feature design  # Skills activate, provide plan
2. /focus "implement feature"  # Command sets focus
3. Continue conversation     # Skills guide implementation
4. /done                     # Command captures completion
```

## See Also

- **[Commands Reference](commands.md)** - 12 workflow commands
- **ADHD Guide:** `/workflow:docs:adhd-guide`
