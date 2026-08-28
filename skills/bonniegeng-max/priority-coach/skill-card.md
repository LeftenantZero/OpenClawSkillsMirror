## Description:

Priority Coach Publish is a gentle personal priority-coaching skill that helps users narrow messy priorities into one to three current focuses and a small action they can start today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for conversational priority coaching when they feel busy, unclear, overloaded, or need to restart after a break. It routes the conversation into lightweight flows for selecting priorities, planning today's first action, starting work, wrapping up, checking habits, reviewing longer-term direction, or reducing load.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional local records may contain personal priorities, session summaries, or sensitive context.

Mitigation: Install only if comfortable with a local journal; save deliberately, avoid saving sensitive raw answers unless necessary, and use the provided delete and export commands to manage records.

Risk: Users may treat priority coaching as decision-making, medical, mental-health, or crisis support.

Mitigation: Keep the skill within prioritization and planning support; for self-harm, violence, severe medical, or serious mental-health crisis signals, stop ordinary coaching and encourage trusted local or professional support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [README](README.md)
- [Router reference](references/router.md)
- [State scripts reference](references/states.md)
- [Cold start reference](references/cold-start.md)
- [Daily flows reference](references/daily-flows.md)
- [Mainline review reference](references/review.md)
- [Memory schema reference](references/memory-schema.md)
- [Copy tone reference](references/copy-tone.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown coaching cards with optional inline shell commands for local record management]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create optional local JSON records only after explicit user consent.]

## Skill Version(s):

0.3.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
