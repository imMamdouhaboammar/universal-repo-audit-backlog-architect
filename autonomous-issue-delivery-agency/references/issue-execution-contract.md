# Issue Execution Contract

Before modifying any source code, the agency translates the selected backlog issue into an internal **Issue Execution Contract**. This contract defines the explicit boundaries of the work and prevents scope creep.

---

## 1. Canonical Contract Schema

Every active issue must satisfy this structured contract:

```markdown
# Issue Execution Contract: #<ISSUE_NUMBER> <ISSUE_TITLE>

## 1. Observable Objective
A concise, binary statement of the finished behavior from the perspective of an end-user or system consumer.

## 2. Confirmed Problem Statement
Evidence-backed description of the defect, missing capability, or vulnerability. Must cite exact error traces, logs, or file locations.

## 3. Explicit Scope Boundaries
### In Scope
- Specific file modifications, functions, and interfaces directly required.
- Unit and integration tests verifying the behavior.
- Directly related documentation updates.

### Out of Scope (Non-Goals)
- Adjacent refactoring or cleanups not strictly required by the issue.
- Unrelated dependency upgrades.
- Speculative features or general performance tuning.

## 4. Affected Surfaces & Blast Radius
- List of exact files, directories, and configuration manifests to be mutated.
- Potential breaking changes or downstream consumers affected.

## 5. Architectural & Security Invariants
- Invariants that MUST remain true throughout execution (e.g., zero API breaking changes, backward-compatible database schema, secret redaction).

## 6. Risk Assessment
- **Risk Level**: `LOW` | `MEDIUM` | `HIGH` | `CRITICAL`
- **Mitigation**: Specific pre-deployment safeguards and rollback strategy.

## 7. Test-Driven Verification Strategy
- **RED Reproduction**: Exact test command and assertions that will prove the defect exists before implementation.
- **GREEN Verification**: Exact test command that will confirm the defect is resolved.
- **Regression Suite**: Commands to verify no regressions in adjacent packages.

## 8. Required Repository Gates
- Unit tests pass (`npm test`, `pytest`, `cargo test`, etc.)
- Linter and typechecker pass (`tsc --noEmit`, `flake8`, `eslint`, etc.)
- Build succeeds cleanly (`npm run build`, `cargo check`, etc.)
- Security review completed with zero blocking findings.

## 9. Specialist Plugins Assigned
- Explicit list of specialist plugins invoked for this task.

## 10. Merge Eligibility Checklist
- [ ] RED test failed for expected reason
- [ ] Minimal implementation completed
- [ ] Atomic commits with Conventional Commit messages
- [ ] Pre-PR verification passed freshly
- [ ] Independent code review passed (zero blocking findings)
- [ ] PR created targeting default branch
- [ ] All remote CI checks green
- [ ] Post-merge default branch health verified
- [ ] Delivery receipt comment posted to issue
```

---

## 2. Sizing & Vertical Tracer Slicing

If an issue is too large to complete within a single coding agent session (estimated effort $XL$), it MUST be decomposed before implementation:

### Decomposition Rules:
1. **Vertical Tracer Slicing**: Cut across layers (UI $\rightarrow$ API $\rightarrow$ Database) to deliver a minimal, verifiable end-to-end outcome rather than horizontal architectural layers in isolation.
2. **Expand $\rightarrow$ Migrate $\rightarrow$ Contract Pattern**:
   - *Phase 1 (Expand)*: Add new columns, endpoints, or data structures alongside existing ones.
   - *Phase 2 (Migrate)*: Shift active application traffic to the new interfaces while keeping old ones intact.
   - *Phase 3 (Contract)*: Deprecate and safely remove legacy code, columns, or routes.
3. **Acyclic Dependency Links**: Link child issues using `Blocked by: #X` and `Blocks: #Y`. Process the unblocked foundation issues first.
