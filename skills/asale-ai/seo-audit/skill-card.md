## Description:

Runs a full website SEO audit that crawls up to 500 pages, detects business type, analyzes technical, content, schema, performance, and AI-readiness signals, and generates an SEO health score with prioritized recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and site operators use this skill to audit a website they are authorized to test, identify technical and content SEO issues, and produce a prioritized remediation plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can crawl many pages on a target website.

Mitigation: Run it only against URLs the user is authorized to test, respect robots.txt, and keep the configured crawl bounds in place.

Risk: The skill writes local report artifacts and may capture screenshots.

Mitigation: Review generated files before sharing them and avoid running the audit on pages containing sensitive or private information unless that handling is intended.

Risk: Optional SEO or Google integrations may use configured credentials.

Mitigation: Use least-privilege credentials and confirm which optional integrations are enabled before running an enriched audit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-audit)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance, Files]

**Output Format:** [Markdown reports with JSON audit data and optional PDF or HTML report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a domain-specific audit directory and may include per-category findings, screenshots, and report files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
