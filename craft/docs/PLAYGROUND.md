# Command Playground

⏱️ **15 minutes** • 🟢 Beginner • ✓ Interactive learning

> **TL;DR** (30 seconds)
> - **What:** Interactive examples showing exactly what happens when you run craft commands
> - **Why:** Learn by seeing real command outputs and understanding the workflow
> - **How:** Follow along with each example, run the commands yourself, compare outputs
> - **Next:** Graduate to [Visual Workflows](workflows/index.md) to see how commands connect

Try these commands yourself and see the magic happen!

!!! tip "Follow Along"
    Open your terminal and run these commands as you read. The best way to learn is by doing!

---

## Scenario 1: Your First craft Command

**Goal:** See all available commands

**Command:**
```bash
/craft:hub
```

**What Happens:**
```
┌─────────────────────────────────────────────────────────────┐
│ /craft:hub - Command Discovery                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 69 commands available across 9 categories                   │
│                                                             │
│ 🎯 SMART (4 commands)                                       │
│   /craft:do              - Universal task router            │
│   /craft:orchestrate     - Multi-agent coordination         │
│   /craft:check           - Pre-flight validation            │
│   /craft:help            - Context-aware help               │
│                                                             │
│ 📚 DOCUMENTATION (13 commands)                              │
│   /craft:docs:update     - Smart doc generation             │
│   /craft:docs:sync       - Stale doc detection              │
│   /craft:docs:check      - Doc validation                   │
│   ...                                                       │
│                                                             │
│ [... more categories ...]                                   │
└─────────────────────────────────────────────────────────────┘
```

**Why This Matters:**
- You can always run `/craft:hub` to see what's available
- Commands are organized by category for easy discovery
- Each command has a one-line description

---

## Scenario 2: Let AI Route Your Task

**Goal:** Add form validation to your project

**Command:**
```bash
/craft:do "add form validation"
```

**What Happens (Behind the Scenes):**

1. **Task Analysis** - task-analyzer skill examines your request
2. **Context Detection** - Checks your project type (Python, Node, etc.)
3. **Skill Selection** - Activates backend-designer or frontend-designer skill
4. **Command Routing** - Routes to appropriate command or agent

**Terminal Output:**
```
🎯 Analyzing task: "add form validation"

📊 Detected context:
   - Project type: Python (FastAPI)
   - Framework: FastAPI + Pydantic
   - Current location: /api/endpoints/

🧠 Skills activated:
   - backend-designer (API validation patterns)
   - test-strategist (validation test cases)

⚡ Executing:
   1. Adding Pydantic validators to schema
   2. Creating custom validation rules
   3. Adding error response models
   4. Generating test cases

✅ Complete! Added validation to:
   - schemas/user.py
   - tests/test_validation.py
```

**What You Learn:**
- One command handles the entire workflow
- AI selects the right tools automatically
- You don't need to remember which command to use

---

## Scenario 3: Pre-Flight Checks

**Goal:** Make sure everything is good before committing

**Command:**
```bash
/craft:check
```

**What Happens:**
```
🔍 Running pre-flight checks...

✅ Tests: All passing (47 tests in 2.3s)
✅ Linting: No issues found
✅ Docs: Up to date
✅ Git: Clean working directory
✅ Dependencies: All resolved

🎉 All checks passed! Safe to commit.

💡 Pro Tip: Run /craft:check --for release for full release audit
```

**If Something Fails:**
```
🔍 Running pre-flight checks...

✅ Tests: All passing (47 tests in 2.3s)
❌ Linting: 3 issues found
   - src/api/routes.py:42: Line too long (E501)
   - src/api/routes.py:67: Unused import (F401)
   - tests/test_api.py:15: Missing docstring (D100)

⚡ Auto-fixing lint issues...
✅ Fixed 3 lint issues

🎉 All checks passed after auto-fix!
```

**What You Learn:**
- Pre-flight checks catch issues early
- Many issues auto-fix automatically
- Prevents broken commits

---

## Scenario 4: Create a Documentation Site

**Goal:** Create an ADHD-friendly docs site in under 5 minutes

**Commands:**
```bash
# Option 1: Interactive wizard
/craft:site:create

# Option 2: Quick mode (no prompts)
/craft:site:create --preset adhd-focus --quick
```

**What Happens (Quick Mode):**
```
🚀 Creating documentation site...

📊 Detected:
   - Project: myproject
   - Type: Python package (pyproject.toml)
   - Repo: github.com/user/myproject

🎨 Applying preset: adhd-focus
   - Colors: Calm forest green (#2d6a4f)
   - Theme: Material with ADHD optimizations
   - Features: TL;DR boxes, time estimates, visual workflows

📝 Creating files:
   ✅ mkdocs.yml (site configuration)
   ✅ docs/index.md (homepage with features)
   ✅ docs/QUICK-START.md (30-second guide)
   ✅ docs/REFCARD.md (command reference)
   ✅ docs/stylesheets/extra.css (ADHD-friendly styles)
   ✅ .github/workflows/docs.yml (auto-deploy)

🔨 Building site...
   ✅ Site built successfully in 0.7s

🎉 Done! Your ADHD-friendly docs site is ready!

Next steps:
  • Preview: mkdocs serve (or /craft:site:preview)
  • Edit content: docs/index.md
  • Deploy: git push (auto-deploys via GitHub Actions)
```

**What You Learn:**
- Site creation is fully automated
- 8 ADHD-friendly presets available
- Auto-deployment included

---

## Scenario 5: Update All Documentation

**Goal:** Update docs after adding a new feature

**Command:**
```bash
/craft:docs:update
```

**What Happens:**
```
🔍 Detecting changes...

📊 Found changes:
   - New command: /myapp:feature
   - Modified: src/api/routes.py
   - Modified: src/cli/main.py

🧠 Smart detection suggests:
   ✅ Update CLI help epilogs
   ✅ Regenerate commands reference
   ✅ Update REFCARD.md
   ⏭️  Skip: No API changes detected
   ⏭️  Skip: No guide updates needed

⚡ Executing updates...

1. Updating CLI help epilogs...
   ✅ Updated: src/cli/main.py

2. Regenerating commands reference...
   ✅ Generated: docs/reference/commands.md

3. Updating REFCARD.md...
   ✅ Added: /myapp:feature entry

4. Running validation...
   ✅ No broken links
   ✅ Navigation structure valid
   ✅ All mermaid diagrams render

🎉 Documentation updated successfully!

Changed files:
  - src/cli/main.py
  - docs/reference/commands.md
  - docs/REFCARD.md

💡 Next: Run /craft:docs:check to validate everything
```

**What You Learn:**
- Smart detection avoids unnecessary updates
- Multiple docs updated in one command
- Validation runs automatically

---

## Scenario 6: Release Workflow

**Goal:** Run a full release audit before publishing

**Command:**
```bash
/craft:check --for release
```

**What Happens:**
```
🔍 Running FULL RELEASE AUDIT...

1. ⏱️  Testing...
   ✅ Unit tests: 47 passed in 2.3s
   ✅ Integration tests: 12 passed in 5.1s
   ✅ E2E tests: 8 passed in 12.7s

2. ⏱️  Code Quality...
   ✅ Linting: No issues
   ✅ Type checking: All types valid
   ✅ Security scan: No vulnerabilities

3. ⏱️  Documentation...
   ✅ All docs up to date
   ✅ No broken links
   ✅ Changelog updated

4. ⏱️  Git Status...
   ✅ Working directory clean
   ✅ All commits pushed
   ✅ On main branch

5. ⏱️  Dependencies...
   ✅ No security vulnerabilities
   ✅ All dependencies resolved
   ✅ Lock file up to date

6. ⏱️  Build...
   ✅ Builds successfully
   ✅ Distribution files created

🎉 RELEASE READY!

Safe to publish version 1.2.0

Next steps:
  • Create git tag: git tag v1.2.0
  • Push tag: git push origin v1.2.0
  • Create release: gh release create v1.2.0
```

**What You Learn:**
- Release checks are comprehensive
- Multiple validation gates
- Clear next steps provided

---

## Try It Yourself

Now that you've seen how commands work, try these challenges:

!!! example "Challenge 1: Discovery"
    Run `/craft:hub` and pick 3 commands that sound interesting. Try them!

!!! example "Challenge 2: Automation"
    Run `/craft:do "improve my error handling"` and watch AI route it automatically

!!! example "Challenge 3: Workflow"
    Run `/craft:check` → fix any issues → run again until it passes

!!! example "Challenge 4: Documentation"
    Run `/craft:docs:sync` to see if your docs are stale

!!! example "Challenge 5: Site Creation"
    Run `/craft:site:create --preset adhd-focus --quick` to create a docs site

---

## Common Patterns

### Before Every Commit
```bash
/craft:check                  # Quick validation
# Fix any issues that appear
git add .
git commit -m "message"
```

### After Adding a Feature
```bash
/craft:docs:update            # Update all docs
/craft:check                  # Validate everything
```

### Before a Release
```bash
/craft:check --for release    # Full audit
/craft:docs:changelog         # Generate changelog
# Create release when checks pass
```

### When Stuck
```bash
/craft:help                   # Context-aware suggestions
/craft:do "what you want"     # Let AI figure it out
```

---

## What's Next?

You've seen individual commands in action. Now learn how they work together:

<div class="grid cards" markdown>

- :bar_chart: **[Visual Workflows](workflows/index.md)**

    See 5 complete workflows with diagrams

- :books: **[Commands Overview](commands/overview.md)**

    Explore all 69 commands organized by category

- :rocket: **[Quick Reference](REFCARD.md)**

    Command cheat sheet for quick lookup

- :brain: **[ADHD Guide](ADHD-QUICK-START.md)**

    Optimized learning path (under 2 minutes)

</div>
