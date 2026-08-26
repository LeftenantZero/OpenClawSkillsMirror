## Description:

PDF Editor helps agents edit and organize PDF files with operations such as merge, split, extract, rotate, delete, insert, convert, optimize, compare, crop-related cleanup, and watermark management through the ComPDFKit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

ComPDFKit SDK License Agreement

## Use Case:

External users and document-workflow agents use this skill to perform local PDF page organization, cleanup, conversion, compression, comparison, and watermark tasks on Windows or macOS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads and runs a proprietary third-party ComPDFKit CLI from the vendor CDN on first use.

Mitigation: Inform the user before download, use the official ComPDFKit distribution endpoint, and verify the CLI with its help command before processing documents.

Risk: Trial license activation sends the user's email address to ComPDFKit.

Mitigation: Ask for the email address, explain that it is used only for license activation, and send it only after the user confirms.

Risk: Explicit overwrite options can replace existing PDF outputs.

Mitigation: Use clear output paths and pass overwrite flags only when the user has requested or confirmed replacement.

## Reference(s):

- [PDF Editor on ClawHub](https://clawhub.ai/compdf-youna/skills/pdf-editor-compdf)
- [ComPDF](https://www.compdf.com/?utm_source=clawhub&utm_medium=skillhub&utm_campaign=pdf_skill_pdf_editor&ref_platform_id=clawhub_skills)
- [ComPDF Security Policy](https://www.compdf.com/security)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with platform-specific shell commands and generated PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local PDF files or directories; first use may require downloading the vendor CLI and activating a trial license.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
