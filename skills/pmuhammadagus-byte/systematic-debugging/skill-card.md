## Description:

Use a structured four-phase process to identify root causes of technical issues before applying fixes, ensuring reliable and verified resolutions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when debugging test failures, production bugs, unexpected behavior, performance issues, build failures, or integration problems. It guides the agent through root-cause investigation, pattern analysis, hypothesis testing, and verified implementation before proposing fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic commands can expose secrets, signing identities, keychain state, environment variables, or other sensitive operational data.

Mitigation: Approve only the minimum diagnostic command needed and redact API keys, tokens, passwords, secrets, PII, and signing details before sharing logs.

Risk: Helper scripts run user-supplied commands or project tests and do not make those commands inherently safe.

Mitigation: Review commands before execution, avoid destructive operations, and run reproduction or bisection helpers only in an appropriate workspace.

## Reference(s):

- [Systematic Debugging on ClawHub](https://clawhub.ai/pmuhammadagus-byte/skills/systematic-debugging)
- [Root Cause Tracing](artifact/root-cause-tracing.md)
- [Defense-in-Depth Validation](artifact/defense-in-depth.md)
- [Condition-Based Waiting](artifact/condition-based-waiting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagnostic checklists, reproduction commands, validation patterns, and small helper scripts.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
