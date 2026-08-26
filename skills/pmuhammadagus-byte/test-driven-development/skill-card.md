## Description:

Guides an agent to implement features, bug fixes, refactoring, and behavior changes by writing a failing test first, adding minimal code to pass, and refactoring while tests stay green.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill when implementing code changes that should follow strict test-driven development. It helps structure work around the red-green-refactor cycle and can scaffold pytest RED-state tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The strict TDD workflow may cause an agent to discard or rewrite implementation code that was created before a failing test.

Mitigation: Use this skill only where strict TDD is desired, and confirm before applying its discard-and-rewrite rule to existing user-authored changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/test-driven-development)
- [Writing Good Tests](writing-good-tests.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create pytest test scaffold files when the bundled helper script is used.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
