# Week Plans - Claude Plugins

**Current Week:** Week 2 (Starting 2024-12-24)
**Focus:** Mode System Implementation

---

## Week 2: Mode System Implementation

**Status:** Ready to Start
**Goal:** Implement mode system with strict performance guarantees
**Reference:** `MODE-SYSTEM-DESIGN.md` for complete specification

### Overview

Implement the mode system that provides explicit control over command behavior depth and performance.

**Key Principles:**
- Modes are VERBS (debug, optimize, release)
- Default = fast, lightweight (< 10s)
- NO automatic mode detection (explicit only)
- Backward compatible (existing commands unchanged)
- Strict performance guarantees

### Week 2 Schedule

---

## Day 1 (Monday): Plugin Command Updates - Part 1

### Morning: Update `/rforge:analyze` Command (2-3 hours)

**File:** `plugins/rforge/commands/analyze.md`

**Tasks:**
1. **Add mode parameter to frontmatter**
   ```yaml
   arguments:
     - name: context
       description: What changed or what to focus on
       required: false
       type: string
     - name: mode
       description: Analysis depth (debug, optimize, release)
       required: false
       type: string
       default: "default"
     - name: format
       description: Output format (json, markdown, terminal)
       required: false
       type: string
       default: "terminal"
   ```

2. **Add mode behavior section to instructions**
   - Default mode (< 10s): Balanced, critical issues, recent changes
   - Debug mode (30s-2m): Deep inspection, all dependencies, detailed traces
   - Optimize mode (1-3m): Performance analysis, profiling, bottlenecks
   - Release mode (2-5m): Comprehensive validation, R CMD check equivalent

3. **Update command instructions**
   - Detect mode from argument
   - Respect time budget for mode
   - Delegate to MCP with mode parameter
   - Format output appropriately

4. **Test command**
   ```bash
   /rforge:analyze                           # Default mode
   /rforge:analyze --mode debug              # Debug mode
   /rforge:analyze --mode release            # Release mode
   /rforge:analyze --mode debug --format json  # Mode + format
   ```

**Success Criteria:**
- [ ] Mode parameter parsed correctly
- [ ] Mode-specific behavior documented
- [ ] Command instructions updated
- [ ] Test cases pass

### Afternoon: Update `/rforge:status` Command (2-3 hours)

**File:** `plugins/rforge/commands/status.md`

**Tasks:**
1. **Add mode and format parameters**
   - Same pattern as analyze command
   - Default, debug, optimize, release modes

2. **Define mode behaviors**
   - Default (2-5s): Quick dashboard, health score, critical warnings
   - Debug (15-30s): Per-package breakdown, all warnings, dependency tree
   - Optimize (30s-1m): Performance metrics, load times, slow functions
   - Release (1-2m): CRAN readiness, version validation, breaking changes

3. **Update command instructions**
   - Mode-specific status checks
   - Time budget enforcement
   - Output formatting

4. **Test command**
   ```bash
   /rforge:status                    # Default mode
   /rforge:status --mode debug       # Debug mode
   /rforge:status --format markdown  # Markdown output
   ```

**Success Criteria:**
- [ ] Mode parameter works correctly
- [ ] Different modes show appropriate detail
- [ ] Performance within time budgets
- [ ] Backward compatible (no mode = default)

### Evening: Documentation (30 min)

**Tasks:**
- [ ] Update command reference with mode examples
- [ ] Create quick mode comparison table
- [ ] Document time budgets

---

## Day 2 (Tuesday): Plugin Command Updates - Part 2

### Morning: Add Format Support (2-3 hours)

**Tasks:**
1. **Implement format handlers**
   - Terminal format (Rich, default)
   - JSON format (machine-readable)
   - Markdown format (documentation)

2. **Update analyze and status commands**
   - Add format instructions
   - Test format parameter
   - Verify format + mode combinations

3. **Test format combinations**
   ```bash
   /rforge:analyze --format json
   /rforge:analyze --mode debug --format json
   /rforge:status --format markdown
   /rforge:status --mode release --format markdown
   ```

**Success Criteria:**
- [ ] JSON format outputs valid JSON
- [ ] Markdown format outputs valid markdown
- [ ] Terminal format uses Rich formatting
- [ ] All mode + format combinations work

### Afternoon: Backward Compatibility Testing (1-2 hours)

**Tasks:**
1. **Test existing usage patterns**
   ```bash
   # These must work exactly as before
   /rforge:analyze "Updated mediation algorithm"
   /rforge:status
   /rforge:quick
   /rforge:analyze
   ```

2. **Verify default behavior**
   - Commands without mode use default
   - Default mode is fast (< 10s)
   - Output looks correct
   - No breaking changes

3. **Document compatibility**
   - Update migration guide
   - Document default behavior
   - Add backward compatibility tests

**Success Criteria:**
- [ ] All existing commands work unchanged
- [ ] Default behavior is fast and useful
- [ ] No breaking changes detected
- [ ] Documentation updated

### Evening: Create Command Examples (1 hour)

**Tasks:**
- [ ] Create example gallery
- [ ] Show each mode with real output
- [ ] Document when to use each mode
- [ ] Add to USAGE-GUIDE.md

---

## Day 3 (Wednesday): MCP Server Integration

### Morning: Add Mode Parameter to MCP Tools (2-3 hours)

**Location:** RForge MCP server (separate repository)

**Tasks:**
1. **Update `rforge_analyze` tool**
   ```python
   @mcp_tool
   async def rforge_analyze(
       context: str = "General analysis",
       mode: str = "default",
       format: str = "terminal"
   ) -> Dict[str, Any]:
       """Analyze with mode-specific behavior"""
       # Implementation
   ```

2. **Update `rforge_status` tool**
   - Add mode and format parameters
   - Implement mode-specific logic
   - Add time budget tracking

3. **Add time budget enforcement**
   ```python
   time_budgets = {
       "default": 10,      # seconds
       "debug": 120,       # 2 minutes
       "optimize": 180,    # 3 minutes
       "release": 300      # 5 minutes
   }

   # Set timeout based on mode
   timeout = time_budgets.get(mode, 10)
   ```

4. **Test MCP tools**
   - Call tools directly with different modes
   - Verify time budgets respected
   - Check output quality

**Success Criteria:**
- [ ] MCP tools accept mode parameter
- [ ] Time budgets enforced
- [ ] Mode-specific behavior implemented
- [ ] Format parameter works

### Afternoon: Implement Mode-Specific Logic (2-3 hours)

**Tasks:**
1. **Default mode implementation**
   - Fast analysis (< 10s)
   - Critical issues only
   - Recent changes focus
   - Quick health metrics

2. **Debug mode implementation**
   - Deep inspection (30s-2m)
   - All dependencies (recursive)
   - Complete file scans
   - Detailed error traces

3. **Optimize mode implementation**
   - Performance analysis (1-3m)
   - Profile R code
   - Analyze load times
   - Detect bottlenecks

4. **Release mode implementation**
   - Comprehensive validation (2-5m)
   - R CMD check equivalent
   - Test suite execution
   - CRAN compliance check

**Success Criteria:**
- [ ] Each mode has distinct behavior
- [ ] Time budgets respected
- [ ] Quality guarantees met
- [ ] Error handling robust

### Evening: Integration Testing (1 hour)

**Tasks:**
- [ ] Test plugin → MCP integration
- [ ] Verify mode parameter passed correctly
- [ ] Test all mode + format combinations
- [ ] Document any issues

---

## Day 4 (Thursday): Performance Testing & Validation

### Morning: Performance Benchmarking (2-3 hours)

**Tasks:**
1. **Create performance test suite**
   ```bash
   # Test each command in each mode
   time /rforge:analyze                  # Should be < 10s
   time /rforge:analyze --mode debug     # Should be < 120s
   time /rforge:analyze --mode optimize  # Should be < 180s
   time /rforge:analyze --mode release   # Should be < 300s
   ```

2. **Record performance metrics**
   | Command | Mode | Target | Actual | Status |
   |---------|------|--------|--------|--------|
   | analyze | default | < 10s | ? | ⬜ |
   | analyze | debug | < 120s | ? | ⬜ |
   | analyze | optimize | < 180s | ? | ⬜ |
   | analyze | release | < 300s | ? | ⬜ |
   | status | default | < 5s | ? | ⬜ |
   | status | debug | < 30s | ? | ⬜ |

3. **Identify performance issues**
   - Commands exceeding time budgets
   - Bottlenecks in mode-specific logic
   - Optimization opportunities

4. **Optimize as needed**
   - Tune default mode (most important)
   - Ensure debug mode useful
   - Balance optimize mode depth

**Success Criteria:**
- [ ] Default modes meet < 10s guarantee (MUST)
- [ ] Other modes meet time budgets (SHOULD)
- [ ] Performance documented
- [ ] Optimization plan created if needed

### Afternoon: Quality Testing (2-3 hours)

**Tasks:**
1. **Test quality guarantees**
   - Default: Catches 80% of critical issues
   - Debug: Catches 95% of all issues
   - Optimize: Identifies top 3-5 bottlenecks
   - Release: CRAN submission confidence

2. **Create test scenarios**
   ```bash
   # Introduce known issues
   - Missing dependency
   - Outdated documentation
   - Slow function
   - CRAN policy violation

   # Test detection in each mode
   /rforge:analyze --mode default   # Should catch critical
   /rforge:analyze --mode debug     # Should catch all
   /rforge:analyze --mode optimize  # Should find slow function
   /rforge:analyze --mode release   # Should find CRAN issue
   ```

3. **Verify output quality**
   - Default: Actionable, concise
   - Debug: Detailed, thorough
   - Optimize: Specific, quantified
   - Release: Comprehensive, confident

**Success Criteria:**
- [ ] Quality guarantees met
- [ ] Output is useful in each mode
- [ ] No false positives/negatives
- [ ] Documentation accurate

### Evening: Edge Case Testing (1 hour)

**Tasks:**
- [ ] Test with invalid mode values
- [ ] Test with empty projects
- [ ] Test with large ecosystems
- [ ] Test timeout handling
- [ ] Document edge cases

---

## Day 5 (Friday): Documentation & Polish

### Morning: Mode Usage Guide (2-3 hours)

**File:** `docs/MODE-USAGE-GUIDE.md`

**Content:**
1. **Overview**
   - What are modes?
   - Why use modes?
   - Mode principles

2. **Mode Reference**
   - Default mode (when, why, examples)
   - Debug mode (when, why, examples)
   - Optimize mode (when, why, examples)
   - Release mode (when, why, examples)

3. **Decision Flowchart**
   ```
   Need results quickly? → Default
   Debugging an issue? → Debug
   Improving performance? → Optimize
   Preparing for release? → Release
   ```

4. **Real-world Examples**
   - Daily development workflow
   - Debugging workflow
   - Performance tuning workflow
   - Release preparation workflow

5. **Performance Guide**
   - Time budget expectations
   - When to use each mode
   - Combining modes with formats

**Success Criteria:**
- [ ] Guide is comprehensive
- [ ] Examples are practical
- [ ] Decision flowchart is clear
- [ ] Performance expectations documented

### Afternoon: Update Documentation (2 hours)

**Tasks:**
1. **Update COMMAND-CHEATSHEET.md**
   - Add mode column
   - Show mode syntax
   - Document time budgets

2. **Update USAGE-GUIDE.md**
   - Add mode examples to workflows
   - Update workflow templates
   - Show mode best practices

3. **Update command reference**
   - Regenerate with mode parameters
   - Add mode examples
   - Document format combinations

4. **Create MODE-QUICK-REFERENCE.md**
   - One-page mode guide
   - Quick decision tree
   - Common patterns

**Success Criteria:**
- [ ] All docs updated
- [ ] Mode system well-documented
- [ ] Examples are clear
- [ ] Quick reference is helpful

### Evening: Final Testing & Deployment (1 hour)

**Tasks:**
1. **Final validation**
   ```bash
   # Run comprehensive test suite
   python scripts/validate-all-plugins.py

   # Test all mode combinations
   bash test-modes.sh

   # Verify documentation
   mkdocs build --strict
   ```

2. **Create release notes**
   - Document mode system addition
   - List new features
   - Show examples
   - Note backward compatibility

3. **Deploy to GitHub**
   ```bash
   git add .
   git commit -m "feat: implement mode system for rforge commands"
   git push origin main
   ```

4. **Monitor deployment**
   - Watch GitHub Actions
   - Verify docs deployed
   - Check for errors

**Success Criteria:**
- [ ] All tests pass
- [ ] Documentation builds
- [ ] GitHub Pages deploys
- [ ] No errors in CI/CD

---

## Week 2 Success Metrics

### Must Have ✅
- [ ] Mode system implemented for 2+ commands
- [ ] Default mode meets < 10s guarantee
- [ ] Backward compatibility maintained (100%)
- [ ] Mode usage guide published
- [ ] Performance benchmarks documented

### Nice to Have 🎁
- [ ] All 4 modes implemented (default, debug, optimize, release)
- [ ] Format support complete (json, markdown, terminal)
- [ ] Mode decision flowchart created
- [ ] Video walkthrough recorded
- [ ] Performance optimizations applied

### Quality Indicators 📊
- [ ] No breaking changes
- [ ] Time budgets respected
- [ ] Output quality meets guarantees
- [ ] Documentation is comprehensive
- [ ] Real-world testing successful

---

## Daily Standup Template

Use this each day to track progress:

```markdown
## Day X Standup

### Completed Yesterday
- [ ] Task 1
- [ ] Task 2

### Today's Focus
- [ ] Task 1
- [ ] Task 2

### Blockers
- None / [List blockers]

### Performance Notes
- Default mode: X seconds
- Debug mode: X seconds
- Issues found: [List]

### Next Steps
- [What's next after today]
```

---

## Testing Checklist

### Plugin Commands
- [ ] `/rforge:analyze` accepts mode parameter
- [ ] `/rforge:analyze` default mode < 10s
- [ ] `/rforge:analyze` debug mode < 120s
- [ ] `/rforge:analyze` optimize mode < 180s
- [ ] `/rforge:analyze` release mode < 300s
- [ ] `/rforge:status` accepts mode parameter
- [ ] `/rforge:status` modes work correctly
- [ ] Format parameter works (json, markdown, terminal)
- [ ] Mode + format combinations work

### MCP Integration
- [ ] MCP tools accept mode parameter
- [ ] Time budget tracking works
- [ ] Timeout enforcement works
- [ ] Mode-specific logic implemented
- [ ] Error handling robust

### Backward Compatibility
- [ ] Commands without mode work
- [ ] Default behavior unchanged
- [ ] No breaking changes
- [ ] Existing workflows unaffected

### Performance
- [ ] Default mode < 10s (MUST)
- [ ] Debug mode < 120s (SHOULD)
- [ ] Optimize mode < 180s (SHOULD)
- [ ] Release mode < 300s (SHOULD)
- [ ] Performance documented

### Quality
- [ ] Default catches 80% critical issues
- [ ] Debug catches 95% all issues
- [ ] Optimize identifies bottlenecks
- [ ] Release provides CRAN confidence
- [ ] Output is actionable

### Documentation
- [ ] Mode usage guide complete
- [ ] Command reference updated
- [ ] Cheatsheet updated
- [ ] Examples provided
- [ ] Quick reference created

---

## Troubleshooting Guide

### Common Issues

**Issue: Mode parameter not recognized**
- Check command frontmatter has mode argument
- Verify argument type is string
- Check default value is "default"

**Issue: Performance exceeds budget**
- Profile mode-specific logic
- Identify bottlenecks
- Consider caching
- May need to reduce scope

**Issue: Mode-specific behavior not working**
- Check MCP tool receives mode parameter
- Verify mode value passed correctly
- Check mode-specific logic branches
- Test MCP tool independently

**Issue: Format output incorrect**
- Verify format parameter passed
- Check format handlers implemented
- Test format independently
- Validate output structure

---

## Week 2 Deliverables

### Code
1. Updated plugin commands (analyze, status)
2. Mode-aware MCP tools
3. Format handlers (json, markdown, terminal)
4. Time budget enforcement
5. Performance optimizations

### Documentation
1. MODE-SYSTEM-DESIGN.md (complete specification)
2. MODE-USAGE-GUIDE.md (how to use modes)
3. MODE-QUICK-REFERENCE.md (one-page guide)
4. Updated command reference
5. Updated USAGE-GUIDE.md
6. Updated COMMAND-CHEATSHEET.md

### Testing
1. Performance benchmark results
2. Quality validation report
3. Backward compatibility tests
4. Edge case documentation

### Deployment
1. GitHub commit with mode system
2. Documentation deployed to GitHub Pages
3. Release notes published

---

## Week 1 Review (For Context)

### Completed ✅
- [x] RForge consolidation (3 → 13 commands)
- [x] Hybrid delegation architecture
- [x] Plugin installation and testing
- [x] Documentation automation (CI/CD)
- [x] Mode system design

### Deferred to Week 2+
- [ ] Real-world testing on mediationverse
- [ ] Command cheatsheet
- [ ] Usage guide improvements
- [ ] Command aliases
- [ ] Enhanced error messages

---

## Week 3 Preview

**Focus:** Refinement, Testing, Documentation

**Planned Activities:**
1. Real-world testing on mediationverse ecosystem
2. Command aliases implementation
3. Enhanced error messages
4. Additional usage examples
5. Video tutorials (optional)
6. Performance tuning based on usage
7. Community feedback incorporation

**Estimated Effort:** 10-15 hours

---

## Resources & References

### Key Documents
- **MODE-SYSTEM-DESIGN.md** - Complete mode system specification
- **PROJECT-ROADMAP.md** - Overall project roadmap
- **EDGE-CASES-AND-GOTCHAS.md** - Troubleshooting guide
- **USAGE-GUIDE.md** - General usage guide

### Tools & Scripts
- `validate-all-plugins.py` - Plugin validation
- `generate-docs.sh` - Documentation generation
- `install-plugin.sh` - Plugin installation

### External References
- Claude Code plugin documentation
- MCP server documentation
- RForge MCP server repository

---

## Contact & Support

### If Something Goes Wrong
1. Check `EDGE-CASES-AND-GOTCHAS.md`
2. Review mode system design
3. Test individual components
4. Check GitHub Actions logs
5. Review MCP server logs

### Resources
- Documentation: https://data-wise.github.io/claude-plugins/
- Repository: https://github.com/Data-Wise/claude-plugins
- MCP Server: (separate repository)

---

**Ready to implement mode system!** 🚀

**Start with:** Day 1, Morning - Update `/rforge:analyze` command
**Reference:** MODE-SYSTEM-DESIGN.md for specifications
**Goal:** Mode system working by end of week
