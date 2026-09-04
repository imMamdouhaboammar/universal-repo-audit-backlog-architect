#!/usr/bin/env python3
"""Safely extract repository snapshot and state without mutating anything."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run_cmd(cmd: list[str], cwd: Path) -> str:
    try:
        res = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        return res.stdout.strip()
    except Exception as e:
        return f"Error: {e}"


def get_git_info(repo_dir: Path) -> dict:
    git_dir = repo_dir / ".git"
    if not git_dir.exists():
        return {"is_git": False}

    current_branch = run_cmd(["git", "branch", "--show-current"], repo_dir)
    head_sha = run_cmd(["git", "rev-parse", "HEAD"], repo_dir)
    remote_url = run_cmd(["git", "config", "--get", "remote.origin.url"], repo_dir)
    status = run_cmd(["git", "status", "--porcelain"], repo_dir)
    recent_commits_raw = run_cmd(["git", "log", "-n", "5", "--oneline"], repo_dir)
    recent_commits = recent_commits_raw.splitlines() if recent_commits_raw else []
    latest_tags_raw = run_cmd(["git", "tag", "--sort=-creatordate"], repo_dir)
    latest_tags = latest_tags_raw.splitlines()[:5] if latest_tags_raw else []

    return {
        "is_git": True,
        "current_branch": current_branch or "DETACHED_HEAD",
        "head_sha": head_sha,
        "remote_url": remote_url or "None",
        "working_tree_clean": len(status) == 0,
        "uncommitted_files": status.splitlines() if status else [],
        "recent_commits": recent_commits,
        "latest_tags": latest_tags,
    }


def detect_toolchain(repo_dir: Path) -> list[str]:
    manifests = []
    if (repo_dir / "package.json").is_file():
        manifests.append("Node.js (package.json)")
    if (repo_dir / "bun.lockb").is_file() or (repo_dir / "bun.lock").is_file():
        manifests.append("Bun runtime")
    if (repo_dir / "pnpm-lock.yaml").is_file():
        manifests.append("pnpm package manager")
    if (repo_dir / "Cargo.toml").is_file():
        manifests.append("Rust (Cargo.toml)")
    if (repo_dir / "pyproject.toml").is_file():
        manifests.append("Python (pyproject.toml)")
    if (repo_dir / "requirements.txt").is_file():
        manifests.append("Python (requirements.txt)")
    if (repo_dir / "go.mod").is_file():
        manifests.append("Go (go.mod)")
    if (repo_dir / "Dockerfile").is_file() or (repo_dir / "compose.yaml").is_file():
        manifests.append("Docker containerization")
    if (repo_dir / ".github" / "workflows").is_dir():
        manifests.append("GitHub Actions CI/CD")
    return manifests


def detect_safeguard_commands(repo_dir: Path) -> list[str]:
    commands = []
    pkg_json = repo_dir / "package.json"
    if pkg_json.is_file():
        try:
            data = json.loads(pkg_json.read_text(encoding="utf-8"))
            scripts = data.get("scripts", {})
            for key in ("test", "lint", "typecheck", "build", "check"):
                if key in scripts:
                    commands.append(f"npm run {key}")
        except Exception:
            pass
    if (repo_dir / "Cargo.toml").is_file():
        commands.extend(["cargo test", "cargo check", "cargo clippy"])
    if (repo_dir / "pyproject.toml").is_file() or (repo_dir / "pytest.ini").is_file():
        commands.append("pytest")
    if (repo_dir / "go.mod").is_file():
        commands.append("go test ./...")
    return commands


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=None, help="Optional positional path to repository")
    parser.add_argument("--repo", type=Path, default=None, help="Path to repository")
    parser.add_argument("--json", action="store_true", help="Output JSON format")
    args = parser.parse_args()

    repo = (args.path or args.repo or Path.cwd()).resolve()
    snapshot = {
        "repository_path": str(repo),
        "git": get_git_info(repo),
        "toolchain": detect_toolchain(repo),
        "safeguards": detect_safeguard_commands(repo),
    }

    if args.json:
        print(json.dumps(snapshot, indent=2))
    else:
        print(f"# Repository Snapshot: {repo.name}")
        print(f"- Remote URL: {snapshot['git'].get('remote_url', 'N/A')}")
        print(f"- Current Branch: {snapshot['git'].get('current_branch', 'N/A')}")
        print(f"- HEAD SHA: {snapshot['git'].get('head_sha', 'N/A')}")
        print(f"- Clean Working Tree: {snapshot['git'].get('working_tree_clean', False)}")
        print(f"- Detected Toolchains: {', '.join(snapshot['toolchain']) or 'None'}")
        print(f"- Available Safeguard Commands: {', '.join(snapshot['safeguards']) or 'None'}")


if __name__ == "__main__":
    main()
