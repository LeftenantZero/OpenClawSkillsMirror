## Description:

Security-and-hardeni helps agents automate security and hardening workflows, including structured input handling, security review guidance, remediation steps, and report-style outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to inspect security-sensitive code or workflows, generate hardening guidance, and produce structured remediation or status outputs for automation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read and command execution authority.

Mitigation: Run it in a limited workspace, require explicit approval before command execution or remediation, and review proposed changes before applying them.

Risk: The skill makes security-hardening and data-protection claims that are not backed by concrete implementation evidence.

Mitigation: Treat outputs as advisory, independently verify findings and fixes, and do not rely on claimed encryption or hardening protections without separate validation.

Risk: Security review workflows may expose sensitive code, configuration, or credentials.

Mitigation: Avoid providing secrets unless necessary, redact sensitive values where possible, and use a test repository or restricted workspace for evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/security-and-hardening)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured responses with optional code, command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include status metadata, remediation guidance, and error details.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
