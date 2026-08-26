## Description:

YouTube Full helps agents search YouTube, browse channels and playlists, and fetch transcripts or metadata through TranscriptOut for video research and summarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs YouTube search results, channel or playlist listings, video metadata, or transcripts for research, summarization, quotation, translation, and monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube searches, channel or playlist identifiers, selected video IDs, and transcript requests are sent to TranscriptOut.

Mitigation: Use the skill only when that sharing is acceptable, and avoid sensitive research queries unless the user has approved the request.

Risk: The setup flow asks the agent to handle signup codes and persist a TranscriptOut API key.

Mitigation: Create the account and key in a browser when possible, store the key in a scoped secret manager, and avoid placing it in a broad persistent shell environment.

Risk: Bulk transcript jobs can submit many videos and spend credits quickly.

Mitigation: Require confirmation before bulk jobs and use bounded channel or playlist selections rather than transcribing large result sets by default.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/artemchuikin/skills/youtube-full)
- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API Documentation](https://transcriptout.com/docs)
- [TranscriptOut Auth Setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with curl commands and JSON or text API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY; TranscriptOut endpoints may consume account credits depending on the request.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
