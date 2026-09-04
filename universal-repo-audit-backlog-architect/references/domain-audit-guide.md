# 14-Domain Audit Inspection Guide

Systematic gap analysis protocol covering the 14 core engineering and product dimensions. Use during Phase 7 to ensure comprehensive discovery without guessing or superficial checklists.

---

## A. Correctness

Identify bugs, logical flaws, broken edge cases, and unexpected runtime states.

### What to inspect
- Core business logic flows, conditional branches, state transitions, and edge cases.
- Error handling paths: look for swallowed exceptions, silent `catch {}`, or empty error responses.
- Concurrency and async handling: race conditions, unhandled Promise rejections, missing locks/mutexes.
- Input validation boundaries: missing type guards, unvalidated request payloads, boundary overflow.
- State mutation invariants: out-of-order state updates, stale cache reads, zombie listeners.

### Grounded Signals
- Unhandled null/undefined dereferences in high-traffic call chains.
- Missing default/fallback branches in exhaustive switch/pattern matches.
- Off-by-one errors in pagination, slicing, or time-window calculations.
- Asynchronous operations executed without `await` or missing error callbacks.

---

## B. Security and Privacy

Identify vulnerabilities, access control lapses, secret exposure, and data leakage risks.

### What to inspect
- Authentication & Authorization: missing route guards, IDOR vulnerabilities, broken JWT validation, role confusion.
- Secret & Credential Handling: hardcoded tokens, secrets committed in git history, exposed client-side environment variables.
- Injection vectors: SQL/NoSQL injection, Command injection, SSRF, XSS (reflected/DOM/stored), Template injection.
- Trust boundaries: unauthenticated webhook receivers, deserialization of untrusted data, path traversal (`../`).
- Sensitive data exposure: PII logged in plaintext, auth headers in error messages, CORS misconfigurations (`*` with credentials).

### Safety Invariant
- **Never publish weaponizable exploit payloads, live secrets, or real customer credentials in tracker Issues.**
- If a vulnerability is critical and exploitable, follow private security disclosure protocols (e.g., repository `SECURITY.md` or private draft advisory).

---

## C. Reliability

Identify resilience defects, crash vectors, recovery gaps, and cascading failure risks.

### What to inspect
- Network resilience: missing timeouts, infinite retries, lack of exponential backoff or jitter.
- Transactional integrity: partial writes across distributed systems or non-atomic multi-table updates.
- Resource management: unbounded connection pools, unclosed file descriptors, leaking event listeners.
- Graceful degradation: circuit breakers, fallback providers, health check responsiveness under load.
- Process lifecycle: startup dependency ordering, graceful shutdown (`SIGTERM`/`SIGINT`), cleanup of background queues.

### Grounded Signals
- API clients instantiated without configured connect/read timeouts.
- Background jobs that retry endlessly on permanent client errors (4xx).
- Lack of idempotency keys on payment, order, or state-changing webhook ingestion endpoints.

---

## D. Performance

Identify verifiable bottlenecks, algorithmic inefficiencies, excessive overhead, and resource hogs.

### What to inspect
- Database query patterns: N+1 queries, unindexed foreign keys, table scans, oversized `SELECT *`.
- Network & Serialization: oversized JSON payloads, chatty waterfalls, uncompressed assets, missing pagination.
- Client/UI rendering: unnecessary component re-renders, layout thrashing, unmemoized expensive calculations, unbounded lists.
- Compute & Memory: quadratic algorithms ($O(N^2)$), memory retention in long-lived singletons, blocking event loops.

### Gating Invariant
- **Do NOT open speculative performance issues based on feelings.**
- Every performance Issue must cite either:
  1. A measured baseline / flamegraph / query log.
  2. A demonstrable algorithmic bottleneck with concrete complexity analysis.
  3. A specific profiling/measurement spike with an observable hypothesis.

---

## E. Data Integrity

Identify schema anomalies, unsafe migration steps, orphaned records, and consistency hazards.

### What to inspect
- Database schemas: missing foreign key constraints, nullable columns lacking defaults, lack of unique constraints.
- Migration hygiene: destructive migrations (dropping columns/tables in a single deployment), locking large tables.
- Data synchronization: dual-write inconsistencies between database and search index/cache.
- State machines: invalid transitions permitted by schema or application code.

### Migration Invariant
- Require the **Expand -> Migrate -> Contract** pattern for non-trivial database or contract changes.

---

## F. Testing and Quality Safeguards

Identify missing test tiers, deceptive coverage, flaky assertions, and skipped validations.

### What to inspect
- Test suite structure: unit, integration, contract, end-to-end, and smoke test suites.
- Coverage gaps: critical business workflows with zero automated assertions.
- Test quality: over-mocked tests that assert against mock implementations rather than real boundaries, missing assertions.
- Test suite health: flaky tests, skipped/commented-out tests (`it.skip`), excessive test run duration.
- Safety tooling: typecheck (`tsc`, `mypy`), linting (`eslint`, `ruff`), mutation testing, security scanning (`trivy`, `semgrep`).

### Grounded Signals
- Critical auth or checkout flows covered only by 3-year-old mock tests.
- CI pipelines configured with `|| true` or `--continue-on-error` on test steps.

---

## G. Architecture and Technical Debt

Identify structural friction, misplaced boundaries, tight coupling, and brittle abstractions.

### What to inspect
- Module boundaries: circular dependencies, leaky abstractions, presentation logic accessing raw database drivers.
- Domain model integrity: business rules scattered across controllers, duplicated domain calculations.
- Code size and complexity: God classes, 2000-line functions with cyclomatic complexity > 30.
- Legacy debt: deprecated libraries, obsolete compatibility layers, abandoned experiment flags.

### Discipline Invariant
- **Architectural elegance is not a sufficient reason to open an Issue.**
- The architectural defect must have a demonstrable engineering cost: high defect rate, blocking parallel development, or making changes dangerous.

---

## H. Developer Experience (DX)

Identify friction in local development, onboarding, toolchain ergonomics, and feedback loops.

### What to inspect
- Onboarding flow: does `git clone && install && dev` work seamlessly out of the box?
- Environment configuration: missing `.env.example`, undocumented secret requirements, platform incompatibilities.
- Build & Run speed: slow hot-module replacement (HMR), sluggish compilation, brittle local containers/runners.
- Script hygiene: package manifests containing broken, obsolete, or undocumented scripts.

---

## I. CI/CD and Release Engineering

Identify build fragility, pipeline bottlenecks, unsafe deployment assumptions, and release risks.

### What to inspect
- CI workflows: missing build caches, uncapped job matrix execution, lack of lint/typecheck gates before tests.
- Build reproducibility: unpinned dependencies in lockfiles, non-deterministic build artifacts.
- Release automation: manual release steps prone to human error, lack of semantic versioning or changelog automation.
- Deployment safety: missing smoke tests post-deploy, lack of automated rollbacks, unmonitored canary phases.

---

## J. Observability and Operations

Identify blind spots in production monitoring, un-actionable telemetry, and debugging hurdles.

### What to inspect
- Structured logging: unstructured `console.log` dumps, missing correlation IDs (`requestId`, `traceId`).
- Metrics & Telemetry: missing latency histograms, error counters, or queue depth metrics.
- Distributed tracing: broken trace propagation across microservice or async boundaries.
- Error reporting: uncaptured unhandled rejections, noisy error alerts lacking diagnostic context.
- Operational health: missing or superficial `/healthz` / `/readyz` endpoints.

---

## K. Accessibility (A11y) and UX

Identify interface friction, accessibility non-compliance, and user experience stumbling blocks.

### What to inspect
- Keyboard accessibility: missing tab navigation, trapped focus, missing visible focus rings.
- Screen reader support: missing ARIA attributes, empty alt text, non-semantic button/link markup.
- Visual standards: color contrast ratios below WCAG AA, text truncation on mobile screens.
- UX edge cases: missing empty states, missing error banners, unresponsive action buttons lacking loading indicators.

---

## L. Documentation

Identify documentation drift, stale guides, missing API specifications, and architectural silos.

### What to inspect
- Getting Started / Setup: instructions in `README.md` that fail on a clean machine.
- API Documentation: undocumented public endpoints, missing parameter schemas, stale request/response examples.
- Architecture records: missing Architecture Decision Records (ADRs) for complex domain systems.
- Code comments: stale comments contradicting the implementation, unfulfilled `TODO(2021)` tags.

---

## M. Product Strategy and Workflow Gaps

Identify incomplete user loops, missing workflow steps, friction points, and natural feature extensions.

### What to inspect
- User journey loops: onboarding -> activation -> core value -> retention -> sharing.
- Friction points: manual exports required where automated handoffs are natural.
- Missing core capabilities: features strongly implied by existing infrastructure but not exposed to users.
- Edge-case handling: how does the system behave when data is deleted, user cancels subscription, or limits are reached?

### Product Invariant
- Every product feature proposal must answer: **"Why should this specific repository have this?"**
- Base proposals on existing domain evidence and user needs, not generic trends.

---

## N. Ideas, Spikes, and RFCs

Formulate experimental hypotheses, technical investigations, and architectural spikes.

### What to inspect
- High-uncertainty technologies: evaluating alternative databases, migration to a new rendering engine, or LLM integrations.
- Architectural pivots: moving from monolith to modular monolith or adopting event sourcing.
- Open product questions: testing user appetite for a new collaboration paradigm.

### Spike Invariant
- Spike deliverables must be **knowledge or a validated decision**, not unvetted production code.
- Acceptance criteria must be framed to prove or disprove the hypothesis.
