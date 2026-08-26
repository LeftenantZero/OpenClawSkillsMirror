## Description:

TDD guides agents through test-driven coding and bug fixing with a Red-Green-Refactor workflow, test execution process, and test design strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to apply test-first workflows when fixing bugs, adding behavior, designing unit tests, and reporting test execution results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation triggers and mandatory first-action behavior may cause an agent to enter the TDD workflow before the user clearly requests it.

Mitigation: Enable or invoke the skill only for explicit TDD, bug-fix, or test-run requests; narrow trigger wording where possible.

Risk: The workflow can lead to creating tests, running broad test suites, or preparing commits in sensitive repositories.

Mitigation: Require user confirmation before commits or broad test execution, and report the selected test scope and results clearly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/tdd)
- [TDD Cycle](artifact/cycle.md)
- [Test Run](artifact/run.md)
- [Test Strategies](artifact/test-strategies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide test authoring, test execution, result reporting, and commit timing within the agent workflow.]

## Skill Version(s):

0.3.3 (source: server release metadata and changelog, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
