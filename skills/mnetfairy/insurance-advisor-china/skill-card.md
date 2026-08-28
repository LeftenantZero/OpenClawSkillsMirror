## Description:

An AI insurance advisor for mainland China that helps individuals and families with insurance consultation, product comparison, plan design, application guidance, premium estimation, coverage-gap analysis, compliance reminders, and claims support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents serving individuals or families in mainland China use this skill to answer insurance planning questions, compare products, estimate premiums, design coverage plans, and provide compliance-oriented reminders.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: Insurance recommendations may rely on static local product data and may not reflect current insurer terms or availability.

Mitigation: Treat recommendations as informational and verify current product terms, availability, premiums, and underwriting requirements with insurers before acting.

Risk: Maintenance scripts under scripts/datafix can rewrite product data and patch skill Python files.

Mitigation: Do not run scripts/datafix unless intentionally maintaining the package; review the changes and use dry-run behavior where available before applying edits.

## Reference(s):

- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Regulatory Compliance Notes](references/compliance.md)
- [Insurance Product Database](references/products.json)
- [Insurance Database Analysis Report (2026-08-26)](references/%E4%BF%9D%E9%99%A9%E8%B5%84%E6%96%99%E5%BA%93%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A_2026-08-26.md)
- [Product Library Analysis Report (2026-08-21)](references/_repo_analysis_2026-08-21.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese natural-language guidance and Markdown tables, with JSON emitted by helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product and compliance references; helper scripts accept JSON input and print JSON results.]

## Skill Version(s):

2.0.59 (source: server release evidence; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
