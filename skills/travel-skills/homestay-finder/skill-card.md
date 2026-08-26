## Description:

特色民宿 helps agents search and recommend distinctive homestays and guesthouses in China using structured filters or natural-language requests, returning prices, ratings, addresses, images, and booking links from travel platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to find domestic China homestays, guesthouses, and boutique lodging by destination, attractions, dates, budget, or preference text. It supports search and recommendation workflows but does not complete bookings directly.

### Deployment Geography for Use:

Global; lodging coverage is currently primarily within China.

## Known Risks and Mitigations:

Risk: The skill sends destinations, dates, search terms, and preference text to cloud proxy services and downstream travel platforms.

Mitigation: Avoid entering sensitive personal details beyond what is needed for lodging search, and install only if this external data flow is acceptable.

Risk: Prices, availability, ratings, images, and booking links can change on the travel platforms after the skill returns results.

Mitigation: Verify current details and total cost on the linked booking platform before making travel decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/homestay-finder)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with lodging names, prices, ratings, addresses, source labels, booking links, images, and follow-up travel prompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns up to 15 deduplicated lodging results for structured search; recommendation output depends on the upstream travel platform response.]

## Skill Version(s):

1.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
