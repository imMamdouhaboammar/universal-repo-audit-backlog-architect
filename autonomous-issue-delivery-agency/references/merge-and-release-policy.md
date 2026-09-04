# Merge, Release, and Deployment Policy

This document establishes the authority boundaries, merge readiness criteria, protection invariants, and rollback protocols for the **Autonomous Issue Delivery Agency**.

---

## 1. Autonomous Merge Authority

The agency is granted explicit authority to autonomously merge Pull Requests for completed issues **only when ALL of the following criteria are objectively verified**:

- [ ] Issue scope is 100% complete with all acceptance criteria satisfied.
- [ ] Latest branch head SHA has passed all fresh local verification gates.
- [ ] All required remote status checks and CI workflows are `GREEN`.
- [ ] Required independent reviews are satisfied with zero unresolved `BLOCKING` or `IMPORTANT` findings.
- [ ] Code Owners review requirements are satisfied (where configured).
- [ ] The branch has no merge conflicts and is rebased cleanly onto the target branch.
- [ ] The Pull Request targets the effective default branch (`main` or `master`).
- [ ] The merge does NOT trigger an unauthorized irreversible production database mutation.

---

## 2. Never Bypass Repository Protections

> [!CAUTION]
> Even if the executing agent, token, or service account possesses GitHub **Administrator** privileges:
>
> **The agent MUST NEVER bypass branch protection rules, required CI checks, required reviews, or merge queues.**
>
> Administrative capability is not permission to ignore engineering discipline. If a check fails, diagnose and repair it. Never force-merge past a red gate.

---

## 3. Merge Strategies & Git Hygiene

The agency respects existing repository conventions for merge strategies:

1. **Squash and Merge**: Preferred when the repository prioritizes clean, linear default branch history where each commit corresponds 1:1 with an issue.
2. **Rebase and Merge**: Preferred when atomic individual commits within the branch must be preserved in the main history.
3. **Merge Commit**: Preferred when explicitly mandated by repository policy to preserve feature branch topology.

*Never rewrite published default branch history. Never use force-push (`git push --force`) on protected branches.*

---

## 4. Decoupling Merge from Deployment

> [!NOTE]
> **Merge $\neq$ Production Deployment**
>
> Merging code into the default branch integrates verified behavior into the shared mainline. It does NOT authorize or imply an immediate production deployment unless the repository possesses an automated CD pipeline explicitly authorized by user policy.
>
> If production deployment requires manual approval, tag creation, or cloud infrastructure mutation, the agency stops at:
> ```text
> STATUS: MERGED TO DEFAULT BRANCH
> DEPLOYMENT: PENDING HUMAN AUTHORITY
> ```

---

## 5. Rollback and Incident Recovery Protocol

If an unexpected failure or regression is detected on the default branch immediately following a merge:

1. **Halt Backlog Execution**: Do NOT select the next issue from the queue.
2. **Identify Impact**: Determine if the defect can be hotfixed in under 15 minutes or requires an immediate revert.
3. **Revert Procedure**:
   - Create a revert branch: `git checkout -b revert-<PR_NUMBER>-<SHA>`
   - Revert the merge commit: `git revert -m 1 <MERGE_SHA>`
   - Verify the revert locally: run unit tests and smoke tests.
   - Open and merge the emergency revert PR.
4. **Reopen the Original Issue**: Add incident details, stack traces, and failure hypotheses to the issue.
5. **Resume**: Only resume normal backlog processing once the default branch is proven green.
