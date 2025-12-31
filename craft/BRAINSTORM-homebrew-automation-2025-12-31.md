# Homebrew Automation for Craft Plugin

**Generated:** 2025-12-31
**Mode:** feature | **Depth:** default
**Context:** Lessons learned from aiterm/atlas/flow-cli/nexus-cli homebrew automation

---

## Background: What We Built Today

Created a reusable Homebrew workflow system:
1. **Centralized workflow** - `homebrew-tap/.github/workflows/update-formula.yml`
2. **Auto-merge PRs** - No manual intervention needed
3. **Multi-source support** - GitHub tarballs and PyPI packages
4. **Token management** - Fine-grained PAT for tap access

---

## Quick Wins (< 30 min each)

### ⚡ 1. New Skill: `homebrew-release-workflow`
**Benefit:** Generate release workflows for any repo

```markdown
# /craft:dist:homebrew-workflow
Generate GitHub Actions workflow for automated Homebrew formula updates.

Output:
- .github/workflows/homebrew-release.yml (GitHub source)
- .github/workflows/homebrew-release.yml (PyPI source)
```

### ⚡ 2. Enhance `/craft:dist:homebrew` Command
**Benefit:** One command to set up full automation

Add subcommands:
- `ait craft dist:homebrew formula` - Generate formula only (existing)
- `ait craft dist:homebrew workflow` - Generate release workflow
- `ait craft dist:homebrew token` - Guide for token setup
- `ait craft dist:homebrew setup` - Full setup wizard

### ⚡ 3. Formula Validation Skill
**Benefit:** Catch errors before release

```bash
/craft:dist:homebrew validate
# Runs: brew audit --strict --online Formula/name.rb
# Checks: desc length, license SPDX, test block, SHA256
```

---

## Medium Effort (1-2 hours)

### □ 4. Homebrew Setup Wizard
**User Story:** As a developer releasing a new tool, I want a guided setup so I don't miss any steps.

**Flow:**
```
/craft:dist:homebrew setup

1. Detect project type (Python/Node/Go/Rust/Shell)
2. Generate formula template
3. Create release workflow
4. Guide token creation
5. Add token to repo secrets
6. Create initial release
7. Verify installation works
```

### □ 5. PyPI Resource URL Updater
**User Story:** As a Python package maintainer, I want automatic updates to resource URLs when PyPI changes them.

**Problem:** PyPI resource URLs change, breaking formulas (nexus-cli issue)

**Solution:**
```bash
/craft:dist:homebrew update-resources nexus-cli

# Fetches current URLs from PyPI API
# Updates Formula/nexus-cli.rb with new URLs
# Creates PR or commits directly
```

### □ 6. Multi-Formula Release Coordinator
**User Story:** As a maintainer of multiple tools, I want to release them together when they have dependencies.

**Example:** rforge ecosystem packages need coordinated releases

```bash
/craft:dist:homebrew release-batch \
  --packages "mediationverse,rmediation,pmed" \
  --order "dependency"
```

---

## Long-term (Future sessions)

### □ 7. Homebrew Cask Support
**Current:** Only Formula (CLI tools)
**Future:** Cask support for desktop apps (like Scribe)

Features needed:
- DMG/PKG URL handling
- Livecheck integration
- Postflight scripts
- zap trash paths

### □ 8. Cross-Platform Support
**Current:** macOS-focused (Homebrew)
**Future:** Generate for multiple package managers

```bash
/craft:dist:package --targets homebrew,apt,chocolatey,scoop
```

### □ 9. Formula Dependency Graph
**User Story:** Visualize which formulas depend on each other in the tap.

```bash
/craft:dist:homebrew deps
# Output: Mermaid diagram of formula dependencies
```

### □ 10. Homebrew Analytics Dashboard
**User Story:** Track install counts and usage patterns.

```bash
/craft:dist:homebrew stats aiterm
# Shows: installs/day, version distribution, errors
```

---

## Acceptance Criteria

### For Quick Wins (MVP)

| Feature | Acceptance Criteria |
|---------|---------------------|
| `homebrew-workflow` skill | Generates valid workflow, passes linting |
| Enhanced `dist:homebrew` | New subcommands work, help text updated |
| Formula validation | Catches common audit failures |

### For Medium Effort

| Feature | Acceptance Criteria |
|---------|---------------------|
| Setup wizard | New user can go from 0 to working formula in < 10 min |
| Resource updater | Successfully updates nexus-cli URLs from PyPI API |
| Batch release | Releases 3+ packages in correct dependency order |

---

## Implementation Priority

```
Priority 1 (This week):
├── ⚡ homebrew-workflow skill
├── ⚡ Enhanced dist:homebrew command
└── ⚡ Formula validation

Priority 2 (Next week):
├── □ Setup wizard
└── □ PyPI resource updater

Priority 3 (Future):
├── □ Multi-formula coordinator
├── □ Cask support
└── □ Cross-platform packages
```

---

## Technical Notes

### Reusable Workflow Location
```
Data-Wise/homebrew-tap/.github/workflows/update-formula.yml
```

### Workflow Call Pattern
```yaml
uses: Data-Wise/homebrew-tap/.github/workflows/update-formula.yml@main
with:
  formula_name: myapp
  version: ${{ needs.prepare.outputs.version }}
  sha256: ${{ needs.prepare.outputs.sha256 }}
  source_type: github  # or pypi
  auto_merge: true
secrets:
  tap_token: ${{ secrets.HOMEBREW_TAP_GITHUB_TOKEN }}
```

### Token Requirements
- Fine-grained PAT
- Scope: `Data-Wise/homebrew-tap` only
- Permissions: Contents (R/W), Pull requests (R/W)

---

## Related Files to Create/Update

| File | Action |
|------|--------|
| `craft/skills/distribution/homebrew-workflow-expert.md` | Create |
| `craft/commands/dist/homebrew-workflow.md` | Create |
| `craft/commands/dist/homebrew.md` | Update with subcommands |
| `craft/skills/distribution/homebrew-formula-expert.md` | Update with automation |

---

## Recommended Path

→ **Start with Quick Win #1** (homebrew-workflow skill) because:
1. Immediately useful for new repos
2. Codifies the pattern we just built
3. Low effort, high value
4. Builds foundation for wizard

→ Then **Quick Win #2** to integrate into existing command structure

→ Then **Quick Win #3** to catch errors early
