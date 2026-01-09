# SPEC: MCP Server Integration Options

**Created:** 2026-01-08
**Status:** Phase 1 - Configuration Tooling (Option 4)
**Author:** Engineering Analysis via `/brainstorm deep feat save`

---

## Executive Summary

This specification outlines 4 integration approaches for tighter coupling between the `mcp-servers` project and `claude-plugins` monorepo, ranging from minimal configuration improvements (1 day) to full monorepo unification (3-4 days).

**Recommended Approach:** Phased implementation starting with **Option 4** (Configuration-Only Integration) to deliver immediate value with zero breaking changes, then evaluate whether to evolve to **Option 1** (Git Submodule) or **Option 2** (npm Workspace) based on real-world feedback.

---

## Current State

### Architecture

**Two-Layer System:**
```
claude-plugins/ (Monorepo - 4 Plugins)
├── rforge/               # Orchestrator (delegates to rforge-mcp)
├── craft/                # Full-stack toolkit
├── statistical-research/ # Pure plugin (no MCP)
└── workflow/             # ADHD-friendly

mcp-servers/ (Separate Directory - 12+ Servers)
├── rforge/               # R package orchestrator (292 tests passing)
├── statistical-research/ # Statistical tools (14 tools, 17 skills)
├── shell/                # Shell command execution
├── nexus/                # Knowledge workflow
└── [8 more servers]
```

### Integration Patterns

**1. Orchestrator Pattern** (rforge plugin → rforge-mcp)
- Plugin commands delegate to MCP tools via `mcp.call_tool()`
- Production-ready: 292 tests, 4ms performance, 100% success rate
- Mode system: default/debug/optimize/release (<10s to <300s)
- Format options: terminal/json/markdown

**2. Pure Plugin Pattern** (statistical-research)
- Self-contained shell-based APIs
- No MCP dependency
- MCP server used independently across Desktop, CLI, browser

### Pain Points

1. **Configuration Spread:** `~/.claude/settings.json`, `.claude/settings.local.json`, browser extension config
2. **Separate Projects:** Two directories with independent lifecycles
3. **Development Workflow:** Must install both plugin AND MCP server
4. **Documentation Drift:** Plugin docs separate from MCP server docs

---

## Integration Options

### Option 1: Coordinated Dual-Repo with Git Submodule

**Overview:** Add `mcp-servers/` as git submodule with coordination tooling.

**Changes:**
- Add submodule: `git submodule add ../mcp-servers .mcp-servers`
- Configuration manager generates `settings.json` from plugin metadata
- Cross-repo CI/CD validation
- Shared documentation build

**Pros:**
- ✅ Minimal disruption (repos stay separate)
- ✅ Preserves MCP independence (Desktop, CLI, browser)
- ✅ Quick implementation (1-2 days)
- ✅ Standard practice (git submodules)

**Cons:**
- ❌ Submodule complexity for contributors
- ❌ Two repos to manage (though coordinated)
- ❌ Configuration sync script dependency

**Effort:** 1-2 days

**When to Use:** Value MCP independence. Fits current architecture.

---

### Option 2: npm Workspace Monorepo

**Overview:** Convert to npm workspace monorepo with unified dependencies.

**Changes:**
- Move `mcp-servers/*` into `claude-plugins/mcp-servers/`
- Root `package.json` with workspaces
- Unified dependencies (one lockfile)
- Single git repository

**Structure:**
```
claude-plugins/
├── package.json          # Root workspace
├── plugins/
│   ├── rforge/
│   └── craft/
├── mcp-servers/
│   ├── rforge/
│   └── statistical-research/
└── shared/              # NEW: Shared utilities
```

**Pros:**
- ✅ Industry-standard (Turborepo, Nx patterns)
- ✅ Unified dependency management
- ✅ Easy cross-package references
- ✅ Changesets for coordinated releases

**Cons:**
- ❌ Major restructuring (breaking changes)
- ❌ MCP servers lose independence
- ❌ Larger repository

**Effort:** 3-4 days

**When to Use:** Committed to tight integration and 5+ plugins. Best long-term.

---

### Option 3: Plugin-Embedded MCP

**Overview:** Embed MCP server code directly in plugin packages.

**Changes:**
- Move MCP server into plugin directory
- Single npm package (plugin + MCP)
- Single version, single release

**Structure:**
```
claude-plugins/rforge/
├── .claude-plugin/
├── commands/
├── agents/
├── mcp-server/         # NEW: Embedded
│   ├── src/index.ts
│   └── tools/
└── scripts/install.sh  # Installs both
```

**Pros:**
- ✅ Simplest for end users (one package)
- ✅ Guaranteed version compatibility
- ✅ Unified development

**Cons:**
- ❌ MCP not reusable independently
- ❌ Breaks statistical-research pattern (MCP used elsewhere)
- ❌ Not suitable for pure plugins

**Effort:** 2-3 days per plugin

**When to Use:** ONLY for primary MCP consumers. Good for RForge, NOT statistical-research.

---

### Option 4: Configuration-Only Integration (RECOMMENDED PHASE 1) 🎯

**Overview:** Improve configuration tooling only. Zero structural changes.

**Changes:**
- Configuration generator (`scripts/configure-all.sh`)
- Validation tool (`scripts/validate-mcp.sh`)
- Plugin MCP metadata (`.claude-plugin/mcp-config.json`)
- Documentation cross-references

**Plugin Metadata Format:**
```json
{
  "requires": {
    "rforge-mcp": {
      "version": ">=0.1.0",
      "description": "R package ecosystem orchestrator",
      "install": "npm install -g rforge-mcp",
      "config": {
        "command": "npx",
        "args": ["rforge-mcp"],
        "env": {}
      }
    }
  }
}
```

**Pros:**
- ✅ Minimal change (1 day)
- ✅ Non-breaking, additive only
- ✅ Low risk, easy rollback
- ✅ Can evolve to other options

**Cons:**
- ❌ Doesn't solve documentation drift
- ❌ Doesn't solve release coordination

**Effort:** 1 day

**When to Use:** Best starting point. Delivers immediate value, gathers data.

---

## Comparative Analysis

| Dimension | Option 1 | Option 2 | Option 3 | Option 4 |
|-----------|----------|----------|----------|----------|
| **Effort** | 1-2 days | 3-4 days | 2-3d/plugin | 1 day |
| **Complexity** | Medium | Medium-High | Medium | Low |
| **User Experience** | Good | Great | Excellent | Okay |
| **MCP Independence** | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| **Breaking Changes** | None | Major | Medium | None |
| **Maintainability** | Medium | Excellent | Good | Current |

---

## Recommended Implementation Plan

### Phase 1 (This Week): Option 4 - Configuration Tooling 🎯

**Goal:** Improve current state with zero breaking changes.

#### Step 1: Configuration Generator (2 hours)

**File:** `scripts/configure-all.sh`

**Purpose:** Scans installed plugins for MCP requirements, generates/updates `~/.claude/settings.json`

**Features:**
- Detects plugins with `.claude-plugin/mcp-config.json`
- Validates MCP servers installed
- Merges configurations into settings.json
- Idempotent (safe to run multiple times)

**Implementation:**
```bash
#!/bin/bash
# MCP Configuration Generator

PLUGIN_DIR="$HOME/.claude/plugins"
SETTINGS_FILE="$HOME/.claude/settings.json"

for plugin in "$PLUGIN_DIR"/*; do
  if [[ -f "$plugin/.claude-plugin/mcp-config.json" ]]; then
    echo "Found MCP requirements: $(basename $plugin)"
    jq -r '.requires | to_entries[] | "\(.key): \(.value.install)"' \
      "$plugin/.claude-plugin/mcp-config.json"
  fi
done

# Merge into settings.json (implementation details below)
```

#### Step 2: Validation Tool (1 hour)

**File:** `scripts/validate-mcp.sh`

**Purpose:** Checks required MCP servers installed and configured correctly.

**Features:**
- Validates settings.json entries
- Checks commands exist on system
- Reports missing/misconfigured servers
- Exit code indicates success/failure

**Implementation:**
```bash
#!/bin/bash
# MCP Server Validation

validate_mcp() {
  local mcp_name=$1
  local required_by=$2

  if ! jq -e ".mcpServers[\"$mcp_name\"]" ~/.claude/settings.json >/dev/null; then
    echo "❌ Missing: $mcp_name (required by $required_by)"
    return 1
  fi

  local cmd=$(jq -r ".mcpServers[\"$mcp_name\"].command" ~/.claude/settings.json)
  if ! command -v $cmd &> /dev/null; then
    echo "⚠️  Warning: Command not found: $cmd"
    return 1
  fi

  echo "✅ Valid: $mcp_name"
  return 0
}
```

#### Step 3: Plugin MCP Metadata (30 min)

**File:** `rforge/.claude-plugin/mcp-config.json` (NEW)

**Purpose:** Declares MCP server requirements for rforge plugin.

**Content:**
```json
{
  "$schema": "https://schema.claude.ai/plugin-mcp-config.json",
  "requires": {
    "rforge-mcp": {
      "version": ">=0.1.0",
      "description": "R package ecosystem orchestrator",
      "install": "npm install -g rforge-mcp",
      "config": {
        "command": "npx",
        "args": ["rforge-mcp"],
        "env": {}
      }
    }
  }
}
```

#### Step 4: Update Install Scripts (1 hour)

**File:** `rforge/scripts/install.sh` (UPDATE)

**Changes:**
```bash
# Add after plugin installation
echo "Configuring MCP servers..."
if [[ -x "$REPO_ROOT/scripts/configure-all.sh" ]]; then
  "$REPO_ROOT/scripts/configure-all.sh"
fi

echo "Validating MCP configuration..."
if [[ -x "$REPO_ROOT/scripts/validate-mcp.sh" ]]; then
  if ! "$REPO_ROOT/scripts/validate-mcp.sh"; then
    echo "⚠️  Warning: MCP validation failed. Run manually to fix."
  fi
fi
```

#### Step 5: Documentation Updates (1.5 hours)

**Files:**
- `KNOWLEDGE.md` - Add section 12: "MCP Server Configuration"
- `README.md` - Add "MCP Server Setup" section
- `rforge/README.md` - Add requirements section

**KNOWLEDGE.md Addition:**
```markdown
## 12. MCP Server Configuration

### Configuration Generator

Plugins can declare MCP server requirements in `.claude-plugin/mcp-config.json`.

**Generate Configuration:**
```bash
./scripts/configure-all.sh
```

**Validate Configuration:**
```bash
./scripts/validate-mcp.sh
```

### Plugin MCP Metadata Format

See `rforge/.claude-plugin/mcp-config.json` for schema example.
```

---

### Verification & Testing

**After Implementation:**

1. **Configuration Generator Test:**
```bash
# Backup existing config
cp ~/.claude/settings.json ~/.claude/settings.json.backup

# Run generator
./scripts/configure-all.sh

# Verify settings.json updated
jq '.mcpServers' ~/.claude/settings.json
```

2. **Validation Tool Test:**
```bash
# Should pass with rforge-mcp installed
./scripts/validate-mcp.sh

# Test negative case (should fail)
npm uninstall -g rforge-mcp
./scripts/validate-mcp.sh
npm install -g rforge-mcp  # Restore
```

3. **Install Script Test:**
```bash
# Uninstall plugin
./rforge/scripts/uninstall.sh

# Reinstall (should auto-configure MCP)
./rforge/scripts/install.sh

# Verify
./scripts/validate-mcp.sh
```

4. **Integration Test:**
```bash
# Test rforge plugin with MCP server
cd /tmp && mkdir test-r-package && cd test-r-package
git init

# In Claude Code: /rforge:status
# Expected: Status output from rforge-mcp server
```

5. **Documentation Test:**
```bash
mkdocs build --strict
grep -r "MCP Server Configuration" docs/
```

---

### Phase 2 (1-2 Weeks): Evaluate

**Goal:** Use Phase 1 improvements, gather feedback, decide next steps.

**Decision Criteria:**
- Did configuration tooling solve main pain points?
- Is MCP server independence still critical?
- Scale concerns (5+ plugins)?
- Remaining friction points?

**Outcomes:**
- **Stay with Option 4:** If tooling solves problems
- **Upgrade to Option 1:** If coordination needed, independence valued
- **Upgrade to Option 2:** If committed to tight integration and scale

---

### Phase 3 (Future): Execute Next Phase If Needed

Based on Phase 2 evaluation, implement Option 1, 2, or 3 using:
- Feature branch via git worktree
- Comprehensive tests
- Migration guide
- Rollback plan

---

## Success Criteria

### Option 4 Implementation Complete When:

1. ✅ `scripts/configure-all.sh` successfully generates MCP configs
2. ✅ `scripts/validate-mcp.sh` accurately reports status
3. ✅ Plugin install scripts use new tooling
4. ✅ Documentation includes MCP setup instructions
5. ✅ All tests pass (configuration, validation, integration)
6. ✅ Zero breaking changes to existing workflows

### Ready for Phase 2 Evaluation When:

- Used in production for 1-2 weeks
- Remaining friction identified and documented
- Data gathered for Option 1/2/3 decision

---

## Scenario-Based Recommendations

**You want improvement NOW:**
→ Option 4 (1 day, immediate value)

**You value MCP independence:**
→ Option 1 (git submodule coordination)

**You're building for scale (5+ plugins):**
→ Option 2 (npm workspace monorepo)

**RForge is tightly coupled:**
→ Option 3 for RForge only (keep statistical-research independent)

**Mixed ecosystem:**
→ Hybrid approach (pure plugins stay pure, RForge embeds MCP)

---

## Critical Files

### Create (Option 4):
- `scripts/configure-all.sh` - Configuration generator
- `scripts/validate-mcp.sh` - Validation tool
- `rforge/.claude-plugin/mcp-config.json` - MCP metadata

### Modify (Option 4):
- `rforge/scripts/install.sh` - Add MCP configuration step
- `KNOWLEDGE.md` - Add MCP configuration section
- `README.md` - Add MCP setup section
- `rforge/README.md` - Add requirements section

---

## Risk Assessment

### Option 4 Risk: LOW ✅
- Non-breaking, additive only
- Can rollback by deleting scripts
- Existing workflows unchanged

### Option 1 Risk: MEDIUM ⚠️
- Git submodules add complexity
- Can remove submodule if unsuccessful

### Option 2/3 Risk: HIGH 🔴
- Major restructuring (breaking changes)
- Requires migration guide and rollback plan
- Only attempt after Option 4 proves insufficient

---

## Next Steps

1. **This Week:** Implement Option 4 (configuration tooling)
2. **1-2 Weeks:** Use in production, gather feedback
3. **Evaluate:** Decide whether to evolve to Option 1, 2, 3, or stay with 4
4. **Future:** If needed, implement next phase using git worktree for safe experimentation

---

## References

- Plan file: `/Users/dt/.claude/plans/vast-skipping-turtle.md`
- Current architecture: `KNOWLEDGE.md` (Orchestrator Pattern, Pure Plugin Pattern)
- RForge integration testing: `docs/MCP-INTEGRATION-TESTING.md` (292 tests, 100% passing)
- Git worktree workflows: `KNOWLEDGE.md` section 11 (for Phase 3 experimentation)

---

**End of Specification**
