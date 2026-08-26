## Description:

Retrieves traceable keyword, search result, trend, GEO, competitor, and backlink data for SEO research and analysis via SignalDig.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, growth teams, and developers use this skill to request scoped, evidence-linked SEO research for keywords and domains through SignalDig, including keyword metrics, related keywords, SERP observations, trends, competitor analysis, GEO visibility, and backlinks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SignalDig API keys can grant account access if exposed.

Mitigation: Configure keys through the client or environment secret mechanism and do not commit or paste them into shared files.

Risk: SEO queries, target domains, market, language, and related request metadata are sent to SignalDig during use.

Mitigation: Use the smallest sufficient data scope and confirm the user is comfortable sending the target research metadata to SignalDig.

Risk: The skill cannot produce live SEO evidence when the SignalDig MCP server, tools, or account plan are unavailable.

Mitigation: Verify the MCP connection before research and stop rather than fabricating metrics or evidence.

Risk: Duplicate or overly broad live requests can waste account quota or return more data than needed.

Mitigation: Reuse prior request_id values and stable idempotency keys, and request only the specific SEO data families needed for the task.

## Reference(s):

- [Setup Guide: Connect the SignalDig SEO MCP Server](references/setup-guide.md)
- [SEO Research Functional Contract](references/mcp-contract.md)
- [SignalDig](https://signaldig.com/)
- [ClawHub Skill Page](https://clawhub.ai/jerrykik/skills/research-seo-signals)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Concise Markdown report with evidence IDs, limitations, and source request_id.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured SignalDig MCP server and API key; default depth is concise unless a full export is requested.]

## Skill Version(s):

1.5.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
