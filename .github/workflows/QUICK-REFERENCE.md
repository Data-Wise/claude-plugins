# GitHub Actions Quick Reference

**Project:** Claude Plugins - RForge Mode System
**Last Updated:** 2025-12-24

---

## Workflow Quick Start

### Check All Workflows Status
```bash
# View recent workflow runs
gh run list --limit 10

# Watch a specific workflow
gh run watch
```

### Trigger Manual Runs
```bash
# Deploy documentation manually
gh workflow run deploy-docs.yml

# Run benchmarks with baseline comparison
gh workflow run benchmark.yml -f compare_baseline=true

# Re-run failed workflow
gh run rerun <run-id>
```

---

## Workflows at a Glance

| Workflow | Trigger | Duration | Purpose |
|----------|---------|----------|---------|
| `validate.yml` | Push, PR | ~5-8 min | Main CI: structure, tests, coverage |
| `deploy-docs.yml` | Push to main | ~4 min | Build & deploy GitHub Pages |
| `benchmark.yml` | Weekly Mon 9am | ~5 min | Performance benchmarks |
| `validate-plugins.yml` | Push, PR | ~3-4 min | Multi-plugin validation |
| `docs.yml` | Push to main | ~3 min | Legacy doc deployment |

---

## CI Pipeline (validate.yml)

### What It Does
1. ✅ Validates RForge plugin structure
2. ✅ Runs 96 unit tests on Python 3.9-3.12
3. ✅ Generates coverage report (≥80% required)
4. ✅ Tests mode system components
5. ✅ Validates documentation builds
6. ✅ Checks performance benchmarks

### Success Criteria
- All required files present
- JSON configs valid
- Command frontmatter complete
- No hardcoded paths
- 96/96 tests pass
- Coverage ≥ 80%
- All tests < 1s
- Docs build without errors

### Quick Debug
```bash
# Run full CI locally
python3 -m pytest tests/unit/ -v --cov=rforge --cov-fail-under=80

# Check structure
test -f rforge/PLUGIN.md && echo "✅" || echo "❌"

# Validate JSON
python3 -m json.tool rforge/package.json > /dev/null && echo "✅"

# Build docs
mkdocs build --strict
```

---

## Documentation Deployment (deploy-docs.yml)

### What It Does
1. 📝 Generates command reference
2. 📊 Generates architecture diagrams
3. 🗂️ Updates MkDocs navigation
4. 🏗️ Builds MkDocs site
5. 🚀 Deploys to GitHub Pages

### Output
**Live Site:** https://data-wise.github.io/claude-plugins/

### Quick Deploy
```bash
# Manual trigger via web UI
# GitHub → Actions → Deploy Documentation → Run workflow

# Or via CLI
gh workflow run deploy-docs.yml

# Check deployment status
gh run list --workflow=deploy-docs.yml --limit 5
```

### Local Preview
```bash
# Generate all docs
./scripts/generate-docs.sh

# Serve locally
mkdocs serve
# Visit: http://127.0.0.1:8000
```

---

## Performance Benchmarks (benchmark.yml)

### What It Does
1. ⏱️ Runs pytest-benchmark on all tests
2. 📊 Analyzes performance statistics
3. ⚠️ Identifies slow tests (>1s)
4. ✅ Validates time budget compliance
5. 📈 Compares with baseline (if available)
6. 📄 Generates weekly report

### Schedule
- **Automatic:** Every Monday 9:00 AM UTC
- **Manual:** Via workflow_dispatch

### Artifacts
- `benchmark-results-{sha}` (90 days)
- `performance-summary` (365 days)

### Quick Benchmark
```bash
# Run locally
python3 -m pytest tests/unit/ --benchmark-only

# Compare with saved baseline
python3 -m pytest tests/unit/ --benchmark-compare=0001

# Save new baseline
python3 -m pytest tests/unit/ --benchmark-autosave
```

---

## Common Commands

### Workflow Management
```bash
# List all workflows
gh workflow list

# View workflow file
gh workflow view validate.yml

# Enable/disable workflow
gh workflow enable validate.yml
gh workflow disable benchmark.yml
```

### Run Management
```bash
# List recent runs
gh run list --limit 20

# View specific run
gh run view <run-id>

# Download artifacts
gh run download <run-id>

# Delete old runs (cleanup)
gh run list --limit 100 --json databaseId --jq '.[].databaseId' | xargs -I {} gh api repos/:owner/:repo/actions/runs/{} -X DELETE
```

### Debugging
```bash
# View logs
gh run view <run-id> --log

# View failed jobs only
gh run view <run-id> --log-failed

# Re-run failed jobs
gh run rerun <run-id> --failed
```

---

## Performance Targets

### Test Speed
- **All 96 unit tests:** < 1s total
- **Individual test:** < 100ms max
- **Coverage generation:** < 5s

### CI Duration
- **validate.yml:** < 10 min (parallel)
- **deploy-docs.yml:** < 5 min
- **benchmark.yml:** < 10 min

### Mode Time Budgets
- **default:** 30s (MUST - strict)
- **debug:** 180s (SHOULD - flexible)
- **optimize:** 120s (SHOULD - flexible)
- **release:** 30s (MUST - strict)

---

## Monitoring

### Status Badges

Add to README.md:
```markdown
![CI Status](https://github.com/Data-Wise/claude-plugins/workflows/CI%20-%20Validate%20%26%20Test/badge.svg)
![Docs](https://github.com/Data-Wise/claude-plugins/workflows/Deploy%20Documentation/badge.svg)
![Benchmarks](https://github.com/Data-Wise/claude-plugins/workflows/Performance%20Benchmark/badge.svg)
```

### Check Status
```bash
# Overall status
gh run list --workflow=validate.yml --limit 1 --json conclusion --jq '.[0].conclusion'

# All workflows status
gh run list --limit 1 --json workflow,conclusion
```

---

## Troubleshooting

### Issue: Test Failures on Python 3.9

**Cause:** Compatibility issues with older Python
**Fix:**
```bash
# Test locally with Python 3.9
pyenv install 3.9.18
pyenv shell 3.9.18
python -m pytest tests/unit/ -v
```

### Issue: Coverage Below 80%

**Cause:** Missing test coverage
**Fix:**
```bash
# Generate HTML coverage report
python -m pytest tests/unit/ --cov=rforge --cov-report=html
open htmlcov/index.html

# Identify missing coverage
python -m pytest tests/unit/ --cov=rforge --cov-report=term-missing
```

### Issue: Docs Build Fails

**Cause:** Broken links or invalid markdown
**Fix:**
```bash
# Build with verbose output
mkdocs build --strict --verbose

# Validate plugins
python3 scripts/validate-all-plugins.py
```

### Issue: Slow Tests

**Cause:** Tests exceeding 1s threshold
**Fix:**
```bash
# Identify slow tests
python -m pytest tests/unit/ --durations=0

# Run with profiling
python -m pytest tests/unit/ --profile
```

---

## Best Practices

### Before Push
```bash
# Run full validation
python3 -m pytest tests/unit/ -v --cov=rforge --cov-fail-under=80

# Validate YAML
yamllint .github/workflows/*.yml

# Check docs build
mkdocs build --strict
```

### Branch Protection
1. Require `validate.yml` to pass
2. Require code review
3. Require branch to be up-to-date
4. No force push to main

### Artifact Management
1. Download important benchmarks
2. Clean up old artifacts monthly
3. Save baselines before major changes

---

## Quick Links

- **Actions Dashboard:** https://github.com/Data-Wise/claude-plugins/actions
- **Workflows Directory:** `.github/workflows/`
- **Full Documentation:** [README.md](.github/workflows/README.md)
- **Project Docs:** https://data-wise.github.io/claude-plugins/

---

## Emergency Commands

### Disable All Workflows
```bash
for workflow in validate deploy-docs benchmark; do
  gh workflow disable $workflow.yml
done
```

### Re-enable All Workflows
```bash
for workflow in validate deploy-docs benchmark; do
  gh workflow enable $workflow.yml
done
```

### Force Documentation Rebuild
```bash
gh workflow run deploy-docs.yml
gh run watch
```

### Clear All Artifacts
```bash
# WARNING: This deletes ALL artifacts!
gh api repos/:owner/:repo/actions/artifacts --paginate --jq '.artifacts[] | .id' | xargs -I {} gh api repos/:owner/:repo/actions/artifacts/{} -X DELETE
```

---

**Next Steps:**
1. Commit workflows: `git add .github/workflows/ && git commit -m "ci: add comprehensive CI/CD workflows"`
2. Push to dev: `git push origin dev`
3. Monitor first run: `gh run watch`
4. Merge to main after validation
5. Check GitHub Pages deployment

---

**Questions?** See [README.md](.github/workflows/README.md) for detailed documentation.
