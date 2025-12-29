# TODO - Workflow Plugin

**Current Version:** 2.1.6 (Stable)
**Next Version:** 2.2.0 (Planning Phase)
**Last Updated:** 2025-12-29

---

## 🔄 Current Sprint: Planning & RForge Improvements

**Status:** Ready for implementation decisions
**Duration:** 2-3 weeks
**Goal:** Stabilize v0.1.0 with RForge patterns before expanding features

### This Week (Dec 24-31)
- [x] Create planning documents (.STATUS, TODO.md, IDEAS.md)
- [x] Analyze workflow vs documentation gaps
- [x] Review RForge improvement patterns
- [ ] Decide v0.2.0 scope (Commands vs Testing first?)
- [ ] Test mode system improvements with real usage

---

## 📋 Implementation Backlog

### Priority 1: RForge Improvements (2-3 weeks)

**Week 1: Mode System** (5 hours)
- [ ] Add time budgets to /brainstorm modes
  - [ ] quick mode: < 60 seconds (MUST)
  - [ ] default mode: < 300 seconds (SHOULD)
  - [ ] thorough mode: < 1800 seconds (MAX)
- [ ] Add format parameter (--format terminal|json|markdown)
- [ ] Implement time budget enforcement
- [ ] Create mode selection guide
- [ ] Update documentation

**Week 2: Testing Infrastructure** (8 hours)
- [ ] Create pytest infrastructure
  - [ ] tests/conftest.py with fixtures
  - [ ] tests/unit/ directory
  - [ ] tests/integration/ directory
  - [ ] tests/performance/ directory
- [ ] Write unit tests (40-60 total)
  - [ ] test_mode_parsing.py (10 tests)
  - [ ] test_brainstorm_modes.py (15 tests)
  - [ ] test_agent_delegation.py (10 tests)
  - [ ] test_skill_activation.py (10 tests)
  - [ ] test_backward_compat.py (5 tests)
- [ ] Add test requirements (pytest, pytest-asyncio, pytest-mock)
- [ ] Run all tests (target: < 2s execution)

**Week 3: CI/CD** (6 hours)
- [ ] Create dedicated workflow (.github/workflows/validate-workflow.yml)
- [ ] Add matrix testing (Python 3.9-3.12)
- [ ] Add performance benchmarking job
- [ ] Add documentation validation job
- [ ] Deploy and verify all jobs passing

**Success Criteria:**
- Mode system with time budgets enforced
- 40+ pytest tests (< 2s execution, 100% passing)
- Dedicated CI/CD (5+ jobs passing)
- 3 output formats (terminal, json, markdown)

---

### Priority 2: v0.2.0 Commands (12-18 hours) - OPTIONAL

**Decision Point:** Implement after RForge improvements OR defer based on user feedback?

#### /analyze Command (4-6 hours)
- [ ] Create commands/analyze.md
- [ ] Implement mode system (quick/default/comprehensive)
- [ ] Architecture diagram generation
- [ ] Technical debt analysis
- [ ] Dependency mapping
- [ ] Write 10-15 tests

#### /review Command (4-6 hours)
- [ ] Create commands/review.md
- [ ] Security vulnerability scan
- [ ] Code quality metrics
- [ ] Best practice validation
- [ ] Write 10-15 tests

#### /optimize Command (4-6 hours)
- [ ] Create commands/optimize.md
- [ ] Performance profiling recommendations
- [ ] Bottleneck identification
- [ ] Optimization suggestions
- [ ] Write 10-15 tests

**Note:** These commands may overlap with existing plugins (code-review, performance-engineer). Validate need with user feedback first.

---

### Priority 3: Documentation Updates (2-3 hours)

- [ ] Create PROJECT-ROADMAP.md (extract from README)
- [ ] Update README with realistic v0.2.0 timeline
- [ ] Add mode selection flowchart diagram
- [ ] Create architecture diagram (Mermaid)
- [ ] Update QUICK-START.md with mode examples
- [ ] Update REFCARD.md with mode syntax

---

## 🚀 v2.1.6 Brainstorm UX - Future Enhancements

**Added:** 2025-12-29
**Reference:** `docs/design/BRAINSTORM-UX.md`

### Session Storage (Priority: High)
- [ ] Persist brainstorm sessions to disk for actual resume functionality
- [ ] Store: topic, mode, depth, output, timestamp, project
- [ ] Location: `~/.claude/brainstorm-sessions/` or project `.brainstorm/`
- [ ] Enable `/brainstorm` to resume from saved state

### Tab-Completion Dropdown (Priority: Medium)
- [ ] Create folder-based sub-commands for true Tab dropdown
- [ ] Structure: `brainstorm/quick.md`, `brainstorm/thorough.md`, etc.
- [ ] Enables: `/brainstorm/` + Tab → shows modes as dropdown
- [ ] Blocked by: Claude Code feature support

### Multi-Select Questions (Priority: Low)
- [ ] Combine depth + focus in single question if AskUserQuestion limit increases
- [ ] Current limit: 4 options max per question
- [ ] Would reduce from 2 questions to 1

### Voice Input (Priority: Future)
- [ ] "Hey Claude, brainstorm auth" → same interactive flow
- [ ] Depends on Claude Code voice input support

---

## 🐛 Known Issues

**None Currently!**

v2.1.6 is stable with no reported bugs.

**Potential Issues to Watch:**
- Agent delegation timeout edge cases
- Mode detection conflicts (multiple keywords)
- File save permissions in restricted directories

---

## 📊 Progress Tracking

### v2.1.6: Interactive Brainstorm UX ✅ COMPLETE (Dec 29, 2025)
- [x] Two-question interactive flow (Depth → Focus)
- [x] Smart context detection (conversation, git, .STATUS)
- [x] Session resume for new sessions
- [x] Topic-first flow (provide topic, then menus)
- [x] Skip menus with full args
- [x] Comprehensive design documentation
- [x] Updated REFCARD.md and QUICK-START.md

### v0.1.0: Foundation ✅ COMPLETE
- [x] 3 auto-activating skills
- [x] /brainstorm command (6 modes)
- [x] Workflow orchestrator agent
- [x] 60+ design patterns documented
- [x] Basic bash tests
- [x] Comprehensive documentation

### Planning Phase: Documentation ✅ COMPLETE (Dec 24, 2024)
- [x] Gap analysis (WORKFLOW-PLUGIN-STATUS.md)
- [x] RForge improvement plan
- [x] .STATUS file created
- [x] TODO.md created
- [x] IDEAS.md created

### Week 1: Mode System 📅 NOT STARTED
- [ ] Time budgets
- [ ] Format handlers
- [ ] Mode guide
- [ ] Testing

### Week 2-3: Testing & CI/CD 📅 NOT STARTED
- [ ] Pytest infrastructure
- [ ] 40-60 tests
- [ ] Dedicated CI/CD
- [ ] Performance benchmarks

### v0.2.0: Feature Expansion 📅 PLANNING
- [ ] /analyze command
- [ ] /review command
- [ ] /optimize command
- [ ] Expanded test coverage

---

## 🎯 Definition of Done

### For RForge Improvements Phase
- [ ] Mode system with 3 time budgets enforced
- [ ] 40+ pytest tests (100% passing, < 2s)
- [ ] 3 output formats working
- [ ] Dedicated CI/CD workflow (all jobs passing)
- [ ] Documentation updated
- [ ] 1 week real-world testing
- [ ] User feedback collected

### For v0.2.0 Commands (IF Implemented)
- [ ] 3 new commands implemented
- [ ] Each command has 3 modes
- [ ] 30+ additional tests (70+ total)
- [ ] All CI/CD jobs passing
- [ ] Documentation comprehensive
- [ ] Real-world validation

---

## 📅 Timeline

**Current:** v0.1.0 Stable (Dec 24, 2024)

**Week 1 (Dec 24-31):**
- Planning decisions
- Start mode system improvements

**Week 2 (Jan 1-7):**
- Complete mode system
- Testing infrastructure
- Begin CI/CD setup

**Week 3 (Jan 8-14):**
- Complete CI/CD
- Format handlers
- Documentation updates

**v0.2.0 Decision (Jan 15):**
- Evaluate: Implement commands OR ship improvements?
- Set timeline based on user feedback

**Target:** ~20 hours remaining work (RForge improvements only)

---

## 🔗 Related Documents

**Planning:**
- `.STATUS` - Current state snapshot
- `IDEAS.md` - Enhancement backlog
- `WORKFLOW-PLUGIN-STATUS.md` - Detailed gap analysis

**Implementation:**
- `WORKFLOW-STATISTICAL-RESEARCH-IMPROVEMENTS.md` - RForge patterns
- `commands/brainstorm.md` - Current command reference
- `tests/test-plugin-structure.sh` - Existing tests

**Documentation:**
- `README.md` - User documentation
- `PATTERN-LIBRARY.md` - 60+ design patterns
- `docs/QUICK-START.md` - Getting started guide

---

**Last Review:** 2024-12-24
**Next Review:** After Week 1 mode system work (2024-12-31)
