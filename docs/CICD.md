# CI/CD Documentation

**Consolidated:** 2026-01-07
**Status:** Active and Deployed
**Platform:** GitHub Actions

This document consolidates the CI/CD infrastructure for the claude-plugins monorepo.

---

## Overview

The CI/CD pipeline automates validation, testing, documentation deployment, and performance monitoring using GitHub Actions. Three main workflows ensure code quality and automate deployment processes.

### Key Workflows

| Workflow | Purpose | Trigger | Duration |
|----------|---------|---------|----------|
| **validate-plugins.yml** | Multi-plugin validation and testing | Push, PR | ~2 minutes |
| **deploy-docs.yml** | Documentation site deployment | Push to main | ~4 minutes |
| **craft-ci.yml** | Craft plugin-specific CI | Push, PR | ~1 minute |

---

## Workflow Details

### 1. Plugin Validation (validate-plugins.yml)

**Purpose:** Validate structure and integrity of all plugins

**Matrix Strategy:**
```yaml
strategy:
  matrix:
    plugin:
      - craft
      - rforge
      - statistical-research
      - workflow
```

**Validation Steps:**
1. **Structure Check** - Required files present (plugin.json, package.json, README.md, LICENSE)
2. **JSON Validation** - Valid JSON in package.json and plugin.json
3. **Required Fields** - All required metadata fields present
4. **Command Structure** - Markdown files have proper frontmatter
5. **Path Safety** - No hardcoded paths in commands/lib
6. **Link Validation** - No obvious broken links in README

**Triggers:**
- Push to main, dev branches
- Pull requests
- Changes to plugin directories or workflows

**Duration:** ~28 seconds per plugin (parallel execution)

---

### 2. Documentation Deployment (deploy-docs.yml)

**Purpose:** Automated documentation generation and GitHub Pages deployment

**Jobs:**

#### Build Documentation
```yaml
- Generate command reference from all plugins
- Generate architecture diagrams (Mermaid)
- Update MkDocs navigation
- Build with strict mode (fail on warnings)
- Upload build artifacts
```

#### Deploy to GitHub Pages
```yaml
- Deploy to gh-pages branch
- Force orphan commits (clean history)
- Verify deployment successful
- Site URL: https://data-wise.github.io/claude-plugins/
```

**Triggers:**
- Push to main branch
- Changes to docs/, plugins/, scripts/
- Manual workflow dispatch

**Duration:** ~4 minutes

**Output:** Live documentation site at https://data-wise.github.io/claude-plugins/

---

### 3. Craft Plugin CI (craft-ci.yml)

**Purpose:** Plugin-specific testing for the Craft plugin

**Python Matrix:**
```yaml
python-version: ['3.9', '3.10', '3.11', '3.12']
```

**Test Suite:**
- 96+ unit tests
- Mode system tests
- Integration tests
- Performance validation
- Coverage reporting (≥80%)

**Features:**
- Codecov integration
- Coverage artifact upload
- Multi-Python version testing
- Performance benchmarks

**Triggers:**
- Push to main, dev branches
- Pull requests
- Changes to craft/ directory

**Duration:** ~33 seconds

---

## Pre-commit Hooks

**Location:** `.pre-commit-config.yaml`

**Hooks:**
1. **JSON Validation** - Validate all .json files
2. **YAML Validation** - Validate all .yml/.yaml files
3. **File Fixes** - EOF, trailing whitespace, line endings
4. **Plugin Validation** - Run validate-all-plugins.py
5. **Frontmatter Check** - Ensure commands have frontmatter
6. **Package JSON Check** - Validate package.json files
7. **Plugin JSON Check** - Validate plugin.json files

**Setup:**
```bash
pip install pre-commit
pre-commit install
```

**Manual Run:**
```bash
pre-commit run --all-files
```

---

## Testing Infrastructure

### Unit Tests (pytest)

**Configuration:** `pytest.ini`

**Test Markers:**
```ini
unit              # Fast, isolated tests
integration       # May require external services
performance       # Performance benchmark tests
e2e               # End-to-end full workflow tests
mode_system       # Mode system specific tests
backward_compat   # Backward compatibility tests
time_budget       # Time budget validation tests
slow              # Tests taking > 1 second
```

**Run Tests:**
```bash
# All tests
pytest

# Specific markers
pytest -m unit
pytest -m integration
pytest -m mode_system

# With coverage
pytest --cov=rforge --cov-report=html

# Specific plugin
cd craft && pytest tests/
```

### Coverage Requirements

- **Minimum:** 80% code coverage
- **Reporting:** HTML reports in `htmlcov/`
- **CI Integration:** Codecov for trend tracking
- **Per-Plugin:** Each plugin has own test suite

---

## Repository Scripts

**Location:** `scripts/`

### Validation Scripts

**validate-all-plugins.py**
- Validates structure of all plugins
- Checks required files
- Validates JSON syntax
- Verifies naming conventions
- Used by pre-commit and CI

**Usage:**
```bash
python3 scripts/validate-all-plugins.py
```

### Documentation Scripts

**generate-command-reference.py**
- Extracts commands from all plugins
- Generates markdown reference
- Updates `docs/COMMAND-REFERENCE.md`

**generate-architecture-diagrams.py**
- Creates Mermaid diagrams for each plugin
- Flow and structure diagrams
- Outputs to `docs/diagrams/`

**update-mkdocs-nav.py**
- Scans docs directory
- Auto-generates navigation in mkdocs.yml
- Maintains consistent structure

**Usage:**
```bash
# Generate all documentation
python3 scripts/generate-command-reference.py
python3 scripts/generate-architecture-diagrams.py
python3 scripts/update-mkdocs-nav.py

# Or use shortcut
python3 scripts/generate-docs.sh
```

---

## Deployment Process

### Documentation Site

**Manual Deployment:**
```bash
# Build locally
mkdocs build --strict

# Serve locally
mkdocs serve
# Opens at http://127.0.0.1:8000

# Deploy to GitHub Pages (automatic via CI)
# Push to main triggers deploy-docs.yml
```

**Automatic Deployment:**
1. Push changes to main branch
2. GitHub Actions triggers deploy-docs.yml
3. Documentation built with MkDocs
4. Deployed to gh-pages branch
5. Live at https://data-wise.github.io/claude-plugins/

**Deployment Verification:**
- HTTP 200 status check
- Site accessibility validation
- Build artifact retention (90 days)

---

## Performance Monitoring

### Benchmarks

**Weekly Benchmarks (benchmark.yml):**
- Performance regression detection
- Time budget compliance
- Quality metric tracking
- Historical trend analysis

**Per-Commit Validation:**
- All tests complete < 1 second
- Mode system time budgets enforced
- Coverage thresholds maintained

### Metrics Tracked

**Quality Metrics:**
- Test pass rate
- Code coverage percentage
- Documentation completeness
- Validation errors

**Performance Metrics:**
- Test execution time
- Build duration
- Deployment time
- Response times

---

## Troubleshooting

### Common Issues

**1. Validation Fails on JSON**
```bash
# Check JSON syntax
python3 -m json.tool package.json
python3 -m json.tool .claude-plugin/plugin.json
```

**2. Documentation Build Fails**
```bash
# Test locally with strict mode
mkdocs build --strict

# Check for warnings
mkdocs build 2>&1 | grep WARNING
```

**3. Tests Fail in CI but Pass Locally**
```bash
# Use same Python version as CI
python3.10 -m pytest

# Check for environment-specific issues
env | grep PYTHON
```

**4. Pre-commit Hooks Fail**
```bash
# Run hooks manually
pre-commit run --all-files

# Skip hooks temporarily (not recommended)
git commit --no-verify
```

---

## Best Practices

### For Contributors

1. **Run tests locally before pushing**

   ```bash
   pytest
   ```

2. **Validate plugin structure**

   ```bash
   python3 scripts/validate-all-plugins.py
   ```

3. **Check pre-commit hooks**

   ```bash
   pre-commit run --all-files
   ```

4. **Test documentation builds**

   ```bash
   mkdocs build --strict
   ```

### For Plugin Developers

1. **Follow structure standards** - See CLAUDE.md
2. **Add tests for new features** - Maintain ≥80% coverage
3. **Update documentation** - Keep README and docs/ in sync
4. **Use semantic versioning** - MAJOR.MINOR.PATCH
5. **Test multi-Python** - Support Python 3.9-3.12

---

## CI/CD Statistics

### Workflow Performance

**Validation Pipeline:**
- Average duration: 28 seconds per plugin
- Success rate: 99%+
- Matrix: 4 plugins in parallel

**Documentation Deployment:**
- Average duration: 4 minutes
- Build success rate: 100%
- Deployment success rate: 100%

**Craft CI:**
- Average duration: 33 seconds
- Multi-Python matrix: 4 versions
- Test success rate: 100%

### Resource Usage

**GitHub Actions Minutes:**
- Validation: ~2 min per run
- Documentation: ~4 min per deployment
- Craft CI: ~2 min per run
- Total monthly: ~200 minutes (well within free tier)

---

## Future Enhancements

### Planned Improvements

1. **Automated Release** - Auto-publish to npm on tag
2. **Dependency Scanning** - Automated security updates
3. **Performance Regression** - Automated baseline comparison
4. **Multi-OS Testing** - Test on Windows, macOS, Linux
5. **Nightly Builds** - Comprehensive overnight testing

### Under Consideration

- **Docker Integration** - Containerized testing
- **Artifact Registry** - Store build artifacts
- **Code Quality Metrics** - SonarQube integration
- **Automated Changelog** - Generate from commits

---

## References

### Original Development Documents

All source documents archived in `sessions/cicd-development/`:

- CI-CD-DOCS-COMPLETE.md - Documentation implementation
- CI-CD-WORKFLOWS-COMPLETE.md - Workflow implementation
- CICD-DEPLOYMENT-SUMMARY.md - Deployment summary
- CICD-FILES-CREATED.txt - File inventory
- DEVOPS-IMPLEMENTATION-COMPLETE.md - DevOps setup
- DEVOPS-VALIDATION-SUMMARY.md - Validation details

### Related Documentation

- [CLAUDE.md](CLAUDE.md) - Developer guide with CI/CD commands
- Workflow definitions: `.github/workflows/` in repository root
- Test configuration: `pytest.ini` in repository root
- Hook configuration: `.pre-commit-config.yaml` in repository root

---

**Last Updated:** 2026-01-07
**Maintained By:** Data-Wise Team
