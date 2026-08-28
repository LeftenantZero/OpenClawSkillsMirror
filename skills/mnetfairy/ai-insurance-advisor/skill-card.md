## Description:

AI Insurance Advisor is a mainland China insurance assistant for coverage planning, product comparison, premium estimation, coverage-gap analysis, compliance prompts, claims questions, social copy, sales training scripts, and agent sales support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to discuss insurance needs, compare bundled product data, estimate premiums, design coverage plans, and receive Chinese-language insurance guidance. Insurance agents may also use it to draft social posts, training scripts, and compliant customer-facing explanations.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance recommendations, premiums, product availability, exclusions, or sales-channel fit may be incorrect or outdated.

Mitigation: Verify product details with licensed insurance professionals or insurers before making purchase, renewal, cancellation, or claims decisions.

Risk: The skill may ask for sensitive personal, health, family, and financial context during insurance needs analysis.

Mitigation: Collect only the minimum information needed, obtain user consent, and avoid retaining or sharing sensitive details outside the insurance consultation workflow.

Risk: A contact flow can point users to a named insurance sales company after the user asks for contact information.

Mitigation: Present contact information only after explicit user interest, keep the choice optional, and encourage comparison across licensed multi-company insurance agencies or brokerages.

## Reference(s):

- [Insurance product database](references/products.json)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Chinese-language Markdown guidance and structured JSON from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled static insurance reference data and calculators; product availability, premiums, exclusions, and sales-channel suitability require independent verification.]

## Skill Version(s):

2.0.59 (source: ClawHub release metadata and products metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
