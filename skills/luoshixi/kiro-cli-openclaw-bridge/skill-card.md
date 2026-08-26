## Description: <br>
Connects OpenClaw or any OpenAI-compatible client to a local kiro-cli ACP backend through an ACP-to-OpenAI bridge with streaming responses and tool calls. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[luoshixi](https://clawhub.ai/user/luoshixi) <br>

### License/Terms of Use: <br>
Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) <br>


## Use Case: <br>
Developers and engineers use this skill to configure and run a trusted local bridge that lets OpenClaw or other OpenAI-compatible clients use kiro-cli through ACP for coding workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local bridge can allow connected prompts to read and write files or run shell commands as the local user. <br>
Mitigation: Use it only in trusted local projects, avoid untrusted chat clients or shared channels, and add authentication, explicit permission prompts, path allowlists, and command restrictions before broader use. <br>
Risk: The HTTP API has no API key validation and the bridge auto-approves permission requests. <br>
Mitigation: Keep the service bound to localhost, do not expose the port on a network, and review the code before deployment. <br>
Risk: The artifact license is non-commercial. <br>
Mitigation: Confirm licensing or obtain appropriate permission before any commercial deployment. <br>
Risk: Kiro CLI and related backend services are governed by separate third-party terms. <br>
Mitigation: Review and comply with the Kiro and AWS terms that apply to the intended use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luoshixi/skills/kiro-cli-openclaw-bridge) <br>
- [Project homepage from ClawHub metadata](https://github.com/LuoShiXi/kiro-cli-openclaw-bridge) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>
- [Kiro](https://kiro.dev) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline JSON configuration and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-stream setup and integration guidance for a local bridge.] <br>

## Skill Version(s): <br>
1.2.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
