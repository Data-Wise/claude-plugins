# Mode Controller Skill

Expert in managing craft plugin execution modes for different use cases.

## Mode Definitions

| Mode | Time Budget | Use Case | Behavior |
|------|-------------|----------|----------|
| **default** | < 10s | Quick tasks | Minimal output, fast |
| **debug** | < 120s | Problem solving | Verbose, traces, detailed |
| **optimize** | < 180s | Performance | Profiling, benchmarks |
| **release** | < 300s | Pre-release | Thorough, comprehensive |

## When to Use Each Mode

### Default Mode
- Quick code checks
- Simple lookups
- Status queries
- Day-to-day operations

### Debug Mode
- Investigating errors
- Tracing execution
- Understanding behavior
- Finding root causes

### Optimize Mode
- Performance profiling
- Identifying bottlenecks
- Memory analysis
- Speed improvements

### Release Mode
- Pre-deployment validation
- Complete test suites
- Documentation checks
- Full audits

## Mode Selection Logic

```
If user specifies mode → use that mode
Else if error/bug context → debug mode
Else if performance context → optimize mode
Else if release/deploy context → release mode
Else → default mode
```

## Mode-Specific Behaviors

### Code Commands

| Command | Default | Debug | Optimize | Release |
|---------|---------|-------|----------|---------|
| lint | Quick check | All rules + fix suggestions | Perf rules | All rules + strict |
| coverage | Summary | Line-by-line | Branch analysis | Full report |
| deps-check | Version only | Dependency tree | Size analysis | Security + licenses |
| ci-local | Fast checks | Full trace | Parallel jobs | All CI steps |

### Test Commands

| Command | Default | Debug | Optimize | Release |
|---------|---------|-------|----------|---------|
| run | Quick tests | Verbose + traces | Parallel | Full suite |
| coverage | Summary % | Uncovered lines | Branch % | HTML report |
| debug | Quick trace | Full stack trace | Profiling | All info |

### Architecture Commands

| Command | Default | Debug | Optimize | Release |
|---------|---------|-------|----------|---------|
| analyze | Overview | Deep dive | Hotspots | Full audit |
| review | Quick check | Line-by-line | Perf review | Comprehensive |
| diagram | Simple | Detailed | Data flow | Complete |

### Documentation Commands

| Command | Default | Debug | Optimize | Release |
|---------|---------|-------|----------|---------|
| validate | Links only | All checks | Load time | Full validation |
| sync | Changed files | All files + diff | Minimal updates | Complete sync |
| changelog | Recent | Full history | Compact | Detailed |

## Integration

This skill is automatically activated when:
- User includes mode keyword (debug, optimize, release)
- Context suggests specific mode
- Command supports mode parameter

## Example Usage

```
/craft:code:lint                    # default mode
/craft:code:lint debug              # debug mode - verbose
/craft:code:lint optimize           # optimize mode - perf focus
/craft:code:lint release            # release mode - thorough
```

## Output Format by Mode

### Default
```
✓ Lint passed (3 files checked)
```

### Debug
```
╭─ Lint Results (Debug Mode) ─────────────────────────╮
│ Files: 3                                            │
│ Rules: 45 active                                    │
├─────────────────────────────────────────────────────┤
│ src/main.py:12  - Line too long (82 > 80)          │
│ src/main.py:45  - Unused import 'os'               │
│ src/utils.py:8  - Missing docstring                │
├─────────────────────────────────────────────────────┤
│ Suggestions:                                        │
│   - Run: ruff check --fix                          │
╰─────────────────────────────────────────────────────╯
```

### Optimize
```
╭─ Lint Results (Optimize Mode) ──────────────────────╮
│ Performance Impact:                                 │
│   - 2 inefficient patterns found                   │
│   - Estimated speedup: 15% with fixes              │
├─────────────────────────────────────────────────────┤
│ src/main.py:30  - Use list comprehension           │
│ src/utils.py:15 - Cache repeated call              │
╰─────────────────────────────────────────────────────╯
```

### Release
```
╭─ Lint Results (Release Mode) ───────────────────────╮
│ Status: READY FOR RELEASE                          │
├─────────────────────────────────────────────────────┤
│ ✓ Style checks passed (45 rules)                   │
│ ✓ Type hints validated                             │
│ ✓ Documentation coverage: 95%                      │
│ ✓ No security issues                               │
│ ✓ License headers present                          │
├─────────────────────────────────────────────────────┤
│ Quality Score: 98/100                              │
╰─────────────────────────────────────────────────────╯
```
