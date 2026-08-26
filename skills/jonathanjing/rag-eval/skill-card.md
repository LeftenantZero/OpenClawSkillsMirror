## Description: <br>
Evaluate a specifically provided RAG question, answer, and retrieved contexts with Ragas metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to evaluate RAG answers against retrieved context for faithfulness, answer relevancy, and context precision. It supports single-response checks, hallucination analysis, and batch evaluation of JSONL datasets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud judge use can transmit the question, answer, and retrieved contexts to an external provider. <br>
Mitigation: Use a local judge with RAGAS_LLM for confidential content, or set RAGAS_ALLOW_CLOUD=1 only after provider transmission is approved. <br>
Risk: Saved evaluation records can contain raw questions, answers, and contexts. <br>
Mitigation: Keep the default no-save behavior unless local plaintext retention is intentionally requested; avoid --save, --include-content, and --save-individual for sensitive data. <br>
Risk: User-provided RAG content could be unsafe if interpolated into shell commands. <br>
Mitigation: Write evaluation input to a temporary JSON file and pass it with --input-file instead of embedding user content in command strings. <br>


## Reference(s): <br>
- [ClawHub release homepage](https://clawhub.ai/jonathanjing/rag-eval) <br>
- [ClawHub skill page](https://clawhub.ai/jonathanjing/skills/rag-eval) <br>
- [Ragas documentation](https://docs.ragas.io/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [JSON score reports with human-readable Markdown summaries and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce single-response or batch evaluation results; raw evaluation content is not saved unless explicitly requested.] <br>

## Skill Version(s): <br>
1.2.3 (source: server release metadata, artifact metadata, and changelog released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
