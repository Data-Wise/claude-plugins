# Feature Planning

Plan and scope new features with structured breakdown.

## Usage

```bash
/craft:plan:feature <feature_description>
```

## What This Does

1. **Analyzes feature request** and context
2. **Breaks down into tasks** with estimates
3. **Identifies dependencies** and risks
4. **Creates actionable plan** with acceptance criteria

## Planning Outputs

| Output | Description |
|--------|-------------|
| User Stories | Who, what, why format |
| Tasks | Concrete implementation steps |
| Estimates | Time estimates per task |
| Dependencies | Blocking items |
| Risks | Potential issues |
| Acceptance | How to verify completion |

## Options

- `--scope <level>` - MVP, full, or enterprise
- `--format <type>` - markdown, jira, github
- `--output <file>` - Save plan to file
- `--include-tests` - Include test planning

## Examples

```bash
# Plan a feature
/craft:plan:feature "user profile page with avatar upload"

# MVP scope only
/craft:plan:feature "search functionality" --scope mvp

# Include test planning
/craft:plan:feature "payment integration" --include-tests

# Export as GitHub issue
/craft:plan:feature "notifications" --format github
```

## Output

```
Feature Plan: User Profile with Avatar Upload
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User Stories:
  1. As a user, I want to view my profile so I can see my account info
  2. As a user, I want to upload an avatar so I can personalize my account
  3. As a user, I want to edit my profile details so I can keep info current

Tasks:

  Backend (8 hours)
  ├── [ ] Create profile API endpoint (2h)
  ├── [ ] Add avatar upload handler (2h)
  ├── [ ] Implement image resizing (2h)
  └── [ ] Add profile update endpoint (2h)

  Frontend (6 hours)
  ├── [ ] Create profile page component (2h)
  ├── [ ] Add avatar upload widget (2h)
  └── [ ] Implement edit form (2h)

  Infrastructure (2 hours)
  ├── [ ] Set up S3 bucket for avatars (1h)
  └── [ ] Configure CDN (1h)

Dependencies:
  - S3 bucket must be created first
  - Auth system must be in place

Risks:
  ⚠ Image upload may need size limits
  ⚠ CDN cache invalidation for avatar changes

Acceptance Criteria:
  ✓ User can view their profile page
  ✓ User can upload avatar (jpg, png, max 5MB)
  ✓ Avatar displays in header and profile
  ✓ User can edit name, bio, email

Total Estimate: 16 hours (2 days)
```

## Integration

Works with:
- `/craft:plan:sprint` - Sprint planning
- `/craft:arch:plan` - Architecture planning
- `/craft:git:branch` - Create feature branch
