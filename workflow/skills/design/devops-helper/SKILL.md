---
name: devops-helper
description: This skill should be used when the user asks to "set up CI/CD", "deploy my app", "create a Dockerfile", "configure GitHub Actions", "set up testing automation", or "choose a hosting platform", or discusses containers, Kubernetes, deployment pipelines, environment variables, or infrastructure decisions. Provides pragmatic DevOps guidance optimized for indie developers and small teams.
triggers:
  - CI/CD
  - deployment
  - Docker
  - GitHub Actions
  - testing automation
  - infrastructure
  - deployment pipeline
  - continuous integration
  - container
  - Kubernetes
  - hosting
  - environment variables
---

# DevOps Helper Skill

**Auto-activated when:** User discusses deployment, CI/CD, Docker, testing automation, or infrastructure decisions.

## Core Capabilities

### 1. CI/CD Pipelines
- GitHub Actions workflow design
- Test automation (unit, integration, e2e)
- Build optimization
- Deployment strategies (blue/green, canary, rolling)
- Secrets management

### 2. Containerization
- Dockerfile best practices (multi-stage builds)
- Docker Compose for local dev
- Image optimization (layer caching, size reduction)
- Container orchestration (when needed)

### 3. Deployment Platforms
- Platform selection (Vercel, Render, Fly.io, Railway)
- Cost optimization strategies
- Database hosting (Supabase, PlanetScale, Neon)
- Static site hosting (Netlify, GitHub Pages)

### 4. Testing Automation
- Test pyramid (unit > integration > e2e)
- Pre-commit hooks (Husky, lint-staged)
- Code quality gates (coverage thresholds)
- Performance testing basics

## Design Philosophy: Solid Indie

**Ship Fast Principles:**
- Start with platform-as-a-service (Vercel, Render)
- Use managed databases (don't self-host Postgres initially)
- Automate tests, but don't obsess over 100% coverage
- Monitor errors (Sentry), not metrics initially

**Right-Sized DevOps:**
- Solo/small team: GitHub Actions + Vercel
- Need scaling: Add Fly.io or Railway
- Need full control: Then consider AWS/GCP (not before)

**Anti-Patterns to Avoid:**
- ❌ Kubernetes for < 10 person teams
- ❌ Self-hosted infrastructure before product-market fit
- ❌ Complex multi-environment setups (dev/staging/prod initially)
- ❌ Over-monitoring (start with errors, add metrics later)

## Delegation Strategy

When analysis is needed, I will:
1. **Quick assessment** - Identify DevOps problem
2. **Delegate to agents** when feasible:
   - `devops-engineer` agent for pipeline optimization
   - `experienced-engineer` agent for testing strategy
   - `performance-engineer` agent for build performance
3. **Run in background** - Use Task tool with `run_in_background: true`
4. **Synthesize results** - Provide actionable DevOps recommendations

## Example Activation

```
User: "I need to set up deployment for my Next.js app with a PostgreSQL database"

Skill activates and provides:
1. Platform recommendation (Vercel for Next.js + Supabase for PostgreSQL)
2. CI/CD setup (GitHub Actions for tests, Vercel auto-deploys)
3. Environment variables strategy (.env.local, Vercel env vars)
4. Database migrations approach (Drizzle or Prisma)
5. Delegates infrastructure review to devops-engineer agent (background)
6. Returns with complete deployment setup plan
```

## Output Format

When activated, I provide:

### Immediate Response
- **Platform Recommendation**: Best fit for project size/budget
- **Quick Win**: Fastest path to deployment
- **Cost Estimate**: Monthly hosting costs (indie budget)

### Delegated Analysis (Background)
- Launch appropriate agent for infrastructure review
- Provide progress updates
- Synthesize recommendations

### Final Output
- **Deployment strategy** with rationale
- **Step-by-step setup** (numbered, concrete)
- **GitHub Actions workflow** (YAML example)
- **Environment variables checklist**
- **Next steps** (what to deploy first)

## Platform Decision Matrix

| Need | Recommended Platform | Monthly Cost |
|------|---------------------|--------------|
| **Static site** | GitHub Pages / Netlify | Free |
| **Next.js/React** | Vercel | Free tier → $20/mo |
| **Full-stack app** | Render / Railway | $7-20/mo |
| **Python/Django** | Fly.io / Render | $5-15/mo |
| **Database** | Supabase / PlanetScale | Free tier → $25/mo |
| **Background jobs** | Render Cron / Railway | Included |

## CI/CD Templates

I'll provide templates for:

### GitHub Actions Workflow
```yaml
# Basic CI workflow for testing + deployment
name: CI/CD
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: npm test
  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Vercel
        # Vercel auto-deploys via GitHub integration
```

### Docker Multi-Stage Build
```dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package*.json ./
RUN npm ci --production
CMD ["node", "dist/index.js"]
```

## Integration with Existing Workflow

- Auto-activates during `/brainstorm` for deployment discussions
- Works with `/next` (suggests DevOps implementation steps)
- Integrates with `/done` (captures deployment decisions, configs used)

## Cost Optimization Tips

**Free Tier Strategy:**
- Frontend: Vercel/Netlify free tier (hobby projects)
- Backend: Render free tier (spins down after 15 min idle)
- Database: Supabase free tier (500MB, unlimited API requests)
- Monitoring: Sentry free tier (5K events/month)

**Total: $0/month for MVP, scales to ~$50/month at 1K users**

---

**Remember:** This skill auto-activates based on keywords. Keep recommendations indie-friendly (managed platforms, reasonable costs, minimal complexity). Ship fast, scale later.
