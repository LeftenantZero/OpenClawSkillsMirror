## Description:

Guides an agent through completing a development branch after implementation and tests are green, including environment detection, user-selected integration, and safe cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when implementation is complete and tests pass, but the branch still needs a user-controlled decision to merge locally, create a pull request, or remain as-is.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide git merge, push, pull request creation, worktree removal, or branch deletion actions.

Mitigation: Use it only in repositories where branch integration help is intended, and keep the documented test gates, option menus, and explicit confirmations in place.

Risk: Merging into the wrong base branch can be costly to undo.

Mitigation: Confirm the base branch before merging when it is not already known from the plan, conversation, or branch upstream.

Risk: Discarding work can permanently delete commits, a branch, and a worktree.

Mitigation: Proceed with discard only after the user explicitly requests it and types the exact confirmation word.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/finishing-a-development-branch)
- [ClawHub publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with command blocks and user choice menus]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before integration decisions and destructive branch cleanup.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
