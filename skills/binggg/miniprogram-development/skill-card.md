## Description:

Guides agents through WeChat Mini Program development workflows, including project structure, debugging, preview and upload, CloudBase integration, message push, customer service auto-reply, and WeChat search optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to build, modify, debug, preview, upload, and optimize WeChat Mini Programs. It also guides CloudBase-specific mini program work when the project explicitly uses wx.cloud, Tencent CloudBase, message push, customer service auto-reply, or search optimization workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guidance may lead an agent to run upload, deploy, MCP authentication, or CloudBase operations that affect real projects or cloud resources.

Mitigation: Review commands before execution and confirm the project path, appid, cloud environment, and user approval before preview, upload, deployment, authentication, or cloud-resource changes.

Risk: Incorrect Mini Program or CloudBase assumptions can produce broken authentication, wrong environment selection, or unsafe cloud changes.

Mitigation: Apply CloudBase guidance only when the project explicitly uses CloudBase, prefer wx.cloud conventions, avoid hardcoded secrets or environment guesses, and validate project.config.json before operational workflows.

Risk: Invented WeChat DevTools or message-push commands can fail or bypass supported product workflows.

Mitigation: Use WeChat Developer Tools Nightly, wechatide --help, tools.yaml, or the IDE UI to discover supported commands, and avoid undocumented low-level bypasses.

## Reference(s):

- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [Message Push and Customer Service Auto-Reply](references/message-push-customer-service.md)
- [Common Mini Program Pitfalls](references/pitfalls.md)
- [Mini Program SEO and WeChat Search Optimization](references/seo-search-optimization.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program Search SEO](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program Docs](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, JSON configuration, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; may guide agents toward preview, upload, deployment, MCP authentication, and CloudBase operations that require review before execution.]

## Skill Version(s):

1.28.41 (source: server release metadata; artifact frontmatter reports 2.32.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
