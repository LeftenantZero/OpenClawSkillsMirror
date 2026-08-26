## Description:

Use this skill to guide development debugging, test-failure investigation, automation, data analysis, and workflow orchestration for agent-assisted troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to structure debugging work, inspect files, run local commands, process development inputs, and produce structured troubleshooting results. It is best suited for supervised agent workflows where the user can review each command and credentialed operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan describes this as a broad automation/debugging template that may prompt local command execution, file processing, API credentials, or remote services without clear scope.

Mitigation: Install and use only with active supervision; review each proposed command, file operation, credential use, and remote-service action before allowing execution.

Risk: The security verdict is suspicious because the skill is not clearly limited to debugging and gives limited detail about consent, scope, and data handling.

Mitigation: Restrict use to explicit debugging tasks, avoid exposing sensitive data unless necessary, and stop execution when requested actions exceed the user-approved scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/systematic-debugging)
- [SkillHub homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-like structured results and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve local command execution, file processing, API credentials, or remote services depending on the agent task.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
