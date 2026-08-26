## Description:

Add or remove text and image watermarks in PDFs with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document workflow teams use this skill to prepare ComPDF Server API request plans for adding brand, draft, or control watermarks to PDFs and for removing supported watermarks from files prepared for reuse or final delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDFs may be uploaded to ComPDF for processing.

Mitigation: Confirm the affected files, destination, and privacy or compliance fit before upload.

Risk: Watermark removal changes document content.

Mitigation: Keep original files and require explicit authorization before removal, replacement, or overwrite.

Risk: The skill uses a ComPDF API key.

Mitigation: Store the key only in the skill-local api_key file and never display, log, commit, or include it in examples.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF Add Watermark API](https://www.compdf.com/guides/api-reference/v2/watermark-guides)
- [ComPDF Remove Watermark API](https://www.compdf.com/guides/api-reference/v2/del-watermark-guides)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown request plan with endpoint, method, content type, fields, and optional cURL-style command details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes expected task or result fields and the next polling or download step; does not include API keys in examples or final output.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
