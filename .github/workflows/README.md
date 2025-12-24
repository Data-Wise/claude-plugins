# GitHub Actions Workflows

This directory contains automated CI/CD workflows for the Claude Plugins project, with special focus on the RForge plugin mode system.

## Workflows Overview

### 1. `validate.yml` - Main CI Pipeline

**Triggers:**
- Push to `main` or `dev` branches
- Pull requests to `main` or `dev`
- Changes to `rforge/`, `tests/`, `scripts/`, or workflow files

**Jobs:**

#### validate-structure
- Validates RForge plugin structure (required files, directories)
- Checks JSON configuration files (package.json, plugin.json)
- Validates command frontmatter (name, description fields)
- Detects hardcoded paths
- Reports plugin statistics

**Duration:** ~1 minute

#### test-unit (Matrix)
- Runs 96 unit tests on Python 3.9, 3.10, 3.11, 3.12
- Generates coverage report (must be ≥80%)
- Uploads coverage to Codecov (Python 3.11 only)
- Validates test performance (all tests < 1s)
- Uploads HTML coverage report as artifact

**Duration:** ~2-3 minutes per Python version

#### test-mode-system
- Tests mode system components (default, debug, optimize, release)
- Validates time budget enforcement
- Tests format handling (markdown, JSON, minimal)
- Verifies backward compatibility

**Duration:** ~1 minute

#### validate-docs
- Builds MkDocs documentation with `--strict` mode
- Validates documentation structure
- Checks for broken internal links
- Reports documentation statistics

**Duration:** ~1 minute

#### performance-check (Optional)
- Runs performance benchmarks (continues on error)
- Validates time budget configuration
- Reports benchmark statistics

**Duration:** ~1 minute

#### final-summary
- Aggregates all CI check results
- Reports overall success/failure

**Total Duration:** ~5-8 minutes (parallel execution)

---

### 2. `deploy-docs.yml` - Documentation Deployment

**Triggers:**
- Push to `main` branch
- Changes to plugin files, docs, or scripts
- Manual workflow dispatch

**Jobs:**

#### build-docs
- Generates command reference (17+ commands)
- Generates architecture diagrams (8+ diagrams)
- Updates MkDocs navigation automatically
- Builds MkDocs site with strict mode
- Validates build output
- Uploads site as artifact

**Duration:** ~2 minutes

#### deploy
- Downloads build artifact
- Deploys to GitHub Pages (gh-pages branch)
- Uses peaceiris/actions-gh-pages@v3
- Force orphan commits for clean history

**Duration:** ~1 minute

#### verify-deployment
- Waits for GitHub Pages propagation
- Checks site is accessible (HTTP 200)
- Reports deployment status

**Duration:** ~30 seconds

**Total Duration:** ~4 minutes

**Output:** https://data-wise.github.io/claude-plugins/

---

### 3. `benchmark.yml` - Weekly Performance Benchmarks

**Triggers:**
- Schedule: Every Monday at 9:00 AM UTC
- Manual workflow dispatch (with options)

**Jobs:**

#### benchmark
- Runs pytest-benchmark on all unit tests
- Generates JSON benchmark results
- Analyzes performance statistics
- Identifies slow tests (>1s)
- Validates time budget compliance
- Generates performance report
- Uploads results as artifacts (90-day retention)

**Duration:** ~3 minutes

#### compare
- Downloads current benchmark
- Attempts to fetch baseline (from previous runs)
- Compares performance trends
- Calculates summary statistics

**Duration:** ~1 minute

#### report
- Aggregates benchmark data
- Generates weekly summary report
- Uploads to artifacts (365-day retention)
- Provides recommendations

**Duration:** ~30 seconds

**Total Duration:** ~5 minutes

**Artifacts:**
- `benchmark-results-{sha}` (90 days)
- `performance-summary` (365 days)

---

### 4. `validate-plugins.yml` - Multi-Plugin Validation (Existing)

**Triggers:**
- Push/PR to `main` or `dev`
- Changes to any plugin directory

**Validates:**
- rforge-orchestrator
- statistical-research
- workflow

**Jobs:**
- Individual plugin validation (matrix)
- Comprehensive validation script
- Final summary

**Duration:** ~3-4 minutes

---

### 5. `docs.yml` - Legacy Documentation Workflow (Existing)

**Note:** This workflow is superseded by `deploy-docs.yml` for RForge but still maintains other plugins.

**Triggers:**
- Push to `main`
- Changes to plugin commands/skills
- Manual dispatch

---

## Workflow Features

### Performance Optimizations

1. **Caching:**
   - Python pip dependencies cached
   - Faster subsequent runs (~30% speedup)

2. **Parallel Execution:**
   - Matrix strategy for multi-version testing
   - Independent jobs run concurrently

3. **Conditional Steps:**
   - Skip optional checks on failure
   - Continue-on-error for non-critical tasks

### Error Handling

1. **Clear Error Messages:**
   - Colorized output (ANSI colors in summaries)
   - Contextual error reporting
   - Step-by-step validation

2. **Fail-Fast Strategy:**
   - Critical errors halt pipeline
   - Non-critical errors logged as warnings

3. **Artifact Retention:**
   - Coverage reports: 30 days
   - Benchmarks: 90 days
   - Performance summaries: 365 days

### Security

1. **Minimal Permissions:**
   - Only `contents: write` for gh-pages deployment
   - Read-only for other workflows

2. **Secret Management:**
   - Uses `GITHUB_TOKEN` (auto-generated)
   - No custom secrets required

3. **Safe Defaults:**
   - Force orphan for gh-pages (no history leaks)
   - Bot user for commits

---

## Local Testing

### Validate Workflow Syntax

```bash
# Install act (GitHub Actions local runner)
brew install act

# Validate workflow syntax
act -l --workflows .github/workflows/validate.yml

# Run workflow locally (requires Docker)
act push --workflows .github/workflows/validate.yml
```

### Run Tests Locally

```bash
cd /Users/dt/projects/dev-tools/claude-plugins

# Run all unit tests
python3 -m pytest tests/unit/ -v

# Run with coverage
python3 -m pytest tests/unit/ --cov=rforge --cov-report=term-missing

# Run mode system tests only
python3 -m pytest tests/unit/ -m "mode_system" -v

# Run benchmarks
python3 -m pytest tests/unit/ --benchmark-only
```

### Build Docs Locally

```bash
# Generate documentation
python3 scripts/generate-command-reference.py
python3 scripts/generate-architecture-diagrams.py
python3 scripts/update-mkdocs-nav.py

# Build MkDocs site
mkdocs build --strict

# Serve locally
mkdocs serve
# Visit: http://127.0.0.1:8000
```

---

## Monitoring & Maintenance

### Check Workflow Status

1. **GitHub Actions Tab:**
   - https://github.com/Data-Wise/claude-plugins/actions

2. **Branch Protection:**
   - Require `validate.yml` to pass before merge
   - Enable status checks in repo settings

3. **Notifications:**
   - Configure email/Slack for failures
   - Watch repository for workflow updates

### Benchmark Monitoring

1. **Weekly Review:**
   - Check Monday benchmark results
   - Review performance trends
   - Identify regressions

2. **Artifact Management:**
   - Download historical benchmarks
   - Compare trends over time
   - Set up alerts for significant changes

### Documentation Updates

1. **Automatic Deployment:**
   - Every push to `main` triggers rebuild
   - No manual intervention needed

2. **Manual Triggers:**
   - Use workflow_dispatch for immediate updates
   - Force rebuild after major changes

---

## Troubleshooting

### Common Issues

**1. Test Failures on Specific Python Version**
```bash
# Run locally with specific Python version
pyenv install 3.9.18
pyenv shell 3.9.18
python -m pytest tests/unit/ -v
```

**2. Coverage Below Threshold**
```bash
# Check which lines are missing coverage
python -m pytest tests/unit/ --cov=rforge --cov-report=html
open htmlcov/index.html
```

**3. Documentation Build Fails**
```bash
# Build with verbose output
mkdocs build --strict --verbose

# Check for broken links
python3 scripts/validate-all-plugins.py
```

**4. Benchmark Failures**
```bash
# Run benchmarks locally
python -m pytest tests/unit/ --benchmark-only --benchmark-verbose

# Check for slow tests
python -m pytest tests/unit/ --durations=0
```

### Workflow Debugging

**Enable debug logging:**

1. Go to repo Settings → Secrets → Actions
2. Add secret: `ACTIONS_STEP_DEBUG` = `true`
3. Re-run workflow for detailed logs

**Check workflow syntax:**
```bash
# Install yamllint
pip install yamllint

# Validate YAML
yamllint .github/workflows/*.yml
```

---

## Performance Targets

### Test Execution
- **Unit tests:** < 1s total (96 tests)
- **Mode tests:** < 0.5s
- **Coverage generation:** < 5s

### CI Pipeline
- **validate.yml:** < 10 minutes total
- **deploy-docs.yml:** < 5 minutes
- **benchmark.yml:** < 10 minutes

### Time Budgets (Mode System)
- **default mode:** 30s (MUST)
- **debug mode:** 180s (SHOULD)
- **optimize mode:** 120s (SHOULD)
- **release mode:** 30s (MUST)

---

## Next Steps

### Immediate
1. ✅ Workflows created
2. ✅ Documentation complete
3. ⏳ Commit and push workflows
4. ⏳ Verify first CI run
5. ⏳ Check GitHub Pages deployment

### Short-term (This Week)
1. Set up branch protection rules
2. Configure Codecov integration
3. Establish performance baselines
4. Add workflow status badges to README

### Long-term (This Month)
1. Add integration tests workflow
2. Set up automated releases
3. Configure performance alerts
4. Build benchmark comparison dashboard

---

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [pytest-benchmark](https://pytest-benchmark.readthedocs.io/)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [Codecov](https://about.codecov.io/)

---

**Last Updated:** 2025-12-24
**Maintained by:** DevOps Team
**Contact:** See CONTRIBUTING.md
