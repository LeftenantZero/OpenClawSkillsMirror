## Description:

Optimizes content for AI Overviews, ChatGPT web search, Perplexity, and other AI-powered search experiences through GEO analysis of brand signals, AI crawler accessibility, llms.txt status, passage citability, and platform-specific visibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, SEO practitioners, and developers use this skill to audit public web pages for AI-search readiness and receive prioritized guidance for improving AI citations, crawler access, passage citability, and platform-specific visibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch public website data and create a local GEO-ANALYSIS.md report.

Mitigation: Run it only against intended public URLs and review the report before relying on or sharing its recommendations.

Risk: The skill may propose or generate llms.txt or other site-file changes.

Mitigation: Review any generated file before writing or replacing site assets, and treat llms.txt as optional rather than a Google ranking lever.

Risk: The skill's GEO scores and recommendations are heuristic and may depend on optional SEO tools when configured.

Mitigation: Validate high-impact recommendations against official search guidance, first-party analytics, and Search Console data before implementation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-geo)
- [Google AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google Search Central AI optimization announcement](https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing)
- [Google third-party SEO tools guidance](https://developers.google.com/search/docs/fundamentals/third-party-seo)
- [Google helpful content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google AI optimization guide synthesis](references/google-ai-optimization-guide.md)
- [llms.txt evidence-based reframe](references/llmstxt-evidence.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with optional JSON tool outputs, shell commands, configuration snippets, and llms.txt examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create GEO-ANALYSIS.md and may propose or generate llms.txt when requested; review recommendations before applying them to a site.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; skill frontmatter metadata says 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
