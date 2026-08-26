## Description:

WhatsApp Business API integration with managed OAuth for sending messages, managing templates, handling media, and interacting with conversations through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to connect a WhatsApp Business account through Maton, inspect account resources, and perform confirmed message, template, media, phone number, and profile operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes, message sends, template or profile changes, media uploads, deletes, and new connections can affect external recipients or account state.

Mitigation: Default to read and list operations, then require explicit user confirmation with the exact account, recipient or resource ID, and payload before any write or new connection.

Risk: The raw API-key fallback can expose a long-lived Maton credential if printed, logged, passed on a command line, or stored in files.

Mitigation: Prefer OAuth with the Maton CLI; use the raw MATON_API_KEY flow only when the CLI cannot be used, feed credentials through stdin when needed, and never inspect local credential stores or unrelated secrets.

Risk: Multiple Maton profiles or WhatsApp Business connections can route an operation to the wrong account.

Mitigation: Confirm the active profile and connection, and specify the target connection when more than one WhatsApp Business connection is available.

Risk: External WhatsApp Business content may contain adversarial instructions or untrusted data.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into shell commands, and let the user select endpoints and recipients.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/whatsapp-business)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WhatsApp Business API Overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [WhatsApp Business Send Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)
- [WhatsApp Business Message Templates](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates)
- [WhatsApp Business Media Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media)
- [WhatsApp Business Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces CLI and SDK usage guidance; API calls may return JSON from Maton or the WhatsApp Business API.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
