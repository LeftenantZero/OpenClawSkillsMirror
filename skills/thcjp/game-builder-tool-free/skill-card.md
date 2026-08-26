## Description: <br>
3D游戏构建器免费版 helps personal developers and game hobbyists generate playable browser-based 3D game prototypes from natural-language prompts, with Three.js single-file output, local preview, and iterative edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and game hobbyists use this skill to turn natural-language game ideas into playable Three.js browser prototypes for game jams, learning, and creative demonstrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate or edit local game files while iterating on a project. <br>
Mitigation: Use a dedicated temporary game-build directory and review generated changes before reusing or publishing files. <br>
Risk: The local preview workflow can leave a browser server running after testing. <br>
Mitigation: Stop the preview server when testing is complete. <br>
Risk: Any online sharing workflow may upload generated game content outside the local machine. <br>
Mitigation: Confirm exactly what will be uploaded and where before using online sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/game-builder-tool-free) <br>
- [Three.js module CDN](https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js) <br>
- [Three.js addons CDN](https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell commands; generated work commonly takes the form of a single HTML/Three.js game file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or edit local game files, maintain progress notes, and start a local browser preview server.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
