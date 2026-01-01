#!/bin/bash
# Craft Plugin Installer for Claude Code
# Quick install: curl -fsSL https://raw.githubusercontent.com/Data-Wise/claude-plugins/main/craft/install.sh | bash

set -e

PLUGIN_NAME="craft"
PLUGIN_DIR="${HOME}/.claude/plugins/${PLUGIN_NAME}"
REPO_URL="https://github.com/Data-Wise/claude-plugins.git"
TEMP_DIR=$(mktemp -d)

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║  Craft Plugin Installer for Claude Code                  ║"
echo "╠═══════════════════════════════════════════════════════════╣"
echo "║                                                           ║"
echo "║  📦 Installing: craft v1.16.0                            ║"
echo "║  📍 Location: ~/.claude/plugins/craft                    ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check if Claude Code is installed
if ! command -v claude &> /dev/null; then
    echo "⚠️  Claude Code CLI not found."
    echo ""
    echo "Please install Claude Code first:"
    echo "  https://claude.com/claude-code"
    echo ""
    exit 1
fi

# Create plugins directory if it doesn't exist
mkdir -p "${HOME}/.claude/plugins"

# Check if plugin already installed
if [ -d "${PLUGIN_DIR}" ]; then
    echo "📌 Craft plugin already installed at: ${PLUGIN_DIR}"
    echo ""
    read -p "Do you want to reinstall (update)? (y/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "✅ Keeping existing installation"
        exit 0
    fi
    echo "🔄 Removing existing installation..."
    rm -rf "${PLUGIN_DIR}"
fi

# Clone the repository
echo "📥 Cloning craft plugin..."
git clone --depth 1 --filter=blob:none --sparse "${REPO_URL}" "${TEMP_DIR}" > /dev/null 2>&1
cd "${TEMP_DIR}"
git sparse-checkout set craft > /dev/null 2>&1

# Copy to plugins directory
echo "📦 Installing to ~/.claude/plugins/craft..."
cp -r "${TEMP_DIR}/craft" "${PLUGIN_DIR}"

# Cleanup
rm -rf "${TEMP_DIR}"

# Verify installation
if [ -f "${PLUGIN_DIR}/.claude-plugin/plugin.json" ]; then
    VERSION=$(grep '"version"' "${PLUGIN_DIR}/.claude-plugin/plugin.json" | sed 's/.*"\([0-9.]*\)".*/\1/')

    echo ""
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║  ✅ INSTALLATION COMPLETE                                 ║"
    echo "╠═══════════════════════════════════════════════════════════╣"
    echo "║                                                           ║"
    echo "║  Plugin: craft v${VERSION}                                    ║"
    echo "║  Location: ~/.claude/plugins/craft                        ║"
    echo "║                                                           ║"
    echo "║  📚 Documentation:                                        ║"
    echo "║  https://data-wise.github.io/claude-plugins/craft/       ║"
    echo "║                                                           ║"
    echo "║  🚀 Quick Start:                                          ║"
    echo "║  • Restart Claude Code to load the plugin                ║"
    echo "║  • Try: /craft:do <task>                                 ║"
    echo "║  • Help: /craft:help                                     ║"
    echo "║  • Hub: /craft:hub                                       ║"
    echo "║                                                           ║"
    echo "║  74 commands | 8 agents | 21 skills                      ║"
    echo "║                                                           ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo ""
else
    echo "❌ Installation verification failed"
    exit 1
fi
