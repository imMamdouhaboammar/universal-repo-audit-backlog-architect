# Deployment & Packaging Guide: ChatGPT and Codex Plugin

This guide explains how to install and run the **Autonomous Issue Delivery Agency** plugin across OpenAI Codex, ChatGPT Plus / Team / Enterprise, and Agent Skills environments.

---

## 1. Codex Plugin Installation (Local Host)

Codex discovers plugins from `~/.codex/plugins/` and skills from `~/.codex/skills/`.

### Automatic Local Sync
```bash
# Link or copy to Codex plugins directory
mkdir -p ~/.codex/plugins/autonomous-issue-delivery-agency
cp -R . ~/.codex/plugins/autonomous-issue-delivery-agency/

# Link or copy to Codex skills directory
mkdir -p ~/.codex/skills/autonomous-issue-delivery-agency
cp -R . ~/.codex/skills/autonomous-issue-delivery-agency/

# Create canonical alias symlink
ln -sfn ~/.codex/skills/autonomous-issue-delivery-agency ~/.codex/skills/issue-delivery-agency
```

Codex will immediately recognize:
- The plugin via `.codex-plugin/plugin.json` and root `plugin.json`
- The skill via `SKILL.md`

---

## 2. ChatGPT / Custom GPT Deployment

To run in ChatGPT:

1. Open **ChatGPT -> Explore GPTs -> Create a GPT**.
2. Set **Name**: `Autonomous Issue Delivery Agency`.
3. Set **Description**: `Autonomous senior software engineering agency delivering repository issues end-to-end: Issue -> Implement -> Verify -> Review -> PR -> Merge -> Close -> Document -> Repeat.`
4. Paste the prompt from `submission/chatgpt-instructions.md` into the **Instructions** field.
5. In **Conversation Starters**, copy the starter prompts from `submission/chatgpt-instructions.md`.
6. Under **Capabilities**, enable **Code Interpreter** and **Web Search**.
7. Upload `assets/plugin-mark.svg` as the GPT avatar.
8. (Optional) Upload `references/agency-lifecycle-and-state-machine.md` and `references/verification-and-gates.md` to Knowledge files for extra retrieval precision.

---

## 3. OpenAI Platform Directory Submission

If submitting to the OpenAI App / Plugin Directory:
- Manifest: `submission/openai-plugin.json`
- Test cases: `submission/test-cases.json`
- Icon: `assets/plugin-mark.svg`
- Capability type: `skills-only`
