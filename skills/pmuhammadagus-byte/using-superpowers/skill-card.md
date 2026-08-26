## Description:

Guides an agent to use advanced capabilities, tools, skills, and integrations safely and deliberately for a relevant user task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to steer an AI agent toward evidence-first reasoning, tool selection, verification, recovery, and safety practices when a task calls for advanced agent capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill provides broad agent workflow and tool-use discipline, which can affect how an agent selects tools and proceeds through a task.

Mitigation: Install only when a general-purpose agent workflow and safety discipline skill is desired, and review the skill before deployment.

Risk: The optional router script reads local skill descriptions from a configured skills directory.

Mitigation: Point the router only at skill folders that are appropriate for the agent to inspect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/using-superpowers)
- [Antigravity CLI tool mapping](artifact/references/antigravity-tools.md)
- [Codex tool mapping](artifact/references/codex-tools.md)
- [Gemini CLI tool mapping](artifact/references/gemini-tools.md)
- [Pi tool mapping](artifact/references/pi-tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with inline code, shell commands, and configuration snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task plans, verification notes, recovery steps, and tool-specific instructions.]

## Skill Version(s):

1.0.4 (source: evidence.json release.version and metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
