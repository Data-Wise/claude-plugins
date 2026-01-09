# Workflow Plugin - Reference Card

> **Version:** 2.1.6 | **Last Updated:** 2025-12-29

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  WORKFLOW PLUGIN REFERENCE                                         v2.1.6  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  COMMANDS (1)                      │  AUTO-ACTIVATING SKILLS (3)           │
│  ─────────                         │  ─────────────────────────            │
│  /brainstorm [mode] [topic]        │  • backend-designer                   │
│    Enhanced brainstorm with        │    Auto-activates: API design,        │
│    smart detection & delegation    │    database, auth, caching            │
│                                    │                                       │
│  Modes:                            │  • frontend-designer                  │
│    • feature      (MVP scope)      │    Auto-activates: UI/UX,             │
│    • architecture (system design)  │    components, a11y, responsive       │
│    • design       (UI/UX)          │                                       │
│    • backend      (API/DB)         │  • devops-helper                      │
│    • frontend     (components)     │    Auto-activates: CI/CD,             │
│    • devops       (deployment)     │    Docker, deployment, hosting        │
│    • quick        (fast, no agents)│                                       │
│    • thorough     (deep + agents)  │                                       │
│                                    │                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  AGENTS (Background Delegation)                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  workflow-orchestrator - Manages parallel agent execution & synthesis      │
│                                                                             │
│  Delegates to (from experienced-engineer plugin):                          │
│    • backend-architect       • ux-ui-designer        • devops-engineer     │
│    • database-architect      • frontend-specialist   • performance-eng     │
│    • security-specialist     • testing-specialist    • code-quality-rev    │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  SKILL AUTO-ACTIVATION TRIGGERS                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  backend-designer                  │  frontend-designer                    │
│  ────────────────                  │  ─────────────────                    │
│  • API design, REST, GraphQL       │  • UI design, UX design               │
│  • database schema, migration      │  • component architecture             │
│  • authentication, OAuth, JWT      │  • accessibility, a11y, WCAG          │
│  • session management              │  • responsive design, layout          │
│  • rate limiting, caching          │  • React/Vue component                │
│                                    │  • state management, form design      │
│  devops-helper                     │                                       │
│  ─────────────                     │  All skills provide:                  │
│  • CI/CD, deployment               │    ✓ Immediate pattern guidance       │
│  • Docker, container, Kubernetes   │    ✓ Trade-off analysis               │
│  • GitHub Actions, pipeline        │    ✓ "Solid indie" advice             │
│  • infrastructure, hosting         │    ✓ Agent delegation (when needed)   │
│  • environment variables           │    ✓ ADHD-friendly format             │
│                                    │                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  BRAINSTORM COMMAND - INTERACTIVE FLOW (v2.1.6)                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  /brainstorm (no args)             │  /brainstorm "topic"                  │
│  ──────────────────────            │  ────────────────────                 │
│  NEW SESSION:                      │  Shows interactive menus:             │
│    Q-1: Resume previous session?   │    Q1: Depth? (default/quick/thorough)│
│      ○ Resume: [last topic]        │    Q2: Focus? (auto/feature/arch/...)│
│      ○ Resume: [2nd last]          │    → Executes with selections         │
│      ○ Start fresh                 │                                       │
│                                    │                                       │
│  EXISTING SESSION:                 │  /brainstorm feature "auth"           │
│    Smart context detection:        │  ─────────────────────────            │
│    • 1 topic  → uses it            │  Skips menus, executes directly       │
│    • 2-4 topics → asks which       │                                       │
│    • 0/5+ topics → asks free-form  │  /brainstorm quick feature "auth"     │
│    Then: Q1 → Q2 → Execute         │  ───────────────────────────────      │
│                                    │  Full args: skips all menus           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  INTERACTIVE MENU QUESTIONS                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Q-1: Session Resume (new session) │  Q0: Topic (multiple detected)        │
│  ────────────────────────────────  │  ────────────────────────────         │
│  "Continue or start fresh?"        │  "Which topic to brainstorm?"         │
│    ○ Resume: [topic] - [time]      │    ○ [Topic from conversation]        │
│    ○ Resume: [topic 2] - [time]    │    ○ [Topic from git branch]          │
│    ○ Start fresh                   │    ○ [Topic from .STATUS]             │
│                                    │                                       │
│  Q1: Depth Selection               │  Q2: Focus Selection                  │
│  ───────────────────               │  ──────────────────                   │
│  "How deep should analysis be?"    │  "What's the focus area?"             │
│    ○ default (< 5 min)             │    ○ auto-detect (Recommended)        │
│    ○ quick (< 1 min, no agents)    │    ○ feature (user stories, MVP)      │
│    ○ thorough (< 30 min, agents)   │    ○ architecture (system design)     │
│                                    │    ○ backend (API, database)          │
│                                    │  (frontend/design/devops via "Other") │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  DEPTH × FOCUS MATRIX                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│  Depth      │ Time    │ Agents │ Best For                                  │
│  ─────      │ ────    │ ────── │ ────────                                  │
│  quick      │ < 1 min │ None   │ Fast decisions, familiar topics           │
│  default    │ < 5 min │ Maybe  │ Daily brainstorming, balanced             │
│  thorough   │ < 30min │ 2-4    │ Architecture decisions, new domains       │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  OUTPUT FORMAT (ADHD-Friendly)                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  All brainstorms follow this structure:                                    │
│                                                                             │
│    ## Quick Wins (< 30 min each)                                           │
│    1. ⚡ [Action] - [Benefit]                                               │
│    2. ⚡ [Action] - [Benefit]                                               │
│                                                                             │
│    ## Medium Effort (1-2 hours)                                            │
│    - [ ] [Task with clear outcome]                                         │
│                                                                             │
│    ## Long-term (Future sessions)                                          │
│    - [ ] [Strategic item]                                                  │
│                                                                             │
│    ## Recommended Path                                                     │
│    → [Clear recommendation with reasoning]                                 │
│                                                                             │
│    ## Next Steps                                                           │
│    1. [ ] [Immediate action]                                               │
│    2. [ ] [Follow-up]                                                      │
│                                                                             │
│  Files saved to: [project-root]/BRAINSTORM-[topic]-[date].md               │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  COMMON WORKFLOWS                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  Feature Planning                  │  Architecture Review                  │
│  ────────────────                  │  ───────────────────                  │
│  1. Describe feature naturally     │  1. /brainstorm architecture          │
│  2. Skills auto-activate           │  2. Agents analyze in parallel:       │
│  3. /brainstorm thorough [topic]   │     - backend-architect               │
│  4. Review generated plan          │     - database-architect              │
│  5. Start with Quick Wins!         │     - performance-engineer            │
│                                    │  3. Review synthesis (~3 min)         │
│  Quick Design Decision             │  4. Implement quick wins first        │
│  ─────────────────────             │                                       │
│  1. Ask about pattern:             │  Deployment Strategy                  │
│     "JWT or session cookies?"      │  ───────────────────                  │
│  2. backend-designer activates     │  1. Mention deployment need           │
│  3. Get immediate answer           │  2. devops-helper activates           │
│  4. No delegation needed           │  3. Get platform + cost estimate      │
│                                    │  4. /brainstorm devops (optional)     │
│                                    │                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  DESIGN PHILOSOPHY: "SOLID INDIE"                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  ✅ DO                              │  ❌ AVOID                              │
│  ──                                │  ─────                                │
│  • Ship fast, iterate              │  • Microservices (small teams)        │
│  • Proven patterns                 │  • Over-abstraction                   │
│  • Boring technology               │  • Premature optimization             │
│  • Right-sized complexity          │  • Corporate patterns                 │
│  • Cost-conscious (~$50/mo)        │  • Generic repositories               │
│  • Monolith → extract later        │  • Kubernetes (< 10 people)           │
│                                    │                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  AGENT DELEGATION PERFORMANCE                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│  Parallel Execution Example:                                               │
│                                                                             │
│    Task: "Design user auth with OAuth"                                     │
│    Agents launched (parallel):                                             │
│      • backend-architect      (OAuth flow)        ~1m 30s                  │
│      • security-specialist    (security review)   ~45s                     │
│      • ux-ui-designer          (login UI)          ~1m 10s                 │
│      • devops-engineer         (secrets mgmt)      ~50s                    │
│                                                                             │
│    Total time: ~1m 30s (slowest agent, NOT 4m 15s sequential!)             │
│                                                                             │
│    Output: Comprehensive plan with backend, frontend, DevOps, security     │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  TIPS FOR BEST RESULTS                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  Be Specific                       │  Use Right Mode                       │
│  ───────────                       │  ──────────────                       │
│  ✅ "User auth with Google OAuth"  │  Quick validation  → quick mode       │
│  ❌ "auth stuff"                    │  Familiar domain   → skills only      │
│                                    │  Unfamiliar tech   → thorough mode    │
│  Mention Constraints               │  Big decision      → architecture     │
│  ───────────────────               │                                       │
│  • Budget: "$50/month max"         │  Provide Context                      │
│  • Team: "2 developers"            │  ────────────────                     │
│  • Timeline: "1 week MVP"          │  • Existing stack                     │
│                                    │  • Current users                      │
│                                    │  • Growth expectations                │
│                                    │                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  TROUBLESHOOTING                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  Skills not activating?            │  Agent delegation not working?        │
│  ──────────────────────            │  ─────────────────────────────        │
│  • Check plugin installed          │  • Using quick mode?                  │
│  • Restart Claude Code             │  • experienced-engineer installed?    │
│  • Use trigger keywords            │  • Check agent timeout (5 min)        │
│                                    │                                       │
│  Brainstorm not saving?            │  Getting too much detail?             │
│  ──────────────────────            │  ────────────────────────             │
│  • Check write permissions         │  • Use quick mode                     │
│  • Create ~/brainstorms/           │  • Ask for summary only               │
│                                    │  • Skip thorough mode                 │
│                                    │                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Quick Command Reference

| What You Want | What To Do |
|---------------|------------|
| **Interactive flow** | `/brainstorm` → menus guide you |
| **Resume previous session** | `/brainstorm` in new session → pick from list |
| **Topic with menus** | `/brainstorm "auth system"` → Q1: Depth → Q2: Focus |
| **Skip menus entirely** | `/brainstorm quick feature "auth"` |
| **Quick feature ideas** | `/brainstorm quick feature [topic]` |
| **Deep architecture** | `/brainstorm thorough architecture [topic]` |
| **UI/UX design guidance** | Mention "UI design" → frontend-designer activates |
| **API design help** | Mention "API" → backend-designer activates |

### Flow Summary

```
/brainstorm                          → Smart detect → Q1 → Q2 → Execute
/brainstorm "topic"                  → Q1: Depth → Q2: Focus → Execute
/brainstorm feature "topic"          → Execute directly (mode provided)
/brainstorm quick feature "topic"    → Execute directly (all args provided)
```

---

## Pattern Library Quick Reference

### Backend Patterns

- **REST API:** Resources + HTTP methods + versioning
- **Auth:** JWT (stateless) vs Sessions (server state)
- **Database:** Normalized (consistency) vs Denormalized (performance)
- **Caching:** Redis (shared) vs In-memory (single server)

### Frontend Patterns

- **Components:** Container/Presentational split
- **State:** Context (simple) → Zustand (medium) → Redux (complex)
- **A11y:** WCAG 2.1 AA minimum, keyboard nav, ARIA labels
- **Performance:** Code split routes, lazy load images, virtual scroll lists

### DevOps Patterns

- **Platforms:** Vercel (Next.js), Render (full-stack), Fly.io (containers)
- **CI/CD:** GitHub Actions → Test → Auto-deploy
- **Databases:** Supabase (Postgres), PlanetScale (MySQL), MongoDB Atlas
- **Costs:** $0 MVP → ~$25/mo at 1K users → ~$100/mo at 10K

---

## Installation

```bash
cd ~/.claude/plugins
git clone https://github.com/Data-Wise/claude-plugins.git temp
mv temp/workflow .
rm -rf temp
# Restart Claude Code
```

---

## Links

- **Full docs:** [README.md](../README.md)
- **Quick start:** [QUICK-START.md](QUICK-START.md)
- **Doc hub:** [docs/README.md](README.md)
- **Repository:** https://github.com/Data-Wise/claude-plugins

---

**Print this page for quick reference while coding!** 🖨️
