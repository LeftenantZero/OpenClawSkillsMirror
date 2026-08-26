## Description: <br>
Executes an existing project masterplan by implementing each roadmap phase, resolving ambiguity through research, testing and self-auditing the work, and maintaining an execution log for safe resumption. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to build from an already-approved masterplan, resume work from an execution log, and complete implementation phase by phase with testing and self-audit before sign-off. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed for high-agency project execution and may modify code, configuration, logs, and commit history. <br>
Mitigation: Run it in a version-controlled workspace, review diffs and commits, and require tests or verification commands before accepting completed phases. <br>
Risk: Automatic web research during implementation can be inappropriate for confidential or restricted repositories. <br>
Mitigation: Disable web access or require confirmation before searches when working with sensitive project details. <br>
Risk: Running verification commands can affect the local environment or depend on unavailable services. <br>
Mitigation: Use an isolated development environment and review command scope before running project tests, builds, or service checks. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Execution Standards](references/execution-standards.md) <br>
- [Phase Execution Checklist](references/phase-execution-checklist.md) <br>
- [Progress Log Template](references/progress-log-template.md) <br>
- [Resource-Safe Subagent Execution](references/resource-safety.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with code, shell command, configuration, and file-change outputs as needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains or updates a repo-local execution log when executing a masterplan] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
