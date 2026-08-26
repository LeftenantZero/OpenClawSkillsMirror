## Description: <br>
竖版视频生成免费版 helps creators turn Markdown scripts into 9:16 short videos with TTS narration, subtitle card images, subtitle burn-in, and FFmpeg-based MP4 composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators and developers use this skill to convert segmented Markdown scripts into vertical short videos with synchronized narration, subtitles, images, and MP4 output. It is intended for personal content creation and excludes processing copyrighted media content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses command-line media tooling and can operate on local files. <br>
Mitigation: Review proposed commands, script text, and file paths before execution, and run it only in a workspace containing the intended media and script files. <br>
Risk: Cloud TTS usage may send narration text to an external service. <br>
Mitigation: Avoid private or sensitive narration unless using a trusted provider or a local TTS command configured through the skill. <br>
Risk: The published trigger wording is broader than necessary for video generation. <br>
Mitigation: Invoke the skill only for vertical-video generation, audio narration, subtitle, and media-composition requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/lh-video-gen-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash, markdown, JSON, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide the agent to create local script, image, audio, temporary, and MP4 output files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
