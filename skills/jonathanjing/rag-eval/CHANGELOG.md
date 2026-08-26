# Changelog

## [1.2.3] - 2026-08-03
### Fixed
- Give an explicit `RAGAS_LLM=ollama/<model>` selection priority over ambient cloud API keys.
- Keep embeddings local whenever the selected judge is local.
- Reject unsupported explicit judge selectors instead of silently falling through.
- Add regression tests for local judge and embedding selection.

## [1.2.2] - 2026-08-03
### Security
- Made raw-content persistence opt-in for single and batch evaluations.
- Require `RAGAS_ALLOW_CLOUD=1` before transmitting evaluation content to a cloud judge.
- Refuse global pip installation outside an activated virtual environment.

## [1.2.1] - 2026-03-03
### Added
- Simplified installation instructions (Ask OpenClaw / CLI) to SKILL.md and README.md.

## [1.2.0] - 2026-02-23
### Security
- SECURITY FIX: Shell injection vulnerability in SKILL.md instructions. Agent was instructed to echo user content directly; now uses temporary files or --input-file.

## [1.1.1] - 2026-02-23
### Fixed
- setup.sh warns about global pip install and recommends virtualenv.

## [1.1.0] - 2026-02-23
### Fixed
- Declare LLM API key requirement in skill metadata.

## [1.0.0] - 2026-02-23
### Initial Release
- Ragas-based RAG pipeline quality testing (faithfulness, relevancy, precision).
