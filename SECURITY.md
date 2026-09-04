# Security Policy

## Reporting Security Issues

We take the security of this project and any audited repositories seriously. If you believe you have discovered a vulnerability, please do not open a public GitHub issue.

Please report vulnerabilities privately by emailing:
`mamdouh.aboammar@gmail.com`

Include:
- Type of vulnerability
- Steps to reproduce
- Potential impact
- Suggested mitigations (if available)

We will review your submission and respond promptly.

## Security Invariants of this Tool

When running the **Universal Repository Audit & Backlog Architect**:
1. **Strict Read-Only Boundary**: The tool and skill will never modify, patch, or delete target application code.
2. **Zero Credential Exposure**: Discovered secrets, private tokens, connection strings, or authorization headers are strictly redacted (`***REDACTED***`).
3. **Exploit Safety**: The tool documents vulnerability classes, evidence, and remediation steps without generating actionable weaponized exploit payloads.
