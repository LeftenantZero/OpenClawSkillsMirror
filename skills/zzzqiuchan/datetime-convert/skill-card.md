## Description:

Converts dates and times between epoch values, common date formats, time zones, spreadsheet serial numbers, natural-language expressions, date arithmetic, and duration calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzzqiuchan](https://clawhub.ai/user/zzzqiuchan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, support staff, and other agent users use this skill to convert timestamps and date strings, shift time zones, compute date arithmetic, and normalize lists of time values without hand-calculating time math.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Naive date strings can be interpreted in the wrong timezone, causing off-by-hours answers.

Mitigation: Pass an explicit input timezone when the source timezone matters and include the output timezone in the response.

Risk: Ambiguous numeric or slash-formatted dates can be read as the wrong unit or calendar format.

Mitigation: Use the helper's parsed-as notes, force a timestamp unit when needed, and surface ambiguity instead of silently choosing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zzzqiuchan/skills/datetime-convert)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, guidance]

**Output Format:** [Markdown text with optional shell command snippets or JSON output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include timezone labels, parsed-as notes, and ambiguity warnings for date or timestamp inputs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
