## Description:

Helps agents evaluate code review feedback before acting by reading feedback fully, verifying claims against the codebase, clarifying ambiguity, and implementing accepted fixes one item at a time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when receiving review comments to verify technical claims, identify unclear feedback, decide when to push back, and implement accepted fixes carefully.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Malformed routing metadata may cause the skill to trigger less precisely than intended.

Mitigation: Use the skill for code-review feedback workflows and confirm that its guidance is relevant before applying it to a task.

Risk: The workflow can slow down straightforward fixes if clear and correct feedback is treated as ambiguous.

Mitigation: For clear, correct feedback, verify briefly and implement directly, as the skill's own usage guidance allows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/receiving-code-review)
- [Publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown guidance with optional code blocks and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an optional Python helper that classifies review comments from a JSON file.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
