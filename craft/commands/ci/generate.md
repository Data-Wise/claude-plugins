---
description: Generate GitHub Actions CI workflow from project detection
arguments:
  - name: template
    description: Template to use (auto|python|node|r|rust|go|plugin)
    required: false
    default: auto
  - name: output
    description: Output path (defaults to .github/workflows/ci.yml)
    required: false
---

# /craft:ci:generate - Generate CI Workflow

Generate a GitHub Actions workflow file based on project detection or specified template.

## Quick Start

```bash
/craft:ci:generate              # Auto-detect and generate
/craft:ci:generate python       # Force Python template
/craft:ci:generate --output .github/workflows/test.yml
```

## Workflow

1. **Detect** - Run project detection (or use specified template)
2. **Customize** - Adjust based on detected features
3. **Generate** - Write workflow file
4. **Validate** - Check for common issues

## Generated Templates

### Python (UV)

```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ['3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v4

      - name: Set up Python ${{ matrix.python-version }}
        run: uv python install ${{ matrix.python-version }}

      - name: Install dependencies
        run: uv sync --all-extras --dev

      - name: Run linting
        run: uv run ruff check .

      - name: Run type checking
        run: uv run mypy src/

      - name: Run tests
        run: uv run pytest --cov --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        if: matrix.python-version == '3.12'
        with:
          files: ./coverage.xml
```

### Python (Poetry)

```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install Poetry
        uses: snok/install-poetry@v1

      - name: Install dependencies
        run: poetry install

      - name: Run tests
        run: poetry run pytest --cov
```

### Python (Pip)

```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e ".[dev]"

      - name: Run tests
        run: pytest --cov
```

### Node.js (NPM)

```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: ['18', '20', '22']

    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linting
        run: npm run lint --if-present

      - name: Run tests
        run: npm test
```

### Node.js (PNPM)

```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: ['18', '20', '22']

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Run tests
        run: pnpm test
```

### R Package

```yaml
name: R-CMD-check

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  R-CMD-check:
    runs-on: ${{ matrix.config.os }}
    strategy:
      fail-fast: false
      matrix:
        config:
          - {os: macos-latest, r: 'release'}
          - {os: windows-latest, r: 'release'}
          - {os: ubuntu-latest, r: 'devel', http-user-agent: 'release'}
          - {os: ubuntu-latest, r: 'release'}
          - {os: ubuntu-latest, r: 'oldrel-1'}

    steps:
      - uses: actions/checkout@v4

      - uses: r-lib/actions/setup-r@v2
        with:
          r-version: ${{ matrix.config.r }}
          http-user-agent: ${{ matrix.config.http-user-agent }}
          use-public-rspm: true

      - uses: r-lib/actions/setup-r-dependencies@v2
        with:
          extra-packages: any::rcmdcheck
          needs: check

      - uses: r-lib/actions/check-r-package@v2
        with:
          upload-snapshots: true
```

### Rust

```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install Rust
        uses: dtolnay/rust-toolchain@stable
        with:
          components: clippy, rustfmt

      - name: Check formatting
        run: cargo fmt --all -- --check

      - name: Run clippy
        run: cargo clippy --all-targets --all-features -- -D warnings

      - name: Run tests
        run: cargo test --all-features
```

### Go

```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version-file: 'go.mod'

      - name: Run go vet
        run: go vet ./...

      - name: Run tests
        run: go test -v -race -coverprofile=coverage.out ./...

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage.out
```

### Claude Plugin

```yaml
name: Validate Plugin

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Validate plugin structure
        run: |
          test -f .claude-plugin/plugin.json || exit 1
          python3 -m json.tool .claude-plugin/plugin.json > /dev/null
          echo "✅ Plugin structure valid"

      - name: Check for hardcoded paths
        run: |
          if grep -r "/Users/" commands/ 2>/dev/null; then
            echo "❌ Found hardcoded /Users/ paths"
            exit 1
          fi
          echo "✅ No hardcoded paths"

      - name: Validate command files
        run: |
          for f in commands/**/*.md; do
            if [ -f "$f" ]; then
              head -1 "$f" | grep -qE '^---|^#' || echo "⚠️ $f missing structure"
            fi
          done
          echo "✅ Commands validated"
```

## Customization Options

When generating, the command will ask about optional features:

| Feature | Question | Default |
|---------|----------|---------|
| **Coverage** | Upload to Codecov? | Yes if codecov.yml exists |
| **Matrix** | Test multiple versions? | Yes |
| **Linting** | Include lint step? | Yes if config found |
| **Types** | Include type checking? | Yes if mypy/typescript found |
| **Docs** | Build documentation? | Yes if mkdocs/sphinx found |

## Output

```
╭─ CI Workflow Generated ─────────────────────────────────╮
│                                                         │
│  📁 Created: .github/workflows/ci.yml                   │
│                                                         │
│  Template: python-uv                                    │
│  Python versions: 3.10, 3.11, 3.12                     │
│                                                         │
│  Features included:                                     │
│  ✅ Test matrix                                         │
│  ✅ Linting (ruff)                                      │
│  ✅ Type checking (mypy)                                │
│  ✅ Coverage upload                                     │
│  ❌ Documentation build (not detected)                  │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Next Steps:                                            │
│  1. Review the generated workflow                       │
│  2. Add secrets if needed (CODECOV_TOKEN)              │
│  3. Commit and push to trigger CI                       │
│                                                         │
│  → git add .github/workflows/ci.yml                     │
│  → git commit -m "ci: add GitHub Actions workflow"      │
│  → git push                                             │
╰─────────────────────────────────────────────────────────╯
```

## Integration

Works with:
- `/craft:ci:detect` - Run detection first
- `/craft:ci:validate` - Validate generated workflow
- `/craft:check ci` - Quick CI check
- `/craft:git:sync` - Commit and push

## Related Skills

- `project-detector` - Core detection logic
- `devops-helper` - CI/CD best practices
