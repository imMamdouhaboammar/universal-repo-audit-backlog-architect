#!/usr/bin/env bash
# Universal Autonomous Engineering Suite Installer
# Mamdouh Aboammar <https://github.com/imMamdouhaboammar>
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUITE_NAME="universal-repo-audit-backlog-architect"
MODULE_1="universal-repo-audit-backlog-architect"
MODULE_2="autonomous-issue-delivery-agency"

echo "================================================================================"
echo "📦 Installing Universal Autonomous Engineering Suite across AI Agent Ecosystem"
echo "================================================================================"

# 1. Claude Code (~/.claude/skills)
if [ -d "$HOME/.claude" ] || command -v claude >/dev/null 2>&1; then
  mkdir -p "$HOME/.claude/skills"
  ln -sfn "$SCRIPT_DIR/$MODULE_1" "$HOME/.claude/skills/$MODULE_1"
  ln -sfn "$SCRIPT_DIR/$MODULE_2" "$HOME/.claude/skills/$MODULE_2"
  echo "  ✅ Installed for Claude Code -> $HOME/.claude/skills/{$MODULE_1, $MODULE_2}"
fi

# 2. Antigravity & Gemini CLI (~/.gemini/config/skills)
if [ -d "$HOME/.gemini" ]; then
  mkdir -p "$HOME/.gemini/config/skills"
  ln -sfn "$SCRIPT_DIR/$MODULE_1" "$HOME/.gemini/config/skills/$MODULE_1"
  ln -sfn "$SCRIPT_DIR/$MODULE_2" "$HOME/.gemini/config/skills/$MODULE_2"
  echo "  ✅ Installed for Antigravity / Gemini CLI -> $HOME/.gemini/config/skills/{$MODULE_1, $MODULE_2}"
fi

# 3. OpenAI Codex & OpenCode (~/.codex/skills and ~/.codex/plugins)
if [ -d "$HOME/.codex" ]; then
  mkdir -p "$HOME/.codex/skills" "$HOME/.codex/plugins"
  ln -sfn "$SCRIPT_DIR/$MODULE_1" "$HOME/.codex/skills/$MODULE_1"
  ln -sfn "$SCRIPT_DIR/$MODULE_2" "$HOME/.codex/skills/$MODULE_2"
  ln -sfn "$SCRIPT_DIR/${MODULE_1}-codex-plugin" "$HOME/.codex/plugins/$MODULE_1"
  ln -sfn "$SCRIPT_DIR/${MODULE_2}-codex-plugin" "$HOME/.codex/plugins/$MODULE_2"
  echo "  ✅ Installed for OpenAI Codex -> $HOME/.codex/skills/ & plugins/"
fi

# 4. Universal Agent Kernel (~/.agents/skills)
mkdir -p "$HOME/.agents/skills"
ln -sfn "$SCRIPT_DIR/$MODULE_1" "$HOME/.agents/skills/$MODULE_1"
ln -sfn "$SCRIPT_DIR/$MODULE_2" "$HOME/.agents/skills/$MODULE_2"
echo "  ✅ Installed for Universal Agent Kernel -> $HOME/.agents/skills/{$MODULE_1, $MODULE_2}"

# 5. Cursor AI (~/.cursor/skills)
if [ -d "$HOME/.cursor" ]; then
  mkdir -p "$HOME/.cursor/skills"
  ln -sfn "$SCRIPT_DIR/$MODULE_1" "$HOME/.cursor/skills/$MODULE_1"
  ln -sfn "$SCRIPT_DIR/$MODULE_2" "$HOME/.cursor/skills/$MODULE_2"
  echo "  ✅ Installed for Cursor AI -> $HOME/.cursor/skills/{$MODULE_1, $MODULE_2}"
fi

echo ""
echo "🎉 Autonomous Engineering Suite installation successfully completed!"
echo "   Module 1: /universal-repo-audit-backlog-architect"
echo "   Module 2: /autonomous-issue-delivery-agency"
echo "================================================================================"
