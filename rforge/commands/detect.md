---
name: rforge:detect
description: Auto-detect R package project structure (single package, ecosystem, or hybrid)
---

# /rforge:detect - Project Structure Detection

Automatically detect your R package ecosystem structure.

## What It Does

Uses the `rforge_detect` MCP tool to analyze your current directory and identify:
- **Single package**: One R package
- **Ecosystem**: Multiple related packages (like mediationverse)
- **Hybrid**: Mix of packages and other projects

## Usage

```bash
# Detect from current directory
/rforge:detect

# Detect from specific path
/rforge:detect /path/to/packages
```

## Output

Returns project structure classification with:
- Number of packages found
- Dependency relationships
- Project type (single/ecosystem/hybrid)
- Recommended workflows

## Examples

### Single Package
```
📦 Single Package: medfit
Type: R Package
Location: ~/projects/r-packages/medfit
Status: Active development
```

### Ecosystem
```
🏗️ Ecosystem: mediationverse
Packages: 4 (medfit, probmed, medsim, mediationverse)
Structure: Core → Implementations → Meta
Dependencies: 3 internal
```

## Use When

- Starting work on unfamiliar project
- Planning ecosystem-wide changes
- Understanding project structure
- Before running other RForge commands

## Related Commands

- `/rforge:status` - Check health after detection
- `/rforge:deps` - Visualize dependencies
- `/rforge:analyze` - Run full analysis
