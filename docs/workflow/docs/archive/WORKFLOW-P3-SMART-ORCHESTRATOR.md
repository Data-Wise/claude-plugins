# Workflow Plugin Enhancement: Smart Orchestrator (P3)

**Saved for:** workflow plugin v3.0.0
**Source:** PROPOSAL-DEV-TOOLS-CREATIVE.md - Proposal 3
**Date:** 2025-12-26

---

## Concept: AI-Native Smart Commands

Instead of many commands, create **intelligent entry points** that:
- Auto-detect what the user needs
- Delegate to appropriate agents/plugins
- Synthesize results from multiple sources

---

## Proposed Commands (4 total)

### `/workflow:do <task>` - The Universal Command
```
User: /workflow:do add authentication

AI analyzes:
  → Backend task detected
  → Delegates to: backend-architect, security-specialist
  → Frontend needed: delegates to frontend-design
  → Tests needed: delegates to experienced-engineer

Returns: Comprehensive auth implementation plan
```

### `/workflow:plan <feature>` - Intelligent Planning
```
User: /workflow:plan user dashboard

AI:
  → Launches arch analysis, UI planning, API design in parallel
  → Synthesizes into cohesive feature plan
  → Includes wireframes, API spec, implementation steps
```

### `/workflow:check` - Universal Pre-flight
```
Detects project type and runs:
  - R package → R CMD check
  - Python → pytest + mypy
  - Node → npm test + eslint
  - Docs → link validation
  - Git → status, conflicts, divergence
```

### `/workflow:help <topic>` - Context-Aware Help
```
Shows relevant commands from ALL plugins based on:
  - Current project type
  - Recent activity
  - Installed plugins
```

---

## New Skills Required

### Task Analyzer Skill
```markdown
# Task Analyzer Skill

Analyzes natural language requests:
1. Extract intent (create, debug, test, deploy, etc.)
2. Identify domain (backend, frontend, devops, docs)
3. Detect complexity (quick task vs major feature)
4. Select appropriate tools (which plugins/agents)
5. Generate execution plan

Example:
  Input: "add user login with Google OAuth"
  Output:
    - Intent: create
    - Domain: backend + frontend
    - Complexity: medium (2-4 hours)
    - Tools: backend-architect, security-specialist, frontend-design
    - Plan: 1) OAuth flow design, 2) Backend endpoints, 3) Frontend UI
```

### Plugin Router Skill
```markdown
# Plugin Router Skill

Routes requests to appropriate plugins:
- Maintains capability map of installed plugins
- Matches user intent to plugin capabilities
- Handles multi-plugin orchestration
```

### Result Synthesizer Skill
```markdown
# Result Synthesizer Skill

Combines outputs from multiple agents/plugins:
- Deduplication
- Conflict resolution
- Priority ordering
- ADHD-friendly formatting
```

---

## Integration with Existing Workflow

Enhances the ADHD loop:
```
/recap → /next → /focus → /do → /check → /done
                           ↑        ↑
                     (Smart AI)  (Universal)
```

---

## Effort Estimate

- **New commands:** 4
- **New skills:** 3
- **Time:** 1 day
- **Target version:** workflow v3.0.0

---

## Benefits

1. **Minimal cognitive load** - User doesn't need to know which command
2. **AI handles routing** - Smart delegation to right tools
3. **Future-proof** - Works with new plugins automatically
4. **ADHD-friendly** - Just say what you need, AI figures it out

---

## Implementation Notes

- Requires existing orchestrator agent
- Builds on backend/frontend/devops skills
- Can leverage installed marketplace plugins
- Progressive enhancement (works without all plugins)

---

**Status:** Saved for future implementation
**Priority:** After dev-tools plugin (P2) complete
