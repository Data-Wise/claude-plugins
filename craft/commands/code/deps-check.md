# Dependency Check

Check for outdated, missing, or unused dependencies.

## Usage

```bash
/craft:code:deps-check [options]
```

## What This Does

1. **Scans dependencies** from manifest files
2. **Checks for updates** available on package registries
3. **Identifies unused** dependencies in codebase
4. **Detects missing** dependencies (used but not declared)

## Project Type Detection

| Project | Manifest | Registry |
|---------|----------|----------|
| Python | pyproject.toml, requirements.txt | PyPI |
| JavaScript | package.json | npm |
| R | DESCRIPTION | CRAN |
| Go | go.mod | Go Modules |
| Rust | Cargo.toml | crates.io |

## Options

- `--outdated` - Only show outdated packages
- `--unused` - Only show unused packages
- `--missing` - Only show missing packages
- `--update` - Show update commands

## Examples

```bash
# Full dependency check
/craft:code:deps-check

# Check for outdated only
/craft:code:deps-check --outdated

# Show update commands
/craft:code:deps-check --update

# Check for unused dependencies
/craft:code:deps-check --unused
```

## Output

```
Checking dependencies...

OUTDATED (3):
  Package          Current   Latest    Type
  requests         2.28.0    2.31.0    minor
  numpy            1.24.0    1.26.0    minor
  pytest           7.2.0     8.0.0     major

UNUSED (1):
  colorama - not imported anywhere

MISSING (0):
  None detected

Run with --update to see update commands
```

## Integration

Works with:
- `/craft:code:deps-audit` - Security audit
- `/craft:code:release` - Release preparation
