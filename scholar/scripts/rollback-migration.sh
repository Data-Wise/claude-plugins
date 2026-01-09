#!/bin/bash
# Rollback script: Restore statistical-research from backup
# Safely undoes migration from statistical-research → scholar

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

BACKUP_MARKER="$HOME/.claude/.last-migration-backup"
SCHOLAR_DIR="$HOME/.claude/plugins/scholar"
STATISTICAL_RESEARCH_DIR="$HOME/.claude/plugins/statistical-research"

echo -e "${BLUE}╔══════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         Migration Rollback Tool                       ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if backup marker exists
if [[ ! -f "$BACKUP_MARKER" ]]; then
    echo -e "${RED}❌ No recent migration backup found.${NC}"
    echo -e "Cannot automatically rollback."
    echo ""
    echo -e "${YELLOW}Manual rollback:${NC}"
    echo -e "  1. Check ~/.claude/backups/ for statistical-research backup"
    echo -e "  2. Copy backup to $STATISTICAL_RESEARCH_DIR"
    echo -e "  3. Optionally remove $SCHOLAR_DIR"
    exit 1
fi

BACKUP_DIR=$(cat "$BACKUP_MARKER")

# Verify backup exists
if [[ ! -d "$BACKUP_DIR/statistical-research" ]]; then
    echo -e "${RED}❌ Backup directory not found:${NC}"
    echo -e "  $BACKUP_DIR/statistical-research"
    echo -e ""
    echo -e "Cannot restore automatically."
    exit 1
fi

echo -e "${BLUE}Backup found:${NC}"
echo -e "  $BACKUP_DIR/statistical-research"
echo ""

# Show what will happen
echo -e "${YELLOW}Rollback will:${NC}"
echo -e "  1. Restore statistical-research plugin from backup"
echo -e "  2. Remove scholar plugin"
echo -e "  3. Return to pre-migration state"
echo ""

# Confirmation
echo -e "${RED}Are you sure you want to rollback?${NC}"
echo -e "  ${GREEN}[1]${NC} Yes, restore statistical-research and remove scholar"
echo -e "  ${GREEN}[2]${NC} Keep both plugins (don't remove scholar)"
echo -e "  ${GREEN}[3]${NC} Cancel"
echo ""
read -p "Choice [1-3]: " CHOICE

case "$CHOICE" in
    1)
        REMOVE_SCHOLAR=true
        echo -e "${YELLOW}Rolling back migration...${NC}"
        ;;
    2)
        REMOVE_SCHOLAR=false
        echo -e "${GREEN}Restoring statistical-research, keeping scholar...${NC}"
        ;;
    3)
        echo -e "${YELLOW}Rollback cancelled.${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac

echo ""

# Step 1: Restore statistical-research
echo -e "${BLUE}Step 1: Restoring statistical-research...${NC}"

if [[ -d "$STATISTICAL_RESEARCH_DIR" ]]; then
    echo -e "  ${YELLOW}⚠${NC} Existing statistical-research found, removing first..."
    rm -rf "$STATISTICAL_RESEARCH_DIR"
fi

echo -e "  Copying from backup..."
cp -r "$BACKUP_DIR/statistical-research" "$STATISTICAL_RESEARCH_DIR"

echo -e "  ${GREEN}✓ statistical-research restored${NC}"
echo ""

# Step 2: Remove scholar (if requested)
if [[ "$REMOVE_SCHOLAR" == true ]]; then
    echo -e "${BLUE}Step 2: Removing scholar plugin...${NC}"

    if [[ -d "$SCHOLAR_DIR" ]] || [[ -L "$SCHOLAR_DIR" ]]; then
        rm -rf "$SCHOLAR_DIR"
        echo -e "  ${GREEN}✓ scholar removed${NC}"
    else
        echo -e "  ${BLUE}ℹ${NC} scholar not installed"
    fi
    echo ""
else
    echo -e "${BLUE}Step 2: Keeping scholar plugin${NC}"
    echo -e "  ${BLUE}ℹ${NC} Both plugins will be available"
    echo ""
fi

# Success
echo -e "${GREEN}╔══════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║           Rollback Complete! ✓                        ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${BLUE}Status:${NC}"
if [[ -d "$STATISTICAL_RESEARCH_DIR" ]]; then
    COMMAND_COUNT=$(find "$STATISTICAL_RESEARCH_DIR/commands" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    echo -e "  ${GREEN}✓${NC} statistical-research restored ($COMMAND_COUNT commands)"
fi

if [[ -d "$SCHOLAR_DIR" ]]; then
    COMMAND_COUNT=$(find "$SCHOLAR_DIR/src/plugin-api/commands" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    echo -e "  ${GREEN}✓${NC} scholar present ($COMMAND_COUNT commands)"
elif [[ "$REMOVE_SCHOLAR" == true ]]; then
    echo -e "  ${GREEN}✓${NC} scholar removed"
fi

echo ""
echo -e "${BLUE}Next steps:${NC}"
echo -e "  Try: /arxiv \"your query\""
echo -e "  Try: /doi \"10.xxxx/xxxxx\""
echo ""

# Clean up marker
rm -f "$BACKUP_MARKER"

echo -e "${GREEN}Rollback complete!${NC}"
