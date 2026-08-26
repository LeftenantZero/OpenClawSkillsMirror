## Description:

Helps an agent verify code, build, or deployment work with fresh evidence before claiming completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to require fresh verification evidence before an agent claims that code, build, deployment, or task work is complete. It also provides a helper script that can run configured local checks and save a JSON evidence log.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script runs commands from a local verify.json file, so unsafe or unintended commands could execute locally.

Mitigation: Review verify.json before running the helper script and only include verification commands appropriate for the current workspace.

Risk: The evidence file may capture command output that contains secrets, credentials, or other sensitive data.

Mitigation: Review generated evidence before sharing it, and redact or avoid commands that print secrets or sensitive personal data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/verification-before-completion)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with optional shell commands and JSON evidence logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper script reads verify.json command lists and writes verification-evidence.json with exit codes and command output.]

## Skill Version(s):

1.0.5 (source: server release metadata and metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
