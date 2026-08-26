## Description:

元盾 yotta-guardian is a deterministic, cross-agent tool-call guardrail that evaluates exec, write, edit, read, run, and shell actions before execution and returns safety verdicts, matched rules, and audit records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to pre-check potentially dangerous commands, sensitive file writes, system configuration edits, and similar high-impact tool calls before an agent executes them. It helps agents report allow or deny decisions with rule IDs, reasons, exit codes, and optional audit logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can persistently install or overwrite the skill across many agent directories.

Mitigation: Review the installer before use and prefer installing to an explicit skill directory when broad global installation is not required.

Risk: Untrusted verifier commands or networked verifier gateways can expose command details, paths, or content previews.

Mitigation: Use only trusted verifier commands or approved gateways, and avoid sending sensitive tool-call details to untrusted services.

Risk: Audit logs may contain sensitive operational details.

Mitigation: Store audit logs in protected locations and apply the same retention and access controls used for other sensitive operational logs.

## Reference(s):

- [Rules reference](references/rules.md)
- [Policies and exit codes](references/policies.md)
- [Intent verifier protocol](references/intent-verifier.md)
- [ClawHub release page](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-guardian)

## Skill Output:

**Output Type(s):** [text, JSON, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; checker output may be plain text, JSON, Markdown reports, or JSONL audit records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts include allow or deny status, severity, matched rule IDs, reasons, exit codes, and optional audit records.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
