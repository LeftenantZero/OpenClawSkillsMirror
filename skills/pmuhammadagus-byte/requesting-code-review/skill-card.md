## Description:

Dispatches a code reviewer subagent with focused implementation context, git ranges, and review criteria before major changes are merged or extended.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to request structured review of completed code changes against requirements, quality, architecture, testing, and production-readiness expectations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review requests may expose sensitive diffs, requirements, or private project context to a subagent.

Mitigation: Send only focused review context and redact secrets or unnecessary private details before requesting review.

Risk: Reviewer findings can be incomplete or incorrect.

Mitigation: Treat findings as advisory and verify critical or important feedback against the code, requirements, and tests before acting or merging.

Risk: A review workflow could disturb the working tree if the reviewer ignores read-only constraints.

Mitigation: Use read-only git inspection commands for review and create a separate temporary worktree when another revision must be inspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/requesting-code-review)
- [Code Reviewer Prompt Template](code-reviewer.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and review prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes placeholders for implementation description, requirements or plan, base SHA, and head SHA.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
