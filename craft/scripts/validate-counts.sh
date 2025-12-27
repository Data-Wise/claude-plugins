#!/bin/bash
# validate-counts.sh - Validate command/skill/agent counts match documentation
# Usage: ./scripts/validate-counts.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$(dirname "$SCRIPT_DIR")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}Craft Plugin Count Validation${NC}"
echo "=============================="
echo ""

# Count actual files
cd "$PLUGIN_DIR"

# Commands: count all .md files in commands/ (excluding index files)
CMD_COUNT=$(find commands -name "*.md" ! -name "index.md" ! -name "README.md" 2>/dev/null | wc -l | tr -d ' ')

# Skills: count all .md and SKILL.md files in skills/
SKILL_COUNT=$(find skills -name "*.md" -o -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')

# Agents: count all .md files in agents/ (including subdirs)
AGENT_COUNT=$(find agents -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

echo -e "${CYAN}Actual Counts (from files):${NC}"
echo "  Commands: $CMD_COUNT"
echo "  Skills:   $SKILL_COUNT"
echo "  Agents:   $AGENT_COUNT"
echo ""

# Extract documented counts from plugin.json
PLUGIN_JSON=".claude-plugin/plugin.json"
if [ -f "$PLUGIN_JSON" ]; then
    DESC=$(python3 -c "import json; print(json.load(open('$PLUGIN_JSON'))['description'])")

    # Extract numbers from description like "53 commands, 7 agents, 13 skills"
    DOC_CMDS=$(echo "$DESC" | grep -o '[0-9]* commands' | grep -o '[0-9]*' || echo "?")
    DOC_AGENTS=$(echo "$DESC" | grep -o '[0-9]* agents' | grep -o '[0-9]*' || echo "?")
    DOC_SKILLS=$(echo "$DESC" | grep -o '[0-9]* skills' | grep -o '[0-9]*' || echo "?")

    echo -e "${CYAN}Documented Counts (from plugin.json):${NC}"
    echo "  Commands: $DOC_CMDS"
    echo "  Skills:   $DOC_SKILLS"
    echo "  Agents:   $DOC_AGENTS"
    echo ""

    # Compare
    ERRORS=0

    if [ "$CMD_COUNT" != "$DOC_CMDS" ]; then
        echo -e "${RED}✗ Commands mismatch: $CMD_COUNT files vs $DOC_CMDS documented${NC}"
        ERRORS=$((ERRORS + 1))
    else
        echo -e "${GREEN}✓ Commands match: $CMD_COUNT${NC}"
    fi

    if [ "$SKILL_COUNT" != "$DOC_SKILLS" ]; then
        echo -e "${RED}✗ Skills mismatch: $SKILL_COUNT files vs $DOC_SKILLS documented${NC}"
        ERRORS=$((ERRORS + 1))
    else
        echo -e "${GREEN}✓ Skills match: $SKILL_COUNT${NC}"
    fi

    if [ "$AGENT_COUNT" != "$DOC_AGENTS" ]; then
        echo -e "${RED}✗ Agents mismatch: $AGENT_COUNT files vs $DOC_AGENTS documented${NC}"
        ERRORS=$((ERRORS + 1))
    else
        echo -e "${GREEN}✓ Agents match: $AGENT_COUNT${NC}"
    fi

    echo ""

    if [ $ERRORS -gt 0 ]; then
        echo -e "${YELLOW}Found $ERRORS discrepancies. Update plugin.json description:${NC}"
        echo ""
        echo "  \"description\": \"Full-stack developer toolkit - $CMD_COUNT commands, $AGENT_COUNT agents, $SKILL_COUNT skills...\""
        echo ""
        exit 1
    else
        echo -e "${GREEN}All counts validated!${NC}"
    fi
else
    echo -e "${RED}Error: plugin.json not found${NC}"
    exit 1
fi

# Bonus: Show breakdown by category
echo ""
echo -e "${CYAN}Command Breakdown:${NC}"
for dir in commands/*/; do
    if [ -d "$dir" ]; then
        name=$(basename "$dir")
        count=$(find "$dir" -name "*.md" ! -name "index.md" 2>/dev/null | wc -l | tr -d ' ')
        printf "  %-12s %s\n" "$name:" "$count"
    fi
done
# Count root-level commands
ROOT_CMDS=$(find commands -maxdepth 1 -name "*.md" ! -name "index.md" 2>/dev/null | wc -l | tr -d ' ')
printf "  %-12s %s\n" "(root):" "$ROOT_CMDS"

echo ""
echo -e "${CYAN}Skill Breakdown:${NC}"
for dir in skills/*/; do
    if [ -d "$dir" ]; then
        name=$(basename "$dir")
        count=$(find "$dir" -name "*.md" -o -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
        printf "  %-15s %s\n" "$name:" "$count"
    fi
done

echo ""
echo -e "${CYAN}Agent Breakdown:${NC}"
for dir in agents/*/; do
    if [ -d "$dir" ]; then
        name=$(basename "$dir")
        count=$(find "$dir" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
        printf "  %-12s %s\n" "$name:" "$count"
    fi
done
# Count root-level agents
ROOT_AGENTS=$(find agents -maxdepth 1 -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
printf "  %-12s %s\n" "(root):" "$ROOT_AGENTS"
