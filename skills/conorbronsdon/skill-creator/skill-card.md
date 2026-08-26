## Description: <br>
Generate a new Claude Code skill from a plain-language description, including invocation control, arguments, context cost, scaffolding, and testing guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to turn recurring tasks or slash-command ideas into Claude Code skill files with scoped invocation behavior, argument handling, concise descriptions, installation steps, and testing guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated skills can grant tools, hooks, shell execution, or persistence-related behavior if accepted without review. <br>
Mitigation: Review generated SKILL.md frontmatter and body before installation, paying particular attention to allowed-tools, hooks, shell injection, and persistent behavior. <br>
Risk: Generated skill guidance may be incorrect, overbroad, or poorly scoped for the target repository. <br>
Mitigation: Compare the generated skill against host repository conventions and test direct and model-triggered invocation before release. <br>


## Reference(s): <br>
- [Skill Creator on ClawHub](https://clawhub.ai/conorbronsdon/skills/skill-creator) <br>
- [Skill Frontmatter & Behavior Reference](reference.md) <br>
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with fenced SKILL.md examples, command snippets, and review prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local skill files when the user approves saving generated skill content.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
