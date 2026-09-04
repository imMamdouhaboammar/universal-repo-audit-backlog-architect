# Specialist Routing Matrix

The **Autonomous Issue Delivery Agency** operates on the principle of **lean, evidence-driven specialist invocation**. Do NOT invoke all specialists for every task. Assemble the smallest useful team whose capabilities materially match the active issue.

---

## 1. Specialist Roster & Domain Match

| Specialist | Trigger Condition | Primary Value & Deliverables |
|---|---|---|
| **`@Riqor`** | All active issues (Lead Director) | End-to-end task coordination, convention enforcement, conventional commits |
| **`@get-fable`** | All active issues (Lifecycle Engine) | Circuit breaker enforcement, durable handoff states, verification falsification |
| **`@ZzzOps`** | Repositories with ZzzOps configuration | Execution state continuity, dependency tracking, multi-phase ledger management |
| **`@Superpowers`** | Systematic debugging & TDD | RED test formulation, hypothesis falsification, root-cause isolation |
| **`@GitHub`** | PR & Issue management | Real-time issue reading, PR creation, CI check querying, branch merging, closure |
| **`@Remote Desktop Commander`** | Local environment execution | Filesystem mutations, local test runs, build execution, process monitoring |
| **`@Context7`** | Framework & SDK API contracts | Upstream official documentation, breaking changes, version-specific behaviors |
| **`@AI Task Brief Builder`** | Ambiguous or broad issues | Tightening acceptance criteria, establishing non-goals, identifying invariants |
| **`@Codex Engineering Guardrails`** | Architecture & public APIs | API backwards compatibility, migration safety, structural decoupling |
| **`@Fallow Code Analysis` / `@SonarQube`** | Complex code refactoring | Static analysis, cyclomatic complexity alerts, dead code identification |
| **`@CodeRabbit`** | Pre-PR independent review | Independent diff evaluation, logic bugs, edge case discovery, maintainability |
| **`@Codex Security` / `@ArmorCodex`** | Auth, secrets, RLS, inputs | Threat modeling, injection prevention, role boundary verification, safe crypto |
| **`@Testifly` / `@Impeccable`** | User-facing UI changes | Visual hierarchy, responsive layout, keyboard navigation, cross-browser QA |
| **`@Agent Ready`** | Agentic interfaces & metadata | LLMs.txt validation, machine-readable API contracts, tool schema hygiene |
| **`@Supabase`** | Supabase/PostgreSQL backends | Schema migrations, RLS security policies, index optimization, real-time safety |
| **`@Vercel`** | Vercel deployment pipelines | Edge function compatibility, build artifact verification, deployment checks |
| **`@Dependency Upgrade Plan`** | Package upgrades | Transitive dependency analysis, security CVE audits, breaking change migration |

---

## 2. Standard Issue Routing Profiles

### Profile A: Standard Logic Bug / Defect
```text
Core Team:
- @Riqor (Lead)
- @get-fable (Execution Engine)
- @Superpowers (TDD & Falsification)
- @GitHub (Issue & PR)
- @CodeRabbit (Independent Review)
```

### Profile B: Security Boundary / Auth / RLS Issue
```text
Core Team:
- @Riqor (Lead)
- @get-fable (Execution Engine)
- @Codex Security / @ArmorCodex (Threat Modeling & Review)
- @Supabase (if database/RLS involved)
- @CodeRabbit (Independent Review)
- @GitHub (Issue & PR)
```

### Profile C: Frontend UI / Component Polish
```text
Core Team:
- @Riqor (Lead)
- @get-fable (Execution Engine)
- @Build Web Apps / @01 Superdesign (Layout & Styling)
- @Impeccable / @Testifly (Interaction & Accessibility QA)
- @CodeRabbit (Independent Review)
- @GitHub (Issue & PR)
```

### Profile D: Architecture Refactor / API Migration
```text
Core Team:
- @Riqor (Lead)
- @get-fable (Execution Engine)
- @Codex Engineering Guardrails (Interface Compatibility)
- @Context7 (API Contracts)
- @Fallow Code Analysis (Structural Complexity)
- @CodeRabbit (Independent Review)
- @GitHub (Issue & PR)
```

---

## 3. Concurrency & Ownership Rules

- **Read-Only Concurrency**: Multiple specialist plugins may inspect the codebase concurrently during discovery, planning, security auditing, and code review.
- **Strict Single Write Owner**: Exactly ONE execution agent holds the write lock on the repository workspace, filesystem, and active branch. Specialists never perform competing, uncoordinated code mutations.
