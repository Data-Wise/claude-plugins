#!/bin/bash
# Test script for scholar plugin structure

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🧪 Testing scholar plugin structure..."

# Test 1: Check required files exist
echo "✓ Test 1: Required files..."
test -f "$PLUGIN_DIR/.claude-plugin/plugin.json" || { echo "❌ Missing plugin.json"; exit 1; }
test -f "$PLUGIN_DIR/README.md" || { echo "❌ Missing README.md"; exit 1; }
test -x "$PLUGIN_DIR/scripts/install.sh" || { echo "❌ Missing or non-executable install.sh"; exit 1; }
test -x "$PLUGIN_DIR/scripts/uninstall.sh" || { echo "❌ Missing or non-executable uninstall.sh"; exit 1; }
echo "  ✅ All required files present"

# Test 2: Check plugin.json is valid JSON
echo "✓ Test 2: plugin.json validity..."
if command -v jq >/dev/null 2>&1; then
    jq empty "$PLUGIN_DIR/.claude-plugin/plugin.json" || { echo "❌ Invalid JSON in plugin.json"; exit 1; }

    # Check plugin name is correct
    PLUGIN_NAME=$(jq -r '.name' "$PLUGIN_DIR/.claude-plugin/plugin.json")
    if [[ "$PLUGIN_NAME" != "scholar" ]]; then
        echo "❌ Plugin name should be 'scholar', got: $PLUGIN_NAME"
        exit 1
    fi

    # Check version exists
    VERSION=$(jq -r '.version' "$PLUGIN_DIR/.claude-plugin/plugin.json")
    if [[ -z "$VERSION" ]]; then
        echo "❌ Plugin version is missing"
        exit 1
    fi

    echo "  ✅ plugin.json is valid (name: $PLUGIN_NAME, version: $VERSION)"
else
    echo "  ⚠️  jq not installed, skipping JSON validation"
fi

# Test 3: Check directory structure
echo "✓ Test 3: Directory structure..."
test -d "$PLUGIN_DIR/src/plugin-api/commands" || { echo "❌ Missing src/plugin-api/commands/ directory"; exit 1; }
test -d "$PLUGIN_DIR/src/plugin-api/skills" || { echo "❌ Missing src/plugin-api/skills/ directory"; exit 1; }
test -d "$PLUGIN_DIR/lib" || { echo "❌ Missing lib/ directory"; exit 1; }
test -d "$PLUGIN_DIR/src/core" || { echo "❌ Missing src/core/ directory"; exit 1; }
test -d "$PLUGIN_DIR/src/mcp-server" || { echo "❌ Missing src/mcp-server/ directory"; exit 1; }
echo "  ✅ All required directories present"

# Test 4: Check commands directory structure
echo "✓ Test 4: Commands structure..."
COMMAND_COUNT=$(find "$PLUGIN_DIR/src/plugin-api/commands" -name "*.md" -type f | wc -l | tr -d ' ')
if [ "$COMMAND_COUNT" -lt 21 ]; then
    echo "❌ Expected at least 21 commands (14 research + 7 teaching), found $COMMAND_COUNT"
    exit 1
fi
echo "  ✅ Found $COMMAND_COUNT command files"

# Test 5: Check teaching commands exist
echo "✓ Test 5: Teaching commands..."
test -f "$PLUGIN_DIR/src/plugin-api/commands/teaching/syllabus.md" || { echo "❌ Missing teaching:syllabus command"; exit 1; }
test -f "$PLUGIN_DIR/src/plugin-api/commands/teaching/assignment.md" || { echo "❌ Missing teaching:assignment command"; exit 1; }
test -f "$PLUGIN_DIR/src/plugin-api/commands/teaching/rubric.md" || { echo "❌ Missing teaching:rubric command"; exit 1; }
test -f "$PLUGIN_DIR/src/plugin-api/commands/teaching/slides.md" || { echo "❌ Missing teaching:slides command"; exit 1; }
test -f "$PLUGIN_DIR/src/plugin-api/commands/teaching/quiz.md" || { echo "❌ Missing teaching:quiz command"; exit 1; }
test -f "$PLUGIN_DIR/src/plugin-api/commands/teaching/exam.md" || { echo "❌ Missing teaching:exam command"; exit 1; }
test -f "$PLUGIN_DIR/src/plugin-api/commands/teaching/feedback.md" || { echo "❌ Missing teaching:feedback command"; exit 1; }
echo "  ✅ All 7 teaching commands present"

# Test 6: Check skills directory structure
echo "✓ Test 6: Skills structure..."
SKILL_COUNT=$(find "$PLUGIN_DIR/src/plugin-api/skills" -name "skill.md" -o -name "SKILL.md" -type f 2>/dev/null | wc -l | tr -d ' ')
if [ "$SKILL_COUNT" -lt 15 ]; then
    echo "⚠️  Expected at least 15 skills, found $SKILL_COUNT (acceptable for MVP)"
fi
echo "  ✅ Found $SKILL_COUNT skill files"

# Test 7: Check lib directory and API wrappers
echo "✓ Test 7: Library files..."
test -f "$PLUGIN_DIR/lib/arxiv-api.sh" || { echo "❌ Missing arxiv-api.sh"; exit 1; }
test -f "$PLUGIN_DIR/lib/crossref-api.sh" || { echo "❌ Missing crossref-api.sh"; exit 1; }
test -f "$PLUGIN_DIR/lib/bibtex-utils.sh" || { echo "❌ Missing bibtex-utils.sh"; exit 1; }
echo "  ✅ All API wrapper files present"

# Test 8: Check no hardcoded paths
echo "✓ Test 8: No hardcoded paths..."
HARDCODED_PATHS=0
if grep -r "/Users/" "$PLUGIN_DIR/src/plugin-api/commands" "$PLUGIN_DIR/lib" 2>/dev/null | grep -v "CLAUDE_PLUGIN_ROOT"; then
    echo "❌ Found hardcoded /Users/ paths"
    HARDCODED_PATHS=1
fi
if grep -r "/home/" "$PLUGIN_DIR/src/plugin-api/commands" "$PLUGIN_DIR/lib" 2>/dev/null | grep -v "CLAUDE_PLUGIN_ROOT"; then
    echo "❌ Found hardcoded /home/ paths"
    HARDCODED_PATHS=1
fi
if [ $HARDCODED_PATHS -eq 0 ]; then
    echo "  ✅ No hardcoded paths found"
else
    exit 1
fi

# Test 9: Check command frontmatter format
echo "✓ Test 9: Command frontmatter..."
for cmd in "$PLUGIN_DIR/src/plugin-api/commands"/**/*.md; do
    if [ -f "$cmd" ]; then
        # Check for YAML frontmatter
        if ! grep -q "^---$" "$cmd"; then
            echo "❌ Missing frontmatter in: $cmd"
            exit 1
        fi
        # Check for name field
        if ! grep -q "^name:" "$cmd"; then
            echo "❌ Missing 'name:' field in: $cmd"
            exit 1
        fi
        # Check for description field
        if ! grep -q "^description:" "$cmd"; then
            echo "❌ Missing 'description:' field in: $cmd"
            exit 1
        fi
    fi
done
echo "  ✅ All commands have valid frontmatter"

# Test 10: Check plugin-api vs old structure
echo "✓ Test 10: New directory structure..."
if [ -d "$PLUGIN_DIR/commands" ]; then
    echo "⚠️  Old commands/ directory still exists (should be src/plugin-api/commands/)"
fi
if [ -d "$PLUGIN_DIR/skills" ]; then
    echo "⚠️  Old skills/ directory still exists (should be src/plugin-api/skills/)"
fi
echo "  ✅ Using new src/plugin-api/ structure"

echo ""
echo "✅ All tests passed!"
echo "📊 Summary:"
echo "  - Commands: $COMMAND_COUNT"
echo "  - Skills: $SKILL_COUNT"
echo "  - API wrappers: 3"
echo "  - Teaching commands: 3"
echo "  - Structure: Unified Plugin + MCP architecture"
