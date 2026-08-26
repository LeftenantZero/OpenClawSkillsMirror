## Description:

元史 yotta-logs helps agents search and analyze local JSONL conversation logs to recover prior context, decisions, messages, tool usage, and statistics without modifying logs or uploading them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent users use this skill to locate prior conversations, inspect original log excerpts, verify when decisions were made, and summarize local session activity. It is intended for read-only local log retrieval with default redaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can search sensitive local conversation logs and may expose private snippets in the agent context.

Mitigation: Keep redaction enabled, pass a narrow --dir with session/date filters where possible, and avoid sharing retrieved log output externally.

Risk: Security evidence notes review concerns because the skill can read outside the chosen log directory.

Mitigation: Review before installing, run in a least-privilege environment, and provide only trusted explicit log directories.

Risk: Global installation can make local log-search capability available across multiple agent environments.

Mitigation: Install only for the specific agent or project that needs it unless broad availability is intentional.

## Reference(s):

- [CLI protocol](references/cli.md)
- [Session log format](references/format.md)
- [Security boundaries](references/security.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-logs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, JSON]

**Output Format:** [Markdown guidance with inline shell commands; CLI results may be plain text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output redacts suspected secrets unless explicitly disabled.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
