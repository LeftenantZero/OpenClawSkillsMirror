## Description: <br>
生活助手免费版 helps individual users manage personal tasks, summarize long emails, check schedules, create reminders, and archive notes locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual users, freelancers, and independent developers use this skill to capture and break down tasks, summarize email content, detect schedule conflicts, set reminders, and maintain a local personal knowledge archive. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Personal task, email-summary, schedule, note, and reminder data may be stored under ~/.assistant. <br>
Mitigation: Use the skill only for data you are comfortable storing locally, review the ~/.assistant contents, and back up or delete local files according to your retention needs. <br>
Risk: Shell examples create and overwrite files in the user's home directory. <br>
Mitigation: Review commands before running them and execute them only in the intended user account and environment. <br>
Risk: The host agent's LLM may process content submitted for summarization or organization. <br>
Mitigation: Avoid submitting confidential or regulated content unless the configured agent and model provider are approved for that data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/lifestyle-assistant-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-shaped structured responses and inline shell, Python, and YAML examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples create and read local task, email-summary, note, reminder, and preference files under ~/.assistant.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
