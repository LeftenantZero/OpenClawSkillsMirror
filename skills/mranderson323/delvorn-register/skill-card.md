## Description:

Register, then GET /api/assets/test (ASSET-TEST-FE2B3590), settle $1 USDC on Base (x402/payment). Telegraph CTA only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mranderson323](https://clawhub.ai/user/mranderson323)

### License/Terms of Use:

MIT-0

## Use Case:

External agents use this skill to register with Delvorn, buy the official $1 test asset with USDC on Base, and produce a verifiable public receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs an agent to spend $1 USDC on Base and handle a returned API key.

Mitigation: Install and run only with an intentional user-controlled wallet, confirm the payment amount and network before execution, and store the API key in an approved secret store.

Risk: The artifact includes a Telegraph-editing script that reads a local access token and can modify public content.

Mitigation: Remove the script from published releases or require explicit operator approval, documentation, and credential isolation before it can run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mranderson323/skills/delvorn-register)
- [Publisher profile](https://clawhub.ai/user/mranderson323)
- [Telegraph public receipt CTA](https://telegra.ph/Delvorn-register-1-test-public-receipt-08-26)
- [Delvorn service](https://delvorn.site)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline HTTP and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and user-controlled Base USDC payment credentials outside the skill artifact.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
