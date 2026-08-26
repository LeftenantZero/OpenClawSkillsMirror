## Description:

Helps agents use Chinese-language interactions to query and manage Linear issues, projects, and team workflows for planning and progress tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, independent builders, and team operators use this skill to inspect Linear issues, manage projects, create tasks, and track workflow status. It is not intended for personnel performance evaluation or non-Linear project management platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad command and file-changing authority without clear limits on what changes it may make.

Mitigation: Review before installing, avoid broad command or file-write authority, and require confirmation before operations that create or modify issues or projects.

Risk: Linear access could affect real project data if an over-scoped credential is provided.

Mitigation: Use a narrowly scoped Linear token and grant only the permissions needed for the intended task.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with optional shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or perform Linear issue and project operations when the host agent grants credentials and tool access.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
