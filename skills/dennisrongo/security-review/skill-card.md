## Description:

Performs defensive, attacker-minded security reviews of diffs, branches, or modules against a fixed vulnerability catalog and requires concrete attack paths for findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review code they own or are authorized to audit before shipping trust-boundary changes such as endpoints, auth, file handling, payment paths, or user-generated content rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read scoped source files and suggest dependency-audit commands when relevant.

Mitigation: Install it only for defensive reviews of code the user owns or is authorized to audit, and keep the review scope explicit.

Risk: Security-review reports can overstate assurance if coverage is unclear.

Mitigation: Require reports to list checked vulnerability classes, unchecked areas, and avoid claims beyond the reviewed evidence.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown security review report with findings, coverage notes, and occasional command output excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are ranked by severity and include file:line evidence, attack path, recommended fix direction, and explicit unchecked areas.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
