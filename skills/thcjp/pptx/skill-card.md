## Description:

This skill helps agents create, inspect, parse, and automate processing for PPTX and POTX presentation files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they need an agent to work with PowerPoint presentation files, including creating decks, extracting content, converting data, and troubleshooting PPTX processing tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is not clearly bounded to presentation work and may steer the agent toward broad command execution, API credentials, or broad automation.

Mitigation: Use it only for explicit PPTX or POTX tasks, and require confirmation before shell commands, credential use, network services, or changes to user files.

Risk: Presentation processing can expose sensitive file contents or unsafe uploaded content.

Mitigation: Scan files before processing, limit access to necessary files, and avoid exposing extracted content, credentials, or logs beyond the user's requested scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/pptx)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON snippets, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local PPTX or POTX files and optional API credentials when the user requests automation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
