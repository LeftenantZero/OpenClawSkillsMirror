## Description: <br>
面向 IRIS 开发者的 ObjectScript 代码格式化与基础规范检查工具。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers working with InterSystems IRIS or Cache use this skill to format ObjectScript code and perform basic style, naming, lock, transaction, and comment checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to edit files or run validation commands while reviewing IRIS/ObjectScript code. <br>
Mitigation: Review proposed changes and commands before execution, especially in repositories with production code. <br>
Risk: IRIS server credentials may be unnecessary for routine formatting and review tasks. <br>
Mitigation: Avoid providing IRIS server credentials unless the specific task requires a live connection. <br>
Risk: The artifact contains broad capability wording that could be interpreted beyond markdown-only formatting guidance. <br>
Mitigation: Scope use to ObjectScript formatting, style review, and basic compliance checks unless additional evidence supports broader behavior. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with code snippets and optional structured JSON-style result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file edits or validation commands; review outputs before applying changes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
