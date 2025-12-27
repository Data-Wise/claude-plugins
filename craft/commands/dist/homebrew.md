---
description: Generate or update Homebrew formula for your project
arguments:
  - name: action
    description: Action to perform (create|update|validate)
    required: false
    default: create
  - name: tap
    description: Homebrew tap repository (e.g., user/tap)
    required: false
  - name: version
    description: Specific version to use (default: latest tag)
    required: false
---

# /craft:dist:homebrew - Homebrew Formula Generator

Create and maintain Homebrew formulas for your projects.

## Usage

```bash
/craft:dist:homebrew                      # Auto-detect and create formula
/craft:dist:homebrew update               # Update existing formula
/craft:dist:homebrew validate             # Validate formula syntax
/craft:dist:homebrew --tap user/tap       # Specify target tap
/craft:dist:homebrew --version 1.2.3      # Use specific version
```

## Auto-Detection

Detects project type and generates appropriate formula:

### Python Projects (pyproject.toml)
```ruby
class MyApp < Formula
  include Language::Python::Virtualenv

  desc "Description from pyproject.toml"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end
end
```

### Node.js Projects (package.json)
```ruby
class MyApp < Formula
  desc "Description from package.json"
  homepage "https://github.com/user/repo"
  url "https://registry.npmjs.org/myapp/-/myapp-1.0.0.tgz"
  sha256 "..."
  license "MIT"

  depends_on "node"

  def install
    system "npm", "install", *std_npm_args
    bin.install_symlink Dir["#{libexec}/bin/*"]
  end
end
```

### Go Projects (go.mod)
```ruby
class MyApp < Formula
  desc "Description"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "go" => :build

  def install
    system "go", "build", *std_go_args(ldflags: "-s -w")
  end
end
```

### Rust Projects (Cargo.toml)
```ruby
class MyApp < Formula
  desc "Description from Cargo.toml"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "rust" => :build

  def install
    system "cargo", "install", *std_cargo_args
  end
end
```

## Workflow

### 1. Create Formula
```bash
/craft:dist:homebrew

## Output:
✓ Detected: Python project (pyproject.toml)
✓ Found version: 0.3.5 (from git tag)
✓ Calculated SHA256: abc123...
✓ Generated: Formula/myapp.rb

Formula saved to: ./Formula/myapp.rb
```

### 2. Update Existing Formula
```bash
/craft:dist:homebrew update

## Output:
✓ Found existing formula: Formula/myapp.rb
✓ Current version: 0.3.4
✓ New version: 0.3.5 (from git tag)
✓ Updated SHA256
✓ Formula updated

Changes:
  - version: 0.3.4 → 0.3.5
  - sha256: updated
```

### 3. Push to Tap
```bash
/craft:dist:homebrew --tap data-wise/tap

## Output:
✓ Generated formula
✓ Cloned tap: data-wise/tap
✓ Copied Formula/myapp.rb
✓ Committed: "myapp: update to v0.3.5"
✓ Pushed to origin

Formula published to: https://github.com/data-wise/homebrew-tap
```

## Formula Components

| Component | Source |
|-----------|--------|
| `desc` | pyproject.toml description, package.json, Cargo.toml |
| `homepage` | Git remote URL or project URL |
| `url` | GitHub release tarball |
| `sha256` | Calculated from tarball |
| `license` | Detected from LICENSE file or config |
| `depends_on` | Auto-detected from project type |

## Validation

```bash
/craft:dist:homebrew validate

## Output:
✓ Formula syntax valid
✓ URL accessible
✓ SHA256 matches
✓ Dependencies available
✓ Test block present

Ready for submission!
```

## Integration

Works with other craft commands:
- `/craft:check --for release` - Validates before formula generation
- `/craft:git:tag` - Creates version tag
- `/craft:docs:changelog` - Updates changelog

## Tips

- Always run `/craft:check --for release` before generating
- Use semantic versioning for clean formulas
- Include a `test` block for brew audit compliance
- Keep dependencies minimal for faster installs
