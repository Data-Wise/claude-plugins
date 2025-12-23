#!/bin/bash
# Install statistical-research plugin to Claude Code
# Supports development mode (symlink) and production mode (copy)

set -euo pipefail

PLUGIN_NAME="statistical-research"
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="$HOME/.claude/plugins/$PLUGIN_NAME"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parse arguments
DEV_MODE=false
if [[ "${1:-}" == "--dev" ]]; then
    DEV_MODE=true
fi

echo -e "${BLUE}=== Statistical Research Plugin Installer ===${NC}"
echo -e "${BLUE}Plugin: ${YELLOW}$PLUGIN_NAME${NC}"
echo -e "${BLUE}Source: ${YELLOW}$SOURCE_DIR${NC}"
echo -e "${BLUE}Target: ${YELLOW}$TARGET_DIR${NC}"
echo ""

# Create plugins directory if needed
if [[ ! -d "$HOME/.claude/plugins" ]]; then
    echo -e "${YELLOW}Creating plugins directory...${NC}"
    mkdir -p "$HOME/.claude/plugins"
fi

# Remove existing installation
if [[ -e "$TARGET_DIR" ]]; then
    echo -e "${YELLOW}Removing existing installation...${NC}"

    if [[ -L "$TARGET_DIR" ]]; then
        echo -e "  Removing symlink: $TARGET_DIR"
        rm "$TARGET_DIR"
    elif [[ -d "$TARGET_DIR" ]]; then
        echo -e "  Removing directory: $TARGET_DIR"
        rm -rf "$TARGET_DIR"
    else
        echo -e "  Removing file: $TARGET_DIR"
        rm "$TARGET_DIR"
    fi
fi

# Install plugin
if [[ "$DEV_MODE" == true ]]; then
    echo -e "${GREEN}Installing in DEVELOPMENT mode (symlink)...${NC}"
    ln -s "$SOURCE_DIR" "$TARGET_DIR"

    echo -e "${GREEN}✓ Symlinked: $TARGET_DIR → $SOURCE_DIR${NC}"
    echo ""
    echo -e "${BLUE}Changes to source files will be immediately reflected.${NC}"
else
    echo -e "${GREEN}Installing in PRODUCTION mode (copy)...${NC}"
    cp -r "$SOURCE_DIR" "$TARGET_DIR"

    echo -e "${GREEN}✓ Installed to: $TARGET_DIR${NC}"
fi

echo ""
echo -e "${GREEN}✓ $PLUGIN_NAME plugin installed successfully!${NC}"
echo ""

# Verify installation
if [[ -d "$TARGET_DIR" ]] || [[ -L "$TARGET_DIR" ]]; then
    echo -e "${BLUE}=== Plugin Components ===${NC}"

    # Count components
    COMMANDS_COUNT=$(find "$TARGET_DIR/commands" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    SKILLS_COUNT=$(find "$TARGET_DIR/skills" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    LIB_COUNT=$(find "$TARGET_DIR/lib" -name "*.sh" -type f 2>/dev/null | wc -l | tr -d ' ')

    echo -e "  ${GREEN}✓${NC} Commands: $COMMANDS_COUNT slash commands"
    echo -e "  ${GREEN}✓${NC} Skills: $SKILLS_COUNT A-grade skills"
    echo -e "  ${GREEN}✓${NC} Libraries: $LIB_COUNT shell API wrappers"
    echo ""
fi

# Show available commands
echo -e "${BLUE}=== Available Commands ===${NC}"
echo ""
echo -e "${YELLOW}Literature Management:${NC}"
echo -e "  /research:arxiv <query>          - Search arXiv for papers"
echo -e "  /research:doi <doi>              - Look up paper by DOI"
echo -e "  /research:bib:search <query>     - Search BibTeX files"
echo -e "  /research:bib:add <file>         - Add BibTeX entry"
echo ""
echo -e "${YELLOW}Manuscript Writing:${NC}"
echo -e "  /research:manuscript:methods     - Write methods section"
echo -e "  /research:manuscript:results     - Write results section"
echo -e "  /research:manuscript:reviewer    - Respond to reviewers"
echo -e "  /research:manuscript:proof       - Review mathematical proofs"
echo ""
echo -e "${YELLOW}Simulation Studies:${NC}"
echo -e "  /research:simulation:design      - Design Monte Carlo study"
echo -e "  /research:simulation:analysis    - Analyze simulation results"
echo ""
echo -e "${YELLOW}Research Planning:${NC}"
echo -e "  /research:lit-gap <topic>        - Identify literature gaps"
echo -e "  /research:hypothesis <topic>     - Generate hypotheses"
echo -e "  /research:analysis-plan          - Create analysis plan"
echo ""
echo -e "${BLUE}=== 17 A-Grade Skills ===${NC}"
echo -e "Skills automatically activate when relevant:"
echo -e "  ${GREEN}✓${NC} Mathematical: proof-architect, mathematical-foundations, identification-theory, asymptotic-theory"
echo -e "  ${GREEN}✓${NC} Implementation: simulation-architect, algorithm-designer, numerical-methods, computational-inference, statistical-software-qa"
echo -e "  ${GREEN}✓${NC} Writing: methods-paper-writer, publication-strategist, methods-communicator"
echo -e "  ${GREEN}✓${NC} Research: literature-gap-finder, cross-disciplinary-ideation, method-transfer-engine, mediation-meta-analyst, sensitivity-analyst"
echo ""

# Installation mode indicator
if [[ "$DEV_MODE" == true ]]; then
    echo -e "${YELLOW}Development Mode:${NC} Source changes will be immediately available"
    echo -e "To reinstall: $SOURCE_DIR/scripts/install.sh --dev"
else
    echo -e "${YELLOW}Production Mode:${NC} Reinstall to get source updates"
    echo -e "To update: $SOURCE_DIR/scripts/install.sh"
fi

echo ""
echo -e "${GREEN}Ready to use! Try: /research:arxiv \"your query\"${NC}"
