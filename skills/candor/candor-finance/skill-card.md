## Description:

Use Candor for personal finance: organize the user's accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with a signed-in Candor workspace for personal-finance review, record organization, follow-up, budgeting, goals, subscriptions, savings investigations, and evidence-backed next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through sensitive personal-finance records and reversible Candor workspace updates.

Mitigation: Install it only for intended Candor personal-finance work, and review financial findings, transaction rules, budget changes, goal changes, imports, and monitoring cadence before relying on them.

Risk: Account access, credential repair, subscription changes, and payments involve sensitive user controls.

Mitigation: Keep credentials, payment details, and verification codes out of chat; complete account and payment actions only on secure Candor pages or exact safe URLs returned by Candor.

Risk: Financial, tax, insurance, benefit, and investment conclusions can be wrong if based on stale, incomplete, or inapplicable records.

Mitigation: Use the skill's evidence checks, coverage limits, current authoritative sources when required, and explicit user authority before external actions or value-laden financial decisions.

## Reference(s):

- [Candor start page](https://candor.money/START.md?v=0.1.34)
- [ClawHub skill page](https://clawhub.ai/candor/skills/candor-finance)
- [Monitoring recipes](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and the Candor CLI or bundled Candor tools.]

## Skill Version(s):

0.1.34 (source: ClawHub release metadata; skill frontmatter metadata.version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
