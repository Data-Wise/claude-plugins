# Smart Commands

Universal AI-powered commands for intelligent task routing.

## /craft:do

**Purpose:** Universal command that routes tasks to the best workflow automatically.

**Usage:**
```bash
/craft:do "add user authentication"
/craft:do "optimize database queries"
/craft:do "create API documentation"
```

The AI analyzes your request and:
1. Determines the best approach
2. Selects appropriate tools/commands
3. Executes the workflow
4. Reports results

## /craft:orchestrate

**Purpose:** Enhanced orchestrator v2.1 with mode-aware execution and subagent monitoring.

**Usage:**
```bash
/craft:orchestrate "implement auth" optimize    # Fast parallel
/craft:orchestrate "prep release" release       # Thorough audit
/craft:orchestrate status                       # Agent dashboard
/craft:orchestrate timeline                     # Execution timeline
/craft:orchestrate continue                     # Resume session
```

**Features:**
- Mode-aware execution (default/debug/optimize/release)
- Subagent delegation and monitoring
- Chat compression for long sessions
- ADHD-optimized status tracking
- Timeline view of execution

## /craft:check

**Purpose:** Pre-flight checks before commits, PRs, or releases.

**Usage:**
```bash
/craft:check                    # Quick validation
/craft:check --for commit       # Pre-commit checks
/craft:check --for pr           # Pre-PR validation
/craft:check --for release      # Full release audit
```

**Checks:**
- Code linting
- Test execution
- Documentation validation
- Build verification
- Dependency updates

## /craft:help

**Purpose:** Context-aware help and suggestions for your project.

**Usage:**
```bash
/craft:help                     # General suggestions
/craft:help testing             # Deep dive into testing
/craft:help documentation       # Docs-specific help
```

**Features:**
- Analyzes your project structure
- Suggests relevant commands
- Provides context-specific guidance
- Links to documentation
