# Workflow Plugin - Quick Start Guide

> **Version:** 2.1.6 | **Get running in 3 minutes** ⚡

---

## Installation (1 minute)

### Manual Installation

```bash
cd ~/.claude/plugins
git clone https://github.com/Data-Wise/claude-plugins.git temp
mv temp/workflow .
rm -rf temp
```

### Verify

```bash
ls ~/.claude/plugins/workflow
# Should show: .claude-plugin/ commands/ skills/ agents/ README.md
```

**Restart Claude Code** to load the plugin.

---

## First Commands to Try (2 minutes)

### 1. Auto-Activating Skills (Zero Setup!)

Skills activate automatically when you discuss topics. **Try these:**

#### Backend Design
```
You: "I need to design a REST API for user management"

→ backend-designer skill activates
→ Provides API patterns, auth strategies, database design
```

#### Frontend Design
```
You: "How should I structure my React dashboard components?"

→ frontend-designer skill activates
→ Suggests component composition, accessibility tips
```

#### DevOps Help
```
You: "I need to deploy my Next.js app"

→ devops-helper skill activates
→ Recommends platforms (Vercel), estimates costs
```

**No commands needed - skills auto-activate!**

### 2. Interactive Brainstorm (NEW in v2.1.6!)

Just type `/brainstorm` and let the menus guide you:

```bash
/brainstorm
```

**What happens:**
1. **New session?** → Asks if you want to resume a previous brainstorm
2. **Smart detection** → Finds topics from your conversation
3. **Q1: Depth?** → Choose: default (< 5 min) / quick (< 1 min) / thorough (< 30 min)
4. **Q2: Focus?** → Choose: auto-detect / feature / architecture / backend
5. **Execute** → Generates ADHD-friendly output, saves to file

### 3. Topic with Menus

```bash
/brainstorm "user notifications"
```

**What happens:**
1. Skips topic detection (you provided it)
2. **Q1: Depth?** → default / quick / thorough
3. **Q2: Focus?** → auto-detect / feature / architecture / backend
4. Execute with your selections

### 4. Skip Menus Entirely

```bash
/brainstorm quick feature "user notifications"
```

**Output:** 5-7 ideas in Quick Wins / Medium / Long-term format, saved to markdown file. No menus - executes immediately.

### 5. Thorough Brainstorm with Agents

```bash
/brainstorm thorough architecture "OAuth system"
```

**What happens:**
1. Launches 2-4 specialized agents in background
2. Provides immediate ideas
3. Waits ~1-2 min for agent analysis
4. Synthesizes comprehensive implementation plan
5. Saves detailed brainstorm document

---

## Common Workflows

### Workflow 1: Feature Planning

```
1. Describe feature in conversation:
   "I want to add real-time notifications to my app"

2. Skills auto-activate based on keywords:
   - backend-designer (WebSocket/SSE patterns)
   - frontend-designer (notification UI components)

3. Run thorough brainstorm:
   /brainstorm thorough real-time notifications

4. Review generated plan:
   - Technology recommendations
   - Implementation steps
   - Cost estimates
   - Next steps

5. Start building from numbered steps!
```

### Workflow 2: Architecture Review

```
1. Run architecture brainstorm:
   /brainstorm architecture scaling to 10K users

2. Agents analyze in parallel:
   - backend-architect (backend scaling)
   - database-architect (DB optimization)
   - performance-engineer (bottlenecks)

3. Review synthesis:
   - Scalability recommendations
   - Performance optimizations
   - Infrastructure changes

4. Implement quick wins first (< 30 min items)
```

### Workflow 3: Quick Design Decision

```
1. Ask about design pattern:
   "Should I use JWT or session cookies for auth?"

2. backend-designer skill activates:
   - Compares approaches
   - Lists trade-offs
   - Recommends based on team size

3. Get immediate answer (no agent delegation needed)
```

---

## Tips for Best Results

### Get Specific

- ✅ "User authentication with Google OAuth"
- ❌ "auth stuff"

### Mention Constraints

- Budget: "$50/month max"
- Team: "2 developers"
- Timeline: "1 week MVP"

### Include Context

- "Existing stack: Next.js, PostgreSQL, Vercel"
- "Current users: 500, expecting 5K by Q2"

### Choose the Right Approach

| Scenario | Command | What Happens |
|----------|---------|--------------|
| **Just exploring** | `/brainstorm` | Menus guide you through options |
| **Have a topic** | `/brainstorm "topic"` | Q1: Depth → Q2: Focus → Execute |
| **Quick validation** | `/brainstorm quick "topic"` | < 1 min, no agents, skips menus |
| **Know exactly what you want** | `/brainstorm quick feature "topic"` | Skips all menus, executes immediately |
| **Deep dive** | `/brainstorm thorough architecture "topic"` | 2-4 agents, < 30 min |
| **Resume previous work** | `/brainstorm` (new session) | Shows previous sessions to continue |

### Flow Summary

```
/brainstorm                    → Smart detect → Q1 → Q2 → Execute
/brainstorm "topic"            → Q1: Depth → Q2: Focus → Execute
/brainstorm feature "topic"    → Execute directly (mode provided)
/brainstorm quick feature "t"  → Execute directly (all args)
```

---

## Understanding Auto-Activation

Skills activate based on **keywords in conversation:**

### Backend Keywords

- API design, REST, GraphQL
- database, schema, migration
- authentication, OAuth, JWT
- caching, Redis, performance

### Frontend Keywords

- UI, UX, design, layout
- component, React, Vue
- accessibility, a11y, WCAG
- responsive, mobile-first

### DevOps Keywords

- deployment, CI/CD, pipeline
- Docker, container, Kubernetes
- infrastructure, hosting
- GitHub Actions, testing

**Just mention these topics naturally - skills activate automatically!**

---

## Output Format

All brainstorms follow ADHD-friendly format:

```markdown
## Quick Wins (< 30 min each)
1. ⚡ [Action] - [Benefit]
2. ⚡ [Action] - [Benefit]

## Medium Effort (1-2 hours)
- [ ] [Task with clear outcome]

## Long-term (Future sessions)
- [ ] [Strategic item]

## Recommended Path
→ [Clear recommendation with reasoning]

## Next Steps
1. [ ] [Immediate action]
2. [ ] [Follow-up]
```

**Why this format?**
- **Scannable** - Quick visual hierarchy
- **Actionable** - Numbered steps, checkboxes
- **ADHD-friendly** - Quick wins reduce overwhelm
- **Clear priority** - Recommended path highlighted

---

## Troubleshooting

### "Skills aren't activating"

**Check:**
1. Plugin installed? `ls ~/.claude/plugins/workflow/skills`
2. Restarted Claude Code?
3. Using right keywords? (Try: "I need to design an API")

**Test manually:**
```
You: "I need to design a REST API for user CRUD operations"

Expected: backend-designer skill should provide guidance
```

### "Agent delegation not working"

**Possible causes:**
1. Using quick mode? (`/brainstorm quick` skips agents)
2. Missing experienced-engineer plugin? (provides agents)
3. Agent timeout? (5 min max)

**Verify agents available:**
```bash
ls ~/.claude/plugins/experienced-engineer/agents/
# Should list: backend-architect, ux-ui-designer, etc.
```

### "Brainstorm file didn't save"

**Check:**
1. Write permissions in current directory?
2. Fallback: `~/brainstorms/` should exist

**Create fallback manually:**
```bash
mkdir -p ~/brainstorms
chmod 755 ~/brainstorms
```

---

## Next Steps

### Learn More

- **Full docs:** [README.md](../README.md)
- **Reference card:** [REFCARD.md](REFCARD.md)
- **Documentation hub:** [docs/README.md](README.md)

### Try These Next

1. Run `/brainstorm thorough` on your current project
2. Ask about a design decision and watch skills activate
3. Review saved brainstorm files in your project root

### Share Feedback

- What patterns saved you time?
- What felt over-engineered?
- What use cases should we add?

---

**You're ready to go! Start with auto-activating skills - they work immediately with zero setup.** 🚀
