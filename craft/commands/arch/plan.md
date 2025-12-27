# Architecture Planning

Design and plan system architecture for new features or refactoring.

## Usage

```bash
/craft:arch:plan <feature_or_goal>
```

## What This Does

1. **Analyzes requirements** from description
2. **Proposes architecture** options
3. **Identifies trade-offs** for each approach
4. **Creates implementation plan** with steps

## Planning Outputs

| Output | Description |
|--------|-------------|
| Options | 2-3 architecture approaches |
| Trade-offs | Pros/cons for each option |
| Components | Required modules/services |
| Data Model | Entity relationships |
| API Design | Endpoints and contracts |
| Dependencies | Required packages/tools |

## Options

- `--style <pattern>` - Preferred architecture style
- `--constraints <list>` - Technical constraints
- `--timeline <scope>` - MVP vs full implementation
- `--output <file>` - Save plan to file

## Examples

```bash
# Plan new feature
/craft:arch:plan "user authentication with OAuth"

# Plan with constraints
/craft:arch:plan "real-time notifications" --constraints "no websockets"

# MVP scope
/craft:arch:plan "payment processing" --timeline mvp

# Save to file
/craft:arch:plan "microservices migration" --output arch-plan.md
```

## Output

```
Architecture Plan: User Authentication with OAuth
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Requirements:
  - OAuth 2.0 with Google, GitHub
  - Session management
  - Role-based access control

Option A: Session-based (Recommended)
  + Simpler implementation
  + Works with existing stack
  - Requires session storage

Option B: JWT-based
  + Stateless
  + Better for microservices
  - Token refresh complexity

Components:
  ┌─────────────┐    ┌─────────────┐
  │   Frontend  │───▶│  Auth API   │
  └─────────────┘    └──────┬──────┘
                            │
  ┌─────────────┐    ┌──────▼──────┐
  │ OAuth Providers├──│ Auth Service│
  └─────────────┘    └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │  User Store  │
                     └─────────────┘

Implementation Steps:
  1. Set up OAuth provider configs
  2. Create auth service module
  3. Implement callback handlers
  4. Add session middleware
  5. Create user model extensions
  6. Add role-based decorators
  7. Write integration tests

Estimated Effort: 2-3 days
```

## Integration

Works with:
- `/craft:arch:analyze` - Current architecture
- `/craft:arch:diagram` - Visualize plan
- `/craft:plan:feature` - Feature planning
