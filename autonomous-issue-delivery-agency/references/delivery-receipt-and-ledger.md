# Delivery Receipt and Durable Agency Ledger

To guarantee accountability, maintain long-session continuity, and survive context resets, the **Autonomous Issue Delivery Agency** enforces durable receipts and ledger recording for every iteration.

---

## 1. Canonical Issue Delivery Receipt

Upon verifying the merged state on the default branch, the agency posts a formal **Delivery Receipt** comment to the closed GitHub issue:

```markdown
## 📦 Delivery Receipt

**Status**: Completed & Verified Merged

### Pull Request & Commits
- **PR**: #<PR_NUMBER> (<PR_URL>)
- **Merged Into**: `<DEFAULT_BRANCH>`
- **Resulting Commit SHA**: `<MERGE_SHA>`
- **Atomic Commits**:
  - `<COMMIT_SHA_1>` feat(<scope>): <message>
  - `<COMMIT_SHA_2>` test(<scope>): <message>

### Objective Verification Evidence
- `<COMMAND_1>` -> `PASS` (Output summary: `<N> tests passed, 0 failures`)
- `<COMMAND_2>` -> `PASS` (Build and bundle verified cleanly)
- `<COMMAND_3>` -> `PASS` (Typecheck and linter clean)
- **CI Pipeline**: All required checks passed on PR head `<HEAD_SHA>`

### Independent Review
- **Reviewer**: `@CodeRabbit` / Independent Review Specialist
- **Findings**: Zero blocking or important findings remaining. All feedback resolved.

### Acceptance Criteria Verification
- [x] <Observable condition 1>
- [x] <Observable condition 2>
- [x] <Automated regression test passes>

### Documentation & Invariants
- **Documentation**: Updated [`README.md`](...) or `N/A`
- **Security / Privacy**: No credentials exposed, least privilege preserved.
- **Data Migrations**: Backward-compatible schema changes applied or `N/A`.

### Post-Merge Repository Health
- Default branch `<DEFAULT_BRANCH>` verified healthy at `<MERGE_SHA>`.
- Zero post-merge regressions detected.
```

---

## 2. Durable Agency Ledger

The agency maintains durable session state to guarantee continuity across restarts and multi-agent handoffs.

### Durable Facts Recorded:
1. **Last Completed Issue**: ID, title, and outcome (`MERGED`, `CLOSED_NO_CODE`, `BLOCKED`).
2. **Resulting SHA**: Canonical commit on the default branch.
3. **Active Issue**: Current in-flight issue and isolated branch (if paused mid-iteration).
4. **Actionable Queue Snapshot**: Prioritized list of next ready candidates.
5. **Disproven Hypotheses**: Architectural constraints or dead ends discovered to prevent re-testing failed approaches.
6. **Blocker Registry**: Unresolved external dependencies with explicit blocking issue IDs.

### Ledger Storage Locations:
- **Primary External Truth**: GitHub Issues and PR comments.
- **Local Continuity State**: Stored in `.planning/agency-ledger.json` or ZzzOps/Fable durable state when available.
- **Session End Report**: Comprehensive markdown delivery summary presented upon queue exhaustion or session pause.
