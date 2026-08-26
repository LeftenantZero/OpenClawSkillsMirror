## Description:

Helps developers evaluate code review feedback before implementing changes, especially when feedback is unclear or technically questionable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to triage code review comments, decide which suggestions are technically sound, and identify feedback that needs verification before code changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read and execution authority could expose files or run commands outside the intended code-review workflow.

Mitigation: Require explicit per-action confirmation and review each proposed command or file access before allowing execution.

Risk: Credential and API workflows are described without precise endpoints, data flows, or a bounded purpose.

Mitigation: Do not provide API keys or credentials unless the publisher supplies a clear endpoint, data-handling path, and limited workflow.

Risk: Server-resolved source provenance is unavailable for this version.

Mitigation: Review the ClawHub release page, publisher profile, and packaged artifact before installation or use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/receiving-code-review)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown or structured JSON guidance, depending on the agent workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review triage, verification steps, suggested edits, commands, and configuration notes.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
