## Description:

Collect, screen, download, OCR, and archive public Xiaohongshu (RedNote) interview-experience posts for non-technical roles, then optionally generate evidence-linked personalized answers from the user's resume and interview-preparation materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangming1768-alt](https://clawhub.ai/user/yangming1768-alt)

### License/Terms of Use:

MIT

## Use Case:

External candidates and interview-preparation users provide a JD, and the agent collects public RedNote interview-experience posts into local Markdown, Word, and HTML summaries. When the user provides resume or preparation materials, the agent also drafts evidence-linked personalized answers while preserving source citations and personal-evidence boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sets up a local Windows runtime and uses Chrome/OpenCLI with the user's logged-in RedNote session to read public posts and download images.

Mitigation: Require user approval for setup, pause for Chrome extension or login actions, use only documented read/download commands, and stop on CAPTCHA, security verification, or access restrictions.

Risk: Generated archives, resume-derived evidence indexes, and answer drafts may contain personal or interview-preparation information.

Mitigation: Keep processing local, ignore or redact unrelated contact and identity details, and avoid uploading personal files to third-party OCR.

Risk: Public RedNote posts are author self-reports and may be incomplete, changed, deleted, or inaccurate.

Mitigation: Preserve original public text, source URLs, image order, and citations; label OCR as machine-generated; warn when few qualifying posts are available; and avoid treating posts as verified company statements.

Risk: Personalized answer drafts can overstate a candidate's experience if unsupported facts are introduced.

Mitigation: Use only indexed resume or preparation facts, mark answers as directly supported, partial, or insufficient, and require the user to confirm missing facts before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangming1768-alt/skills/interview-experience-rednotes)
- [Server-resolved GitHub provenance](https://github.com/yangming1768-alt/interview-experience-rednotes)
- [Collection workflow](references/collection-workflow.md)
- [Answer workflow](references/answer-workflow.md)
- [Output format](references/output-format.md)
- [Answer output format](references/answer-output-format.md)
- [Windows deployment](references/windows-deployment.md)
- [OpenCLI Xiaohongshu adapter guidance](references/opencli-xiaohongshu.md)
- [OpenCLI project](https://github.com/jackwener/OpenCLI)
- [OpenCLI Xiaohongshu adapter](https://opencli.info/docs/adapters/browser/xiaohongshu.html)
- [OpenCLI Browser Bridge](https://opencli.info/docs/guide/browser-bridge.html)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, DOCX, local HTML, JSON metadata, OCR result files, and local image archives]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates one local task folder per JD with source-linked interview summaries and optional personalized answer documents.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
