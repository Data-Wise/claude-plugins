#!/bin/bash
# Test script for rforge-orchestrator plugin structure

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🧪 Testing rforge-orchestrator plugin structure..."

# Test 1: Check required files exist
echo "✓ Test 1: Required files..."
test -f "$PLUGIN_DIR/.claude-plugin/plugin.json" || { echo "❌ Missing plugin.json"; exit 1; }
test -f "$PLUGIN_DIR/package.json" || { echo "❌ Missing package.json"; exit 1; }
test -f "$PLUGIN_DIR/README.md" || { echo "❌ Missing README.md"; exit 1; }
test -f "$PLUGIN_DIR/LICENSE" || { echo "❌ Missing LICENSE"; exit 1; }
test -x "$PLUGIN_DIR/scripts/install.sh" || { echo "❌ Missing or non-executable install.sh"; exit 1; }
test -x "$PLUGIN_DIR/scripts/uninstall.sh" || { echo "❌ Missing or non-executable uninstall.sh"; exit 1; }
echo "  ✅ All required files present"

# Test 2: Check plugin.json is valid JSON
echo "✓ Test 2: plugin.json validity..."
if command -v jq >/dev/null 2>&1; then
    jq empty "$PLUGIN_DIR/.claude-plugin/plugin.json" || { echo "❌ Invalid JSON in plugin.json"; exit 1; }
    echo "  ✅ plugin.json is valid JSON"
else
    echo "  ⚠️  jq not installed, skipping JSON validation"
fi

# Test 3: Check package.json is valid JSON
echo "✓ Test 3: package.json validity..."
if command -v jq >/dev/null 2>&1; then
    jq empty "$PLUGIN_DIR/package.json" || { echo "❌ Invalid JSON in package.json"; exit 1; }
    echo "  ✅ package.json is valid JSON"
fi

# Test 4: Check commands directory structure
echo "✓ Test 4: Commands structure..."
test -d "$PLUGIN_DIR/commands" || { echo "❌ Missing commands/ directory"; exit 1; }
COMMAND_COUNT=$(find "$PLUGIN_DIR/commands" -name "*.md" -type f | wc -l | tr -d ' ')
if [ "$COMMAND_COUNT" -lt 3 ]; then
    echo "❌ Expected at least 3 commands, found $COMMAND_COUNT"
    exit 1
fi
echo "  ✅ Found $COMMAND_COUNT command files"

# Test 5: Check agents directory structure
echo "✓ Test 5: Agents structure..."
test -d "$PLUGIN_DIR/agents" || { echo "❌ Missing agents/ directory"; exit 1; }
AGENT_COUNT=$(find "$PLUGIN_DIR/agents" -name "*.md" -type f | wc -l | tr -d ' ')
if [ "$AGENT_COUNT" -lt 1 ]; then
    echo "❌ Expected at least 1 agent, found $AGENT_COUNT"
    exit 1
fi
echo "  ✅ Found $AGENT_COUNT agent files"

# Test 6: Check no hardcoded paths
echo "✓ Test 6: No hardcoded paths..."
if grep -r "/Users/" "$PLUGIN_DIR/commands" "$PLUGIN_DIR/agents" 2>/dev/null; then
    echo "❌ Found hardcoded /Users/ paths"
    exit 1
fi
if grep -r "/home/" "$PLUGIN_DIR/commands" "$PLUGIN_DIR/agents" 2>/dev/null; then
    echo "❌ Found hardcoded /home/ paths"
    exit 1
fi
echo "  ✅ No hardcoded paths found"

# Test 7: Check package.json has correct repository
echo "✓ Test 7: Package.json repository..."
if command -v jq >/dev/null 2>&1; then
    REPO_URL=$(jq -r '.repository.url' "$PLUGIN_DIR/package.json")
    if [[ "$REPO_URL" != *"claude-plugins"* ]]; then
        echo "❌ Repository URL should point to claude-plugins monorepo, got: $REPO_URL"
        exit 1
    fi
    echo "  ✅ Repository URL correct"
fi

# Test 8: Check package.json has peerDependencies
echo "✓ Test 8: RForge MCP peer dependency..."
if command -v jq >/dev/null 2>&1; then
    PEER_DEPS=$(jq -r '.peerDependencies | keys[]' "$PLUGIN_DIR/package.json" 2>/dev/null || echo "")
    if [[ "$PEER_DEPS" != *"rforge-mcp"* ]]; then
        echo "❌ Missing rforge-mcp peer dependency"
        exit 1
    fi
    echo "  ✅ RForge MCP peer dependency present"
fi

echo ""
echo "✅ All tests passed!"
echo "📊 Summary:"
echo "  - Commands: $COMMAND_COUNT"
echo "  - Agents: $AGENT_COUNT"
echo "  - Peer dependencies: rforge-mcp"
