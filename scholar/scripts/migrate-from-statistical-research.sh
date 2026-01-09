#!/bin/bash
# Migration wizard: statistical-research → scholar plugin
# Automated migration with backup and rollback capability

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

BACKUP_DIR="$HOME/.claude/backups/statistical-research-$(date +%Y%m%d-%H%M%S)"
SCHOLAR_DIR="$HOME/.claude/plugins/scholar"
STATISTICAL_RESEARCH_DIR="$HOME/.claude/plugins/statistical-research"

echo -e "${BLUE}╔══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  statistical-research → scholar Migration Wizard     ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if statistical-research is installed
if [[ ! -d "$STATISTICAL_RESEARCH_DIR" ]]; then
    echo -e "${YELLOW}statistical-research plugin not found.${NC}"
    echo -e "Nothing to migrate. You can install scholar directly:"
    echo -e "  cd scholar && ./scripts/install.sh"
    exit 0
fi

echo -e "${BLUE}Migration Overview:${NC}"
echo -e "  statistical-research has 14 research commands"
echo -e "  scholar has 21 commands (14 research + 7 teaching)"
echo ""
echo -e "${GREEN}✓ All research commands preserved${NC}"
echo -e "${GREEN}✓ 7 NEW teaching commands added${NC}"
echo -e "${GREEN}✓ Same command names (no relearning)${NC}"
echo -e "${GREEN}✓ Enhanced with teaching workflows${NC}"
echo ""

# Check scholar installation status
if [[ -d "$SCHOLAR_DIR" ]]; then
    echo -e "${YELLOW}⚠ scholar plugin already installed${NC}"
    echo -e "Existing installation will be updated."
    echo ""
fi

# Summary of changes
echo -e "${BLUE}What will change:${NC}"
echo ""
echo -e "${YELLOW}Commands (Identical):${NC}"
echo -e "  /arxiv              →  /arxiv (no change)"
echo -e "  /doi                →  /doi (no change)"
echo -e "  /bib:search         →  /bib:search (no change)"
echo -e "  /bib:add            →  /bib:add (no change)"
echo -e "  /manuscript:*       →  /manuscript:* (no change)"
echo -e "  /simulation:*       →  /simulation:* (no change)"
echo -e "  /scholar:*          →  /scholar:* (no change)"
echo ""
echo -e "${GREEN}NEW Commands (Teaching):${NC}"
echo -e "  /teaching:syllabus    - Generate course syllabi"
echo -e "  /teaching:assignment  - Create homework assignments"
echo -e "  /teaching:rubric      - Generate grading rubrics"
echo -e "  /teaching:slides      - Create lecture slides"
echo -e "  /teaching:quiz        - Generate quiz questions"
echo -e "  /teaching:exam        - Create comprehensive exams"
echo -e "  /teaching:feedback    - Generate student feedback"
echo ""

# Ask for confirmation
echo -e "${YELLOW}Ready to migrate?${NC}"
echo -e "  ${GREEN}[1]${NC} Yes, migrate now (recommended)"
echo -e "  ${GREEN}[2]${NC} No, install scholar alongside statistical-research (keep both)"
echo -e "  ${GREEN}[3]${NC} Cancel"
echo ""
read -p "Choice [1-3]: " CHOICE

case "$CHOICE" in
    1)
        MODE="migrate"
        echo -e "${GREEN}Proceeding with migration...${NC}"
        ;;
    2)
        MODE="install-alongside"
        echo -e "${GREEN}Installing scholar alongside statistical-research...${NC}"
        ;;
    3)
        echo -e "${YELLOW}Migration cancelled.${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac

echo ""

# Create backup
echo -e "${BLUE}Step 1: Creating backup...${NC}"
mkdir -p "$BACKUP_DIR"

if [[ -d "$STATISTICAL_RESEARCH_DIR" ]]; then
    echo -e "  Backing up statistical-research → $BACKUP_DIR/statistical-research"
    cp -r "$STATISTICAL_RESEARCH_DIR" "$BACKUP_DIR/statistical-research"
fi

if [[ -d "$SCHOLAR_DIR" ]]; then
    echo -e "  Backing up scholar → $BACKUP_DIR/scholar"
    cp -r "$SCHOLAR_DIR" "$BACKUP_DIR/scholar"
fi

echo -e "  ${GREEN}✓ Backup created${NC}"
echo ""

# Install scholar
echo -e "${BLUE}Step 2: Installing scholar plugin...${NC}"
SCHOLAR_SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ ! -d "$SCHOLAR_SOURCE" ]]; then
    echo -e "${RED}❌ Error: Scholar source directory not found${NC}"
    echo -e "Expected: $SCHOLAR_SOURCE"
    exit 1
fi

# Install scholar (production mode)
cd "$SCHOLAR_SOURCE"
./scripts/install.sh

echo -e "  ${GREEN}✓ Scholar installed${NC}"
echo ""

# Migrate or preserve statistical-research
if [[ "$MODE" == "migrate" ]]; then
    echo -e "${BLUE}Step 3: Removing statistical-research plugin...${NC}"

    if [[ -d "$STATISTICAL_RESEARCH_DIR" ]] || [[ -L "$STATISTICAL_RESEARCH_DIR" ]]; then
        rm -rf "$STATISTICAL_RESEARCH_DIR"
        echo -e "  ${GREEN}✓ statistical-research removed${NC}"
    fi

    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║           Migration Complete! ✓                       ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}Summary:${NC}"
    echo -e "  ${GREEN}✓${NC} statistical-research backed up to:"
    echo -e "    $BACKUP_DIR/statistical-research"
    echo -e "  ${GREEN}✓${NC} scholar installed with 21 commands"
    echo -e "  ${GREEN}✓${NC} All research commands work identically"
    echo -e "  ${GREEN}✓${NC} 7 new teaching commands available"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo -e "  1. Try: /arxiv \"your query\" (works same as before)"
    echo -e "  2. Try: /teaching:syllabus \"Course Name\" (NEW!)"
    echo -e "  3. See all commands: scholar/README.md"
    echo ""
    echo -e "${YELLOW}Rollback if needed:${NC}"
    echo -e "  ./scholar/scripts/rollback-migration.sh"
    echo -e "  (Restores statistical-research from backup)"
    echo ""

elif [[ "$MODE" == "install-alongside" ]]; then
    echo -e "${BLUE}Step 3: Configuration complete${NC}"
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║         Both Plugins Installed ✓                      ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}You now have:${NC}"
    echo -e "  ${GREEN}✓${NC} statistical-research (14 research commands)"
    echo -e "  ${GREEN}✓${NC} scholar (21 commands: 14 research + 7 teaching)"
    echo ""
    echo -e "${YELLOW}Note:${NC} Commands are identical between plugins."
    echo -e "You can use either plugin for research workflows."
    echo ""
    echo -e "${BLUE}Recommended:${NC}"
    echo -e "  Once comfortable with scholar, remove statistical-research:"
    echo -e "  rm -rf $STATISTICAL_RESEARCH_DIR"
    echo ""
fi

# Verification
echo -e "${BLUE}Verification:${NC}"
if [[ -d "$SCHOLAR_DIR" ]]; then
    COMMAND_COUNT=$(find "$SCHOLAR_DIR/src/plugin-api/commands" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    echo -e "  ${GREEN}✓${NC} Scholar plugin active ($COMMAND_COUNT commands)"
fi

if [[ -d "$STATISTICAL_RESEARCH_DIR" ]]; then
    echo -e "  ${BLUE}ℹ${NC} statistical-research still present"
fi

echo ""
echo -e "${GREEN}Migration wizard complete!${NC}"
echo ""

# Save backup location for rollback
echo "$BACKUP_DIR" > "$HOME/.claude/.last-migration-backup"
