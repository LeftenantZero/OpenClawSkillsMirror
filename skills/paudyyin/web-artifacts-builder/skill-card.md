## Description: <br>
Build elaborate multi-component HTML artifacts using React, Tailwind CSS, and shadcn/ui. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agents use this skill to initialize React, TypeScript, Tailwind CSS, and shadcn/ui projects and bundle completed web artifacts into a single self-contained HTML file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup and bundling scripts install npm or pnpm packages and may install pnpm globally. <br>
Mitigation: Review the shell scripts before execution and run them only in a project workspace you are comfortable modifying. <br>
Risk: Troubleshooting or rebuild steps can remove generated dependency files such as node_modules and package-lock.json. <br>
Mitigation: Keep source changes under version control and confirm the target project directory before running cleanup or reinstall commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/web-artifacts-builder) <br>
- [shadcn/ui components](https://ui.shadcn.com/docs/components) <br>
- [Tailwind CSS documentation](https://tailwindcss.com/docs) <br>
- [Radix UI primitives](https://www.radix-ui.com/themes/docs/overview/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a configured frontend project and a bundled single-file HTML artifact when its scripts are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
