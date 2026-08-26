## Description:

Figma API integration with managed OAuth for reading design files, nodes, version history, rendered images, comments, reactions, and published components or styles from file and team libraries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to inspect Figma files, export node images, review comments, and audit design-system assets through Maton's managed Figma connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires trusting Maton as the gateway for a user's Figma account.

Mitigation: Install only when Maton is an acceptable gateway, review OAuth scopes during connection, and prefer read-only access when possible.

Risk: Writes such as posting or deleting comments can affect shared Figma files and notify collaborators.

Mitigation: Require exact user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: Multiple Maton or Figma connections can cause requests to target the wrong account or workspace.

Mitigation: Specify the intended connection when multiple accounts or connections exist and verify account context before changing shared files.

## Reference(s):

- [ClawHub Figma Skill](https://clawhub.ai/maton/skills/figma)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Figma REST API Introduction](https://developers.figma.com/docs/rest-api/)
- [Figma File Endpoints](https://developers.figma.com/docs/rest-api/file-endpoints/)
- [Figma Comment Endpoints](https://developers.figma.com/docs/rest-api/comments-endpoints/)
- [Figma Component Endpoints](https://developers.figma.com/docs/rest-api/component-endpoints/)
- [Figma Dev Resource Endpoints](https://developers.figma.com/docs/rest-api/dev-resources-endpoints/)
- [Figma Rate Limits](https://developers.figma.com/docs/rest-api/rate-limits/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, a user-provided Figma file URL, and explicit confirmation before write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
