# Code & Testing Commands

Development workflow tools with mode support - 17 commands.

## Linting & Code Quality

### /craft:code:lint

```bash
/craft:code:lint                # default mode
/craft:code:lint debug          # Verbose with suggestions
/craft:code:lint optimize       # Fast parallel linting
```

## Testing

### /craft:test:run

```bash
/craft:test:run                 # default mode
/craft:test:run debug           # Verbose test output
/craft:test:run release         # Full suite with coverage
```

## CI/CD Commands

### /craft:code:ci-fix
Auto-fix common CI/CD issues (linting, formatting, missing files).

### /craft:code:ci-local
Run CI checks locally before pushing.

## Dependencies

### /craft:code:deps-audit
Security audit of dependencies with vulnerability reports.

### /craft:code:deps-check
Check for outdated dependencies and breaking changes.

## Documentation Integration

### /craft:code:docs-check
Validate code documentation is up-to-date with implementation.

## Release Management

### /craft:code:release
Complete release checklist (tests, docs, changelog, version bump).

## Advanced Testing

### /craft:test:cli-gen
Generate CLI test suites with comprehensive coverage.

### /craft:test:cli-run
Run CLI-specific tests with output validation.

### /craft:test:watch
Watch mode for continuous testing during development.

## Other Commands

- `/craft:code:debug` - Systematic debugging
- `/craft:code:demo` - Create demonstrations
- `/craft:code:refactor` - Refactoring guidance
- `/craft:code:review` - Code review assistance
- `/craft:test:generate` - Test generation
- `/craft:test:strategy` - Testing strategy
