# Contributing to Universal Repository Audit & Backlog Architect

Thank you for your interest in contributing!

## Code of Conduct

Please maintain a collaborative, respectful, and evidence-grounded environment.

## Design Philosophy

This repository adheres to the **Omni-Skill** standard:
- Skills must be 100% portable across Agent Skills (Gemini CLI / Antigravity), Claude Code, ChatGPT, and OpenAI Codex.
- Zero host-specific hardcoded paths in instructions.
- Strict read-only boundary during repository auditing.
- Falsifiable, binary acceptance criteria for all generated issues.

## Local Development & Validation

Before submitting a Pull Request, verify that all portability gates and validators pass:

```bash
# --- Zero-Install CLI & Manifests ---
# 0. Run Bun distribution test suite
bun test
bun ./bin/cli.js info

# --- Module 1: Backlog Architect ---
# 1. Run backlog validator against test fixture
python3 universal-repo-audit-backlog-architect/scripts/validate_backlog.py universal-repo-audit-backlog-architect/tests/fixtures/sample_issue.md

# 2. Run repository snapshot extractor sanity check
python3 universal-repo-audit-backlog-architect/scripts/extract_repo_snapshot.py .

# 3. Verify cross-platform portability
python3 ~/.gemini/config/skills/omni-skill/scripts/validate_portability.py universal-repo-audit-backlog-architect --targets agent-skills,claude-code,chatgpt,codex

# --- Module 2: Autonomous Delivery Agency ---
# 4. Run delivery contract and receipt validators
python3 autonomous-issue-delivery-agency/scripts/validate_delivery_contract.py --contract autonomous-issue-delivery-agency/tests/fixtures/sample_contract.md
python3 autonomous-issue-delivery-agency/scripts/validate_delivery_contract.py --receipt autonomous-issue-delivery-agency/tests/fixtures/sample_receipt.md

# 5. Run agency snapshot extractor sanity check
python3 autonomous-issue-delivery-agency/scripts/run_agency_snapshot.py .

# 6. Run unit tests
python3 -m unittest discover -s autonomous-issue-delivery-agency/tests -p "test_*.py"

# 7. Verify cross-platform portability
python3 ~/.gemini/config/skills/omni-skill/scripts/validate_portability.py autonomous-issue-delivery-agency --targets agent-skills,claude-code,chatgpt,codex
```

## Commit Conventions

We follow Conventional Commits:
- `feat(...)`: New capability or domain audit addition
- `fix(...)`: Bug fix in scripts or templates
- `docs(...)`: Documentation improvements
- `refactor(...)`: Code cleanup without behavior modification
