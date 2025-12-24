#!/usr/bin/env bash
#
# Master documentation generation script
#
# Runs all documentation generators in sequence:
# 1. Command reference generator
# 2. Architecture diagram generator
# 3. MkDocs navigation updater
# 4. (Optional) Build and deploy to GitHub Pages
#
# Usage:
#   ./generate-docs.sh              # Generate docs only
#   ./generate-docs.sh --build      # Generate + build with mkdocs
#   ./generate-docs.sh --deploy     # Generate + deploy to GitHub Pages
#

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# Parse arguments
BUILD=false
DEPLOY=false

for arg in "$@"; do
    case $arg in
        --build)
            BUILD=true
            ;;
        --deploy)
            DEPLOY=true
            BUILD=true  # Deploy requires build
            ;;
        --help|-h)
            cat << EOF
${BOLD}Documentation Generation Script${NC}

${BOLD}USAGE:${NC}
    $0                   Generate documentation files
    $0 --build           Generate docs + build with mkdocs
    $0 --deploy          Generate docs + deploy to GitHub Pages

${BOLD}STEPS:${NC}
    1. Generate command reference from frontmatter
    2. Generate architecture diagrams (Mermaid)
    3. Update mkdocs.yml navigation
    4. (Optional) Build with mkdocs
    5. (Optional) Deploy to GitHub Pages

${BOLD}REQUIREMENTS:${NC}
    - Python 3.10+
    - PyYAML (pip install pyyaml)
    - mkdocs (pip install mkdocs mkdocs-material)  # For --build/--deploy

EOF
            exit 0
            ;;
    esac
done

# Print header
echo -e "${BOLD}${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BOLD}${BLUE}  Documentation Generation${NC}"
echo -e "${BOLD}${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Change to repo root
cd "$REPO_ROOT"

# Step 1: Generate command reference
echo -e "${BOLD}Step 1/3: Generating command reference...${NC}"
python3 scripts/generate-command-reference.py
echo ""

# Step 2: Generate architecture diagrams
echo -e "${BOLD}Step 2/3: Generating architecture diagrams...${NC}"
python3 scripts/generate-architecture-diagrams.py
echo ""

# Step 3: Update mkdocs navigation
echo -e "${BOLD}Step 3/3: Updating mkdocs.yml navigation...${NC}"
python3 scripts/update-mkdocs-nav.py
echo ""

echo -e "${GREEN}✅ Documentation generation complete!${NC}"
echo ""

# Optional: Build with mkdocs
if [ "$BUILD" = true ]; then
    echo -e "${BOLD}Building documentation site with mkdocs...${NC}"

    # Check if mkdocs is installed
    if ! command -v mkdocs &> /dev/null; then
        echo -e "${RED}❌ mkdocs not found${NC}"
        echo -e "${YELLOW}   Install with: pip install mkdocs mkdocs-material${NC}"
        exit 1
    fi

    mkdocs build

    echo ""
    echo -e "${GREEN}✅ Documentation built successfully!${NC}"
    echo -e "${BLUE}   Output: site/${NC}"
    echo ""
fi

# Optional: Deploy to GitHub Pages
if [ "$DEPLOY" = true ]; then
    echo -e "${BOLD}Deploying to GitHub Pages...${NC}"

    # Check if we're in a git repo
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        echo -e "${RED}❌ Not in a git repository${NC}"
        exit 1
    fi

    # Check for uncommitted changes
    if ! git diff-index --quiet HEAD --; then
        echo -e "${YELLOW}⚠️  Uncommitted changes detected${NC}"
        echo -e "${YELLOW}   Commit changes before deploying${NC}"
        exit 1
    fi

    mkdocs gh-deploy --clean

    echo ""
    echo -e "${GREEN}✅ Deployed to GitHub Pages!${NC}"
    echo -e "${BLUE}   URL: https://data-wise.github.io/claude-plugins/${NC}"
    echo ""
fi

# Summary
echo -e "${BOLD}${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BOLD}${BLUE}  Summary${NC}"
echo -e "${BOLD}${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Generated files:"
echo "  ✅ docs/COMMAND-REFERENCE.md"
echo "  ✅ docs/diagrams/ (8 files)"
echo "  ✅ mkdocs.yml (updated navigation)"

if [ "$BUILD" = true ]; then
    echo "  ✅ site/ (built documentation)"
fi

if [ "$DEPLOY" = true ]; then
    echo "  ✅ Deployed to GitHub Pages"
fi

echo ""
echo "Next steps:"

if [ "$BUILD" != true ]; then
    echo "  - Preview locally: mkdocs serve"
    echo "  - Build site: ./scripts/generate-docs.sh --build"
fi

if [ "$DEPLOY" != true ] && [ "$BUILD" = true ]; then
    echo "  - Deploy to GitHub Pages: ./scripts/generate-docs.sh --deploy"
fi

echo "  - View command reference: docs/COMMAND-REFERENCE.md"
echo "  - View diagrams: docs/diagrams/"
echo ""
