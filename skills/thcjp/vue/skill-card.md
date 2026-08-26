## Description:

规避 helps developers identify and avoid common Vue reactivity, ref/reactive, computed timing, and Composition API mistakes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and engineering teams use this skill to review Vue code or implementation plans for common reactivity and Composition API mistakes. Its broad automation claims should be constrained to Vue-related review, guidance, and carefully approved changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command execution authority beyond its Vue mistake-avoidance purpose.

Mitigation: Invoke it only for Vue-related review or implementation tasks, and manually approve proposed file changes and commands before execution.

Risk: The artifact describes API, webhook, and system-connection use that is not well scoped to Vue review.

Mitigation: Do not provide API keys, credentials, or sensitive project data unless the publisher provides clearer operational boundaries and the task requires those secrets.

Risk: Server security evidence marks the release as suspicious and under-scoped.

Mitigation: Run the skill in a least-privilege sandbox and inspect generated commands, configuration, and code before applying them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/vue)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose code edits, configuration changes, and command execution steps through the host agent.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
