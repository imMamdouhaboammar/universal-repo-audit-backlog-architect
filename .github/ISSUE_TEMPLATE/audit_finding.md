---
name: Audit Finding / Backlog Item
about: Propose a new backlog item identified during a repository audit
title: "[DOMAIN] Brief descriptive title"
labels: ["audit-finding", "triage-needed"]
assignees: ''
---

### Summary
<!-- 1-3 sentences stating what needs to be done and why -->

### Classification
- **Type**: Bug Fix | Feature | Technical Debt | Performance | Security | Testing | Documentation | Architecture | CI/CD | DX | Observability | Accessibility | Spike/RFC
- **Priority**: P0 | P1 | P2 | P3
- **Severity**: Critical | High | Medium | Low
- **Confidence**: High | Medium | Low
- **Estimated Effort**: XS | S | M | L
- **Implementation Readiness**: Ready to implement | Blocked | Needs refinement

### Problem Statement & Business/Technical Impact
<!-- Describe what is currently wrong, sub-optimal, or missing -->

### Evidence & Reproduction
- **Status**: CONFIRMED | INFERRED | PROPOSED
- **Findings / Error Output / Traces**:
```text
<!-- Paste logs, test failure output, or file inspection traces -->
```

### Affected Components & Scope
- `path/to/affected/file`

### Non-Goals / Explicit Out-of-Scope
- <!-- What will NOT be done in this issue -->

### Dependencies & Sequencing
- **Blocked by**: None
- **Blocks**: None

### Testing Strategy & Verification Plan
- Unit tests to add/modify:
- Integration / E2E verification:
- Manual or automated command:

### Acceptance Criteria
- [ ] Condition 1
- [ ] Condition 2
- [ ] Automated tests pass
