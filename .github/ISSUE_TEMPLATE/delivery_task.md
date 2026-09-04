---
name: Autonomous Delivery Task
about: Execution-ready delivery task for the Autonomous Issue Delivery Agency
title: "[DELIVERY] Brief descriptive title"
labels: ["agency-ready", "needs-execution"]
assignees: ''
---

### Summary
<!-- Binary statement of the observable outcome to deliver -->

### Classification
- **Type**: Bug Fix | Feature | Security | Technical Debt | Performance | Architecture | DX
- **Priority**: P0 | P1 | P2 | P3
- **Estimated Effort**: XS | S | M | L
- **Risk Level**: LOW | MEDIUM | HIGH | CRITICAL
- **Implementation Readiness**: Ready to implement | Blocked

### Problem Statement
<!-- Concrete evidence, error logs, or missing behavior -->

### Explicit Scope
#### In Scope
- `path/to/target/file`
- Unit and regression tests

#### Out of Scope (Non-Goals)
- Adjacent refactorings or speculative additions

### Invariants
- Zero breaking public API changes
- Credential safety (no secrets exposed)

### Test Strategy
- **RED Test**: Command proving the failure
- **GREEN Verification**: Command confirming resolution

### Acceptance Criteria
- [ ] Observable functional criterion 1
- [ ] Observable functional criterion 2
- [ ] Fresh unit/integration tests pass cleanly
- [ ] Independent code review approved with zero blocking findings
- [ ] Pull request verified merged and default branch healthy
