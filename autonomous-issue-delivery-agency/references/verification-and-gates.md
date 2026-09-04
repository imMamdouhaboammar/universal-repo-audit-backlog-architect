# Verification, Gates, and Quality Protocols

The **Autonomous Issue Delivery Agency** adheres to a strict evidence-first culture. No claim of progress, readiness, or completion is valid without fresh, reproducible verification evidence.

---

## 1. Test-Driven Development (TDD) Protocol

For any behavior modification, defect fix, API update, or logic enhancement:

```text
BEHAVIOR CONTRACT
   ↓
TEST HARNESS SETUP
   ↓
RED (Falsifiable Failure)
   ↓
MINIMAL GREEN IMPLEMENTATION
   ↓
FOCUSED REFACTOR
   ↓
VERIFIED GREEN
```

### Critical Rules for RED:
- The test must fail specifically due to the missing implementation or defect.
- A failure due to syntax errors, import errors, broken fixtures, or bad mock wiring is NOT a valid RED state.
- A test that passes before implementation proves nothing and must be rejected.
- Regression tests must be permanently checked into the repository test suite alongside the fix.

---

## 2. Pre-PR Verification Matrix

Before opening a Pull Request, the agency must execute a full falsification pass based on the risk profile of the changes:

| Verification Gate | Command Example | Pass Criteria |
|---|---|---|
| **Focused Unit Tests** | `bun test auth.test.ts`, `pytest -k auth` | 100% passing tests for modified components |
| **Regression Suite** | `bun test`, `pytest`, `cargo test` | Zero regressions across adjacent packages |
| **Typecheck** | `bun x tsc --noEmit`, `mypy src/` | Zero type errors |
| **Linter** | `bun x eslint .`, `flake8` | Zero lint errors or style violations |
| **Build & Bundle** | `bun run build`, `cargo build` | Clean compilation with zero warnings/errors |
| **Security Audit** | SAST scan / Dependency vulnerability check | Zero high/critical vulnerabilities |
| **Runtime Smoke Test** | CLI invocation / test server boot | Process boots cleanly and exits with code 0 |

---

## 3. The Verification Freshness Law

> [!IMPORTANT]
> **Any code mutation immediately invalidates all prior verification evidence.**
>
> If a developer or agent edits a single line of code after running tests, those tests are **stale**. The agent must re-run all relevant verification commands and capture fresh output before asserting readiness.

---

## 4. Independent Code & Security Review

Self-review by the implementer is necessary but insufficient. The agency requires an independent review step before PR submission:

### Review Finding Triage:
- **`BLOCKING`**: Correctness bugs, logic flaws, memory leaks, unhandled exceptions, security vulnerabilities. *Must be resolved before PR creation or merge.*
- **`IMPORTANT`**: Performance bottlenecks, maintainability issues, missing docstrings on public APIs, test coverage gaps. *Should normally be resolved before merge.*
- **`MINOR`**: Non-blocking stylistic suggestions or cosmetic refactorings. *May be deferred.*
- **`INVALID`**: Reviewer suggestions that contradict repository architecture or verified facts. *Must be explicitly refuted with technical evidence.*

### Review Repair Loop:
1. Identify valid findings.
2. Formulate minimal code adjustments.
3. Run targeted regression tests.
4. Stage and commit atomically.
5. Re-run complete verification suite.

---

## 5. Post-Merge Base Health Gate

Merging a PR is NOT the final step of an iteration. After the remote PR status reaches `MERGED`:

1. **Fetch Default Branch**: Pull the updated base branch (`git fetch origin main`).
2. **Verify Merge SHA**: Confirm the remote HEAD matches the expected merge commit.
3. **Execute Post-Merge Smoke Check**: Run the repository's primary test suite against the merged default branch.
4. **Immediate Incident Protocol**:
   - If the merged change causes a regression on the default branch, the agency MUST NOT proceed to the next issue.
   - The default branch is in an incident state. The agency must immediately isolate the regression, revert or hotfix the change, and return the default branch to a green state before continuing.
