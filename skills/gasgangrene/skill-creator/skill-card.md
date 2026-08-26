## Description: <br>
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agent builders use this skill to design, author, validate, package, and iterate on reusable skill packages with clear workflows, references, scripts, and assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or modified skills may contain incorrect or misleading guidance if accepted without review. <br>
Mitigation: Review generated skill content before installing, sharing, or deploying it. <br>
Risk: Initialization and packaging workflows write files and can include unintended content if pointed at the wrong workspace. <br>
Mitigation: Keep output paths scoped to the intended skill workspace and inspect packaged contents before release. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gasgangrene/skills/skill-creator) <br>
- [Workflow Patterns](references/workflows.md) <br>
- [Output Patterns](references/output-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, generated files, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create skill directories, validation output, packaged .skill archives, and configuration metadata when used by an agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
