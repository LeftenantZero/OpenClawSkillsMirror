## Description: <br>
Process PDF files with Python and command-line tools for reading, extraction, merging, splitting, rotation, watermarking, creation, form filling, encryption or decryption, and OCR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect, transform, create, secure, OCR, and fill PDF documents using documented Python libraries, command-line tools, and bundled helper scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes local PDFs and can create derived files that may contain personal, financial, legal, or business information. <br>
Mitigation: Use it only on documents you are authorized to process, and delete intermediate extracted data, crops, images, JSON files, and filled PDFs when they are no longer needed. <br>
Risk: Password decryption support could be misused on documents the operator is not authorized to access. <br>
Mitigation: Use password decryption only for documents you own or are explicitly authorized to process. <br>
Risk: Form-filling workflows can place values in incorrect locations if field IDs or bounding boxes are wrong. <br>
Mitigation: Run the bundled validation checks and visually review generated validation images or filled PDFs before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/pdf) <br>
- [PDF Processing Guide](artifact/SKILL.md) <br>
- [PDF Forms Guide](artifact/forms.md) <br>
- [PDF Processing Advanced Reference](artifact/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown with Python, JavaScript, shell, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Helper scripts can produce derived local files such as filled PDFs, extracted text, images, spreadsheets, and JSON metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
