## Description:

Secure computer-to-computer networking for AI agents: gossip broadcast, direct messaging, CRDT synchronization, group encryption, post-quantum encryption, and NAT traversal for decentralized applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use x0x to give AI agents secure peer-to-peer networking, messaging, shared state, group encryption, task orchestration, and local REST/WebSocket control for decentralized applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes remote command execution features for peer agents.

Mitigation: Keep remote exec disabled unless required, allow only verified trusted peers, and use strict exact-command ACLs.

Risk: The skill can forward local TCP ports to peer machines.

Mitigation: Enable forwards only for specific trusted peers and loopback targets, maintain strict connect allowlists, and remove unused forwards.

Risk: The local daemon API token can authorize sensitive networking actions.

Mitigation: Keep the daemon token local, avoid putting durable tokens in URLs, and use short-lived session tokens for browser or WebSocket access.

Risk: Autostart can leave a privileged peer-networking layer running when it is not needed.

Mitigation: Avoid autostart unless the deployment requires it, and review downloaded installers or binaries before enabling the daemon.

## Reference(s):

- [x0x ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Saorsa Labs homepage](https://saorsalabs.com)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Security and cryptography documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Remote exec documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [Symphony integration documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [OpenClaw Linux x64 GNU release asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [OpenClaw macOS ARM64 release asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [OpenClaw Windows x64 release asset](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with shell, JSON, TOML, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes install commands, daemon configuration, CLI usage, REST/WebSocket examples, and security guidance.]

## Skill Version(s):

0.39.10 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
