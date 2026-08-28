## Description:

ClawVision East Edition is a Chinese local export skill that reads selected OpenClaw session history, summarizes it with a local LLM, and writes HTML, Markdown, PowerPoint, and PNG summary files to local disk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill when they explicitly want to turn a selected conversation into a local visual summary and export package. It is intended for local session review, sharing, and presentation workflows where the user controls the chosen session and output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected session history can contain secrets, credentials, personal data, or internal identifiers that may be included in local exports.

Mitigation: Use the skill only after confirming the intended session and scope; avoid sensitive chats unless the generated files are reviewed before sharing.

Risk: The skill writes local export files and uses local execution to render visual outputs.

Mitigation: Install and run it only when local file writes and the disclosed rendering workflow are acceptable for the target workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision-ee)
- [Project homepage](https://github.com/monaxamo/clawvision-ee)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance plus local HTML, PNG, Markdown, and PowerPoint export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written to local paths selected or confirmed during the skill workflow.]

## Skill Version(s):

1.0.8 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
