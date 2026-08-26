## Description: <br>
Create quick, disposable terminal or UI prototypes to validate specific design decisions, then discard them or merge the validated decisions into real work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product builders use this skill when they need an agent to create a short-lived prototype that answers a focused logic, state, interaction, or UI design question before committing to production implementation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words such as prototype or demo may invoke the skill for work that does not actually need a prototype. <br>
Mitigation: Confirm the specific decision or question to validate before creating files. <br>
Risk: Generated prototype files may be mistaken for production-ready code. <br>
Mitigation: Use explicit prototype, spike, or explore naming and delete the files or merge only the validated decision after review. <br>
Risk: Prototype code may intentionally skip tests, full error handling, and production hardening. <br>
Mitigation: Treat outputs as temporary learning artifacts and perform normal review, testing, and hardening before any production use. <br>
Risk: Prototype work can touch data paths if a validation question involves persistence or external integration. <br>
Mitigation: Use mock data, scratch databases, or clearly disposable local files, and review before connecting to real data. <br>


## Reference(s): <br>
- [Prototype patterns](references/prototype-patterns.md) <br>
- [Rapid validation methods](references/rapid-validation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Markdown] <br>
**Output Format:** [Markdown guidance with inline code examples and command suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prototype artifacts should be temporary, clearly named, and reviewed before keeping, committing, or connecting to real data.] <br>

## Skill Version(s): <br>
2.1.0 (source: release evidence, package.json, SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
