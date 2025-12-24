# Mode System Monitoring & Observability

**Date:** 2024-12-24
**Version:** 2.0.0
**Status:** Ready for Implementation

---

## Overview

Comprehensive monitoring and observability strategy for the RForge plugin mode system, tracking usage, performance, errors, and user adoption.

---

## Table of Contents

1. [Monitoring Philosophy](#monitoring-philosophy)
2. [Metrics to Track](#metrics-to-track)
3. [Logging Strategy](#logging-strategy)
4. [Performance Monitoring](#performance-monitoring)
5. [Error Tracking](#error-tracking)
6. [Usage Analytics](#usage-analytics)
7. [Alerting](#alerting)
8. [Dashboards](#dashboards)
9. [Incident Response](#incident-response)

---

## Monitoring Philosophy

### Core Principles

1. **Proactive Detection**: Catch issues before users report them
2. **Data-Driven Decisions**: Use metrics to guide improvements
3. **User-Centric**: Track metrics that matter to user experience
4. **Performance First**: Time budgets are primary success metric
5. **Privacy Respecting**: Collect only necessary data, no PII

### Observability Pillars

```
Metrics        → Quantitative data (latency, error rates)
Logs           → Event stream (command executions, errors)
Traces         → Request flow (plugin → MCP → R)
User Feedback  → Qualitative data (satisfaction, issues)
```

---

## Metrics to Track

### Performance Metrics

**Primary Metrics:**

```yaml
command_duration_seconds:
  type: histogram
  labels: [command, mode, format]
  buckets: [1, 2, 5, 10, 30, 60, 120, 300]
  description: "Command execution time in seconds"
  target:
    analyze_default: < 10s
    analyze_debug: < 120s
    status_default: < 5s

command_success_rate:
  type: gauge
  labels: [command, mode]
  description: "Percentage of successful command executions"
  target: > 99%

time_budget_exceeded_total:
  type: counter
  labels: [command, mode]
  description: "Number of times time budget was exceeded"
  target: < 1% of executions
```

**Secondary Metrics:**

```yaml
mcp_server_latency_seconds:
  type: histogram
  labels: [tool_name]
  description: "MCP server tool call latency"

format_generation_duration_seconds:
  type: histogram
  labels: [format]
  description: "Time to format output"

cache_hit_rate:
  type: gauge
  labels: [cache_type]
  description: "Cache effectiveness"
```

---

### Usage Metrics

**Adoption Metrics:**

```yaml
command_executions_total:
  type: counter
  labels: [command, mode, format]
  description: "Total command executions"

mode_distribution:
  type: gauge
  labels: [mode]
  description: "Percentage of executions by mode"
  target:
    default: 70%
    debug: 20%
    optimize: 5%
    release: 5%

format_distribution:
  type: gauge
  labels: [format]
  description: "Percentage of executions by format"

unique_users:
  type: gauge
  description: "Number of active users"
```

**Feature Usage:**

```yaml
mode_system_adoption_rate:
  type: gauge
  description: "Percentage of commands using explicit modes"
  target: > 30% by week 2

backward_compatible_usage:
  type: gauge
  description: "Percentage using v1.0.0 syntax"

advanced_feature_usage:
  type: counter
  labels: [feature]
  description: "Usage of advanced features (mode + format combos)"
```

---

### Quality Metrics

**Error Metrics:**

```yaml
error_rate:
  type: gauge
  labels: [command, error_type]
  description: "Error rate percentage"
  target: < 1%

error_total:
  type: counter
  labels: [command, error_type, mode]
  description: "Total errors by type"

validation_errors_total:
  type: counter
  labels: [parameter]
  description: "Parameter validation errors"
```

**Health Metrics:**

```yaml
plugin_health_score:
  type: gauge
  description: "Overall plugin health (0-100)"
  target: > 95

mcp_server_availability:
  type: gauge
  description: "MCP server uptime percentage"
  target: > 99.9%

documentation_accuracy_score:
  type: gauge
  description: "Documentation vs implementation match"
  target: 100%
```

---

## Logging Strategy

### Log Levels

```yaml
DEBUG:
  purpose: "Detailed debugging information"
  examples:
    - "Mode detection: detected 'debug' from context"
    - "Time budget: 3.2s / 10s (32% used)"
  enabled: Development only

INFO:
  purpose: "Normal operation events"
  examples:
    - "Command executed: /rforge:analyze mode=default format=terminal duration=4.2s"
    - "MCP tool called: rforge_status mode=default"
  enabled: Always

WARNING:
  purpose: "Potential issues, recoverable"
  examples:
    - "Time budget exceeded: 12s > 10s target (soft limit)"
    - "Cache miss: rebuilding analysis"
  enabled: Always

ERROR:
  purpose: "Error conditions, command failed"
  examples:
    - "Invalid mode parameter: 'invalid_mode'"
    - "MCP server unreachable"
  enabled: Always

CRITICAL:
  purpose: "Critical failures requiring immediate attention"
  examples:
    - "Plugin initialization failed"
    - "Corrupt configuration file"
  enabled: Always
```

---

### Log Format

**Structured JSON Logs:**

```json
{
  "timestamp": "2024-12-24T10:30:00.123Z",
  "level": "INFO",
  "component": "rforge.commands.analyze",
  "event": "command_executed",
  "data": {
    "command": "/rforge:analyze",
    "mode": "default",
    "format": "terminal",
    "duration_ms": 4200,
    "success": true,
    "time_budget_ms": 10000,
    "time_budget_used_pct": 42
  },
  "user": {
    "id": "user_hash_abc123",
    "session_id": "session_xyz789"
  },
  "context": {
    "package_count": 4,
    "packages": ["medfit", "probmed", "medsim", "mediationverse"]
  }
}
```

---

### Log Files

```bash
# Location: ~/.claude/logs/

plugin-commands.log      # All command executions
plugin-performance.log   # Performance metrics
plugin-errors.log        # Errors and warnings
plugin-usage.log         # Usage analytics
plugin-debug.log         # Debug information (dev only)
```

**Rotation Policy:**

```yaml
max_size: 100MB
max_files: 10
compression: gzip
retention: 30 days
```

---

## Performance Monitoring

### Real-Time Performance Tracking

**Script:** `scripts/monitor-performance.sh`

```bash
#!/bin/bash
# Real-time performance monitoring

LOG_FILE="$HOME/.claude/logs/plugin-performance.log"
ALERT_THRESHOLD=10000  # 10 seconds for default mode

echo "Monitoring plugin performance..."
echo "Alert threshold: ${ALERT_THRESHOLD}ms for default mode"

tail -f "$LOG_FILE" | jq -c 'select(.event == "command_executed")' | while read -r line; do
  command=$(echo "$line" | jq -r '.data.command')
  mode=$(echo "$line" | jq -r '.data.mode')
  duration=$(echo "$line" | jq -r '.data.duration_ms')
  budget=$(echo "$line" | jq -r '.data.time_budget_ms')
  used_pct=$(echo "$line" | jq -r '.data.time_budget_used_pct')

  # Color code based on performance
  if [ "$duration" -gt "$budget" ]; then
    color="\033[91m"  # Red
    status="EXCEEDED"
  elif [ "$used_pct" -gt 80 ]; then
    color="\033[93m"  # Yellow
    status="WARNING"
  else
    color="\033[92m"  # Green
    status="OK"
  fi

  echo -e "${color}[$status] ${command} mode=${mode} ${duration}ms / ${budget}ms (${used_pct}%)\033[0m"

  # Alert if default mode exceeds budget
  if [ "$mode" == "default" ] && [ "$duration" -gt "$ALERT_THRESHOLD" ]; then
    ./scripts/alert-slow-execution.sh "$line"
  fi
done
```

---

### Performance Benchmarking

**Script:** `scripts/benchmark-modes.py`

```python
#!/usr/bin/env python3
"""Benchmark all modes and track performance over time."""

import json
import time
from pathlib import Path
from datetime import datetime
from rforge.commands import AnalyzeCommand, StatusCommand

def benchmark_command(command, mode, iterations=5):
    """Benchmark a command in a specific mode."""
    durations = []

    for i in range(iterations):
        start = time.time()
        try:
            result = command.execute(mode=mode)
            duration = time.time() - start
            durations.append(duration)
        except Exception as e:
            print(f"Error in iteration {i+1}: {e}")
            continue

    return {
        "mean": sum(durations) / len(durations),
        "min": min(durations),
        "max": max(durations),
        "p95": sorted(durations)[int(len(durations) * 0.95)],
        "iterations": len(durations)
    }

def main():
    """Run all benchmarks."""
    results = {
        "timestamp": datetime.now().isoformat(),
        "benchmarks": {}
    }

    # Benchmark analyze command
    analyze = AnalyzeCommand()
    for mode in ["default", "debug", "optimize", "release"]:
        print(f"Benchmarking /rforge:analyze mode={mode}...")
        results["benchmarks"][f"analyze_{mode}"] = benchmark_command(analyze, mode)

    # Benchmark status command
    status = StatusCommand()
    for mode in ["default", "debug", "optimize", "release"]:
        print(f"Benchmarking /rforge:status mode={mode}...")
        results["benchmarks"][f"status_{mode}"] = benchmark_command(status, mode)

    # Save results
    results_dir = Path.home() / ".claude" / "benchmarks"
    results_dir.mkdir(exist_ok=True)

    filename = f"benchmark-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    results_file = results_dir / filename

    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {results_file}")

    # Print summary
    print("\n" + "="*60)
    print("BENCHMARK SUMMARY")
    print("="*60)

    for name, stats in results["benchmarks"].items():
        print(f"\n{name}:")
        print(f"  Mean: {stats['mean']:.2f}s")
        print(f"  P95:  {stats['p95']:.2f}s")
        print(f"  Max:  {stats['max']:.2f}s")

if __name__ == "__main__":
    main()
```

---

## Error Tracking

### Error Categories

```yaml
ValidationError:
  severity: LOW
  action: Log and return user-friendly error
  examples:
    - Invalid mode parameter
    - Invalid format parameter
    - Missing required argument

TimeBudgetExceeded:
  severity: MEDIUM
  action: Log warning, return partial results
  examples:
    - Default mode > 10s
    - Debug mode > 120s

MCPServerError:
  severity: HIGH
  action: Log error, retry once, fallback if needed
  examples:
    - MCP server unreachable
    - Tool call timeout
    - Invalid tool response

PluginError:
  severity: CRITICAL
  action: Log critical, notify admin, disable feature
  examples:
    - Plugin initialization failed
    - Corrupt configuration
    - Unhandled exception
```

---

### Error Logging

**Script:** `scripts/monitor-errors.sh`

```bash
#!/bin/bash
# Real-time error monitoring

ERROR_LOG="$HOME/.claude/logs/plugin-errors.log"

echo "Monitoring plugin errors..."

tail -f "$ERROR_LOG" | jq -c 'select(.level == "ERROR" or .level == "CRITICAL")' | while read -r line; do
  level=$(echo "$line" | jq -r '.level')
  error_type=$(echo "$line" | jq -r '.data.error_type')
  message=$(echo "$line" | jq -r '.data.message')
  timestamp=$(echo "$line" | jq -r '.timestamp')

  if [ "$level" == "CRITICAL" ]; then
    color="\033[91m\033[1m"  # Bold red
    echo -e "${color}[CRITICAL] ${timestamp} ${error_type}: ${message}\033[0m"
    ./scripts/alert-critical-error.sh "$line"
  else
    color="\033[93m"  # Yellow
    echo -e "${color}[ERROR] ${timestamp} ${error_type}: ${message}\033[0m"
  fi
done
```

---

## Usage Analytics

### Usage Tracking

**Script:** `scripts/analyze-usage.py`

```python
#!/usr/bin/env python3
"""Analyze plugin usage patterns."""

import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter

def analyze_usage(hours=24):
    """Analyze usage over last N hours."""
    usage_log = Path.home() / ".claude" / "logs" / "plugin-usage.log"

    cutoff = datetime.now() - timedelta(hours=hours)
    commands = []
    modes = []
    formats = []

    with open(usage_log) as f:
        for line in f:
            try:
                entry = json.loads(line)
                timestamp = datetime.fromisoformat(entry["timestamp"])

                if timestamp < cutoff:
                    continue

                commands.append(entry["data"]["command"])
                modes.append(entry["data"]["mode"])
                formats.append(entry["data"]["format"])
            except:
                continue

    total = len(commands)
    if total == 0:
        print("No usage data in last {hours} hours")
        return

    print(f"\n{'='*60}")
    print(f"USAGE ANALYSIS - Last {hours} hours")
    print(f"{'='*60}")
    print(f"\nTotal Executions: {total}")

    print(f"\n--- Commands ---")
    for cmd, count in Counter(commands).most_common():
        pct = (count / total) * 100
        print(f"  {cmd}: {count} ({pct:.1f}%)")

    print(f"\n--- Modes ---")
    for mode, count in Counter(modes).most_common():
        pct = (count / total) * 100
        print(f"  {mode}: {count} ({pct:.1f}%)")

    print(f"\n--- Formats ---")
    for fmt, count in Counter(formats).most_common():
        pct = (count / total) * 100
        print(f"  {fmt}: {count} ({pct:.1f}%)")

if __name__ == "__main__":
    analyze_usage(hours=24)
```

---

## Alerting

### Alert Conditions

```yaml
Critical Alerts:
  - Plugin initialization failed
  - MCP server down > 5 minutes
  - Error rate > 10%
  - Critical bug reported

High Priority:
  - Default mode > 10s (> 5% of executions)
  - Error rate > 5%
  - Time budget exceeded > 10%

Medium Priority:
  - Performance regression > 20%
  - Cache hit rate < 50%
  - Documentation outdated

Low Priority:
  - Mode adoption < 10% after 1 week
  - Unusual usage patterns
  - Feature request
```

---

### Alert Scripts

**Critical Alert:** `scripts/alert-critical-error.sh`

```bash
#!/bin/bash
# Alert on critical errors

ERROR_DATA="$1"

# Extract details
timestamp=$(echo "$ERROR_DATA" | jq -r '.timestamp')
error_type=$(echo "$ERROR_DATA" | jq -r '.data.error_type')
message=$(echo "$ERROR_DATA" | jq -r '.data.message')

# Log to incident file
INCIDENT_FILE="$HOME/.claude/incidents/incident-$(date +%Y%m%d-%H%M%S).json"
echo "$ERROR_DATA" > "$INCIDENT_FILE"

# Send notification (macOS)
osascript -e "display notification \"${message}\" with title \"CRITICAL: Plugin Error\" sound name \"Basso\""

# Create GitHub issue (if in production)
if [ "$ENVIRONMENT" == "production" ]; then
  gh issue create \
    --title "CRITICAL: ${error_type}" \
    --body "$(cat <<EOF
**Timestamp:** ${timestamp}
**Error Type:** ${error_type}
**Message:** ${message}

**Incident File:** ${INCIDENT_FILE}

**Action Required:** Immediate investigation
EOF
)" \
    --label "critical,bug"
fi
```

---

## Dashboards

### Real-Time Dashboard

**Script:** `scripts/dashboard.sh`

```bash
#!/bin/bash
# Real-time monitoring dashboard

clear

while true; do
  clear
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  RFORGE MODE SYSTEM - MONITORING DASHBOARD"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  date
  echo ""

  # Performance metrics (last hour)
  echo "--- PERFORMANCE (Last Hour) ---"
  python3 scripts/get-performance-summary.py --hours=1

  echo ""
  echo "--- ERRORS (Last Hour) ---"
  python3 scripts/get-error-summary.py --hours=1

  echo ""
  echo "--- USAGE (Last Hour) ---"
  python3 scripts/get-usage-summary.py --hours=1

  echo ""
  echo "--- HEALTH ---"
  python3 scripts/get-health-status.py

  echo ""
  echo "Refresh every 10s (Ctrl+C to exit)"

  sleep 10
done
```

---

### Historical Dashboard

**Generate weekly report:**

```bash
#!/bin/bash
# scripts/weekly-report.sh

WEEK_START=$(date -v-7d +%Y-%m-%d)
WEEK_END=$(date +%Y-%m-%d)

echo "Generating weekly report: ${WEEK_START} to ${WEEK_END}..."

python3 scripts/generate-weekly-report.py \
  --start="$WEEK_START" \
  --end="$WEEK_END" \
  --output="reports/week-$(date +%Y-W%V).md"

echo "Report generated: reports/week-$(date +%Y-W%V).md"
```

---

## Incident Response

### Incident Response Workflow

```
1. DETECT
   ├─ Alert triggered
   ├─ Log critical error
   └─ Create incident file

2. ASSESS
   ├─ Check severity
   ├─ Identify scope (all users vs. subset)
   └─ Estimate impact

3. RESPOND
   ├─ HIGH: Rollback immediately
   ├─ MEDIUM: Disable feature, investigate
   └─ LOW: Fix in next release

4. RESOLVE
   ├─ Apply fix
   ├─ Test thoroughly
   └─ Deploy

5. DOCUMENT
   ├─ Create incident report
   ├─ Document lessons learned
   └─ Update runbooks
```

---

### Runbooks

**Performance Degradation:**

```bash
# Symptom: Default mode > 10s

# 1. Check current performance
python3 scripts/benchmark-modes.py

# 2. Compare to baseline
diff baseline_metrics.json current_metrics.json

# 3. Profile slow execution
python3 -m cProfile -o profile.stats rforge/commands/analyze.py

# 4. Identify bottleneck
python3 -m pstats profile.stats

# 5. Fix and validate
# (make code changes)
pytest tests/performance/ -v

# 6. Deploy fix
git commit -m "perf: optimize default mode execution"
git push
```

---

**High Error Rate:**

```bash
# Symptom: Error rate > 5%

# 1. Check error types
python3 scripts/analyze-error-logs.py --hours=1

# 2. Identify common pattern
grep -E "ERROR|CRITICAL" ~/.claude/logs/plugin-errors.log | \
  jq -r '.data.error_type' | sort | uniq -c | sort -rn

# 3. Reproduce error
# (create test case)

# 4. Fix root cause
# (make code changes)

# 5. Validate fix
pytest tests/ -v

# 6. Deploy
git commit -m "fix: resolve common error pattern"
git push
```

---

## Metrics Collection

### Automated Collection

**Cron job:** Add to crontab

```bash
# Collect metrics every 5 minutes
*/5 * * * * python3 ~/projects/dev-tools/claude-plugins/scripts/collect-metrics.py

# Generate hourly summary
0 * * * * python3 ~/projects/dev-tools/claude-plugins/scripts/hourly-summary.py

# Daily report
0 9 * * * python3 ~/projects/dev-tools/claude-plugins/scripts/daily-report.py

# Weekly report
0 9 * * 1 bash ~/projects/dev-tools/claude-plugins/scripts/weekly-report.sh
```

---

## Privacy & Compliance

### Data Collection Policy

**Collected:**
- Command usage (command, mode, format)
- Performance metrics (duration, success/failure)
- Error information (type, message)
- Session metadata (session ID, timestamp)

**NOT Collected:**
- User names or emails
- File contents or code
- Package details (beyond count)
- Personal information

**Retention:**
- Logs: 30 days
- Metrics: 90 days
- Aggregated reports: 1 year
- Incident reports: Indefinite

---

## Next Steps

1. **Implement logging** (Day 2)
2. **Set up monitoring scripts** (Day 3)
3. **Create dashboards** (Day 4)
4. **Configure alerts** (Day 4)
5. **Test incident response** (Day 5)
6. **Deploy monitoring** (Day 5)

---

**Status:** Monitoring strategy defined, ready for implementation

**Next Action:** Implement structured logging in command files

---
