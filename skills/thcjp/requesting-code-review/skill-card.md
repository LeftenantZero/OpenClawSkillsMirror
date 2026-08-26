## Description:

Automates code review and development workflow tasks with structured input, markdown or JSON-style outputs, and error-handling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to request code review, inspect implementation work, and receive structured findings or follow-up commands before merging changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is broadly scoped for development automation and may read project files or propose command execution.

Mitigation: Use it only for explicit code-review tasks and review proposed commands before execution.

Risk: The artifact mentions API credentials and setup flows, which can expose secrets if copied into prompts or logs.

Mitigation: Avoid providing secrets or API keys unless necessary, and redact sensitive values from inputs and outputs.

Risk: Security evidence marks the release as suspicious because its stated code-review purpose expands into generic automation.

Mitigation: Constrain use to repositories and tasks where broad file access and development guidance are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/requesting-code-review)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review findings, remediation guidance, command suggestions, and structured success or error metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
