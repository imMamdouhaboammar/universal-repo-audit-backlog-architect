#!/usr/bin/env python3
"""Validate backlog issues for structure, falsifiable acceptance criteria, and DAG acyclicity."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED_SECTIONS = [
    "Summary",
    "Classification",
    "Problem",
    "Evidence",
    "Why This Matters",
    "Desired Outcome",
    "Scope",
    "Non-Goals",
    "Acceptance Criteria",
    "Definition of Done",
]

VALID_PRIORITIES = {"P0", "P1", "P2", "P3"}
VALID_EFFORTS = {"XS", "S", "M", "L", "XL"}
VALID_READINESS = {
    "READY FOR AGENT",
    "BLOCKED",
    "NEEDS RESEARCH",
    "NEEDS PRODUCT DECISION",
    "RFC / EXPERIMENT",
    "RFC/EXPERIMENT",
}

VAGUE_CRITERIA_PATTERNS = [
    re.compile(r"code quality is good", re.I),
    re.compile(r"performance is improved", re.I),
    re.compile(r"ux is better", re.I),
    re.compile(r"things work nicely", re.I),
    re.compile(r"add unit tests$", re.I),
]


def parse_issue_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_title = ""
    current_lines: list[str] = []

    for line in text.splitlines():
        if line.startswith("## "):
            if current_title:
                sections[current_title] = "\n".join(current_lines).strip()
            current_title = line[3:].strip()
            current_lines = []
        elif current_title:
            current_lines.append(line)

    if current_title:
        sections[current_title] = "\n".join(current_lines).strip()

    return sections


def extract_dependencies(text: str) -> tuple[list[str], list[str]]:
    blocked_by: list[str] = []
    blocks: list[str] = []

    for line in text.splitlines():
        line_clean = line.strip()
        if re.search(r"blocked by\s*:", line_clean, re.I):
            ids = re.findall(r"#([a-zA-Z0-9_-]+)", line_clean)
            blocked_by.extend(ids)
        elif re.search(r"blocks\s*:", line_clean, re.I):
            ids = re.findall(r"#([a-zA-Z0-9_-]+)", line_clean)
            blocks.extend(ids)

    return blocked_by, blocks


def detect_cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    """Detect cycles in dependency graph using DFS."""
    visited: set[str] = set()
    rec_stack: set[str] = set()
    cycles: list[list[str]] = []

    def dfs(node: str, path: list[str]):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, path + [neighbor])
            elif neighbor in rec_stack:
                cycle_start = path.index(neighbor) if neighbor in path else 0
                cycles.append(path[cycle_start:] + [neighbor])
        rec_stack.remove(node)

    for node in graph:
        if node not in visited:
            dfs(node, [node])

    return cycles


def validate_issue_file(path: Path, repo_root: Path | None = None) -> list[dict]:
    findings = []
    text = path.read_text(encoding="utf-8", errors="replace")
    sections = parse_issue_sections(text)

    # Check required sections
    for sec in REQUIRED_SECTIONS:
        found = any(sec.lower() == k.lower() for k in sections)
        if not found:
            findings.append({
                "severity": "error",
                "code": "MISSING_SECTION",
                "message": f"Missing required section: '## {sec}' in {path.name}",
            })

    # Check Acceptance Criteria checkboxes and vagueness
    criteria_text = ""
    for k, v in sections.items():
        if "acceptance criteria" in k.lower():
            criteria_text = v
            break

    checkboxes = re.findall(r"-\s*\[\s*\]\s+(.+)", criteria_text)
    if len(checkboxes) < 2:
        findings.append({
            "severity": "error",
            "code": "INSUFFICIENT_CRITERIA",
            "message": f"Acceptance criteria must have at least 2 '- [ ]' checkboxes in {path.name}",
        })

    for cb in checkboxes:
        for pat in VAGUE_CRITERIA_PATTERNS:
            if pat.search(cb):
                findings.append({
                    "severity": "error",
                    "code": "VAGUE_CRITERION",
                    "message": f"Falsifiable criterion violated in {path.name}: '{cb}'",
                })

    # Check Classification fields
    class_text = ""
    for k, v in sections.items():
        if "classification" in k.lower():
            class_text = v
            break

    priority_match = re.search(r"\*?\*?Priority\*?\*?\s*:\s*`?(P[0-3])`?", class_text, re.I)
    if not priority_match:
        findings.append({
            "severity": "error",
            "code": "INVALID_PRIORITY",
            "message": f"Valid priority (P0-P3) missing in Classification in {path.name}",
        })

    effort_match = re.search(r"\*?\*?(?:Estimated\s+)?Effort\*?\*?\s*:\s*`?(XS|S|M|L|XL)`?", class_text, re.I)
    if effort_match and effort_match.group(1).upper() == "XL":
        findings.append({
            "severity": "warning",
            "code": "XL_NEEDS_DECOMPOSITION",
            "message": f"Issue {path.name} is estimated as XL and should be decomposed",
        })

    readiness_match = re.search(
        r"\*?\*?(?:Implementation\s+)?Readiness\*?\*?\s*:\s*`?(READY FOR AGENT|BLOCKED|NEEDS RESEARCH|NEEDS PRODUCT DECISION|RFC\s*/\s*EXPERIMENT)`?",
        class_text,
        re.I,
    )
    if not readiness_match:
        findings.append({
            "severity": "error",
            "code": "INVALID_READINESS",
            "message": f"Valid Readiness state missing in Classification in {path.name}",
        })

    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Directory containing issue files or single markdown issue")
    parser.add_argument("--repo", type=Path, default=None, help="Root path of repository for checking file paths")
    parser.add_argument("--json", action="store_true", help="Output JSON findings")
    args = parser.parse_args()

    target = args.target.resolve()
    issue_files = [target] if target.is_file() else sorted(target.glob("*.md"))

    all_findings = []
    dep_graph: dict[str, list[str]] = {}

    for issue_file in issue_files:
        file_id = issue_file.stem
        dep_graph.setdefault(file_id, [])
        findings = validate_issue_file(issue_file, args.repo)
        all_findings.extend(findings)

        text = issue_file.read_text(encoding="utf-8", errors="replace")
        blocked_by, blocks = extract_dependencies(text)
        for dep in blocked_by:
            dep_graph[file_id].append(dep)
        for target_id in blocks:
            dep_graph.setdefault(target_id, []).append(file_id)

    # Detect cycles in the DAG
    cycles = detect_cycles(dep_graph)
    for cycle in cycles:
        all_findings.append({
            "severity": "error",
            "code": "DEPENDENCY_CYCLE",
            "message": f"Dependency cycle detected: {' -> '.join(cycle)}",
        })

    errors = [f for f in all_findings if f["severity"] == "error"]
    warnings = [f for f in all_findings if f["severity"] == "warning"]

    if args.json:
        print(json.dumps({
            "valid": len(errors) == 0,
            "issues_inspected": len(issue_files),
            "error_count": len(errors),
            "warning_count": len(warnings),
            "findings": all_findings,
        }, indent=2))
    else:
        print(f"Validated {len(issue_files)} issue(s).")
        print(f"Errors: {len(errors)}, Warnings: {len(warnings)}")
        for f in all_findings:
            prefix = "[ERROR]" if f["severity"] == "error" else "[WARN]"
            print(f"{prefix} ({f['code']}): {f['message']}")

    if errors:
        exit(1)


if __name__ == "__main__":
    main()
