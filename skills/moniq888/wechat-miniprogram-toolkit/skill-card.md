## Description:

Guides agents through WeChat Mini Program full-stack development, including project initialization, cloud development, authentication, payments, live features, analytics, sharing, TypeScript, content safety, hardware APIs, performance, CI/CD, and subpackage analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moniq888](https://clawhub.ai/user/moniq888)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create, configure, optimize, and release WeChat Mini Programs with cloud services, authentication, payments, messaging, analytics, content safety, hardware integrations, and CI/CD workflows. It also provides subpackage analysis guidance for staying within WeChat package size limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples and workflows may involve payments, identity, analytics, Wi-Fi credentials, deployment, and release automation where live secrets or personal data could be exposed.

Mitigation: Use test credentials during setup, keep live merchant keys, AppSecrets, private keys, access tokens, Wi-Fi passwords, and user personal data out of prompts and source files, and move sensitive values into approved secrets managers.

Risk: The skill may propose package installation, project edits, CI/CD configuration, release submission, or skill file updates.

Mitigation: Require explicit human confirmation and code review before executing commands, changing project files, configuring automation, submitting releases, or accepting self-updates.

Risk: Copied examples may not enforce sufficient authorization, privacy controls, or least-privilege database access for a production mini program.

Mitigation: Revise generated examples to use server-side authorization, consent and privacy controls, and least-privilege database rules before production use.

## Reference(s):

- [Wechat Miniprogram Toolkit on ClawHub](https://clawhub.ai/moniq888/skills/wechat-miniprogram-toolkit)
- [WeChat Mini Program official framework documentation](https://developers.weixin.qq.com/miniprogram/dev/framework/)
- [WeChat cloud development guide](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/)
- [WeChat Mini Program subpackages](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/)
- [WeChat Skyline rendering](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/)
- [WeChat Skyline Worklet animation](https://developers.weixin.qq.com/miniprogram/dev/framework/view/skyline/worklet-animation.html)
- [WeChat WXS reference](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxs/)
- [miniprogram-ci package](https://www.npmjs.com/package/miniprogram-ci)
- [Project initialization template](references/project-init.md)
- [Cloud development guide](references/cloud-dev.md)
- [Authentication guide](references/auth.md)
- [Payment guide](references/payment.md)
- [Subpackage strategy](references/subpackage.md)
- [CI/CD guide](references/ci-cd.md)
- [Subpackage analyzer script](scripts/analyze_subpackages.py)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate project files, CI/CD workflow configuration, and app.json subpackage configuration snippets for review before use]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
