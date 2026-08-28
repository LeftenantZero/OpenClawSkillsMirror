## Description:

Check the trust rating of any x402 service before paying it, and of any skill before installing it. Free JSON, daily, sybil-resistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladaf](https://clawhub.ai/user/aladaf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to check external trust ratings before paying x402 endpoints or installing skills. It helps decide whether to proceed, limit spend, ask the user, or avoid an unknown or low-rated target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trust lookups disclose the checked host or skill slug to the rating provider.

Mitigation: Use the skill only when sharing that target with the rating provider is acceptable for the task.

Risk: Optional deeper checks may spend small x402 amounts through the user's wallet.

Mitigation: Run paid history or audit endpoints only when explicitly requested and after confirming the expected cost.

Risk: Ratings are external trust signals and do not guarantee service quality or safety.

Mitigation: Treat ratings as one input to the decision and continue applying the skill's threshold policy before payment or installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/aladaf/skills/x402-trust-check)
- [Agent Economy Report service ratings](https://agenteconomy.report/s/)
- [Agent Economy Report rating policy](https://agenteconomy.report/s/policy)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown with inline shell commands and concise risk guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference JSON rating fields returned by the external rating service.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
