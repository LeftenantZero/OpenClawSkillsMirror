## Description:

A bilingual R-based meta-analysis assistant for clinical researchers that helps plan systematic reviews, run pairwise and network meta-analyses, generate figures, and provide reproducible R code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External clinical researchers, medical and statistical teams, and evidence-based medicine learners use this skill to choose review topics, prepare study data, run common and advanced meta-analysis workflows, and present results with reproducible code and figures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analysis summary data, hostname-derived hashes, locale, and explicitly chosen IPD or cloud inputs may be sent to listed Coze services.

Mitigation: Use only data approved for that cloud transfer, and avoid confidential or regulated patient-level data unless the deployment has been independently approved.

Risk: Bug reports include user-controlled free text that can accidentally contain sensitive details.

Mitigation: Review and sanitize bug-report descriptions before sending them.

Risk: Cloud computation is the sole numerical analysis path, so service outages or authorization failures can prevent curated calculations.

Mitigation: Treat cloud failure responses as unavailable analysis results and do not rely on uncurated fallback text for clinical or regulatory decisions.

Risk: The release bundles shared service tokens for the cloud workflow.

Mitigation: Review endpoint approval and credential handling before deploying the skill in a controlled environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/meta-analysis)
- [Project homepage](https://github.com/medstatstar/meta-analysis)
- [English README](https://github.com/medstatstar/meta-analysis/blob/main/README.md)
- [Chinese README](https://github.com/medstatstar/meta-analysis/blob/main/README_zh-CN.md)
- [Advanced API reference](references/advanced_api.md)
- [Interactive analysis menu](references/interactive_menu.md)
- [Topic selection workflow](references/topic-selection.md)
- [Inline rendering reference](references/inline_rendering.md)
- [Data templates reference](references/data_templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown conversation responses with inline SVG figures, generated analysis files, reproducible R code, CSV backups, and optional HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include analysis_complete.R, results_summary.md, SVG or PNG figures, data_backup.csv, and HTML reports in the current workspace.]

## Skill Version(s):

2.1.9 (source: frontmatter, parsed metadata, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
