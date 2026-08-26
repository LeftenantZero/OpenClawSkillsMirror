## Description:

Netlify API integration with managed OAuth for viewing sites, deploys, builds, DNS zones, and environment variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and support agents use this skill to inspect Netlify account, site, deploy, build, DNS, webhook, form, and environment-variable state through Maton. It can guide administrative actions when the user explicitly approves the target resource and intended change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer Netlify resources with broad account impact, including DNS, environment variables, site deletion, build hooks, and webhooks.

Mitigation: Install only for Netlify administration, prefer read-only calls first, and require explicit confirmation before any POST, PUT, PATCH, or DELETE with the target account, connection, resource identifiers, and intended effect.

Risk: OAuth tokens, Maton API keys, and provider-issued tokens could be exposed if printed, logged, persisted, or passed through command arguments.

Mitigation: Use Maton OAuth and the operating system credential store where possible; never print, dump, or persist credentials, and use the documented stdin-based raw HTTP fallback only when the CLI cannot be installed.

Risk: Multiple Maton accounts or Netlify connections can make the target account ambiguous.

Mitigation: List and verify the active account and connection before changes, and specify the intended profile or connection when more than one is available.

Risk: External Netlify API data may contain untrusted content that should not direct follow-up actions.

Mitigation: Treat returned content as data, validate identifiers and payloads separately, and do not execute or interpolate API response text into shell commands.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI Documentation](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks](https://docs.netlify.com/configure-builds/build-hooks/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to read/list guidance; mutating Netlify operations require explicit user approval with specific resource identifiers.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
