## Description:

Convert Word, Excel, PPT, HTML, TXT, CSV, RTF, PNG, and JPG files into PDF with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and teams use this skill to plan ComPDF document or image-to-PDF conversions for sharing, approvals, printing, reporting, compliance workflows, and archiving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents may be uploaded to ComPDF for conversion, including sensitive or regulated files.

Mitigation: Review affected files before upload and obtain confirmation for uploads unless the user has already authorized them.

Risk: The skill-local api_key file stores private credential material.

Mitigation: Keep the api_key file private, exclude it from publishing and version control, and avoid displaying or logging the key.

Risk: The bundled API reference is broader than this skill's supported document and image-to-PDF operations.

Mitigation: Restrict use to the supported operations named in SKILL.md and use exact endpoint details from the matching reference section.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-documents-to-pdf)
- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF API overview](https://www.compdf.com/guides/api-reference/v2/api-overview)
- [ComPDF authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF request workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF Portal](https://www.compdf.com/compdf-portal/signin?utm_source=clawhub&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=clawhub_compdfkit_skills_en)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown with endpoint, method, content type, request fields, expected response fields, and next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ComPDF request details and credential setup guidance, but must not display or log API keys.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
