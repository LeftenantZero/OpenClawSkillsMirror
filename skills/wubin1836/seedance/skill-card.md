## Description:

Seedance 视频生成 helps creators, marketing teams, e-commerce teams, and short-form video teams generate AI videos from text or reference media through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, e-commerce operators, and developers use this skill to submit Seedance video-generation jobs from prompts and optional image, video, or audio references. It supports AI Hive media upload, task tracking, and local result download for ads, product videos, social content, short drama, and comic-style video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selected media files to AI Hive/object storage before generation.

Mitigation: Only provide media you are authorized to upload, and review files before running generation or upload commands.

Risk: Generation requests may incur API costs.

Mitigation: Check runtime model pricing and routing before bulk use; start with a small test task when cost sensitivity matters.

Risk: The API key enables access to the AI Hive account used by the skill.

Mitigation: Keep the key private, prefer environment variables or the 0600 config file, and rotate the key if it is exposed.

Risk: Broad activation wording may surface the skill during AI-video or e-commerce research where generation is not intended.

Mitigation: Use it only when the user intends to run AI Hive Seedance generation, upload media, query tasks, or download generated results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance)
- [AI Hive API base](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated task JSON and downloaded video files when executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload selected local media to AI Hive/object storage, submit paid generation tasks, poll task status, and save generated media to the configured local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
