## Description:

通过 AI Hive 使用 GPT Image 2 完成图片生成与编辑，覆盖文生图、图生图、多参考合成、商品图、海报文字、换背景、角色一致性和广告版本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, ecommerce operators, and developers use this skill to generate or edit GPT Image 2 visuals through AI Hive, including campaign concepts, controlled image edits, multi-reference compositions, product imagery, posters with short text, and channel variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and media selected by the user are uploaded to the third-party AI Hive service.

Mitigation: Use only media the user intends to share with AI Hive, and avoid private or sensitive reference files unless that upload is explicitly acceptable.

Risk: The AI Hive API key may be stored locally for repeated use.

Mitigation: Prefer environment or command-line credentials when appropriate, keep local config permissions restricted, and rotate the key if it may have been exposed.

Risk: Generated commercial imagery can contain incorrect product facts, text, logos, packaging details, or platform-policy issues.

Mitigation: Review generated outputs against the prompt, references, brand requirements, legal copy, and current target-platform policies before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)
- [AI Hive OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands; generated tasks may return JSON status and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided prompts, optional reference images, batch count, model parameters, routing mode, and output directory.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact CHANGELOG top entry lists 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
