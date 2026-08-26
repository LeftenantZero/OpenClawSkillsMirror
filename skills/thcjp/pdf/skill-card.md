## Description:

PDF处理工具 helps agents extract text and tables from PDF files, create and merge PDFs, and fill PDF forms for document-processing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and workflow builders use this skill to automate PDF text and table extraction, PDF generation, file merging, and form filling. It is suited to document-processing workflows where an agent can read, write, and execute local PDF tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad command access could run commands beyond the PDF operations the reader expects.

Mitigation: Use the skill only in a sandbox or trusted workspace and restrict execution to known PDF tools and local Python libraries.

Risk: Unclear external API and API key guidance could expose credentials or PDF contents.

Mitigation: Do not provide API keys or process sensitive PDFs unless the publisher documents the provider, scopes, and data handling; prefer local processing.

Risk: PDF parsing can fail or produce incomplete results for scanned, encrypted, unusually large, or complex-layout PDFs.

Mitigation: Validate outputs before relying on them, use OCR or specialized tooling when needed, and split very large files into smaller batches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/pdf)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with Python and shell code blocks; extracted content may be text, JSON, or generated PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require local PDF libraries such as pypdf or pdfplumber and read/write/exec access in the active workspace.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
