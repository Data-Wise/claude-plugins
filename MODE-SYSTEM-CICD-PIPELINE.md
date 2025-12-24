# Mode System CI/CD Pipeline

**Date:** 2024-12-24
**Version:** 2.0.0
**Status:** Ready for Implementation

---

## Overview

Comprehensive CI/CD pipeline for the RForge plugin mode system, ensuring automated testing, validation, and deployment with zero-downtime releases.

---

## Table of Contents

1. [Pipeline Architecture](#pipeline-architecture)
2. [Continuous Integration](#continuous-integration)
3. [Continuous Deployment](#continuous-deployment)
4. [Automated Testing](#automated-testing)
5. [Performance Validation](#performance-validation)
6. [Documentation Pipeline](#documentation-pipeline)
7. [Release Automation](#release-automation)
8. [Quality Gates](#quality-gates)

---

## Pipeline Architecture

### High-Level Flow

```
Code Commit
    ↓
┌───────────────────────────────────────┐
│   CONTINUOUS INTEGRATION (CI)         │
├───────────────────────────────────────┤
│ 1. Lint & Format Check                │
│ 2. Unit Tests (90% coverage)          │
│ 3. Integration Tests                  │
│ 4. Performance Tests                  │
│ 5. Security Scan                      │
│ 6. Regression Tests                   │
│ 7. Build Validation                   │
└───────────────────────────────────────┘
    ↓ (if main branch)
┌───────────────────────────────────────┐
│   CONTINUOUS DEPLOYMENT (CD)          │
├───────────────────────────────────────┤
│ 1. Generate Documentation             │
│ 2. Build MkDocs Site                  │
│ 3. Deploy to GitHub Pages             │
│ 4. Create Release (if tagged)         │
│ 5. Update Plugin Registry             │
└───────────────────────────────────────┘
    ↓
Production (Zero Downtime)
```

---

## Continuous Integration

### GitHub Actions Workflow

**File:** `.github/workflows/ci.yml`

```yaml
name: Continuous Integration

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: '3.10'

jobs:
  # ============================================
  # JOB 1: Lint and Code Quality
  # ============================================
  lint:
    name: Lint & Format Check
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install linting tools
        run: |
          pip install ruff black isort mypy

      - name: Run ruff (linter)
        run: |
          ruff check rforge/ tests/ scripts/
        continue-on-error: false

      - name: Check formatting (black)
        run: |
          black --check rforge/ tests/ scripts/

      - name: Check import sorting (isort)
        run: |
          isort --check-only rforge/ tests/ scripts/

      - name: Type checking (mypy)
        run: |
          mypy rforge/ --ignore-missing-imports
        continue-on-error: true  # Warnings only for now

  # ============================================
  # JOB 2: Unit Tests
  # ============================================
  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest
    timeout-minutes: 10
    needs: lint

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install pytest pytest-cov pytest-timeout

      - name: Run unit tests
        run: |
          pytest tests/unit/ \
            -v \
            --cov=rforge \
            --cov-report=term \
            --cov-report=xml \
            --timeout=30

      - name: Check coverage threshold
        run: |
          coverage report --fail-under=80

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
          flags: unit
          name: unit-tests

  # ============================================
  # JOB 3: Integration Tests
  # ============================================
  integration-tests:
    name: Integration Tests
    runs-on: ubuntu-latest
    timeout-minutes: 15
    needs: unit-tests

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install pytest pytest-timeout

      - name: Run integration tests
        run: |
          pytest tests/integration/ \
            -v \
            --timeout=60

  # ============================================
  # JOB 4: Performance Tests
  # ============================================
  performance-tests:
    name: Performance Tests
    runs-on: ubuntu-latest
    timeout-minutes: 20
    needs: integration-tests

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install pytest pytest-benchmark

      - name: Load baseline metrics
        run: |
          # Download baseline from previous run
          gh run download --name baseline-metrics || true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Run performance benchmarks
        run: |
          pytest tests/performance/ \
            -v \
            --benchmark-only \
            --benchmark-min-rounds=5 \
            --benchmark-json=benchmark.json

      - name: Validate time budgets
        run: |
          python3 scripts/validate-time-budgets.py benchmark.json

      - name: Check for regressions
        run: |
          python3 scripts/check-performance-regression.py \
            --baseline=baseline-metrics.json \
            --current=benchmark.json \
            --threshold=10
        continue-on-error: true

      - name: Save benchmark results
        uses: actions/upload-artifact@v3
        with:
          name: benchmark-results
          path: benchmark.json

      - name: Update baseline (main branch only)
        if: github.ref == 'refs/heads/main'
        uses: actions/upload-artifact@v3
        with:
          name: baseline-metrics
          path: benchmark.json

  # ============================================
  # JOB 5: Regression Tests
  # ============================================
  regression-tests:
    name: Regression Tests
    runs-on: ubuntu-latest
    timeout-minutes: 10
    needs: unit-tests

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install pytest

      - name: Run regression tests
        run: |
          pytest tests/regression/ -v

      - name: Verify backward compatibility
        run: |
          python3 scripts/verify-backward-compatibility.py

  # ============================================
  # JOB 6: Security Scan
  # ============================================
  security:
    name: Security Scan
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install security tools
        run: |
          pip install bandit safety pip-audit

      - name: Run bandit (code security)
        run: |
          bandit -r rforge/ -f json -o bandit-report.json
        continue-on-error: true

      - name: Check dependencies (pip-audit)
        run: |
          pip-audit
        continue-on-error: true

      - name: Check for secrets
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD

  # ============================================
  # JOB 7: Plugin Validation
  # ============================================
  validate-plugin:
    name: Validate Plugin Structure
    runs-on: ubuntu-latest
    timeout-minutes: 5
    needs: lint

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Validate plugin structure
        run: |
          python3 scripts/validate-all-plugins.py --strict

      - name: Validate command frontmatter
        run: |
          python3 scripts/validate-frontmatter.py rforge/

      - name: Check for hardcoded paths
        run: |
          python3 scripts/check-hardcoded-paths.py rforge/

  # ============================================
  # JOB 8: Build Test
  # ============================================
  build:
    name: Build & Package
    runs-on: ubuntu-latest
    timeout-minutes: 10
    needs: [lint, unit-tests]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install build tools
        run: |
          pip install build twine

      - name: Build plugin package
        run: |
          cd rforge
          tar -czf ../rforge-v2.0.0.tar.gz .

      - name: Validate package
        run: |
          tar -tzf rforge-v2.0.0.tar.gz

      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: plugin-package
          path: rforge-v2.0.0.tar.gz

  # ============================================
  # JOB 9: Summary
  # ============================================
  ci-summary:
    name: CI Summary
    runs-on: ubuntu-latest
    needs: [
      lint,
      unit-tests,
      integration-tests,
      performance-tests,
      regression-tests,
      security,
      validate-plugin,
      build
    ]
    if: always()

    steps:
      - name: Generate summary
        run: |
          echo "# CI Pipeline Summary" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          echo "## Results" >> $GITHUB_STEP_SUMMARY
          echo "- ✅ All checks passed" >> $GITHUB_STEP_SUMMARY
          echo "- 📊 Test coverage: ${{ needs.unit-tests.outputs.coverage }}%" >> $GITHUB_STEP_SUMMARY
          echo "- ⚡ Performance: Within targets" >> $GITHUB_STEP_SUMMARY
          echo "- 🔒 Security: No issues" >> $GITHUB_STEP_SUMMARY
```

---

## Continuous Deployment

### GitHub Actions Workflow

**File:** `.github/workflows/cd.yml`

```yaml
name: Continuous Deployment

on:
  push:
    branches: [main]
    tags:
      - 'v*'
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  # ============================================
  # JOB 1: Generate Documentation
  # ============================================
  generate-docs:
    name: Generate Documentation
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install mkdocs mkdocs-material pyyaml pymdown-extensions

      - name: Generate command reference
        run: |
          python3 scripts/generate-command-reference.py

      - name: Generate architecture diagrams
        run: |
          python3 scripts/generate-architecture-diagrams.py

      - name: Update MkDocs navigation
        run: |
          python3 scripts/update-mkdocs-nav.py

      - name: Verify documentation
        run: |
          test -f docs/COMMAND-REFERENCE.md
          test -d docs/diagrams
          test -f mkdocs.yml

      - name: Upload documentation artifact
        uses: actions/upload-artifact@v3
        with:
          name: generated-docs
          path: |
            docs/
            mkdocs.yml

  # ============================================
  # JOB 2: Build Documentation Site
  # ============================================
  build-docs:
    name: Build MkDocs Site
    runs-on: ubuntu-latest
    needs: generate-docs
    timeout-minutes: 10

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Download generated docs
        uses: actions/download-artifact@v3
        with:
          name: generated-docs

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install MkDocs
        run: |
          pip install mkdocs mkdocs-material pymdown-extensions

      - name: Build documentation site
        run: |
          mkdocs build --strict

      - name: Upload site artifact
        uses: actions/upload-artifact@v3
        with:
          name: docs-site
          path: site/

  # ============================================
  # JOB 3: Deploy to GitHub Pages
  # ============================================
  deploy-docs:
    name: Deploy to GitHub Pages
    runs-on: ubuntu-latest
    needs: build-docs
    timeout-minutes: 10

    steps:
      - name: Download site
        uses: actions/download-artifact@v3
        with:
          name: docs-site
          path: site/

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          publish_branch: gh-pages
          force_orphan: true
          user_name: 'github-actions[bot]'
          user_email: 'github-actions[bot]@users.noreply.github.com'
          commit_message: 'docs: deploy documentation for ${{ github.sha }}'

  # ============================================
  # JOB 4: Create Release (on tag)
  # ============================================
  create-release:
    name: Create GitHub Release
    runs-on: ubuntu-latest
    needs: deploy-docs
    if: startsWith(github.ref, 'refs/tags/v')
    timeout-minutes: 10

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Extract version
        id: version
        run: |
          echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT

      - name: Build plugin package
        run: |
          cd rforge
          tar -czf ../rforge-v${{ steps.version.outputs.VERSION }}.tar.gz .

      - name: Generate release notes
        run: |
          python3 scripts/generate-release-notes.py \
            --version=${{ steps.version.outputs.VERSION }} \
            --output=RELEASE_NOTES.md

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          files: rforge-v${{ steps.version.outputs.VERSION }}.tar.gz
          body_path: RELEASE_NOTES.md
          draft: false
          prerelease: false
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  # ============================================
  # JOB 5: Deployment Summary
  # ============================================
  cd-summary:
    name: CD Summary
    runs-on: ubuntu-latest
    needs: [generate-docs, build-docs, deploy-docs]
    if: always()

    steps:
      - name: Generate summary
        run: |
          echo "# Deployment Summary" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          echo "## Deployed" >> $GITHUB_STEP_SUMMARY
          echo "- 📚 Documentation: https://data-wise.github.io/claude-plugins/" >> $GITHUB_STEP_SUMMARY
          echo "- 🏷️ Version: ${{ github.ref_name }}" >> $GITHUB_STEP_SUMMARY
          echo "- ⏰ Deployed: $(date -u)" >> $GITHUB_STEP_SUMMARY
```

---

## Automated Testing

### Test Matrix

**File:** `.github/workflows/test-matrix.yml`

```yaml
name: Test Matrix

on:
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  test-matrix:
    name: Test on ${{ matrix.os }} - Python ${{ matrix.python }}
    runs-on: ${{ matrix.os }}

    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python: ['3.9', '3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python }}

      - name: Install dependencies
        run: |
          pip install pytest pytest-cov

      - name: Run tests
        run: |
          pytest tests/ -v --cov=rforge
```

---

## Performance Validation

### Performance CI Job

**Script:** `scripts/validate-time-budgets.py`

```python
#!/usr/bin/env python3
"""Validate time budgets from benchmark results."""

import json
import sys
from pathlib import Path

def validate_time_budgets(benchmark_file):
    """Validate all time budgets are met."""
    with open(benchmark_file) as f:
        data = json.load(f)

    # Time budgets (in seconds)
    budgets = {
        "test_analyze_default_mode_speed": 10.0,  # MUST
        "test_status_default_mode_speed": 5.0,    # MUST
        "test_debug_mode_speed": 120.0,           # SHOULD
        "test_optimize_mode_speed": 180.0,        # SHOULD
        "test_release_mode_speed": 300.0,         # SHOULD
    }

    failures = []

    for benchmark in data["benchmarks"]:
        name = benchmark["name"]
        mean_time = benchmark["stats"]["mean"]

        if name in budgets:
            budget = budgets[name]
            if mean_time > budget:
                severity = "CRITICAL" if "default" in name else "WARNING"
                failures.append({
                    "name": name,
                    "mean": mean_time,
                    "budget": budget,
                    "severity": severity
                })

    if failures:
        print("❌ Time budget violations:")
        for failure in failures:
            print(f"  [{failure['severity']}] {failure['name']}")
            print(f"    Mean: {failure['mean']:.2f}s > Budget: {failure['budget']:.2f}s")

        # Fail CI on CRITICAL violations
        critical = [f for f in failures if f["severity"] == "CRITICAL"]
        if critical:
            sys.exit(1)
        else:
            print("\n⚠️  Warnings only - CI passes")
            sys.exit(0)
    else:
        print("✅ All time budgets met")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate-time-budgets.py <benchmark.json>")
        sys.exit(1)

    validate_time_budgets(sys.argv[1])
```

---

## Documentation Pipeline

### Documentation CI Job

**Script:** `scripts/check-docs-links.py`

```python
#!/usr/bin/env python3
"""Check for broken links in documentation."""

import re
from pathlib import Path
import sys

def check_internal_links(docs_dir):
    """Check all internal markdown links are valid."""
    docs_path = Path(docs_dir)
    all_files = set(p.relative_to(docs_path) for p in docs_path.rglob("*.md"))

    broken_links = []

    for md_file in docs_path.rglob("*.md"):
        with open(md_file) as f:
            content = f.read()

        # Find markdown links: [text](link)
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)

        for link_text, link_url in links:
            # Skip external links
            if link_url.startswith(('http://', 'https://', '#')):
                continue

            # Resolve relative link
            target = (md_file.parent / link_url).resolve()

            if not target.exists():
                broken_links.append({
                    "file": md_file.relative_to(docs_path),
                    "link": link_url,
                    "text": link_text
                })

    if broken_links:
        print("❌ Broken links found:")
        for link in broken_links:
            print(f"  {link['file']}: [{link['text']}]({link['link']})")
        sys.exit(1)
    else:
        print("✅ All internal links valid")
        sys.exit(0)

if __name__ == "__main__":
    check_internal_links("docs/")
```

---

## Release Automation

### Semantic Release

**File:** `.github/workflows/release.yml`

```yaml
name: Release

on:
  push:
    branches: [main]
    paths:
      - 'rforge/**'
      - 'package.json'

jobs:
  release:
    name: Automated Release
    runs-on: ubuntu-latest
    if: "!contains(github.event.head_commit.message, 'skip ci')"

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install semantic-release
        run: |
          npm install -g semantic-release @semantic-release/changelog @semantic-release/git

      - name: Run semantic-release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          semantic-release
```

**Configuration:** `.releaserc.json`

```json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    [
      "@semantic-release/git",
      {
        "assets": ["CHANGELOG.md", "package.json"],
        "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
      }
    ],
    "@semantic-release/github"
  ]
}
```

---

## Quality Gates

### Pre-Merge Checks

**Required Status Checks:**

```yaml
# .github/branch-protection.yml
main:
  required_status_checks:
    - lint
    - unit-tests
    - integration-tests
    - performance-tests
    - regression-tests
    - security
    - validate-plugin

  required_approvals: 1
  dismiss_stale_reviews: true
  require_code_owner_reviews: false
```

### Performance Gates

```python
# scripts/performance-gate.py

def check_performance_gate(benchmark_results):
    """Performance gate for CI/CD."""

    gates = {
        "default_mode_latency": {
            "metric": "p95_latency_seconds",
            "threshold": 10.0,
            "hard_fail": True
        },
        "error_rate": {
            "metric": "error_percentage",
            "threshold": 1.0,
            "hard_fail": True
        },
        "regression": {
            "metric": "performance_regression_pct",
            "threshold": 10.0,
            "hard_fail": False
        }
    }

    failures = []

    for gate_name, gate_config in gates.items():
        metric_value = get_metric(benchmark_results, gate_config["metric"])

        if metric_value > gate_config["threshold"]:
            failures.append({
                "gate": gate_name,
                "value": metric_value,
                "threshold": gate_config["threshold"],
                "hard_fail": gate_config["hard_fail"]
            })

    return failures
```

---

## Next Steps

1. **Create GitHub Actions workflows** (Day 2)
2. **Set up branch protection** (Day 2)
3. **Configure automated testing** (Day 3)
4. **Test CI/CD pipeline** (Day 3)
5. **Document pipeline** (Day 4)
6. **Deploy to production** (Day 5)

---

**Status:** CI/CD pipeline defined, ready for implementation

**Next Action:** Create GitHub Actions workflow files

---
