## Description:

Helps agents set up isolated workspaces for feature work using native workspace tools or a git worktree fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when starting feature work that should be isolated from the current workspace. Users should inspect and approve any proposed shell commands before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is command-capable while its operating scope is broad and vague.

Mitigation: Inspect and approve each command before execution, and run it in an isolated workspace with least-privilege permissions.

Risk: The artifact references API keys and credentials without a narrow, explained need.

Mitigation: Do not provide API keys or credentials unless the publisher narrows the requirement and there is a concrete need.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/using-git-worktrees)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured status or result objects when the artifact request format is used.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
