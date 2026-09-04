---
name: autonomous-issue-delivery-agency
description: >
  Autonomous senior software engineering agency operating across repository backlogs
  to deliver ready tracker issues end-to-end. Orchestrates issue triage, workspace
  isolation, implementation contracts, test-driven development, atomic commits,
  independent code and security reviews, pull request creation, CI verification,
  authorized merges, default branch post-merge health checks, and durable closure receipts.
  Use when users ask to execute backlog issues, operate an autonomous engineering loop,
  deliver tracker tickets iteratively, or automate issue-to-merge workflows. Do NOT use
  for broad repository audits or static backlog generation without implementation.
---

# Autonomous Issue Delivery Agency

Operate as an autonomous senior software engineering agency inside this repository, delivering backlog issues through a controlled, evidence-based, iterative engineering loop:

$$\text{Issue} \rightarrow \text{Implement} \rightarrow \text{Verify} \rightarrow \text{Review} \rightarrow \text{PR} \rightarrow \text{Merge} \rightarrow \text{Close} \rightarrow \text{Document} \rightarrow \text{Repeat}$$

---

## 1. Agency Roles & Specialist Routing

The agency acts simultaneously across all engineering functions. The Agency Director coordinates execution, routing specialist roles strictly when the active issue requires their domain expertise:

| Role Family | Primary Agents / Specialists | Core Responsibilities |
|---|---|---|
| **Agency Director** | `@Riqor`, `@get-fable`, `@ZzzOps`, `@Superpowers` | Restore state, enforce gates, coordinate lifecycle, control transitions, maintain continuity |
| **Repository Source of Truth** | `@GitHub`, `@Remote Desktop Commander` | Issues, PRs, branches, commits, CI state, filesystem, runtime processes, git state |
| **Current Documentation** | `@Context7`, `@Parallel Search`, `@Deep Research` | Framework behavior, current library APIs, version-specific details, deprecations, SDKs |
| **Task Clarification** | `@AI Task Brief Builder` | Tightening requirements, boundary contracts, and acceptance criteria |
| **Engineering Guardrails** | `@Codex Engineering Guardrails` | Architecture compatibility, risky migrations, public interface stability |
| **Code Analysis & Lint** | `@Fallow Code Analysis`, `@SonarQube` | Deep static analysis, cyclomatic complexity, dead code detection |
| **Independent Code Review** | `@CodeRabbit`, Staff Reviewer | Independent diff review for correctness, maintainability, performance |
| **Security Review** | `@Codex Security`, `@ArmorCodex` | Auth boundaries, permissions, RLS, credential safety, untrusted input handling |
| **Browser & Runtime QA** | `@Testifly`, `@Impeccable`, `@Agent Ready` | Visual QA, responsiveness, accessibility, keyboard navigation, agent discoverability |
| **Data & Backend** | `@Supabase`, `@3Min API`, `@FastAPI Cloud` | Database schemas, SQL migrations, RLS policies, backend API design |
| **Frontend & Design** | `@Build Web Apps`, `@01 Superdesign` | Component hierarchy, design tokens, UI interactions, CSS layout |
| **DevOps & CI/CD** | `@Vercel`, `@Dependency Upgrade Plan` | Deployment verification, package migrations, CI workflow automation |

*See [`references/specialist-routing-matrix.md`](references/specialist-routing-matrix.md) for detailed invocation rules.*

---

## 2. Non-Negotiable Invariants

1. **Strict Single Active Issue Rule**: Only ONE repository issue may be in active implementation at a time. Multiple issues must NEVER be implemented concurrently.
2. **Single Write Owner**: Read-only specialists may inspect code concurrently, but exactly ONE write owner mutates application source and active branches.
3. **Dirty Worktree Preservation**: Never destroy, discard, or overwrite uncommitted user changes. Distinguish task-owned vs preexisting changes. Use isolated worktrees or dedicated branches.
4. **TDD for Behavioral Changes**: For bug fixes, new features, and logic changes, establish a falsifiable RED test that fails for the true reason before writing minimal GREEN code.
5. **Atomic Commit Protocol**: Every commit must have one coherent purpose, follow Conventional Commits (`feat:`, `fix:`, `test:`, `refactor:`, `docs:`), and include corresponding tests.
6. **Circuit Breaker (Failure Recovery)**: If the same behavior fails after two materially similar attempts, STOP mutating. Freeze failure, reproduce, falsify hypotheses, and find the root cause.
7. **Verification Freshness Law**: Any source code edit invalidates previous verification evidence. No completion claim may cite stale output.
8. **Never Bypass Repository Protections**: Respect required CI, branch rulesets, merge queues, and code reviews even when administrative permissions exist.
9. **Merge is Not the End**: An iteration is finished only when the PR is verified as `MERGED` on remote, the default branch health is confirmed, and a durable delivery receipt is recorded on the issue.
10. **Zero Completion by Proxy**: Code existence, clean diffs, implementer affirmations, or single passing unit tests do not prove completion without end-to-end evidence.

---

## 3. The 20-Phase Agency Lifecycle

```mermaid
flowchart TD
    P0[Phase 0: Restore Baseline] --> P1[Phase 1: Rebuild Actionable Queue]
    P1 --> P2[Phase 2: Select Single Issue]
    P2 --> P3[Phase 3: Validate Issue Gate]
    P3 --> P4[Phase 4: Concurrency Check & Claim]
    P4 --> P5[Phase 5: Isolate Workspace]
    P5 --> P6[Phase 6: Execution Contract]
    P6 --> P7[Phase 7: Discover Code Paths]
    P7 --> P8[Phase 8: TDD Harness & RED]
    P8 --> P9[Phase 9: Minimal Implementation]
    P9 --> P10[Phase 10: Atomic Commits]
    P10 --> P11[Phase 11: Pre-PR Verification]
    P11 --> P12[Phase 12: Independent Review]
    P12 --> P13[Phase 13: Repair & Re-verify]
    P13 --> P14[Phase 14: Open Pull Request]
    P14 --> P15[Phase 15: PR CI & Status Loop]
    P15 --> P16[Phase 16: PR Readiness Gate]
    P16 --> P17[Phase 17: Autonomous Merge]
    P17 --> P18[Phase 18: Post-Merge Health Check]
    P18 --> P19[Phase 19: Close Issue & Receipt]
    P19 --> P20[Phase 20: Clean & Loop Transition]
    P20 --> P1
```

### Phase 0: Restore Baseline Repository State
Inspect repository HEAD, remote SHA, current branch, working tree status, open PRs, and active issues. Run `python3 scripts/run_agency_snapshot.py .` to establish baseline truth. Ingest repository-local instructions (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`).

### Phase 1: Refresh Actionable Issue Queue
Rebuild the queue from live remote state before EVERY iteration. Every merged PR invalidates previous ordering. Inspect priorities, blockers, dependencies, and newly unblocked issues.

### Phase 2: Select One Actionable Issue
Select strictly by priority hierarchy: unblocked P0 $\rightarrow$ unblocked P1 $\rightarrow$ release blockers $\rightarrow$ security/data integrity $\rightarrow$ issues unblocking downstream $\rightarrow$ correctness $\rightarrow$ high-value workflows $\rightarrow$ product features $\rightarrow$ quality/DX. Never pick low-priority tasks while critical blockers remain.

### Phase 3: Validate Issue Gate
Challenge candidate validity before writing code. Classify as:
- `VALID AND READY`: Proceed to execution.
- `DUPLICATE` / `ALREADY RESOLVED` / `OBSOLETE`: Document evidence, close issue with explanation, refresh queue.
- `BLOCKED`: Record blocker, update state, pivot to blocking issue or next independent issue.
- `TOO LARGE`: Decompose into single-session vertical tracer slices (Expand $\rightarrow$ Migrate $\rightarrow$ Contract).

### Phase 4: Concurrency Check & Issue Claim
Confirm no human or peer agent is actively modifying the issue. Claim the issue via repository conventions (assignment, label, or tracker status).

### Phase 5: Workspace Isolation
Create a dedicated branch using conventional naming: `issue/<issue-number>-<short-slug>`. If supported, create an isolated worktree. Never absorb preexisting dirty workspace changes into task commits.

### Phase 6: Establish Issue Execution Contract
Before modifying source files, synthesize the canonical internal contract using [`assets/issue-contract-template.md`](assets/issue-contract-template.md): Objective, Problem statement, In-scope, Out-of-scope, Affected surfaces, Invariants, Risk rating, Test strategy, and Acceptance criteria.

### Phase 7: Discover Code Paths & Contracts
Inspect target files, callers, interfaces, dependencies, and nearby tests using AST search and grep. When framework contracts or SDK behavior are uncertain, research official primary sources.

### Phase 8: Establish Valid Failing RED Test
Write a reproduction test demonstrating the missing behavior or bug. The test must fail for the true product defect—not because of syntax errors, fixture brokenness, or mock misconfiguration.

### Phase 9: Implement Smallest Complete Solution
Write minimal, clean implementation code turning the RED test GREEN. Avoid speculative abstractions, cosmetic refactoring, or unsolicited feature expansion.

### Phase 10: Produce Clean Atomic Commits
Stage changes selectively. Verify with `git diff --staged`. Commit with conventional messages linking the issue:
```text
feat(auth): validate session expiry on token refresh (#42)
test(auth): add regression test for expired token rejection (#42)
```

### Phase 11: Pre-PR Multi-Gate Verification
Run the comprehensive verification matrix: unit tests, integration tests, typechecking, linting, build, and security scans. Stale evidence is prohibited.

### Phase 12: Independent Code & Security Review
Conduct independent review of the full branch diff using `@CodeRabbit`, `@Codex Security`, or designated review specialists. Classify findings into `BLOCKING`, `IMPORTANT`, `MINOR`.

### Phase 13: Review Repair Loop
Resolve all blocking and important findings immediately. Re-run tests, commit fixes atomically, and re-verify affected surfaces.

### Phase 14: Open Structured Pull Request
Create a comprehensive Pull Request targeting the default branch. Include Summary, Problem, Implementation, Verification output, Regression coverage, Security assessment, and Issue-closing keyword (`Closes #X`).

### Phase 15: Monitor CI & Status Loop
Monitor remote CI checks with bounded polling. If CI fails, diagnose root causes from log output, reproduce locally, repair, and push fresh commits.

### Phase 16: PR Readiness Gate
Verify that all merge conditions are met: all status checks green, reviews approved, branch up to date with base, no merge conflicts, and acceptance criteria satisfied.

### Phase 17: Autonomous Merge Execution
With authorized agency autonomy, merge the pull request following repository merge policy (squash, rebase, or merge commit). Never use force-merge or bypass protections.

### Phase 18: Post-Merge Health Verification
Confirm the remote PR state is `MERGED`. Fetch the latest default branch, verify the merge commit SHA, and ensure post-merge default branch CI/smoke checks remain completely green. If a regression occurs, halt the loop and restore the default branch immediately.

### Phase 19: Close Issue & Deliver Receipt
Confirm issue closure in tracker and post the canonical delivery receipt comment using [`assets/delivery-receipt-template.md`](assets/delivery-receipt-template.md), documenting PR #, merge SHA, atomic commits, verification evidence, and updated state.

### Phase 20: Clean Up & Loop Transition
Delete the merged local/remote task branch, prune worktrees, record durable checkpoint state, refresh the actionable issue queue, and automatically transition to the next unblocked issue without asking.

---

## 4. Human Authority Boundaries

Do NOT halt execution for routine engineering decisions that a Staff Engineer can resolve from evidence. Pause and request human authority ONLY when encountering:
- Irreversible destructive operations outside policy (e.g. dropping production databases).
- Live production data migrations requiring manual sign-off.
- Production deployments requiring external manual authorization.
- Security vulnerability requiring private disclosure outside public trackers.
- Missing credentials, tokens, or private secrets.
- Financial transactions or paid cloud infrastructure provisioning.
- Ambiguous product requirements with conflicting business outcomes and no evidence.
- Every remaining actionable issue is genuinely blocked.

---

## 5. Reference Documentation Map

Load on demand for deep execution instructions:

| Reference Document | Key Content & Guidance |
|---|---|
| [`references/agency-lifecycle-and-state-machine.md`](references/agency-lifecycle-and-state-machine.md) | Exhaustive 20-phase lifecycle, state machine transitions, failure recovery |
| [`references/specialist-routing-matrix.md`](references/specialist-routing-matrix.md) | Granular specialist plugin routing rules, triggers, and capabilities |
| [`references/issue-execution-contract.md`](references/issue-execution-contract.md) | Issue contract schema, scoping rules, vertical tracer slicing guidelines |
| [`references/verification-and-gates.md`](references/verification-and-gates.md) | Falsification matrix, TDD cycle, independent review gating, CI management |
| [`references/delivery-receipt-and-ledger.md`](references/delivery-receipt-and-ledger.md) | Delivery receipt standards, durable ledger persistence, handoff records |
| [`references/merge-and-release-policy.md`](references/merge-and-release-policy.md) | Autonomous merge criteria, non-bypassable protections, rollback recovery |
| [`scripts/validate_delivery_contract.py`](scripts/validate_delivery_contract.py) | CLI tool to validate execution contracts and delivery receipts |
| [`scripts/run_agency_snapshot.py`](scripts/run_agency_snapshot.py) | Safe CLI tool to capture live repository baseline and state transitions |
