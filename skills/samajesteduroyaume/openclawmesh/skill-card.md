## Description:

Openclaw Mesh connects OpenClaw to opt-in local, LAN, and WAN P2P AI agent meshes for peer discovery, task delegation, streaming inference, vector memory, multimodal tasks, and exposing selected local tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samajesteduroyaume](https://clawhub.ai/user/samajesteduroyaume)

### License/Terms of Use:

MIT License with Commercial Services Addendum

## Use Case:

Developers and engineers use Openclaw Mesh to let OpenClaw agents discover peers, delegate AI inference or memory tasks, stream responses, and optionally expose local tools across a P2P mesh after explicit network and peer consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote mesh use can send prompts, files, memory, media, tool results, or intermediate model data to peers.

Mitigation: Enable P2P networking only when needed, verify peer identity and permissions, and avoid sending sensitive data unless the selected peers and transport protections are appropriate.

Risk: Gateway payment and admin features can expose services, credentials, metadata, or database paths if configured casually.

Mitigation: Treat the gateway as a separate service and keep it on localhost unless strong admin tokens, PSKs or TrustStore identities, TLS/WSS, firewall rules, and protected database storage are configured.

Risk: WAN discovery, relay, DHT, or STUN settings can expose a node beyond the local machine.

Mitigation: Leave WAN behavior disabled unless external exposure is intended, and require TLS/WSS plus PSK or TrustStore identity controls before exposing a node.

Risk: Default or hardcoded Bitcoin wallet and gateway settings may be unsafe for payment use.

Mitigation: Review and replace wallet, gateway, and payment settings before enabling payment workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samajesteduroyaume/skills/openclawmesh)
- [Server-resolved source repository](https://github.com/samajesteduroyaume/OpenClawMesh)
- [README](README.md)
- [Architecture](ARCHITECTURE.md)
- [Protocol specification](references/PROTOCOL_SPEC.md)
- [Security model](references/SECURITY_MODEL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include peer-call payload examples and configuration guidance for opt-in networked execution.]

## Skill Version(s):

0.1.11 (source: server release metadata, created 2026-08-28; artifact frontmatter and pyproject.toml declare 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
