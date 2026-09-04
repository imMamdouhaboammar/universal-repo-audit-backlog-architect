# Issue Execution Contract: #{{ISSUE_NUMBER}} {{ISSUE_TITLE}}

## 1. Observable Objective
{{OBSERVABLE_OBJECTIVE}}

## 2. Confirmed Problem Statement
{{PROBLEM_STATEMENT}}

## 3. Explicit Scope Boundaries
### In Scope
- {{IN_SCOPE_ITEM_1}}
- {{IN_SCOPE_ITEM_2}}

### Out of Scope (Non-Goals)
- {{NON_GOAL_1}}
- {{NON_GOAL_2}}

## 4. Affected Surfaces & Blast Radius
- {{AFFECTED_FILE_1}}
- {{AFFECTED_FILE_2}}

## 5. Architectural & Security Invariants
- {{INVARIANT_1}}
- {{INVARIANT_2}}

## 6. Risk Assessment
- **Risk Level**: `{{RISK_LEVEL}}` (LOW | MEDIUM | HIGH | CRITICAL)
- **Mitigation Strategy**: {{MITIGATION_STRATEGY}}

## 7. Test-Driven Verification Strategy
- **RED Reproduction Test**: `{{RED_COMMAND}}`
- **GREEN Verification Test**: `{{GREEN_COMMAND}}`
- **Regression Suite**: `{{REGRESSION_COMMAND}}`

## 8. Required Repository Gates
- Unit Tests: `PASS`
- Typecheck & Lint: `PASS`
- Build & Compilation: `PASS`
- Independent Review: `APPROVED`

## 9. Specialist Plugins Assigned
- {{SPECIALIST_1}}
- {{SPECIALIST_2}}

## 10. Merge Eligibility Checklist
- [ ] RED test verified failing for true defect
- [ ] Minimal implementation completed
- [ ] Atomic commits with Conventional Commit messages
- [ ] Pre-PR verification executed freshly
- [ ] Independent code review passed with zero blocking findings
- [ ] Pull Request opened targeting default branch
- [ ] All remote CI checks green
- [ ] Post-merge default branch health verified
- [ ] Delivery receipt posted to closed issue
