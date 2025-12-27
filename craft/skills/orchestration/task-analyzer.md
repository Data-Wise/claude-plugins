# Task Analyzer Skill

Expert in analyzing natural language task descriptions and routing to appropriate craft commands.

## When to Use

This skill is automatically activated when:
- User invokes `/craft:do <task>`
- User describes a development task
- Context suggests multi-step workflow needed

## Capabilities

### Intent Recognition

Identifies task intent from natural language:

| Intent | Keywords | Example |
|--------|----------|---------|
| **Create** | add, create, implement, build, new | "add user authentication" |
| **Fix** | fix, debug, resolve, repair, issue | "fix the login bug" |
| **Test** | test, verify, check, validate | "test the api endpoints" |
| **Document** | document, docs, readme, explain | "document the api" |
| **Release** | release, deploy, publish, ship | "prepare for release" |
| **Refactor** | refactor, clean, improve, optimize | "refactor the utils module" |
| **Review** | review, audit, analyze | "review the architecture" |

### Domain Detection

Identifies affected domain from context:

| Domain | Indicators | Commands |
|--------|------------|----------|
| **API** | api, endpoint, rest, graphql | arch:plan, code:test-gen |
| **UI** | ui, component, page, view | frontend-designer skill |
| **Database** | db, database, model, schema | backend-designer skill |
| **Auth** | auth, login, permission | arch:plan, code:test-gen |
| **Testing** | test, coverage, spec | test:run, test:coverage |
| **Docs** | docs, readme, changelog | docs:sync, docs:validate |

### Workflow Selection

Maps intent + domain to optimal command sequence:

```
Feature Workflow:
  1. /craft:arch:plan     - Design the feature
  2. /craft:code:test-gen - Generate tests (TDD)
  3. /craft:git:branch    - Create feature branch
  4. → Implementation     - User implements
  5. /craft:test:run      - Verify tests pass
  6. /craft:git:sync      - Commit changes

Bug Fix Workflow:
  1. /craft:code:debug    - Analyze the issue
  2. /craft:test:debug    - Isolate in tests
  3. → Fix               - User implements fix
  4. /craft:test:run      - Verify fix
  5. /craft:git:sync      - Commit fix

Release Workflow:
  1. /craft:code:deps-audit  - Security scan
  2. /craft:test:run release - Full test suite
  3. /craft:code:lint release - Comprehensive lint
  4. /craft:docs:changelog   - Update changelog
  5. /craft:code:release     - Release workflow
```

### Complexity Assessment

Determines task complexity for mode selection:

| Complexity | Indicators | Default Mode |
|------------|------------|--------------|
| **Simple** | Single file, quick fix | default |
| **Medium** | Few files, feature | default |
| **Complex** | Many files, architecture | debug |
| **Critical** | Release, security | release |

## Output Format

### Analysis Report
```
╭─ Task Analysis ─────────────────────────────────────╮
│ Input: "add user authentication"                   │
├─────────────────────────────────────────────────────┤
│ Intent: Create (feature)                           │
│ Domain: Authentication                             │
│ Complexity: Medium                                 │
│ Workflow: Feature Development                      │
├─────────────────────────────────────────────────────┤
│ Recommended Commands:                              │
│   1. /craft:arch:plan       Design auth system    │
│   2. /craft:code:test-gen   Generate auth tests   │
│   3. /craft:git:branch      Create feature/auth   │
╰─────────────────────────────────────────────────────╯
```

## Integration

Works with:
- `/craft:do` - Primary entry point
- `/craft:check` - Validation after workflows
- All category commands (code, test, arch, etc.)
- All design skills (backend, frontend, devops)

## Example Analyses

### Simple Task
```
Input: "fix typo in readme"
Analysis:
  - Intent: Fix
  - Domain: Documentation
  - Complexity: Simple
  - Command: Direct edit (no routing needed)
```

### Complex Task
```
Input: "implement oauth2 login with google"
Analysis:
  - Intent: Create (feature)
  - Domain: Authentication + API
  - Complexity: Complex
  - Workflow: Feature Development
  - Skills: backend-designer, devops-helper
  - Commands: arch:plan → code:test-gen → git:branch
```
