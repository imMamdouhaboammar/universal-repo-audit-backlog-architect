# Evidence Discipline, Safety Boundaries & Redaction Protocols

This reference codifies the non-negotiable safety guardrails and evidence classification rules that govern the repository audit lifecycle.

---

## 1. Strict Mutation Boundary

The core directive of this mission is **AUDIT AND BACKLOG CREATION, NOT IMPLEMENTATION**.

### Strictly Permitted
- Reading any repository file, documentation, configuration, commit history, branch, tag, issue, or PR.
- Executing safe, read-only, non-destructive inspection commands (e.g., `git status`, `git log`, `npm test`, `pytest`, `cargo check`, `tsc --noEmit`, `eslint`).
- Reading issue trackers, project boards, labels, milestones, and release notes.
- Creating real Issues in the repository tracker (when permissions allow) or writing structured issue markdown files.
- Applying labels, milestones, parent-child links, and dependency relationships to newly created issues.

### Strictly Forbidden
- **Modifying any application or test source files.**
- Fixing discovered bugs or applying patches during the audit.
- Upgrading dependencies in `package.json`, `Cargo.toml`, `requirements.txt`, etc.
- Refactoring code or formatting files.
- Running destructive migrations or modifying database state.
- Creating implementation branches or opening pull requests.
- Mutating git history (`git reset --hard`, `git rebase`, `git clean`).
- Touching or discarding an existing dirty working tree.

> [!CAUTION]
> If a test or command fails during discovery, treat it as **evidence of a problem to be recorded in an Issue**. Never modify source code to make verification pass during this mission.

---

## 2. Evidence Classification Hierarchy

Every technical finding must be tagged with its epistemic status:

1. **CONFIRMED**:
   - Backed by direct repository inspection: exact file path, line numbers, compiler error log, test execution trace, or git commit hash.
   - Example: "File `auth/jwt.ts:L42` parses token payload without verifying signature; verified via unit test `tests/jwt_test.ts` which successfully signs with invalid key."
2. **INFERRED**:
   - Strongly suggested by architectural boundaries, missing guards, or known library behaviors, but not directly executed or reproduced in the current session.
   - Example: "Inferred that database connection pool may exhaust under high concurrent load because `db.connect()` lacks a pool ceiling in `config/database.ts`."
3. **PROPOSED**:
   - A prospective design, architectural restructuring, or product enhancement that does not yet exist.
   - Example: "Proposed adding an asynchronous Redis task queue to offload PDF rendering from web worker processes."

Never represent an `INFERRED` hypothesis as a `CONFIRMED` defect.

---

## 3. Secret and Credential Redaction Protocol

When auditing repositories, you may encounter exposed credentials, tokens, or private endpoints.

### Rules of Engagement
1. **Never reproduce secret values in issue bodies**: Replace all tokens, API keys, passwords, and private certificates with generic redaction markers (e.g., `[REDACTED_API_KEY]`, `sk-[REDACTED]`).
2. **Do not publish weaponizable exploit code**: If an injection or auth bypass vulnerability is discovered, describe the vulnerability conceptually at the trust boundary level. Do not publish turnkey attack scripts in public issue trackers.
3. **Private Security Advisories**: If the repository has a `SECURITY.md` or a private security reporting workflow (e.g., GitHub Security Advisories), use it instead of public issues when public disclosure would create immediate risk.

---

## 4. Failure and Stop Conditions

Halt and report an explicit blocker rather than fabricating success when:
- Repository files or git history cannot be read.
- Issue tracker API returns `401 Unauthorized` or `403 Forbidden` (in this case, write complete markdown issue files to `.planning/issues/` or an artifact directory and inform the user).
- Working tree state is fatally corrupted and read-only inspection cannot proceed.
