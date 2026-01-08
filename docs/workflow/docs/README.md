# Workflow Plugin - Documentation

> **Complete documentation for the Workflow Plugin v0.1.0**

---

## 📚 Documentation Index

### Quick References

| Document | Purpose | Read Time |
|----------|---------| ----------|
| **[QUICK-START.md](QUICK-START.md)** | Get running in 3 minutes | 2 min |
| **[REFCARD.md](REFCARD.md)** | One-page command reference | 2 min |

### Detailed Guides

| Document | Purpose | Location |
|----------|---------|----------|
| **[README.md](../README.md)** | Main plugin documentation | Root |
| **Skills Guide** | Auto-activating skills explained | `skills/design/` |
| **Agent Guide** | Orchestrator agent details | `agents/` |

---

## 🚀 Getting Started

**New users:** Start with [QUICK-START.md](QUICK-START.md)

**Need a reminder:** Check [REFCARD.md](REFCARD.md)

**Installing:** See [Installation](#installation) below

---

## 📖 What's What

### QUICK-START.md
Perfect for:
- First-time users
- Getting up and running fast
- Learning basic workflows

**Contents:**
- Installation (1 minute)
- First commands to try
- Common workflows
- Tips and troubleshooting

### REFCARD.md
Perfect for:
- Quick command lookups
- Refreshing your memory
- One-page printable reference

**Contents:**
- All commands in tables
- Auto-activation triggers
- Common workflows
- Pattern library quick reference
- Troubleshooting quick reference

### Main README (../README.md)
Perfect for:
- Detailed feature explanation
- Understanding how it works
- Design philosophy

**Contents:**
- Features and capabilities
- Auto-activation details
- Agent delegation system
- Plugin architecture
- Examples and use cases

---

## 📂 Plugin Structure

```
workflow/
├── docs/                      # 👈 You are here
│   ├── README.md              # This file
│   ├── QUICK-START.md         # 3-minute guide
│   └── REFCARD.md             # One-page reference
├── commands/                  # 1 slash command
│   └── brainstorm.md          # Enhanced /brainstorm
├── skills/                    # 3 auto-activating skills
│   └── design/
│       ├── backend-designer.md     # Backend patterns
│       ├── frontend-designer.md    # UI/UX patterns
│       └── devops-helper.md        # DevOps patterns
├── agents/                    # 1 orchestrator agent
│   └── orchestrator.md        # Background delegation manager
├── tests/                     # Unit tests
│   └── test-plugin-structure.sh
├── README.md                  # Main documentation
├── package.json               # npm metadata
└── LICENSE                    # MIT license
```

---

## 🎯 Finding What You Need

### I want to...

**Get started quickly**
→ [QUICK-START.md](QUICK-START.md)

**Look up a command**
→ [REFCARD.md](REFCARD.md)

**Install the plugin**
→ [Installation](#installation) below

**Understand auto-activation**
→ [REFCARD.md - Skill Triggers](REFCARD.md#skill-auto-activation-triggers)

**See example workflows**
→ [QUICK-START.md - Common Workflows](QUICK-START.md#common-workflows)

**Troubleshoot issues**
→ [QUICK-START.md - Troubleshooting](QUICK-START.md#troubleshooting)

**Learn about design philosophy**
→ [Main README - Design Philosophy](../README.md#design-patterns-library)

---

## 🔧 How It Works

The workflow plugin uses a **3-layer system**:

### 1. Auto-Activating Skills (Immediate Guidance)
- Monitor conversation for keywords
- Activate automatically when relevant
- Provide quick patterns and recommendations
- Example: Mention "API design" → backend-designer skill activates

### 2. Enhanced Commands (Structured Workflows)
- `/brainstorm` command with smart mode detection
- Analyzes context to select appropriate approach
- Launches agents for deep analysis when needed
- Saves all output to markdown files

### 3. Background Agents (Deep Analysis)
- Orchestrator manages parallel agent execution
- Selects 2-4 specialized agents based on topic
- Agents run in background (non-blocking)
- Results synthesized into comprehensive plan

**Example flow:**
1. You mention "user authentication"
2. backend-designer skill activates (immediate patterns)
3. You run `/brainstorm thorough auth`
4. Orchestrator launches 4 agents in parallel:
   - backend-architect (OAuth flow)
   - security-specialist (security review)
   - ux-ui-designer (login UI)
   - devops-engineer (secrets management)
5. After ~1.5 min, comprehensive plan generated
6. Output saved to `BRAINSTORM-user-authentication-2025-12-23.md`

---

## 💡 Key Features

✨ **Auto-activation** - Skills trigger automatically based on conversation keywords

⚡ **Smart detection** - `/brainstorm` auto-detects mode from context

🤖 **Parallel agents** - Multiple agents run simultaneously for speed

📊 **Result synthesis** - Combines agent outputs into unified recommendations

🧠 **ADHD-friendly** - Scannable format, quick wins, clear next steps

🎯 **Solid indie design** - Pragmatic advice, no over-engineering

---

## 📊 Component Overview

| Component | Count | Purpose |
|-----------|-------|---------|
| **Commands** | 1 | `/brainstorm` with smart detection |
| **Skills** | 3 | backend-designer, frontend-designer, devops-helper |
| **Agents** | 1 | workflow-orchestrator (delegates to 9+ specialized agents) |

### Auto-Activating Skills

| Skill | Triggers On | Provides |
|-------|-------------|----------|
| **backend-designer** | API, database, auth keywords | Backend patterns, database design, auth flows |
| **frontend-designer** | UI, component, a11y keywords | UI patterns, component structure, accessibility |
| **devops-helper** | CI/CD, deployment keywords | Platform recommendations, cost estimates, pipelines |

### Agent Delegation (via orchestrator)

The orchestrator can delegate to these agents from the experienced-engineer plugin:

- backend-architect
- database-architect
- security-specialist
- ux-ui-designer
- frontend-specialist
- devops-engineer
- performance-engineer
- testing-specialist
- code-quality-reviewer

---

## 🔗 External Links

- **Plugin Repository:** https://github.com/Data-Wise/claude-plugins
- **GitHub Release:** (v0.1.0 coming soon)
- **Monorepo Documentation:** [../../KNOWLEDGE.md](../../KNOWLEDGE.md)

---

## 📦 Installation

### Manual Installation

```bash
cd ~/.claude/plugins
git clone https://github.com/Data-Wise/claude-plugins.git temp
mv temp/workflow .
rm -rf temp
```

**Restart Claude Code** to load the plugin.

### Verify Installation

```bash
ls ~/.claude/plugins/workflow
# Should show: .claude-plugin/ commands/ skills/ agents/ README.md
```

### Uninstall

```bash
rm -rf ~/.claude/plugins/workflow
```

**Restart Claude Code** to complete uninstall.

---

## ⚙️ Configuration

### No Configuration Required!

The plugin works out of the box with sensible defaults.

### Optional: Agent Delegation Control

Skills automatically delegate to agents when thorough analysis is needed.

**Control delegation:**
- Use `/brainstorm quick` to skip agent delegation
- Use `/brainstorm thorough` to force deep analysis
- Auto-detection uses conversation context

**Required plugins:**
- `experienced-engineer` plugin (provides specialized agents)
- Typically included with Claude Code installation

---

## 📝 Document Maintenance

**Last Updated:** 2025-12-23
**Plugin Version:** 0.1.0
**Documentation Version:** 1.0.0

**Release:** (GitHub release coming soon)

---

## 🎓 Learning Path

### For New Users
1. Read [QUICK-START.md](QUICK-START.md) (3 min)
2. Try auto-activating skills (mention "API design")
3. Run `/brainstorm quick feature notifications`
4. Review saved brainstorm file

### For Power Users
1. Read [Main README](../README.md) (10 min)
2. Study [REFCARD.md](REFCARD.md) for all options
3. Experiment with `/brainstorm thorough` modes
4. Review skill files in `skills/design/` for patterns

### For Developers
1. Check plugin structure in `workflow/`
2. Read skill frontmatter for trigger keywords
3. Review orchestrator agent for delegation logic
4. Run tests: `bash tests/test-plugin-structure.sh`

---

## 💬 Support & Feedback

**Found a bug?** Open an issue on GitHub

**Have a use case?** Share in Discussions

**Want to contribute?** See [Contributing](../README.md#contributing)

**Need help?** Start with [QUICK-START.md](QUICK-START.md) troubleshooting

---

**Need help?** Start with [QUICK-START.md](QUICK-START.md) or check [REFCARD.md](REFCARD.md) for quick answers!
