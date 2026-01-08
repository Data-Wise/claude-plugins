# CI Templates

Exemplary CI configurations from dev-tools projects. Use these as templates for new projects.

## Python/uv Projects

**Reference:** aiterm, nexus-cli

```yaml
name: Tests

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

permissions:
  contents: read
  checks: write

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest]
        python-version: ["3.10", "3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v4
        with:
          enable-cache: true
          cache-dependency-glob: "uv.lock"

      - name: Set up Python ${{ matrix.python-version }}
        run: uv python install ${{ matrix.python-version }}

      - name: Install dependencies
        run: uv sync --all-extras --dev

      - name: Run tests with coverage
        run: uv run pytest --cov=<package> --cov-report=xml -v

      - name: Upload coverage to Codecov
        if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.12'
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage.xml
```

**Key features:**
- Multi-platform (Ubuntu + macOS)
- Multi-Python version matrix
- uv for fast dependency management
- Codecov integration

---

## Node.js Projects

**Reference:** atlas

```yaml
name: Tests

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main, dev]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20, 22]

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run unit tests
        run: npm run test:unit

      - name: Run integration tests
        run: npm run test:integration
```

**Key features:**
- Multi-Node version matrix (18, 20, 22)
- npm caching
- Separate unit/integration test jobs

---

## Tauri Projects (Rust + Vite)

**Reference:** scribe

```yaml
name: Tests

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  frontend-tests:
    name: Frontend Tests (Vitest)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run typecheck
      - run: npm run test:run

  rust-tests:
    name: Rust Tests
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
      - uses: Swatinem/rust-cache@v2
        with:
          workspaces: src-tauri
      - name: Install dependencies (Ubuntu)
        if: matrix.os == 'ubuntu-latest'
        run: |
          sudo apt-get update
          sudo apt-get install -y libwebkit2gtk-4.1-dev libappindicator3-dev librsvg2-dev patchelf
      - working-directory: src-tauri
        run: cargo test
      - working-directory: src-tauri
        run: cargo clippy -- -D warnings
```

**Key features:**
- Separate frontend (Vitest) and backend (cargo) jobs
- Rust caching with Swatinem/rust-cache
- WebKit dependencies for Linux

---

## MCP Server Projects

**Reference:** statistical-research, project-refactor

```yaml
name: Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20, 22]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

**For Bun-based MCP servers:**
```yaml
      - uses: oven-sh/setup-bun@v1
      - run: bun install
      - run: bun test
```

---

## Documentation Deployment (MkDocs)

**Reference:** aiterm, atlas, nexus-cli

```yaml
name: Deploy Documentation

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install uv
        uses: astral-sh/setup-uv@v4

      - run: uv python install 3.12
      - run: uv sync --extra docs
      - run: uv run mkdocs build

      - name: Deploy to GitHub Pages
        if: github.event_name == 'push' && github.ref == 'refs/heads/main'
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

---

## PyPI Publishing

**Reference:** aiterm

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv python install 3.12
      - run: uv build
      - uses: actions/upload-artifact@v4
        with:
          name: python-package-distributions
          path: dist/

  publish:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: pypi
      url: https://pypi.org/p/<package-name>
    permissions:
      id-token: write
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: python-package-distributions
          path: dist/
      - uses: pypa/gh-action-pypi-publish@release/v1
```

**Key:** Uses trusted publishing (no API token needed)

---

## Quick Reference

| Project Type | Test Action | Cache | Matrix |
|--------------|-------------|-------|--------|
| Python/uv | `uv run pytest` | uv.lock | Python 3.10-3.12 |
| Node/npm | `npm test` | npm | Node 18, 20, 22 |
| Rust | `cargo test` | Swatinem/rust-cache | OS matrix |
| Tauri | Both above | Both | OS + Node |
| MCP/Bun | `bun test` | bun | Node versions |

---

*Created: 2025-12-28*
*Source: aiterm, atlas, nexus-cli, scribe CI configurations*
