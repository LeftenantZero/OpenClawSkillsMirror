## Description:

Comprehensive SEO analysis for any website or business type. Full site audits, single-page analysis, technical SEO (crawlability, indexability, Core Web Vitals with INP), schema markup, content quality (E-E-A-T), image optimization, sitemap analysis, and GEO for AI Overviews/ChatGPT/Perplexity. Industry detection for SaaS, e-commerce, local, publishers, agencies. Triggers on: SEO, audit, schema, Core Web Vitals, sitemap, E-E-A-T, AI Overviews, GEO, technical SEO, content quality, page speed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and marketing teams use this skill to run website audits, page-level reviews, technical SEO checks, schema analysis, Core Web Vitals review, local SEO review, backlink analysis, and AI search readiness assessments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full audits may crawl target sites or call configured third-party SEO providers, including paid services.

Mitigation: Confirm the target URL, allowed crawling/API providers, credential availability, and whether paid DataForSEO credits may be consumed before running broad audits.

Risk: Drift monitoring can create baselines, caches, or historical comparisons for target URLs.

Mitigation: Confirm where drift baselines or caches are stored and whether the user wants ongoing monitoring before retaining comparison data.

Risk: SEO recommendations can be incomplete when credentials or provider data are unavailable.

Mitigation: Report missing credentials and the data they unlock instead of implying unavailable SEO, analytics, or backlink data was fetched.

## Reference(s):

- [ClawHub SEO skill page](https://clawhub.ai/asale-ai/skills/seo)
- [Backlink Quality Scoring Methodology](references/backlink-quality.md)
- [Core Web Vitals Thresholds](references/cwv-thresholds.md)
- [E-E-A-T Evaluation Framework](references/eeat-framework.md)
- [Free Backlink Data Sources](references/free-backlink-sources.md)
- [Local Schema Types](references/local-schema-types.md)
- [Local SEO Signals](references/local-seo-signals.md)
- [Maps API Endpoints](references/maps-api-endpoints.md)
- [Maps Free APIs](references/maps-free-apis.md)
- [Google Business Profile Checklist](references/maps-gbp-checklist.md)
- [Maps Geo-Grid](references/maps-geo-grid.md)
- [Content Quality Gates](references/quality-gates.md)
- [Schema Types](references/schema-types.md)
- [The 10-Principle Audit Synthesis Framework](references/thinking-framework.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured recommendations, inline shell commands, and generated schema or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use JSON command output when parsing SEO tool results; optional integrations depend on available credentials and user-approved provider usage.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter metadata.version is 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
