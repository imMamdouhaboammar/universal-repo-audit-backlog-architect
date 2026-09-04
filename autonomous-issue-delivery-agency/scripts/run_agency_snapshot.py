#!/usr/bin/env python3
"""
Agency Repository Snapshot Extractor
Captures real-time repository state (HEAD SHA, branch, working tree cleanliness,
recent commits, remotes, and PR/issue context) for Phase 0 and iteration checkpoints.
"""

import sys
import json
import subprocess
import argparse
from pathlib import Path

def run_cmd(cmd, cwd):
    try:
        res = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return 1, "", str(e)

def get_snapshot(repo_path: Path):
    snapshot = {
        "repository_path": str(repo_path.resolve()),
        "is_git_repo": False,
        "branch": None,
        "head_sha": None,
        "working_tree_clean": False,
        "uncommitted_files": [],
        "remotes": {},
        "recent_commits": [],
        "gh_available": False,
        "open_issues_count": None,
        "open_prs_count": None
    }

    # Verify git repository
    rc, stdout, _ = run_cmd(["git", "rev-parse", "--is-inside-work-tree"], repo_path)
    if rc != 0 or stdout != "true":
        return snapshot

    snapshot["is_git_repo"] = True

    # Current branch
    _, branch, _ = run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"], repo_path)
    snapshot["branch"] = branch

    # Current HEAD SHA
    _, sha, _ = run_cmd(["git", "rev-parse", "HEAD"], repo_path)
    snapshot["head_sha"] = sha

    # Working tree status
    _, status, _ = run_cmd(["git", "status", "--porcelain"], repo_path)
    uncommitted = [line for line in status.splitlines() if line.strip()]
    snapshot["working_tree_clean"] = len(uncommitted) == 0
    snapshot["uncommitted_files"] = uncommitted[:20]

    # Remotes
    _, remotes_out, _ = run_cmd(["git", "remote", "-v"], repo_path)
    for line in remotes_out.splitlines():
        parts = line.split()
        if len(parts) >= 2:
            snapshot["remotes"][parts[0]] = parts[1]

    # Recent commits (last 5)
    _, log_out, _ = run_cmd(["git", "log", "-n", "5", "--pretty=format:%h - %s (%cr) <%an>"], repo_path)
    snapshot["recent_commits"] = log_out.splitlines()

    # Check gh CLI
    rc, _, _ = run_cmd(["gh", "--version"], repo_path)
    if rc == 0:
        snapshot["gh_available"] = True
        # Try fetching issue count
        rc_iss, out_iss, _ = run_cmd(["gh", "issue", "list", "--limit", "100", "--json", "number"], repo_path)
        if rc_iss == 0:
            try:
                snapshot["open_issues_count"] = len(json.loads(out_iss))
            except Exception:
                pass
        # Try fetching PR count
        rc_pr, out_pr, _ = run_cmd(["gh", "pr", "list", "--limit", "100", "--json", "number"], repo_path)
        if rc_pr == 0:
            try:
                snapshot["open_prs_count"] = len(json.loads(out_pr))
            except Exception:
                pass

    return snapshot

def main():
    parser = argparse.ArgumentParser(description="Capture live agency repository snapshot")
    parser.add_argument("repo_path", nargs="?", default=".", help="Path to repository root")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    repo = Path(args.repo_path)
    if not repo.exists():
        print(f"Error: Path '{repo}' does not exist.", file=sys.stderr)
        sys.exit(1)

    snapshot = get_snapshot(repo)

    if args.json:
        print(json.dumps(snapshot, indent=2))
    else:
        print(f"=== Agency Repository Snapshot ===")
        print(f"Path: {snapshot['repository_path']}")
        print(f"Branch: {snapshot['branch']} | HEAD: {snapshot['head_sha']}")
        print(f"Working Tree Clean: {'✅ YES' if snapshot['working_tree_clean'] else '⚠️ NO (Uncommitted changes detected)'}")
        if not snapshot["working_tree_clean"]:
            print(f"Uncommitted Files ({len(snapshot['uncommitted_files'])}):")
            for f in snapshot["uncommitted_files"]:
                print(f"  {f}")
        print("\nRemotes:")
        for name, url in snapshot["remotes"].items():
            print(f"  {name}: {url}")
        print("\nRecent Commits:")
        for c in snapshot["recent_commits"]:
            print(f"  {c}")
        if snapshot["gh_available"]:
            print(f"\nGitHub Context: Open Issues: {snapshot['open_issues_count']} | Open PRs: {snapshot['open_prs_count']}")

if __name__ == "__main__":
    main()
