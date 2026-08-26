## Description:

Audits and reduces AI agent runtime spend in dollars across OpenClaw, Hermes, QM, Claude Code, Cursor, and generic event ingest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xerg](https://clawhub.ai/user/xerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering teams, and FinOps reviewers use xerg to run local AI runtime audits, identify evidence-strict monetary waste and neutral signals, and compare compatible changes after remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xerg can inspect local agent logs, transcripts, state databases, exports, or remote audit sources that may contain sensitive operational metadata.

Mitigation: Use the local audit path first, ask before package fetches or data inspection, and run hosted activation or push only after explicit user approval.

Risk: Audit spend can be observed, locally estimated, or unpriced and is not an authoritative provider invoice.

Mitigation: Present pricing and detector coverage before spend conclusions, and avoid treating incomplete coverage or zero identified findings as proof of no waste.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xerg/skills/xerg)
- [Xerg homepage](https://xerg.ai)
- [Xerg documentation](https://xerg.ai/docs)
- [Xerg skill source](https://xerg.ai/skill.md)
- [Xerg service status](https://status.xerg.ai)
- [@xerg/cli npm package](https://www.npmjs.com/package/@xerg/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command snippets and JSON audit interpretation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local audit guidance by default; hosted pairing or push actions require explicit user approval.]

## Skill Version(s):

0.27.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
