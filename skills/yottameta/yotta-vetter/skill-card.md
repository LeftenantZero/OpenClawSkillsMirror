## Description:

Yuanshen (yotta-vetter) helps agents perform a structured pre-install security review of skills using a four-phase source, code, permissions, and risk checklist plus a lightweight checker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill before installing or evaluating unknown skills to produce a traceable initial security review, source check, and human-review report. It supports marketplace, GitHub, shared-skill, and other pre-install review scenarios where a final human decision is still required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The global installer can persist the skill into many agent environments at once.

Mitigation: Install only into the intended agent environment, preferably with --dir or a single-agent option, and avoid -g/--global unless broad installation is intentional.

Risk: The skill can read target skill directories and optionally write review reports.

Mitigation: Run it only against authorized skill directories and choose report output paths that are appropriate to store or share.

Risk: The source check can contact GitHub for public repository metadata and cache that metadata locally.

Mitigation: Use local check mode or an isolated environment when network access or local metadata caching is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [Four-phase vetting checklist](references/checklist.md)
- [Vetting report template](references/vetting-report-template.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-vetter)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Plain text reports, optional JSON output, Markdown report files, and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against a target skill directory; source checks can query public GitHub metadata and cache that metadata locally.]

## Skill Version(s):

0.1.3 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
