---
description: Universal command that intelligently routes to appropriate craft commands
arguments:
  - name: task
    description: Natural language description of what you want to do
    required: true
---

# /craft:do - Universal Command

Intelligently analyze your task and execute the right craft commands.

## Usage

```bash
/craft:do <task description>
```

## How It Works

1. **Analyze** - Parse task description for intent
2. **Route** - Select appropriate craft commands
3. **Execute** - Run commands in optimal order
4. **Report** - Summarize what was done

## Examples

### Feature Development
```bash
/craft:do add user authentication

# Routes to:
# 1. /craft:arch:plan - Design the feature
# 2. /craft:code:test-gen - Generate tests
# 3. /craft:git:branch - Create feature branch
```

### Bug Fixing
```bash
/craft:do fix the login redirect issue

# Routes to:
# 1. /craft:code:debug - Analyze the issue
# 2. /craft:test:run - Run related tests
# 3. /craft:git:sync - Commit fix
```

### Code Quality
```bash
/craft:do improve code quality

# Routes to:
# 1. /craft:code:lint - Check style
# 2. /craft:test:coverage - Check coverage
# 3. /craft:code:refactor - Suggest improvements
```

### Documentation
```bash
/craft:do update documentation

# Routes to:
# 1. /craft:docs:sync - Sync docs with code
# 2. /craft:docs:validate - Check links
# 3. /craft:docs:changelog - Update changelog
```

### Release Preparation
```bash
/craft:do prepare for release

# Routes to:
# 1. /craft:code:deps-audit - Security scan
# 2. /craft:test:run release - Full tests
# 3. /craft:code:lint release - Full lint
# 4. /craft:docs:changelog - Update changelog
# 5. /craft:code:release - Release workflow
```

## Task Categories

| Category | Keywords | Commands Used |
|----------|----------|---------------|
| **Feature** | add, create, implement, build | arch:plan, code:test-gen, git:branch |
| **Bug** | fix, debug, issue, error | code:debug, test:run, test:debug |
| **Quality** | lint, quality, clean, improve | code:lint, test:coverage, code:refactor |
| **Docs** | document, update docs, readme | docs:sync, docs:validate, docs:changelog |
| **Test** | test, coverage, verify | test:run, test:coverage, test:debug |
| **Release** | release, deploy, publish | deps-audit, lint, test:run, code:release |
| **Architecture** | design, refactor, restructure | arch:analyze, arch:plan, arch:diagram |

## Routing Logic

```
Task Analysis:
  ├── Contains "add/create/implement"
  │   └── Feature workflow
  ├── Contains "fix/debug/error/issue"
  │   └── Bug fix workflow
  ├── Contains "test/coverage/verify"
  │   └── Testing workflow
  ├── Contains "doc/readme/changelog"
  │   └── Documentation workflow
  ├── Contains "release/deploy/publish"
  │   └── Release workflow
  └── Contains "refactor/restructure/design"
      └── Architecture workflow
```

## Output Format

```
╭─ /craft:do "add user authentication" ───────────────╮
│ Task Type: Feature Development                      │
│ Commands: 4                                         │
├─────────────────────────────────────────────────────┤
│ Step 1: /craft:arch:plan                           │
│   ✓ Architecture designed                          │
│                                                     │
│ Step 2: /craft:code:test-gen                       │
│   ✓ 12 test cases generated                        │
│                                                     │
│ Step 3: /craft:git:branch                          │
│   ✓ Branch 'feature/user-auth' created             │
│                                                     │
│ Step 4: Ready to implement                         │
│   Next: Start coding in feature/user-auth          │
├─────────────────────────────────────────────────────┤
│ ✓ Task setup complete                              │
╰─────────────────────────────────────────────────────╯
```

## Integration

Works with all craft commands and skills:
- Routes to appropriate category commands
- Uses skills for specialized analysis
- Chains commands for complex workflows

## Tips

- Be specific for better routing
- Use domain keywords (auth, api, ui, db)
- Add mode hint if needed: "thoroughly test the api"
