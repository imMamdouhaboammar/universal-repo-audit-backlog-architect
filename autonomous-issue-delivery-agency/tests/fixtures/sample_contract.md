# Issue Execution Contract: #42 Fix Session Invalidation Race Condition

## 1. Observable Objective
When a user signs out from one tab, all concurrent sessions and in-flight API requests on other tabs must be invalidated within 500ms without throwing unhandled exceptions.

## 2. Confirmed Problem Statement
Currently, `AuthService.revokeToken()` updates local storage on the active tab but fails to broadcast session invalidation over `BroadcastChannel`. In-flight network requests on background tabs continue with stale tokens resulting in 401 unhandled rejections as seen in `src/auth/session.ts:89`.

## 3. Explicit Scope Boundaries
### In Scope
- Add `BroadcastChannel('auth-sync')` listener to `SessionManager`.
- Terminate in-flight requests on receipt of `LOGOUT` broadcast.
- Add regression test in `test/auth-sync.test.ts`.

### Out of Scope (Non-Goals)
- Migrating authentication providers.
- Changing token storage medium from LocalStorage to IndexedDB.
- Modifying UI sign-in form elements.

## 4. Affected Surfaces & Blast Radius
- `src/auth/session.ts`
- `src/auth/types.ts`
- `test/auth-sync.test.ts`

## 5. Architectural & Security Invariants
- No credentials or raw refresh tokens must ever be sent over `BroadcastChannel`.
- Backward compatibility: Fallback gracefully to `StorageEvent` if `BroadcastChannel` is unsupported.

## 6. Risk Assessment
- **Risk Level**: `MEDIUM`
- **Mitigation Strategy**: Implement feature flag `AUTH_BROADCAST_SYNC` with instant killswitch.

## 7. Test-Driven Verification Strategy
- **RED Reproduction Test**: `bun test test/auth-sync.test.ts` fails before changes with `Expected session invalidation within 500ms, got stale session`.
- **GREEN Verification Test**: `bun test test/auth-sync.test.ts` passes with code 0.
- **Regression Suite**: `bun test` passes across all auth test suites.

## 8. Required Repository Gates
- Unit Tests: `PASS`
- Typecheck & Lint: `PASS`
- Build & Compilation: `PASS`
- Independent Review: `APPROVED`

## 9. Specialist Plugins Assigned
- `@Riqor` (Lead)
- `@get-fable` (Lifecycle Engine)
- `@Codex Security` (Auth Boundary Review)
- `@CodeRabbit` (Independent Diff Review)

## 10. Merge Eligibility Checklist
- [x] RED test verified failing for true defect
- [ ] Minimal implementation completed
- [ ] Atomic commits with Conventional Commit messages
- [ ] Pre-PR verification executed freshly
- [ ] Independent code review passed with zero blocking findings
- [ ] Pull Request opened targeting default branch
- [ ] All remote CI checks green
- [ ] Post-merge default branch health verified
- [ ] Delivery receipt posted to closed issue
