## Description:

Capture a session hand-off so work can resume cleanly in a new Claude session before context runs out.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to checkpoint an active project session before context is lost. It creates a structured hand-off document and a lightweight project-memory pointer so a later session can resume with concrete files, decisions, blockers, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated hand-off files can capture sensitive project context, including secrets, incident details, unreleased work, or internal reasoning.

Mitigation: Review generated hand-off files before committing, syncing, or sharing them outside the project.

Risk: A stale memory pointer can cause a future session to rely on superseded project state.

Mitigation: Remove or replace the pointer when the hand-off is completed or superseded.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/handoff)

## Skill Output:

**Output Type(s):** [markdown, text, configuration, guidance]

**Output Format:** [Markdown hand-off file plus a project-memory pointer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates dated project-local hand-off notes under .claude/handoffs/ and a pointer entry for future-session discovery.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
