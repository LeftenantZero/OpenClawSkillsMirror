## Description:

Prompts an agent to run verification commands before claiming work is complete, creating pull requests, or committing changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill before marking work complete to run verification commands, inspect failures, and report a structured completion status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad command execution capability without concrete command limits.

Mitigation: Use it only in repositories where agent-run verification commands are acceptable; prefer a version with explicit allowed commands or user confirmation before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/verification-before-completion)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON]

**Output Format:** [Markdown guidance with verification command output and optional JSON status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include success status, result data, metadata, and error details.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
