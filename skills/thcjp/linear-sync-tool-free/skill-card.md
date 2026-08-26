## Description: <br>
Linear同步工具免费版 helps an AI agent use the Linear CLI to list and view issues, create basic issues, and inspect teams and projects for project-management workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project contributors use this skill to manage day-to-day Linear work from an agent-driven command line flow, including issue lookup, basic issue creation, team review, and project status checks. It is not intended for personnel performance evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated Linear CLI use can create persistent issues in a Linear workspace. <br>
Mitigation: Require an explicit command preview and user confirmation before running any issue creation command. <br>
Risk: A broad Linear API key can grant more workspace access than the skill needs. <br>
Mitigation: Use a least-privilege Linear API key and avoid storing credentials in source files or shared configuration. <br>
Risk: The skill can be invoked outside its intended Linear project-management context if activation is too broad. <br>
Mitigation: Restrict use to Linear-specific requests for issue, team, and project management. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/linear-sync-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown with inline Linear CLI commands and JSON-style command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Linear CLI commands, configuration guidance, status summaries, execution logs, and error recovery guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
