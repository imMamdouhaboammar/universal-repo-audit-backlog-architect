# Backlog Triage, Prioritization & Readiness Framework

This reference defines the taxonomy, priority calibration, and readiness lifecycle for all backlog candidates.

---

## 1. Priority Model (P0 - P3)

Prioritize based on verifiable risk, user impact, and dependency order. Do not inflate priority without evidence.

### P0 - Critical (Drop everything / Blocker)
- Exploitable critical security vulnerability or active credential leak.
- Credible data corruption, data loss, or database integrity failure.
- Core production service unusable; critical user path completely broken.
- Core release cannot safely proceed due to broken build or packaging.
- *Requirement*: Must be supported by concrete, verified evidence (e.g., reproduction or failing test).

### P1 - High (Current cycle priority)
- Major correctness defect impacting standard user flows.
- Significant security risk or auth weakness (not actively exploited).
- Major reliability issue: unhandled cascading failures, memory leak over time.
- Major user workflow gap blocking adoption.
- Foundation refactor that blocks multiple downstream high-value tickets.

### P2 - Medium (Next cycle / Valuable enhancement)
- Meaningful product enhancement supported by user evidence.
- Verified performance bottleneck with optimization baseline.
- Significant test coverage gap for non-critical paths.
- Meaningful developer experience (DX) friction slowing down team velocity.
- Architecture technical debt with demonstrable maintenance friction.

### P3 - Low (Backlog / Polish / Opportunistic)
- Minor UI polish, copy improvements, or styling fixes.
- Optional developer convenience scripts.
- Speculative architectural cleanup without current pain.
- Exploratory spikes or low-confidence feature ideas.

---

## 2. Severity vs. Priority Distinction

- **Severity**: The technical magnitude of the impact (Critical, Major, Minor, Low).
- **Priority**: The urgency of the sequencing (P0, P1, P2, P3).

*Example*: A broken link in the footer has low severity and low priority (Minor/P3). A subtle race condition in payment processing that occurs once every 10,000 transactions has critical severity and P1 priority.

---

## 3. Confidence and Effort Estimations

### Confidence
- **High**: Directly verified in code, reproducible via test or script, clearly understood.
- **Medium**: Inferred from code patterns and architecture, high likelihood, minor unknowns.
- **Low**: Speculative hypothesis or complex distributed edge case requiring investigation.

### Effort
- **XS**: < 30 minutes. Single line fix, simple docs update.
- **S**: 1-2 hours. Isolated bug fix or small helper with tests.
- **M**: 2-4 hours. Standard vertical slice: API endpoint + domain logic + tests.
- **L**: 1-2 days. Subsystem refactor, complex migration phase, multi-step workflow.
- **XL**: > 2 days. **DECOMPOSE IMMEDIATELY.** Do not leave XL issues in the backlog.

---

## 4. Implementation Readiness States

Assign exactly one readiness state to each Issue:

| State | Definition | Agent Action |
|---|---|---|
| `READY FOR AGENT` | Problem, boundaries, tests, and acceptance criteria are fully specified. | Fresh agent can start work immediately without clarification. |
| `BLOCKED` | A hard technical prerequisite (another Issue or external dependency) must land first. | Do not execute until blocking ticket reaches Done. |
| `NEEDS RESEARCH` | Technical uncertainty is too high for safe implementation. | Convert to an RFC/Spike or research task first. |
| `NEEDS PRODUCT DECISION` | Requires business, pricing, or product direction choice not present in repo. | Await stakeholder decision; do not guess intent. |
| `RFC / EXPERIMENT` | The goal is to prove or disprove a hypothesis, not ship production code. | Produce ADR or benchmark report. |

---

## 5. Backlog Groupings

Group discovered work into the following standard 5 clusters:

- **Group 1**: Critical Correctness, Security, and Release Blockers (P0 and P1 risks).
- **Group 2**: Reliability, Data Integrity, and Performance (production stability).
- **Group 3**: Product Gaps and Features (vertical user-facing value).
- **Group 4**: Engineering Quality (Architecture, Testing, CI/CD, DX, Documentation).
- **Group 5**: Opportunities, Experiments, and Spikes (hypotheses and research).

---

## 6. Gating Rules: Rejecting Low-Value Candidates

Reject or merge candidates that match these antipatterns:
1. **The Phantom Best Practice**: "Add TypeScript strict mode" or "Use microservices" without a demonstrable repository problem.
2. **The Stylistic Nit**: Reformatting code, renaming variables to personal preference, or moving files arbitrarily.
3. **The Unsupported Speculation**: "Performance might be slow if 1M users join" when the repo has 0 users and no bottlenecks.
4. **The Giant Monolith**: "Refactor the backend" or "Improve test coverage".
5. **The Duplicative Shadow**: Re-reporting an issue already tracked in an existing GitHub issue or planned in `ROADMAP.md`.
