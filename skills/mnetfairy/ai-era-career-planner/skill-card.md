## Description:

AI Era Career Planner helps users plan education choices, career transitions, and future job directions by collecting background information, assessing interests and values, evaluating AI-era career impact, and producing a personalized career planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for AI-era career planning, major selection, job direction exploration, and career transition guidance. The agent uses structured assessments and local reference data to produce a personalized Markdown career planning report with recommended paths, AI impact ratings, skills, tools, certifications, and next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The insurance-career section includes a featured insurance agency and phone numbers that users may perceive as endorsements.

Mitigation: Present these entries as informational leads only, keep alternatives visible, and tell users to verify company credentials independently before contacting any company.

Risk: Optional email sending, subscriptions, memory saving, tracking, and report-file generation can create unwanted persistence or external sharing if used casually.

Mitigation: Use those actions only when the user explicitly asks for them and the host environment intentionally permits them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career anchor reference](references/career_anchor.md)
- [Conversation flow engine](references/flow_engine.md)
- [Salary data reference](references/salary_data.md)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Education paths](references/education_paths.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Conversational text or Markdown career planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Markdown report-file generation is described for environments that support it and only when the user explicitly requests export.]

## Skill Version(s):

2.2.371 (source: server release metadata; artifact frontmatter reports 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
