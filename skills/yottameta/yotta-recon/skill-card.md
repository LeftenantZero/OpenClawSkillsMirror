## Description:

元析 yotta-recon helps agents perform authorized TCP port scanning, service identification, and version fingerprinting for security testing and asset inventory without relying on nmap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security testers, asset owners, and agent operators use this skill to inventory authorized targets, identify open ports and common services, and produce findings for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized or overly broad scanning can create legal, operational, or trust risk.

Mitigation: Run check-scope before scanning, prefer scope files for authorized ranges, and use --assume-authorized --yes only when the user has explicit authorization.

Risk: Read-only probes still contact target systems and may appear in logs or monitoring.

Mitigation: Coordinate scans with the asset owner and tune concurrency, rate, and timeout settings to match the authorized test plan.

Risk: Version-based risk labels are fingerprint matches, not confirmed vulnerabilities.

Mitigation: Treat findings as triage signals and require human verification before remediation or escalation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-recon)
- [README](README.md)
- [Scope Guard authorization discipline](references/scope-guard.md)
- [Service and version fingerprints](references/service-fingerprints.md)
- [Protocol probes](references/protocol-probes.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Agent guidance plus CLI output in plain text, JSON, or Markdown report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scan results can include scan_id, timestamp, targets, authorization source, open ports, service and version fingerprints, and risk labels that require human verification.]

## Skill Version(s):

0.1.3 (source: SKILL.md frontmatter, package.json, CHANGELOG, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
