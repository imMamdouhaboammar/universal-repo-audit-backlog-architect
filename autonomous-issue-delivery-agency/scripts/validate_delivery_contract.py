#!/usr/bin/env python3
"""
Delivery Contract and Receipt Validator
Ensures that Issue Execution Contracts and Delivery Receipts adhere to the
Autonomous Issue Delivery Agency specification and contain zero exposed secrets.
"""

import sys
import re
import argparse
from pathlib import Path

SECRET_PATTERNS = [
    re.compile(r"(?:api[_-]?key|secret|token|password|bearer|auth[_-]?token)\s*[:=]\s*['\"][A-Za-z0-9_\-\.]{12,}['\"]", re.IGNORECASE),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{36,}", re.IGNORECASE),
    re.compile(r"sk-[A-Za-z0-9]{20,}", re.IGNORECASE),
    re.compile(r"-----BEGIN (?:RSA )?PRIVATE KEY-----"),
]

REQUIRED_CONTRACT_SECTIONS = [
    "Observable Objective",
    "Problem Statement",
    "Scope Boundaries",
    "In Scope",
    "Out of Scope",
    "Affected Surfaces",
    "Invariants",
    "Risk Assessment",
    "Test-Driven Verification Strategy",
    "Merge Eligibility Checklist",
]

REQUIRED_RECEIPT_SECTIONS = [
    "Status",
    "Pull Request",
    "Merged Into",
    "Resulting Commit SHA",
    "Atomic Commits",
    "Verification Evidence",
    "Independent Review",
    "Acceptance Criteria Verification",
    "Post-Merge Repository Health",
]

def scan_for_secrets(text: str) -> list:
    findings = []
    for line_num, line in enumerate(text.splitlines(), start=1):
        for pattern in SECRET_PATTERNS:
            if pattern.search(line) and "***REDACTED***" not in line and "{{SECRET" not in line:
                findings.append(f"Potential unredacted secret on line {line_num}: {line.strip()[:60]}...")
    return findings

def validate_contract(content: str) -> list:
    errors = []
    for section in REQUIRED_CONTRACT_SECTIONS:
        if section.lower() not in content.lower():
            errors.append(f"Contract missing required section: '{section}'")
    
    # Check for checklist items
    if not re.search(r"- \[[ xX]\]", content):
        errors.append("Contract missing actionable checklist items (`- [ ]`)")
    
    # Check for risk rating
    if not re.search(r"\b(LOW|MEDIUM|HIGH|CRITICAL)\b", content):
        errors.append("Contract missing explicit risk level (LOW, MEDIUM, HIGH, CRITICAL)")
        
    return errors

def validate_receipt(content: str) -> list:
    errors = []
    for section in REQUIRED_RECEIPT_SECTIONS:
        if section.lower() not in content.lower():
            errors.append(f"Receipt missing required section: '{section}'")
            
    # Check for verified checklist items
    if not re.search(r"- \[[xX]\]", content):
        errors.append("Receipt must contain at least one verified acceptance criterion (`- [x]`)")
        
    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate Issue Execution Contract or Delivery Receipt")
    parser.add_argument("--contract", type=str, help="Path to Issue Execution Contract markdown file")
    parser.add_argument("--receipt", type=str, help="Path to Delivery Receipt markdown file")
    args = parser.parse_args()

    if not args.contract and not args.receipt:
        parser.error("Must specify either --contract or --receipt")

    all_errors = []
    target_path = Path(args.contract if args.contract else args.receipt)

    if not target_path.exists():
        print(f"Error: Target file '{target_path}' does not exist.")
        sys.exit(1)

    content = target_path.read_text(encoding="utf-8")

    # Security scan
    secret_findings = scan_for_secrets(content)
    if secret_findings:
        all_errors.extend(secret_findings)

    # Schema scan
    if args.contract:
        all_errors.extend(validate_contract(content))
    elif args.receipt:
        all_errors.extend(validate_receipt(content))

    if all_errors:
        print(f"❌ Validation FAILED for {target_path}:")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        doc_type = "Contract" if args.contract else "Receipt"
        print(f"✅ {doc_type} '{target_path.name}' is valid and meets all agency quality invariants.")
        sys.exit(0)

if __name__ == "__main__":
    main()
