## Description:

Yuan'an detects malicious patterns in AI skills across 13 detector classes and scans Windows/Linux system security baselines with read-only, zero-dependency checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security engineers, and agent operators use this skill to audit AI skill directories for supply-chain risk and to produce read-only system baseline findings before installation or during periodic review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional installers can copy the skill into one or many agent skill folders.

Mitigation: Install only from trusted sources and prefer a scoped --dir or single-agent install when broad agent-environment changes are not intended.

Risk: Audit reports may expose local paths and security posture details even when credentials are redacted.

Mitigation: Treat generated reports as sensitive review artifacts and limit sharing to authorized reviewers.

Risk: Running scans against systems or skills without authorization can create legal, policy, or operational risk.

Mitigation: Run the skill only against systems, skill directories, or environments that the user is authorized to audit.

## Reference(s):

- [Threat Patterns](references/threat-patterns.md)
- [Remediation Guide](references/remediation-guide.md)
- [System Baseline](references/system-baseline.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-security-audit)
- [Publisher profile](https://clawhub.ai/user/yottameta)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and optional text, JSON, or Markdown audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are masked by default and may include local paths, detected patterns, severity levels, and suggested next steps.]

## Skill Version(s):

0.1.5 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
