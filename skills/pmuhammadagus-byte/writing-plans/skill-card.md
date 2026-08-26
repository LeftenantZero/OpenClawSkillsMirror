## Description:

Helps agents create comprehensive, task-by-task implementation plans with file maps, test steps, verification commands, and execution handoff options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agentic coding workers use this skill before multi-step implementation work to produce a complete Markdown plan that maps files, tasks, test cycles, review checks, and handoff options. It is intended for work with clear requirements where a plan should be written before code changes begin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated plans can contain incorrect, incomplete, or misleading implementation guidance.

Mitigation: Review the plan against the source requirements, run the placeholder and type-consistency checks, and execute only after verification steps are clear.

Risk: The skill may recommend subagent-based or inline execution after producing a plan.

Mitigation: Proceed with execution only after the user explicitly chooses an execution option.

Risk: The manifest description is messy and some compliance text is mixed-language.

Mitigation: Confirm the activation trigger and deployment summary during review before publishing or installing the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/writing-plans)
- [Writing Plans Skill Source](artifact/SKILL.md)
- [Plan Document Reviewer Prompt](artifact/plan-document-reviewer-prompt.md)
- [Plan Scaffolding Script](artifact/scripts/make_plan.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown implementation plans with checklists, code blocks, and verification commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write plan files under docs/superpowers/plans unless user preferences override the path.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact metadata reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
