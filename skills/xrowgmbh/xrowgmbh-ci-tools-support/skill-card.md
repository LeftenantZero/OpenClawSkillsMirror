## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage eligible GitLab support issues and discussion threads for the CI Tools components catalog using public documentation, repository content, and request-provided context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support responses could be provided to requesters outside the approved domain list.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS with the intended approved domains and verify requester eligibility before responding.

Risk: Excessive GitLab permissions could expose unrelated project data or actions.

Mitigation: Grant only the GitLab permissions needed to comment, inspect relevant public support context, and apply support labels.

Risk: Private logs or customer details could be repeated in public support threads.

Mitigation: Keep issues confidential when they contain customer details, private URLs, private logs, or internal project names, and do not quote private logs into public places.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown support replies, triage labels, and concise handoff or refusal guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPPORT_TRUSTED_DOMAINS to define approved requester domains.]

## Skill Version(s):

4.181.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
