## Description: <br>
Creates, modifies, and optimizes agent skills with eval testing, benchmark analysis, and description optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to draft new skills, improve existing skills, design evals, compare results, refine descriptions, and package completed skill releases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create and modify local skill files and temporary Claude command entries. <br>
Mitigation: Use it only in a workspace where those file changes are acceptable, and review generated files before installing or publishing a skill. <br>
Risk: Evaluation and description-optimization workflows may run multiple Claude CLI invocations using the current user's Claude Code authentication. <br>
Mitigation: Run eval loops only with the intended account and model, and confirm expected cost, access, and prompt contents before large runs. <br>
Risk: The default eval viewer server path can terminate another local service on the selected port. <br>
Mitigation: Prefer static viewer output in headless or shared environments, or choose an unused port before starting the viewer. <br>
Risk: Rendered eval outputs, including spreadsheets and HTML reports, may contain untrusted content. <br>
Mitigation: Treat generated review artifacts as untrusted and inspect them before opening, sharing, or relying on their contents. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/skill-creator) <br>
- [JSON Schemas](references/schemas.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with code blocks, JSON schemas, generated eval reports, and packaged skill files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify skill files, eval workspaces, HTML review reports, benchmark JSON/Markdown, and .skill packages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter; package.json reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
