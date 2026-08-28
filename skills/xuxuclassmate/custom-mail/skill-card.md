## Description:

Run the Custom Mail Brevo console locally with Docker — compose, preview, attachments, and send history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuxuclassmate](https://clawhub.ai/user/xuxuclassmate)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run a private Docker-based Brevo mail console, configure required secrets, preview messages, attach files, and inspect send history before using or deploying Custom Mail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the wrong Docker image or repository could execute software the user did not intend to trust.

Mitigation: Verify the Docker image or GitHub repository before installing or running the console.

Risk: Weak console credentials can expose the local mail console to unauthorized access.

Mitigation: Set a strong ADMIN_PASSWORD before starting the container.

Risk: The Brevo API key is a sending credential that can be exposed through prompts, logs, shell history, or shared files.

Mitigation: Treat BREVO_API_KEY as a secret, avoid pasting real keys into shared prompts or logs, and prefer protected local secret storage or environment files.

## Reference(s):

- [Custom Mail GitHub Repository](https://github.com/InnoNestX/Custom-Mail)
- [Custom Mail Documentation](https://innonestx.github.io/Custom-Mail/)
- [Custom Mail Docker Hub Image](https://hub.docker.com/r/xuxuclassmate/custom-mail)
- [Custom Mail ClawHub Page](https://clawhub.ai/xuxuclassmate/skills/custom-mail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker run, Docker Compose, environment variable, health check, and deployment commands.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
