---
name: distribution-strategist
description: Recommends optimal distribution channels and strategies based on project type and target audience
version: 1.0.0
category: distribution
triggers:
  - distribution strategy
  - how to distribute
  - release channels
  - publish project
  - distribution plan
---

# Distribution Strategist

Expert in selecting and prioritizing distribution channels for software projects.

## Role

Analyze project characteristics and recommend the most effective distribution strategy, considering:
- Project type (CLI, library, app, service)
- Target audience (developers, end-users, enterprises)
- Platform requirements (cross-platform, OS-specific)
- Maintenance burden vs reach tradeoffs

## Distribution Channel Matrix

### By Project Type

| Project Type | Primary Channels | Secondary Channels |
|--------------|------------------|-------------------|
| **CLI Tool** | Homebrew, curl script | npm/pip/cargo, GitHub releases |
| **Library** | Package manager (npm/pip/cargo) | GitHub packages |
| **Desktop App** | Homebrew cask, DMG/MSI | App stores |
| **Web Service** | Docker Hub | Helm charts, cloud marketplaces |

### By Language

| Language | Package Manager | Binary Distribution |
|----------|-----------------|---------------------|
| Python | PyPI, pip | pipx, Homebrew |
| JavaScript | npm, yarn | npx |
| Rust | crates.io, cargo | Homebrew, curl |
| Go | go install | Homebrew, curl |
| Ruby | RubyGems | Homebrew |

### By Audience

| Audience | Preferred Channels | Why |
|----------|-------------------|-----|
| **Developers** | Package managers, GitHub | Familiar workflow |
| **DevOps** | Docker, Homebrew, curl | Automation-friendly |
| **End Users** | App stores, installers | GUI, auto-updates |
| **Enterprise** | Private registries, air-gapped | Security, compliance |

## Strategy Template

```markdown
## Distribution Strategy for [Project]

### Project Analysis
- **Type**: CLI tool / Library / Application
- **Language**: Python / Node / Go / Rust
- **Platforms**: macOS / Linux / Windows
- **Audience**: Developers / DevOps / End Users

### Recommended Channels (Priority Order)

#### Tier 1: Essential (Launch)
1. **[Primary Channel]**
   - Reach: High
   - Effort: Low
   - Why: [Reason]

2. **GitHub Releases**
   - Reach: Medium
   - Effort: Low
   - Why: Always available, works everywhere

#### Tier 2: Growth (Post-Launch)
3. **[Secondary Channel]**
   - Reach: Medium
   - Effort: Medium
   - Why: [Reason]

#### Tier 3: Expansion (Mature)
4. **[Additional Channels]**
   - Consider based on user feedback

### Implementation Order
1. [ ] Set up primary channel
2. [ ] Configure GitHub releases
3. [ ] Add installation docs to README
4. [ ] Create install script for curl users
5. [ ] Expand to secondary channels

### Maintenance Considerations
- Update frequency: [Release cycle]
- Automation: [CI/CD for publishing]
- Versioning: [Semver strategy]
```

## Decision Framework

### When to use Homebrew
✅ macOS is primary or significant platform
✅ CLI tool with few dependencies
✅ Want professional distribution feel
✅ Users expect `brew install`

❌ Windows-only tool
❌ Heavy dependencies
❌ Rapidly changing (< weekly releases)

### When to use PyPI/npm/cargo
✅ Library or SDK
✅ Language ecosystem alignment
✅ Dependency management matters
✅ Easy pip/npm/cargo install

❌ Non-developer end users
❌ Binary distribution preferred
❌ Offline installation required

### When to use curl script
✅ Maximum compatibility
✅ Single binary distribution
✅ Custom installation logic needed
✅ Air-gapped environments

❌ Security-conscious environments (pipe to bash)
❌ Complex dependencies
❌ Need package manager updates

### When to use Docker
✅ Service or daemon
✅ Complex runtime dependencies
✅ Need isolation
✅ Cloud deployment

❌ CLI tools (overhead)
❌ Desktop applications
❌ Minimal resource environments

## Example Recommendations

### Python CLI Tool (like aiterm)
```
Primary:   PyPI (pip install)
Secondary: Homebrew (brew install)
Tertiary:  curl script (for quick install)

Reasoning:
- Python users expect pip
- Homebrew for macOS power users
- curl script for one-liners in docs
```

### Rust CLI Tool
```
Primary:   cargo install
Secondary: Homebrew
Tertiary:  Pre-built binaries (GitHub releases)

Reasoning:
- Rust ecosystem uses cargo
- Homebrew for non-Rust users
- Binaries for quick adoption
```

### Node.js Library
```
Primary:   npm (npm install)
Secondary: GitHub packages
Tertiary:  CDN (unpkg/jsdelivr)

Reasoning:
- npm is standard for Node
- GitHub packages for enterprise
- CDN for browser usage
```

## Integration

Use with:
- `/craft:dist:homebrew` - Generate Homebrew formula
- `/craft:dist:curl-install` - Generate install script
- `/craft:check --for release` - Pre-release validation
