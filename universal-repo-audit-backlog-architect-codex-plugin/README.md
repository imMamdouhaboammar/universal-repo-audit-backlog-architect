# Deployment & Packaging Guide: ChatGPT and Codex Plugin

This guide explains how to install and run the **Universal Repository Audit & Backlog Architect** plugin across OpenAI Codex, ChatGPT Plus / Team / Enterprise, and Agent Skills environments.

---

## 1. Codex Plugin Installation (Local Host)

Codex discovers plugins from `~/.codex/plugins/` and skills from `~/.codex/skills/`.

### Automatic Local Sync
```bash
# Link or copy to Codex plugins directory
mkdir -p ~/.codex/plugins/universal-repo-audit-backlog-architect
cp -R . ~/.codex/plugins/universal-repo-audit-backlog-architect/

# Link or copy to Codex skills directory
mkdir -p ~/.codex/skills/universal-repo-audit-backlog-architect
cp -R . ~/.codex/skills/universal-repo-audit-backlog-architect/

# Create canonical alias symlink
ln -sfn ~/.codex/skills/universal-repo-audit-backlog-architect ~/.codex/skills/repo-audit-backlog-architect
```

Codex will immediately recognize:
- The plugin via `.codex-plugin/plugin.json` and root `plugin.json`
- The skill via `SKILL.md`

---

## 2. ChatGPT / Custom GPT Deployment

To run in ChatGPT:

1. Open **ChatGPT -> Explore GPTs -> Create a GPT**.
2. Set **Name**: `Universal Repository Audit & Backlog Architect`.
3. Set **Description**: `Deep repository audit, 14-domain gap analysis, and DAG backlog architect. Never modifies code; outputs execution-ready issues.`
4. Paste the prompt from `submission/chatgpt-instructions.md` into the **Instructions** field.
5. In **Conversation Starters**, copy the 4 starter prompts from `submission/chatgpt-instructions.md`.
6. Under **Capabilities**, enable **Code Interpreter** and **Web Search**.
7. Upload `assets/plugin-mark.svg` as the GPT avatar.
8. (Optional) Upload `references/domain-audit-guide.md` and `references/issue-templates.md` to Knowledge files for extra retrieval precision.

---

## 3. OpenAI Platform Directory Submission

If submitting to the OpenAI App / Plugin Directory:
- Manifest: `submission/openai-plugin.json`
- Test cases: `submission/test-cases.json`
- Icon: `assets/plugin-mark.svg`
- Capability type: `skills-only` (no MCP server needed for local repo file analysis)
