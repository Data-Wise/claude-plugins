# Architecture Review

Review code changes for architectural consistency and quality.

## Usage

```bash
/craft:arch:review [options]
```

## What This Does

1. **Analyzes recent changes** or specific files
2. **Checks architecture patterns** are followed
3. **Identifies violations** and anti-patterns
4. **Provides actionable feedback** with examples

## Review Criteria

| Criterion | What's Checked |
|-----------|----------------|
| Layering | Proper layer separation |
| Dependencies | No circular deps, proper direction |
| Patterns | Consistent use of established patterns |
| Coupling | Low coupling between modules |
| Cohesion | High cohesion within modules |
| SOLID | Single responsibility, etc. |

## Options

- `--files <pattern>` - Review specific files
- `--since <ref>` - Changes since git ref
- `--strict` - Fail on any violation
- `--suggest` - Include fix suggestions

## Examples

```bash
# Review recent changes
/craft:arch:review

# Review specific files
/craft:arch:review --files "src/api/**/*.py"

# Review changes since main
/craft:arch:review --since main

# Strict mode for CI
/craft:arch:review --strict
```

## Output

```
Architecture Review
━━━━━━━━━━━━━━━━━━━

Files reviewed: 8
Changes analyzed: 156 lines

VIOLATIONS (2):

1. Layer Violation [MEDIUM]
   File: src/api/handlers.py:45
   Issue: Direct database access in API layer
   Pattern: Use repository pattern

   Current:
     user = db.session.query(User).filter_by(id=user_id).first()

   Suggested:
     user = user_repository.get_by_id(user_id)

2. Circular Dependency [HIGH]
   File: src/services/auth.py
   Issue: auth → user → auth circular import
   Pattern: Extract shared logic to separate module

   Suggested:
     Create src/services/shared.py for common utilities

WARNINGS (1):

1. High Coupling [LOW]
   File: src/services/payment.py
   Issue: 8 direct imports from other services
   Suggestion: Consider facade pattern

Summary: 2 violations, 1 warning
Status: NEEDS ATTENTION
```

## Integration

Works with:
- `/craft:arch:analyze` - Full analysis
- `/craft:code:ci-local` - CI checks
- `/craft:git:sync` - Pre-push validation
