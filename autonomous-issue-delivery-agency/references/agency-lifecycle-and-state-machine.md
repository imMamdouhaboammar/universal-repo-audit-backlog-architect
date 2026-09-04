# Agency Lifecycle and State Machine

This document defines the formal state transitions, recovery loops, queue recomputation rules, and execution invariants of the **Autonomous Issue Delivery Agency**.

---

## 1. The Canonical State Machine

Every actionable issue processed by the agency follows this state machine:

```text
SELECTED
   ↓
VALIDATED
   ↓
CLAIMED
   ↓
ISOLATED
   ↓
CONTRACTED
   ↓
BASELINE_RED
   ↓
IMPLEMENTED
   ↓
COMMITTED_ATOMIC
   ↓
LOCALLY_VERIFIED
   ↓
INDEPENDENTLY_REVIEWED
   ↓
FINDINGS_REPAIRED
   ↓
RE_VERIFIED
   ↓
PR_OPENED
   ↓
CI_CHECKS_GREEN
   ↓
PR_MERGE_READY
   ↓
MERGED
   ↓
MERGE_VERIFIED
   ↓
POST_MERGE_HEALTH_VERIFIED
   ↓
ISSUE_CLOSED
   ↓
RECEIPT_RECORDED
   ↓
WORKSPACE_CLEANED
   ↓
QUEUE_REFRESHED
```

---

## 2. Dynamic Failure Recovery Transitions

The lifecycle is not strictly linear. When unexpected evidence emerges, the state machine transitions backward to ensure complete correctness:

| Trigger Event | Current State | Recovery State | Required Action |
|---|---|---|---|
| Issue already solved or duplicate | `VALIDATED` | `CLOSED_NO_CODE` | Document evidence, close issue with explanation, refresh queue |
| Issue blocked by another issue | `VALIDATED` | `BLOCKED` | Label issue as blocked, pivot to blocking issue or next independent task |
| Issue too broad for one session | `VALIDATED` | `DECOMPOSED` | Break down into vertical tracer slices, select first actionable child |
| Test failure during implementation | `IMPLEMENTED` | `DIAGNOSE` | Inspect test harness, falsify hypothesis, repair implementation |
| Blocking review finding discovered | `INDEPENDENTLY_REVIEWED` | `FINDINGS_REPAIRED` | Write regression test, apply targeted fix, re-verify |
| Remote CI pipeline failure | `CI_CHECKS_PENDING` | `DIAGNOSE_CI` | Inspect CI logs, reproduce locally, push atomic fix |
| Merge conflict introduced | `PR_MERGE_READY` | `REBASE_VERIFY` | Rebase onto latest base, run fresh local checks, push |
| Post-merge regression on base | `MERGE_VERIFIED` | `INCIDENT_REPAIR` | Immediately revert or repair before touching any other issue |

---

## 3. The Circuit Breaker Protocol

When an implementation or test fails repeatedly:

> [!CAUTION]
> If the same behavior fails after **two consecutive attempts**, the Fable Circuit Breaker is triggered. The agent MUST NOT attempt a speculative third edit.

### Circuit Breaker Procedure:
1. **Freeze Execution**: Stop modifying source files immediately.
2. **Capture Evidence**: Save the failing command output, stack traces, and relevant environment variables.
3. **Reproduce Minimally**: Create an isolated reproduction script or test case that isolates the failure.
4. **Formulate Explicit Hypotheses**: Write down 2–3 falsifiable hypotheses for the root cause (e.g., environment difference, unexpected side effect, API contract drift).
5. **Falsify Hypotheses**: Test each hypothesis systematically with evidence.
6. **Resume Execution**: Only proceed with source mutations once the exact root cause has been proven.

---

## 4. Issue Queue Recomputation Rules

Queue ordering must NEVER be statically determined at session start. The agency must refresh and recompute the actionable queue:

1. **Before Every Iteration**: Inspect live GitHub issues, PRs, and branch states.
2. **After Every Merged PR**: A merge modifies the codebase state, potentially unblocking downstream child issues or invalidating subsequent tasks.
3. **Selection Hierarchy**:
   - `P0 (Critical)`: Active vulnerabilities, production crashes, data loss risks.
   - `P1 (High)`: Core functionality defects, release blockers, major regressions.
   - `Unblockers`: Issues that directly unblock multiple downstream tickets.
   - `P2 (Medium)`: High-value features, validated performance improvements, major DX enhancements.
   - `P3 (Low)`: Non-blocking optimizations, minor documentation updates, technical polish.

---

## 5. Termination & Handoff Conditions

The autonomous loop halts gracefully under explicit conditions:

- **Queue Exhausted**: Zero open, unblocked, actionable issues remain in the backlog.
- **All Remaining Work Blocked**: Open issues exist, but every candidate is blocked by external dependencies.
- **External Authority Boundary**: Action requires human authorization (production deployment, destructive DB operation, secret provisioning).
- **Session Boundary Reached**: Long session requires context handoff. The agency persists the durable ledger and outputs a full session handoff report.
