# Sprint Planning

Plan and organize work for upcoming sprint.

## Usage

```bash
/craft:plan:sprint [options]
```

## What This Does

1. **Gathers pending work** from issues, PRs, and backlog
2. **Prioritizes items** based on value and dependencies
3. **Assigns capacity** based on team availability
4. **Creates sprint plan** with goals and metrics

## Planning Process

| Step | Action |
|------|--------|
| 1 | Review backlog and priorities |
| 2 | Estimate remaining work |
| 3 | Set sprint capacity |
| 4 | Select items for sprint |
| 5 | Define sprint goal |

## Options

- `--duration <days>` - Sprint length (default: 14)
- `--capacity <hours>` - Available hours
- `--goal <text>` - Sprint goal statement
- `--from <source>` - Import from GitHub/Jira

## Examples

```bash
# Plan next sprint
/craft:plan:sprint

# 1-week sprint
/craft:plan:sprint --duration 7

# Set capacity
/craft:plan:sprint --capacity 40

# Import from GitHub
/craft:plan:sprint --from github
```

## Output

```
Sprint Plan: Sprint 23 (Dec 26 - Jan 8)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sprint Goal:
  Complete user authentication and profile features

Capacity: 80 hours available

Committed Items:

  HIGH PRIORITY (40 hours)
  ├── #123 User authentication with OAuth (16h)
  ├── #124 User profile page (12h)
  └── #125 Avatar upload feature (12h)

  MEDIUM PRIORITY (24 hours)
  ├── #126 Password reset flow (8h)
  ├── #127 Email verification (8h)
  └── #128 Session management (8h)

  STRETCH GOALS (16 hours)
  ├── #129 Remember me functionality (4h)
  └── #130 Two-factor auth prep (12h)

Sprint Metrics:
  Total Points: 34
  Committed: 28 points (82%)
  Stretch: 6 points (18%)

Dependencies:
  ⚠ #123 blocks #124, #125, #126
  ⚠ External: OAuth provider setup needed

Risks:
  ⚠ OAuth integration may take longer
  ⚠ Image processing library selection

Daily Standup Schedule:
  Mon-Fri 9:00 AM
```

## Integration

Works with:
- `/craft:plan:feature` - Feature breakdown
- `/craft:plan:roadmap` - Long-term planning
- `/craft:git:branch` - Create sprint branches
