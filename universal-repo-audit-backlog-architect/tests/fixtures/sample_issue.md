## Summary
Add JWT authentication signature verification to prevent authorization bypass.

## Classification
- **Type**: `type:security`
- **Priority**: `P0`
- **Severity**: `Critical`
- **Confidence**: `High`
- **Estimated Effort**: `S`
- **Implementation Readiness**: `READY FOR AGENT`

## Problem
The API gateway parses token payload without verifying signature when calling internal services.

## Evidence
File `auth/jwt.ts:L42` uses `jwt.decode()` instead of `jwt.verify()`.
Status: CONFIRMED.

## Why This Matters
An attacker can forge administrative claims and access all tenant data.

## Desired Outcome
All incoming requests verify signature against active public key before processing.

## Scope
- [ ] Update `auth/jwt.ts` to call `jwt.verify`
- [ ] Add unit tests verifying invalid tokens are rejected with 401

## Non-Goals
- Migrating from RSA to Ed25519 keys.

## Proposed Direction
Import verification key and enforce algorithm allowlist.

## Affected Areas
- `auth/jwt.ts`
- `tests/auth_test.ts`

## Dependencies
- **Blocked by**: None identified
- **Blocks**: None identified
- **Related**: None identified

## Risks and Edge Cases
Key rotation timing mismatch.

## Security / Privacy Considerations
Mitigates authentication bypass vulnerability.

## Data / Migration Considerations
No data migration required.

## Testing and Verification Strategy
Run `npm test` covering valid, expired, and tampered signatures.

## Acceptance Criteria
- [ ] Invalid and untrusted JWT signatures return HTTP 401 Unauthorized
- [ ] Valid tokens issued by authorized identity provider authenticate cleanly
- [ ] Existing authentication test suite passes completely

## Definition of Done
- All acceptance criteria satisfied and regression tests passing.

## Rollout / Recovery
Deploy to staging, verify auth metrics, roll out to production.

## References
- RFC 7519

## Notes for Implementation Agent
Do not change public key storage path.
