# Craft Orchestrator Enhancements Brainstorm

**Generated:** 2025-12-27
**Context:** `~/.claude/plugins/craft/` (v1.3.0)
**Current:** orchestrator.md (v1) + orchestrator-v2.md (enhanced)

---

## Current State Assessment

### orchestrator-v2.md Strengths
| Feature | Status | Notes |
|---------|--------|-------|
| Task analysis & decomposition | ✅ | Visual breakdown table |
| Parallel agent delegation | ✅ | 3 patterns (parallel, sequential, fan-out) |
| Status dashboard | ✅ | ADHD-friendly with emoji anchors |
| Chat compression | ✅ | 70%/85% thresholds |
| Error handling | ✅ | Retry logic, recovery options |
| User control commands | ✅ | status, compress, pause, abort |
| Craft command routing | ✅ | Maps to /craft:* commands |

### Gaps Identified
| Gap | Impact | Complexity |
|-----|--------|------------|
| Simulated context % (not real) | Medium | Low |
| No persistent state | High | Medium |
| No actual agent cost tracking | Low | Low |
| Limited mode integration | Medium | Low |
| No session recovery | High | Medium |

---

## Enhancement Options

### Option A: Real Context Tracking (Quick Win)
**Effort:** ⚡ 1-2 hours

Add real context awareness using Claude Code signals:

```markdown
## Changes to orchestrator-v2.md

### New: Context Detection
Claude Code provides context signals in system messages:
- Watch for "context is X% full" warnings
- Parse session metadata when available
- Default to heuristic: ~100 tokens per exchange

### Updated Compression Triggers
| Signal | Action |
|--------|--------|
| System warning about context | Immediate compress |
| >25 exchanges without compression | Proactive compress |
| Large code blocks returned | Compress verbose output |
```

**Pros:** Immediate improvement, no external dependencies
**Cons:** Still heuristic-based

---

### Option B: State Persistence (Recommended)
**Effort:** 🔧 2-4 hours

Add persistent session state for recovery:

```markdown
## New: Session State File

Location: `.claude/orchestrator-session.json`

{
  "session_id": "2025-12-27-abc123",
  "started": "2025-12-27T10:30:00",
  "goal": "Add sensitivity analysis to RMediation",
  "agents": [
    {
      "id": "arch-1",
      "type": "arch",
      "task": "Design sensitivity API",
      "status": "complete",
      "result_summary": "3 methods proposed"
    },
    {
      "id": "code-1",
      "type": "code",
      "task": "Implement primary method",
      "status": "in_progress",
      "progress": 60
    }
  ],
  "completed_work": [
    "✅ Architecture design complete",
    "✅ Test stubs created"
  ],
  "next_actions": [
    "Complete code-1 implementation",
    "Run test suite"
  ],
  "decisions_made": [
    {"decision": "Use bootstrap for CI", "rationale": "Performance"}
  ]
}
```

### New Commands
```bash
/craft:orchestrate continue      # Resume from saved state
/craft:orchestrate save          # Force state save
/craft:orchestrate history       # Show past sessions
```

**Pros:** Survives disconnects, enables long workflows
**Cons:** File management complexity

---

### Option C: Mode Integration (Quick Win)
**Effort:** ⚡ 1 hour

Integrate with craft's mode system:

```markdown
## Orchestrator Modes

| Mode | Behavior |
|------|----------|
| **default** | Single agent, quick tasks |
| **debug** | Verbose agent output, no compression |
| **optimize** | Max parallel agents (4), aggressive compression |
| **release** | Full validation, all agents, comprehensive report |

### Usage
```bash
/craft:orchestrate "add auth" optimize    # Fast parallel execution
/craft:orchestrate "prep release" release # Thorough multi-agent
```
```

**Pros:** Leverages existing mode system
**Cons:** Limited scope

---

### Option D: Agent Pool Management (Medium Effort)
**Effort:** 🔧 3-4 hours

Sophisticated agent scheduling:

```markdown
## Agent Pool Configuration

```yaml
pool:
  max_parallel: 4           # Concurrent limit
  max_total: 10             # Session limit
  priority_queue: true      # P0 agents run first
  resource_budget:
    context_per_agent: 15%  # Max context each agent can consume
    time_per_agent: 5m      # Timeout
```

## Queue Visualization
```
RUNNING (2/4):
  [code-1] ████████░░ 80% - Implementing auth
  [test-1] ██░░░░░░░░ 20% - Setting up tests

QUEUED (2):
  [doc-1]  P1 - Waiting for code-1
  [check-1] P2 - Waiting for test-1

BUDGET: 45% context used | 3 agents remaining
```
```

**Pros:** Better resource management, predictable execution
**Cons:** Added complexity

---

### Option E: Timeline/Gantt View (ADHD Enhancement)
**Effort:** 🔧 2-3 hours

Visual timeline of agent execution:

```markdown
## Timeline View (enabled with `timeline` command)

```
TIME     0    1m    2m    3m    4m    5m
─────────┼─────┼─────┼─────┼─────┼─────┤
arch-1   ██████░░░░░░░░░░░░░░░░░░░░░░░ ✅ 1m
code-1        ░░░░░░████████████████░░░ 🟡 3m
test-1        ░░░░░░░░░░░░████████░░░░░ 🟡 2m
doc-1         ░░░░░░████░░░░░░░░░░░░░░░ ✅ 1m
─────────┼─────┼─────┼─────┼─────┼─────┤
                              NOW ▲
                              ETA: ~2m remaining
```
```

**Pros:** Clear progress visualization, reduces anxiety
**Cons:** Terminal rendering complexity

---

### Option F: Cost Tracking (Low Priority)
**Effort:** ⚡ 1 hour

Track estimated costs per agent:

```markdown
## Cost Tracking

```
| Agent | Tokens In | Tokens Out | Est. Cost |
|-------|-----------|------------|-----------|
| arch-1 | 2,500 | 1,200 | $0.02 |
| code-1 | 8,000 | 4,500 | $0.08 |
| test-1 | 3,000 | 2,000 | $0.03 |
| TOTAL | 13,500 | 7,700 | $0.13 |

Budget: $1.00 | Spent: $0.13 | Remaining: $0.87
```
```

**Pros:** Budget awareness, useful for API users
**Cons:** Estimates only (no real API data)

---

## Recommended Implementation Path

### Quick Wins (Do First)

1. **Option A: Real Context Tracking** - ⚡ 1-2 hours
2. **Option C: Mode Integration** - ⚡ 1 hour

### Medium Term (v1.4.0)

3. **Option B: State Persistence** - 🔧 2-4 hours
4. **Option E: Timeline View** - 🔧 2-3 hours

### Future (v1.5.0+)

5. **Option D: Agent Pool Management** - 🔧 3-4 hours
6. **Option F: Cost Tracking** - ⚡ 1 hour

---

## Quick Win Implementation: Enhanced orchestrator-v2

### Changes to Add

```markdown
## BEHAVIOR 7: Mode-Aware Execution (NEW)

Orchestrator respects craft modes:

| Mode | Max Agents | Compression | Verbosity |
|------|------------|-------------|-----------|
| default | 2 | 70% | Normal |
| debug | 1 (sequential) | 90% | Verbose |
| optimize | 4 | 60% | Minimal |
| release | 4 | 85% | Full report |

### Invocation
/craft:orchestrate "task" [mode]

## BEHAVIOR 8: Improved Context Tracking (NEW)

### Heuristics
- Each agent response: ~500-2000 tokens
- Each user exchange: ~100-500 tokens
- Compression saves: ~60% of archived content

### Triggers
| Condition | Action |
|-----------|--------|
| >20 exchanges | Check compression |
| Agent returns >2000 tokens | Summarize before storing |
| System warning about context | Immediate compression |
| User says "getting long" | Proactive compression |
```

---

## Decision Required

Which enhancements would you like to implement?

| # | Option | Effort | Impact |
|---|--------|--------|--------|
| 1 | Real context tracking | ⚡ 1-2h | Medium |
| 2 | Mode integration | ⚡ 1h | Medium |
| 3 | State persistence | 🔧 2-4h | High |
| 4 | Timeline view | 🔧 2-3h | High (ADHD) |
| 5 | Agent pool management | 🔧 3-4h | Medium |
| 6 | Cost tracking | ⚡ 1h | Low |

**Recommendation:** Start with **1 + 2** (quick wins), then **3** for persistence.

---

## Next Steps

1. [ ] Choose enhancement options (1-6)
2. [ ] Update orchestrator-v2.md with selected features
3. [ ] Add new commands to orchestrate.md
4. [ ] Update craft README with v1.4.0 features
5. [ ] Test with real workflow (e.g., aiterm feature)
