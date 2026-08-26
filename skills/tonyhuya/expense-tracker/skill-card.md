## Description:

Expense Tracker helps users record local income and expenses, review daily or monthly totals, and categorize monthly spending in a local TSV ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonyhuya](https://clawhub.ai/user/tonyhuya)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to manage a personal or household expense ledger from the command line, including recording income and spending, reviewing daily or monthly summaries, and categorizing monthly expenses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool stores spending and income notes in a local TSV file.

Mitigation: Use an appropriate local data directory, protect the ledger file as personal financial data, and set EXPENSE_DATA_DIR when a non-default location is needed.

Risk: The delete command can remove ledger rows.

Mitigation: Review the ledger before deleting entries and keep backups if the records need to be recoverable.

Risk: The documented default data path differs from the script's actual default path.

Mitigation: Check ~/.expense-tracker unless EXPENSE_DATA_DIR is set explicitly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonyhuya/skills/expense-tracker)

## Skill Output:

**Output Type(s):** [text, shell commands]

**Output Format:** [Markdown with inline shell commands and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill writes and reads a local TSV ledger; no network output is indicated by the evidence.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
