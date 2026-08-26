## Description:

Generates evidence-constrained keyword and content-opportunity decisions using SignalDig's Decision MCP, with qualitative confidence, counter-evidence, conditions, risks, and a next validation test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT

## Use Case:

Content strategists, growth teams, and SEO practitioners use this skill to decide whether or how to prioritize a keyword opportunity. It requires the SignalDig Decision MCP and a SignalDig API key, and it returns bounded recommendations from traceable keyword evidence rather than finished content or final business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the workflow sends the keyword, domain, market, language, and related decision context to SignalDig's hosted MCP service.

Mitigation: Use the skill only when that hosted service is intended for the decision workflow, and avoid submitting sensitive context that should not leave the user's environment.

Risk: The workflow depends on a SignalDig API key.

Mitigation: Protect the API key like any other secret and configure it only in the MCP client or environment intended to run the workflow.

Risk: Keyword evidence can be incomplete, partial, or insufficient for a costly content investment.

Mitigation: Keep recommendations bounded by the returned evidence, disclose missing coverage, and use the next validation test before committing to expensive or hard-to-reverse actions.

## Reference(s):

- [SignalDig homepage](https://signaldig.com/)
- [ClawHub skill page](https://clawhub.ai/jerrykik/skills/decide-content-opportunities)
- [Setup guide](references/setup-guide.md)
- [Decision MCP contract](references/mcp-contract.md)
- [Evidence evaluation](references/evidence-evaluation.md)
- [Confidence rubric](references/confidence-rubric.md)
- [Content decision template](references/content-decision-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown decision report with recommendation, decision basis, confidence, counter-evidence, risks, next test, and source job details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision claims should cite real SignalDig request IDs and evidence IDs; the skill does not produce finished content or execute business actions.]

## Skill Version(s):

1.4.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
