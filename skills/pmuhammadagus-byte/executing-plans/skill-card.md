## Description:

Guides an agent to execute a written implementation plan step by step in the current session, with verification after each task and stop points for blockers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when a written implementation plan already exists and should be executed sequentially in the current session. It emphasizes critical plan review, per-step verification, and stopping for unclear instructions or blockers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An inaccurate or incomplete implementation plan could lead the agent to make incorrect code changes.

Mitigation: Review the plan before execution and stop for blockers, unclear instructions, or repeated verification failures.

Risk: Skipping verification could cause the agent to report progress that has not actually passed checks.

Mitigation: Require verification after each step before proceeding or marking the step complete.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code]

**Output Format:** [Markdown guidance with optional shell command prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a written plan and explicit verification before marking each step complete.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
