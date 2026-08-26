## Description:

元真 yotta-humanize helps agents detect and rewrite Chinese text with common AI-style phrasing using deterministic rules, wordlists, and statistical rhythm metrics while preserving facts, named entities, intent, and tone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and content editors use this skill to score, analyze, report on, suggest edits for, and deterministically rewrite Chinese drafts that contain AI-style wording. It is intended for text-level style editing and review, not for creating new content or changing factual claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing globally may make the skill available to multiple agents beyond the user's immediate target.

Mitigation: Install only into intended skill directories and use global installer mode only when shared availability is desired.

Risk: Deterministic rewrite rules can delete boilerplate or change wording in ways that need human editorial judgment.

Mitigation: Review rewritten output, fix lists, and scores before using the edited text, especially for factual, legal, or brand-sensitive content.

Risk: The AI-style score is a style signal and should not be treated as definitive proof of text origin.

Mitigation: Use the score as a review aid and preserve the author's facts, data, named entities, intent, and tone during any follow-up edits.

## Reference(s):

- [24 类检测规则目录](references/patterns.md)
- [评分公式与统计量](references/scoring.md)
- [确定性改写规则](references/rewriting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, Markdown reports, JSON analysis, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes AI-style scores, findings, rewrite suggestions, deterministic rewritten text, fix lists, and CI gate exit codes.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
