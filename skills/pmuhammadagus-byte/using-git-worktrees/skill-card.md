## Description:

Helps an agent isolate git work in a separate worktree so the main working tree is not disturbed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when starting feature work that should be isolated from the current branch. It guides detection of existing isolation, preference for native worktree tools, fallback git worktree creation, setup, and baseline verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may update .gitignore and create a commit before making a project-local worktree.

Mitigation: Review the proposed ignore rule and commit before allowing repository history changes.

Risk: The workflow may run dependency installation or baseline tests that affect the local environment.

Mitigation: Confirm setup and test commands before execution when tighter control over the local environment is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/using-git-worktrees)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose git worktree commands, dependency installation, baseline test commands, and user confirmation prompts.]

## Skill Version(s):

1.0.6 (source: server release evidence and metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
