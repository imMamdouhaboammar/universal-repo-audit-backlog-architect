# Final Repository Audit & Backlog Architecture Report

---

## 1. Repository Snapshot

| Attribute | Details |
|---|---|
| **Repository** | `{{REPO_NAME}}` |
| **Analyzed Branch** | `{{ANALYZED_BRANCH}}` |
| **Analyzed HEAD SHA** | `{{HEAD_SHA}}` |
| **Default Branch** | `{{DEFAULT_BRANCH}}` |
| **Latest Release / Tag** | `{{LATEST_TAG}}` |
| **Working Tree Status** | `{{WORKING_TREE_STATUS}}` |
| **Primary Technology Stack** | `{{PRIMARY_TECH_STACK}}` |
| **Product Purpose** | `{{PRODUCT_SUMMARY}}` |

---

## 2. Current State Assessment

### Product Maturity
{{PRODUCT_MATURITY_ASSESSMENT}}

### Engineering Maturity & Safeguards
{{ENGINEERING_MATURITY_ASSESSMENT}}

### Major Strengths
- {{STRENGTH_1}}
- {{STRENGTH_2}}

### Major Risks & Vulnerabilities
- {{RISK_1}}
- {{RISK_2}}

### Release & Operational Concerns
{{RELEASE_CONCERNS}}

---

## 3. Backlog Metrics & Breakdown

| Category | Dimension | Count |
|---|---|:---:|
| **Total Issues** | Created in Tracker / Backlog | **{{TOTAL_ISSUES}}** |
| **Priority** | P0 (Critical / Blocker) | {{COUNT_P0}} |
| | P1 (High) | {{COUNT_P1}} |
| | P2 (Medium) | {{COUNT_P2}} |
| | P3 (Low) | {{COUNT_P3}} |
| **Domain Type** | Bugs & Correctness | {{COUNT_BUGS}} |
| | Security & Privacy | {{COUNT_SECURITY}} |
| | Reliability, Data & Performance | {{COUNT_RELIABILITY_PERF}} |
| | Product & Features | {{COUNT_FEATURES}} |
| | Engineering Quality (Arch, Test, CI, DX) | {{COUNT_QUALITY}} |
| | Spikes, RFCs & Experiments | {{COUNT_EXPERIMENTS}} |
| **Readiness** | READY FOR AGENT | {{COUNT_READY}} |
| | BLOCKED (Has prerequisites) | {{COUNT_BLOCKED}} |
| | NEEDS RESEARCH | {{COUNT_NEEDS_RESEARCH}} |
| | NEEDS PRODUCT DECISION | {{COUNT_NEEDS_DECISION}} |

---

## 4. Recommended Execution Order (Topological)

Execution order accounts for hard dependencies and minimizes integration risk:

```mermaid
{{TOPOLOGICAL_MERMAID_DAG}}
```

### Wave 1: Immediate Blockers & Foundations (Run in Parallel)
- [ ] `#...` Title (P...)
- [ ] `#...` Title (P...)

### Wave 2: Core Vertical Slices & Migrations
- [ ] `#...` Title (P...) [Blocked by Wave 1]

### Wave 3: Product Capabilities & Enhancements
- [ ] `#...` Title (P...)

### Wave 4: Polish & Secondary Optimizations
- [ ] `#...` Title (P...)

---

## 5. Critical Path Analysis

The critical path dictating minimum cycle time to production readiness:
1. `#...` [P0] -> Solves ...
2. `#...` [P1] -> Unlocks ...
3. `#...` [P1] -> Delivers ...

---

## 6. Catalog of Created Issues

| # | Title | Priority | Readiness | Domain | URL / Path |
|---|---|:---:|:---:|---|---|
| #1 | {{TITLE_1}} | `{{P1}}` | `READY FOR AGENT` | `security` | [View Issue]({{URL_1}}) |
| #2 | {{TITLE_2}} | `{{P1}}` | `READY FOR AGENT` | `correctness` | [View Issue]({{URL_2}}) |
| #3 | {{TITLE_3}} | `{{P2}}` | `BLOCKED` | `product` | [View Issue]({{URL_3}}) |

---

## 7. Deferred Candidates (Deliberately Excluded)

Candidates audited but rejected during triage to prevent backlog bloating:

| Candidate Description | Reason for Exclusion | Category |
|---|---|---|
| `{{CANDIDATE_1}}` | Already addressed in closed PR #... | Duplicate / Resolved |
| `{{CANDIDATE_2}}` | Insufficient evidence; no observable failure | Speculative |
| `{{CANDIDATE_3}}` | Requires fundamental commercial pricing pivot | Needs Product Decision |

---

## 8. Verification Note

- **Executed Safeguards**: Exact commands run during discovery (e.g., `git status`, `npm test`, `cargo check`).
- **External Primary Sources**: Upstream specifications and documentation referenced.
- **Tracker Operations**: Confirmed remote issue creation or local artifact generation.
- **Strict Mutation Boundary**: Verified working tree remained untouched and zero application source code was modified.
