## Description: <br>
知识捕获工具（免费版） helps capture knowledge from conversations and meeting notes by extracting key points, action items, and structured summaries for personal knowledge management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users use this skill to turn conversations, meeting notes, and discussion text into structured knowledge records, summaries, decisions, and action items. It is aimed at lightweight personal knowledge management and daily note capture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read, write, and exec authority while processing conversation content. <br>
Mitigation: Review requested actions before execution, limit file and workspace access, and require explicit approval before shell commands, package installs, exports, callbacks, or modify/delete operations. <br>
Risk: Captured conversations may contain secrets or confidential information, and the artifact does not define clear storage, destination, or deletion safeguards. <br>
Mitigation: Use only with content approved for processing, redact sensitive data first, and confirm the output destination and retention expectations before saving. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-capture-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown and structured JSON-style responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include extracted topics, decisions, action items, references, status fields, logs, and configuration examples.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
