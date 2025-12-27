---
name: homebrew-formula-expert
description: Expert knowledge of Homebrew formula creation, best practices, and troubleshooting
version: 1.0.0
category: distribution
triggers:
  - homebrew formula
  - brew formula
  - homebrew tap
  - formula syntax
  - brew audit
---

# Homebrew Formula Expert

Deep expertise in Homebrew formula creation, maintenance, and best practices.

## Formula Anatomy

```ruby
class MyApp < Formula
  # Metadata
  desc "Short description (< 80 chars, no 'A' or 'An' prefix)"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "64-char-hex-string"
  license "MIT"  # SPDX identifier
  head "https://github.com/user/repo.git", branch: "main"

  # Dependencies
  depends_on "python@3.12"
  depends_on "cmake" => :build  # Build-time only

  # Installation
  def install
    # Installation logic
  end

  # Verification
  test do
    # Test that installation worked
  end
end
```

## Language-Specific Patterns

### Python (virtualenv)
```ruby
class MyPythonApp < Formula
  include Language::Python::Virtualenv

  desc "My Python application"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "python@3.12"

  # For packages with many deps, list resources
  resource "requests" do
    url "https://files.pythonhosted.org/..."
    sha256 "..."
  end

  def install
    virtualenv_install_with_resources
    # Or manual:
    # venv = virtualenv_create(libexec, "python3.12")
    # venv.pip_install resources
    # venv.pip_install buildpath
    # bin.install_symlink libexec/"bin/myapp"
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/myapp --version")
  end
end
```

### Node.js
```ruby
class MyNodeApp < Formula
  desc "My Node.js application"
  homepage "https://github.com/user/repo"
  url "https://registry.npmjs.org/myapp/-/myapp-1.0.0.tgz"
  sha256 "..."
  license "MIT"

  depends_on "node"

  def install
    system "npm", "install", *std_npm_args
    bin.install_symlink Dir["#{libexec}/bin/*"]
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/myapp --version")
  end
end
```

### Go
```ruby
class MyGoApp < Formula
  desc "My Go application"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "go" => :build

  def install
    system "go", "build", *std_go_args(ldflags: "-s -w -X main.version=#{version}")
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/myapp --version")
  end
end
```

### Rust
```ruby
class MyRustApp < Formula
  desc "My Rust application"
  homepage "https://github.com/user/repo"
  url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
  sha256 "..."
  license "MIT"

  depends_on "rust" => :build

  def install
    system "cargo", "install", *std_cargo_args
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/myapp --version")
  end
end
```

## Best Practices

### Description (`desc`)
```ruby
# Good
desc "Terminal optimizer for AI-assisted development"

# Bad
desc "A terminal optimizer for AI-assisted development"  # No 'A'
desc "aiterm is a terminal optimizer..."  # No app name
desc "..."  # Too long (> 80 chars)
```

### URL Patterns
```ruby
# GitHub release (preferred)
url "https://github.com/user/repo/archive/v1.0.0.tar.gz"

# GitHub release with refs/tags (more explicit)
url "https://github.com/user/repo/archive/refs/tags/v1.0.0.tar.gz"

# PyPI
url "https://files.pythonhosted.org/packages/.../myapp-1.0.0.tar.gz"

# npm
url "https://registry.npmjs.org/myapp/-/myapp-1.0.0.tgz"
```

### SHA256 Calculation
```bash
# From URL
curl -sL https://github.com/user/repo/archive/v1.0.0.tar.gz | shasum -a 256

# From file
shasum -a 256 myapp-1.0.0.tar.gz
```

### License (SPDX identifiers)
```ruby
license "MIT"
license "Apache-2.0"
license "GPL-3.0-or-later"
license any_of: ["MIT", "Apache-2.0"]  # Dual license
```

### Dependencies
```ruby
# Runtime dependency
depends_on "python@3.12"

# Build-time only
depends_on "cmake" => :build

# Optional
depends_on "imagemagick" => :optional

# Recommended
depends_on "jq" => :recommended

# Platform-specific
depends_on "linux-headers" => :build if OS.linux?
```

## Common Issues & Fixes

### Issue: Python dependencies missing
```ruby
# Problem: pip install fails due to missing deps

# Solution: Include as resources
resource "click" do
  url "https://files.pythonhosted.org/packages/.../click-8.0.0.tar.gz"
  sha256 "..."
end

# Or install individually
def install
  venv = virtualenv_create(libexec, "python3.12")
  venv.pip_install "click>=8.0"
  venv.pip_install "rich>=13.0"
  venv.pip_install buildpath
end
```

### Issue: Binary not in PATH
```ruby
# Solution: Create symlink
def install
  # ... installation ...
  bin.install_symlink libexec/"bin/myapp"
end
```

### Issue: Test fails
```ruby
# Problem: Command requires config file

# Solution: Create minimal config in test
test do
  (testpath/".config/myapp").mkpath
  (testpath/".config/myapp/config.json").write("{}")
  assert_match version.to_s, shell_output("#{bin}/myapp --version")
end
```

### Issue: brew audit failures
```bash
# Run audit
brew audit --strict --online Formula/myapp.rb

# Common fixes:
# - desc: Remove 'A/An' prefix, keep < 80 chars
# - license: Use SPDX identifier
# - test: Must have test block
# - sha256: Must match URL content
```

## Tap Management

### Create Tap Repository
```bash
# Structure
homebrew-tap/
├── Formula/
│   ├── myapp.rb
│   └── othertool.rb
└── README.md

# Naming: homebrew-<tapname>
# Users install: brew tap user/tapname
```

### Update Formula
```ruby
# Old
url "https://github.com/user/repo/archive/v1.0.0.tar.gz"
sha256 "old-sha256"

# New
url "https://github.com/user/repo/archive/v1.0.1.tar.gz"
sha256 "new-sha256"
```

### Testing Locally
```bash
# Install from local formula
brew install --build-from-source ./Formula/myapp.rb

# Reinstall after changes
brew reinstall --build-from-source ./Formula/myapp.rb

# Uninstall
brew uninstall myapp
```

## Formula Template

```ruby
class {{ClassName}} < Formula
  {{#if python}}
  include Language::Python::Virtualenv
  {{/if}}

  desc "{{description}}"
  homepage "{{homepage}}"
  url "{{url}}"
  sha256 "{{sha256}}"
  license "{{license}}"

  {{#each dependencies}}
  depends_on "{{this}}"
  {{/each}}

  def install
    {{install_commands}}
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/{{binary}} --version")
  end
end
```

## Integration

Use with:
- `/craft:dist:homebrew` - Generate formula automatically
- `/craft:check --for release` - Validate before formula update
- `/craft:git:tag` - Create version for formula
