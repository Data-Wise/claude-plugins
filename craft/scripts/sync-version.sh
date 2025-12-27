#!/bin/bash
# sync-version.sh - Sync version across all craft plugin files
# Usage: ./scripts/sync-version.sh 1.6.0

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$(dirname "$SCRIPT_DIR")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

if [ -z "$1" ]; then
    echo -e "${RED}Error: Version argument required${NC}"
    echo "Usage: $0 <version>"
    echo "Example: $0 1.6.0"
    exit 1
fi

VERSION="$1"

# Validate version format (semver)
if ! [[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9]+)?$ ]]; then
    echo -e "${RED}Error: Invalid version format '$VERSION'${NC}"
    echo "Expected format: X.Y.Z or X.Y.Z-suffix (e.g., 1.6.0 or 1.6.0-dev)"
    exit 1
fi

echo "Syncing craft plugin to version $VERSION..."
echo ""

# 1. Update plugin.json
PLUGIN_JSON="$PLUGIN_DIR/.claude-plugin/plugin.json"
if [ -f "$PLUGIN_JSON" ]; then
    # Use Python for reliable JSON editing (jq may not be installed)
    python3 -c "
import json
with open('$PLUGIN_JSON', 'r') as f:
    data = json.load(f)
data['version'] = '$VERSION'
with open('$PLUGIN_JSON', 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')
"
    echo -e "${GREEN}✓${NC} Updated plugin.json"
else
    echo -e "${YELLOW}⚠${NC} plugin.json not found"
fi

# 2. Update README.md version line
README="$PLUGIN_DIR/README.md"
if [ -f "$README" ]; then
    # Update "- **Version:** X.Y.Z" line
    sed -i '' "s/- \*\*Version:\*\* [0-9]*\.[0-9]*\.[0-9]*[^ ]*/- **Version:** $VERSION/" "$README"
    echo -e "${GREEN}✓${NC} Updated README.md version"
else
    echo -e "${YELLOW}⚠${NC} README.md not found"
fi

# 3. Update ROADMAP.md current version (if exists)
ROADMAP="$PLUGIN_DIR/ROADMAP.md"
if [ -f "$ROADMAP" ]; then
    # Update "## Current Version: X.Y.Z" line
    sed -i '' "s/## Current Version: [0-9]*\.[0-9]*\.[0-9]*[^ ]*/## Current Version: $VERSION/" "$ROADMAP"
    echo -e "${GREEN}✓${NC} Updated ROADMAP.md version"
else
    echo -e "${YELLOW}⚠${NC} ROADMAP.md not found (optional)"
fi

echo ""
echo -e "${GREEN}Version synced to $VERSION${NC}"
echo ""
echo "Next steps:"
echo "  1. Run ./scripts/validate-counts.sh to verify stats"
echo "  2. Update CHANGELOG section in README.md"
echo "  3. Commit: git commit -am 'chore(release): v$VERSION'"
