---
description: Generate curl-based installation scripts for GitHub releases
arguments:
  - name: action
    description: Action to perform (create|update|preview)
    required: false
    default: create
  - name: type
    description: Installation type (binary|source|auto)
    required: false
    default: auto
  - name: update-readme
    description: Add installation instructions to README
    required: false
---

# /craft:dist:curl-install - Installation Script Generator

Generate `install.sh` scripts for direct GitHub installation.

## Usage

```bash
/craft:dist:curl-install                  # Auto-detect and create
/craft:dist:curl-install --type binary    # Binary installation only
/craft:dist:curl-install --type source    # Source installation only
/craft:dist:curl-install --update-readme  # Add to README.md
/craft:dist:curl-install preview          # Show without writing
```

## Generated Script

### Auto-Detection Script
```bash
#!/bin/bash
set -euo pipefail

# myapp installer
# Usage: curl -fsSL https://raw.githubusercontent.com/user/repo/main/install.sh | bash

REPO="user/repo"
BINARY="myapp"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

info() { echo -e "${BLUE}==>${NC} $1"; }
success() { echo -e "${GREEN}✓${NC} $1"; }
error() { echo -e "${RED}✗${NC} $1" >&2; exit 1; }

# Detect OS and architecture
detect_platform() {
    OS=$(uname -s | tr '[:upper:]' '[:lower:]')
    ARCH=$(uname -m)

    case "$ARCH" in
        x86_64) ARCH="amd64" ;;
        aarch64|arm64) ARCH="arm64" ;;
        *) error "Unsupported architecture: $ARCH" ;;
    esac

    echo "${OS}-${ARCH}"
}

# Get latest version
get_latest_version() {
    curl -fsSL "https://api.github.com/repos/${REPO}/releases/latest" |
        grep '"tag_name"' |
        sed -E 's/.*"v?([^"]+)".*/\1/'
}

# Download and install
install() {
    PLATFORM=$(detect_platform)
    VERSION=$(get_latest_version)

    info "Installing ${BINARY} v${VERSION} for ${PLATFORM}"

    URL="https://github.com/${REPO}/releases/download/v${VERSION}/${BINARY}-${PLATFORM}.tar.gz"

    mkdir -p "$INSTALL_DIR"
    curl -fsSL "$URL" | tar -xzf - -C "$INSTALL_DIR"
    chmod +x "${INSTALL_DIR}/${BINARY}"

    success "Installed to ${INSTALL_DIR}/${BINARY}"

    # Check if in PATH
    if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
        echo ""
        info "Add to your shell profile:"
        echo "  export PATH=\"\$PATH:$INSTALL_DIR\""
    fi
}

install
```

### Source Installation (Python)
```bash
#!/bin/bash
set -euo pipefail

REPO="user/repo"
PACKAGE="myapp"

info() { echo "==> $1"; }

# Check Python
command -v python3 >/dev/null || { echo "Python 3 required"; exit 1; }

# Install with pip
info "Installing ${PACKAGE} from PyPI..."
pip3 install --user "$PACKAGE"

info "Installed! Run: $PACKAGE --help"
```

### Source Installation (Node.js)
```bash
#!/bin/bash
set -euo pipefail

PACKAGE="myapp"

# Check Node
command -v npm >/dev/null || { echo "Node.js required"; exit 1; }

# Install globally
npm install -g "$PACKAGE"

echo "Installed! Run: $PACKAGE --help"
```

## Output Files

```
./
├── install.sh              # Main installer
├── scripts/
│   ├── install-binary.sh   # Binary-only version
│   └── install-source.sh   # Source-only version
└── README.md               # Updated with instructions (if --update-readme)
```

## README Integration

```bash
/craft:dist:curl-install --update-readme

# Adds to README.md:
## Installation

### Quick Install (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/user/repo/main/install.sh | bash
```

### Homebrew (macOS)
```bash
brew install user/tap/myapp
```

### pip (Python)
```bash
pip install myapp
```
```

## Platform Detection

| Platform | Architecture | Binary Name |
|----------|--------------|-------------|
| Linux | x86_64 | myapp-linux-amd64 |
| Linux | ARM64 | myapp-linux-arm64 |
| macOS | x86_64 | myapp-darwin-amd64 |
| macOS | ARM64 | myapp-darwin-arm64 |
| Windows | x86_64 | myapp-windows-amd64.exe |

## Features

- **Version detection**: Fetches latest from GitHub API
- **Platform detection**: Auto-detects OS and architecture
- **PATH setup**: Suggests PATH additions if needed
- **Colored output**: User-friendly terminal feedback
- **Error handling**: Clear error messages with `set -euo pipefail`
- **Customizable**: `INSTALL_DIR` environment variable

## Workflow

### 1. Generate Script
```bash
/craft:dist:curl-install

## Output:
✓ Detected: Python project
✓ GitHub repo: Data-Wise/myapp
✓ Latest version: v0.3.5
✓ Generated: install.sh

Test with:
  bash install.sh
```

### 2. Preview Before Writing
```bash
/craft:dist:curl-install preview

## Shows script without writing files
```

### 3. Update README
```bash
/craft:dist:curl-install --update-readme

## Output:
✓ Generated: install.sh
✓ Updated: README.md (Installation section)
```

## Integration

Works with other craft commands:
- `/craft:dist:homebrew` - Generate Homebrew formula
- `/craft:check --for release` - Validate before generating
- `/craft:git:tag` - Create version tag

## Tips

- Test the script locally before committing
- Include checksums for security-conscious users
- Consider adding `--version` flag to specify version
- Use GitHub Actions to auto-generate on release
