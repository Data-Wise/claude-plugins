# Roadmap Generation

Generate and maintain project roadmaps.

## Usage

```bash
/craft:plan:roadmap [options]
```

## What This Does

1. **Analyzes project state** and planned features
2. **Organizes into milestones** and phases
3. **Estimates timelines** based on complexity
4. **Generates visual roadmap** for stakeholders

## Roadmap Elements

| Element | Description |
|---------|-------------|
| Milestones | Major release points |
| Phases | Development stages |
| Features | Grouped by theme |
| Dependencies | Cross-feature relationships |
| Risks | Timeline threats |

## Options

- `--horizon <months>` - Planning horizon (default: 6)
- `--format <type>` - mermaid, markdown, html
- `--output <file>` - Save roadmap to file
- `--update` - Update existing roadmap

## Examples

```bash
# Generate 6-month roadmap
/craft:plan:roadmap

# Quarterly roadmap
/craft:plan:roadmap --horizon 3

# Generate as Mermaid diagram
/craft:plan:roadmap --format mermaid

# Save to file
/craft:plan:roadmap --output ROADMAP.md

# Update existing roadmap
/craft:plan:roadmap --update
```

## Output

```
Project Roadmap: Q1-Q2 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 1: Foundation (Jan 2025)
├── Milestone: v1.0 - Core Platform
│   ├── User Authentication ████████░░ 80%
│   ├── Profile Management ██████░░░░ 60%
│   └── Basic API         ██████████ 100%
└── Target: Jan 15

PHASE 2: Growth Features (Feb-Mar 2025)
├── Milestone: v1.1 - Social Features
│   ├── Friend System      ░░░░░░░░░░ 0%
│   ├── Activity Feed      ░░░░░░░░░░ 0%
│   └── Notifications      ░░░░░░░░░░ 0%
├── Milestone: v1.2 - Monetization
│   ├── Payment Integration ░░░░░░░░░░ 0%
│   └── Subscription Tiers  ░░░░░░░░░░ 0%
└── Target: Mar 31

PHASE 3: Scale (Apr-Jun 2025)
├── Milestone: v2.0 - Enterprise
│   ├── Team Management    ░░░░░░░░░░ 0%
│   ├── Admin Dashboard    ░░░░░░░░░░ 0%
│   └── Analytics          ░░░░░░░░░░ 0%
└── Target: Jun 30

Key Dependencies:
  v1.1 depends on v1.0 completion
  Payment requires legal review
  Enterprise needs security audit

Risks:
  ⚠ Q1 holiday schedule may delay v1.0
  ⚠ Payment provider integration timeline TBD

Timeline Visualization:

Jan     Feb     Mar     Apr     May     Jun
├───────┼───────┼───────┼───────┼───────┤
[  v1.0  ]
        [    v1.1     ]
                [  v1.2  ]
                        [      v2.0        ]
```

## Integration

Works with:
- `/craft:plan:sprint` - Sprint planning
- `/craft:plan:feature` - Feature details
- `/craft:docs:sync` - Update documentation
