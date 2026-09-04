# Canonical Repository Issue Templates

Every created Issue must follow one of the canonical formats below. These templates ensure that any competent engineer or autonomous coding agent can pick up the ticket in a clean session and execute it without rediscovering the repository.

---

## 1. Standard Issue Template

Use for engineering quality, architecture, technical debt, DX, CI/CD, observability, and general improvements.

```markdown
## Summary
A concise explanation of the work and intended outcome.

## Classification
- **Type**: `type:technical-debt` | `type:reliability` | `type:testing` | `type:documentation` | `type:dx` | `type:ci-cd` | `type:observability` | `type:refactor`
- **Priority**: `P0` | `P1` | `P2` | `P3`
- **Severity**: `Critical` | `Major` | `Minor` | `Low`
- **Confidence**: `High` | `Medium` | `Low`
- **Estimated Effort**: `XS` | `S` | `M` | `L`
- **Implementation Readiness**: `READY FOR AGENT` | `BLOCKED` | `NEEDS RESEARCH` | `NEEDS PRODUCT DECISION`

## Problem
Describe the actual problem, defect, risk, or friction. Be concrete and specific.

## Evidence
Repository evidence supporting this Issue:
- Files / Paths: `path/to/file.ts:L45-L60`
- Symbols: `FunctionOrClassName`
- Commands / Results: `npm test` output or compiler diagnostic
- Nature of evidence: **CONFIRMED** (verified in repo) | **INFERRED** (deduced from code structure) | **PROPOSED** (suggested improvement)

## Why This Matters
Explain the operational, maintenance, developer experience, or user impact if left unaddressed.

## Desired Outcome
Describe the observable state that must exist once this Issue is completed.

## Scope
- [ ] Explicit in-scope item 1
- [ ] Explicit in-scope item 2

## Non-Goals
- Explicitly excluded item or follow-up work
- Unrelated refactoring

## Proposed Direction
Guidance on a technically credible approach. Preserve existing architectural invariants.

## Affected Areas
- Packages / Modules:
- Configuration / Environment:
- Automated Tests:

## Dependencies
- **Blocked by**: None identified | #...
- **Blocks**: None identified | #...
- **Related**: None identified | #...

## Risks and Edge Cases
List potential pitfalls, concurrency concerns, backward-compatibility issues, or failure modes.

## Security / Privacy Considerations
State specific security/privacy impacts or explicitly confirm: `No specific security or privacy impact identified during discovery.`

## Data / Migration Considerations
State schema or data migration impacts, or explicitly confirm: `No data migration required.`

## Testing and Verification Strategy
Concrete commands and test types required to verify correctness:
- Unit tests:
- Integration tests:
- Build / Typecheck:

## Acceptance Criteria
- [ ] Observable binary criterion 1
- [ ] Observable binary criterion 2
- [ ] Existing relevant test suites remain green
- [ ] Required documentation updated where applicable

## Definition of Done
- All acceptance criteria satisfied.
- Automated verification passes cleanly (`npm test`, `npm run lint`, etc.).
- No undocumented public interface breaks.
- Working tree clean and ready for review.

## Rollout / Recovery
Rollout strategy, feature flag usage, or rollback procedure.

## References
- Repository files:
- External documentation:

## Notes for Implementation Agent
Critical context, repository traps, gotchas, or environment quirks to prevent wasted discovery time.
```

---

## 2. Bug Issue Template

Use for confirmed defects, broken behavior, and regression failures.

```markdown
## Summary
Concise explanation of the bug and the expected fix.

## Classification
- **Type**: `type:bug`
- **Priority**: `P0` | `P1` | `P2` | `P3`
- **Severity**: `Critical` | `Major` | `Minor` | `Low`
- **Confidence**: `High` | `Medium`
- **Estimated Effort**: `XS` | `S` | `M` | `L`
- **Implementation Readiness**: `READY FOR AGENT` | `BLOCKED`

## Problem
Describe what fails, under what conditions, and who is impacted.

## Evidence
- Code location: `path/to/buggy_code.py:L112`
- Error logs or stack trace:
- Status: **CONFIRMED**

## Reproduction
1. Execute command: `...`
2. Provide input: `...`
3. Observe failure: `...`

## Expected Behavior
What should occur under normal, correct operation.

## Actual Behavior
What actually occurs (e.g., uncaught exception, corrupted state, silent failure).

## Suspected Root Cause
Detailed technical suspicion based on code analysis.

## Regression Test Requirement
A regression test demonstrating the failure MUST be added and fail before the fix, and pass after the fix.

## Scope
- [ ] Fix root cause in `path/to/buggy_code.py`
- [ ] Add automated regression test suite

## Non-Goals
- Broad architectural rewrites of surrounding modules.

## Dependencies
- **Blocked by**: None identified | #...
- **Blocks**: None identified | #...

## Acceptance Criteria
- [ ] Regression test reproducing the bug is committed and passing
- [ ] Core bug is resolved without introducing regressions
- [ ] All existing test suites pass

## Definition of Done
- Fix merged with passing regression coverage.
```

---

## 3. Security Issue Template

Use for vulnerabilities, authorization bypasses, injection risks, and sensitive data exposure.

> [!IMPORTANT]
> Never commit live credentials, API keys, or weaponizable exploit payloads into public trackers. Follow repository `SECURITY.md` if private disclosure is required.

```markdown
## Summary
Concise statement of the security or privacy weakness and required remediation.

## Classification
- **Type**: `type:security`
- **Priority**: `P0` (if actively exploitable) | `P1` | `P2`
- **Severity**: `Critical` | `High` | `Medium` | `Low`
- **Confidence**: `High` | `Medium`
- **Estimated Effort**: `XS` | `S` | `M`
- **Implementation Readiness**: `READY FOR AGENT` | `NEEDS RESEARCH`

## Vulnerability Description
Abstract description of the security defect without weaponizable exploit code.

## Trust Boundaries and Affected Roles
- Trust Boundary: e.g., Public Internet -> Authenticated API Gateway -> Database
- Attacker Profile: e.g., Unauthenticated remote user, authenticated tenant user
- Expected Authorization: e.g., Fail-closed, strict role enforcement

## Evidence
- Vulnerable component: `path/to/auth_middleware.ts:L34`
- Observation: Missing permission check before executing mutation.

## Impact
Potential consequences (e.g., unauthorized data modification, cross-tenant leak).

## Proposed Remediation
Hardening instructions enforcing fail-closed posture and principle of least privilege.

## Acceptance Criteria
- [ ] Authorization / validation check enforced at the trust boundary
- [ ] Automated security regression test verifies rejected unauthorized requests
- [ ] Security logging records unauthorized attempts without leaking sensitive data
```

---

## 4. Performance Issue Template

Use for bottlenecks supported by profiling, query analysis, or concrete algorithmic evidence.

```markdown
## Summary
Concise statement of the bottleneck and the performance target.

## Classification
- **Type**: `type:performance`
- **Priority**: `P1` | `P2` | `P3`
- **Severity**: `Major` | `Minor`
- **Confidence**: `High` | `Medium`
- **Estimated Effort**: `S` | `M` | `L`
- **Implementation Readiness**: `READY FOR AGENT` | `NEEDS RESEARCH`

## Problem & Baseline
- Baseline Metric: e.g., `540ms` p95 response time or $O(N^2)$ algorithm over $N=50,000$ items.
- Measured with: profiling tool, benchmark script, or query log.

## Evidence
- Location: `path/to/heavy_loop.go:L89`
- Observed behavior: Unindexed database query executed inside loop (N+1 query).

## Target Outcome
- Target Metric: e.g., reduce query count from $N+1$ to 1 batch query; latency under `50ms`.

## Proposed Optimization
Batching, indexing, caching, or algorithmic complexity reduction.

## Acceptance Criteria
- [ ] Target metric achieved and verified via automated benchmark
- [ ] No regression in business logic correctness
```

---

## 5. Feature / Product Issue Template

Use for product enhancements and new capabilities directly justified by repository evidence.

```markdown
## Summary
Concise description of the feature and the user value it unlocks.

## Classification
- **Type**: `type:feature` | `type:enhancement`
- **Priority**: `P1` | `P2` | `P3`
- **Estimated Effort**: `S` | `M` | `L`
- **Implementation Readiness**: `READY FOR AGENT` | `NEEDS PRODUCT DECISION`

## Target User and User Problem
- Target user:
- Problem solved:
- Current limitation in repo:

## Why This Belongs in This Repository
Explicit justification of why this repository's architecture and product mission call for this capability.

## User Workflow
1. User initiates: `...`
2. System processes: `...`
3. User receives: `...`

## Proposed Vertical Slice
Include all layers required for an end-to-end verifiable outcome (e.g., schema, domain logic, API, UI).

## Acceptance Criteria
- [ ] Complete end-to-end workflow functions as specified
- [ ] Automated integration/e2e tests cover happy path and edge cases
- [ ] User-facing documentation updated
```

---

## 6. RFC / Spike / Research Template

Use for high-uncertainty ideas, technical evaluations, and architectural proposals.

```markdown
## Summary
Formulation of the hypothesis or investigation question to resolve.

## Classification
- **Type**: `type:research` | `type:spike` | `type:rfc`
- **Priority**: `P2` | `P3`
- **Estimated Effort**: `S` | `M`
- **Implementation Readiness**: `RFC / EXPERIMENT`

## Hypothesis / Research Question
What specific technical or product uncertainty needs resolution?

## Evaluation Plan
1. Baseline measurement or prototype experiment.
2. Comparative analysis against alternatives.
3. Risk and migration assessment.

## Deliverable
A documented decision record (ADR / RFC) recommending Go or No-Go with evidence.

## Acceptance Criteria
- [ ] Current baseline / status quo documented
- [ ] Candidate approaches evaluated against performance, complexity, and maintenance criteria
- [ ] Recommendation documented in an ADR or RFC summary
- [ ] Definitive Go / No-Go decision enabled for leadership
```
