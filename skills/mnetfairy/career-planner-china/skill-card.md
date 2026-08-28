## Description:

Career Planner China helps Chinese-speaking users plan careers in the AI era by gathering background information, assessing interests and values, evaluating AI impact, and producing personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for AI-era career planning, major selection, job transition advice, and China-focused salary, industry, and education-path guidance. The skill walks users through progressive intake and produces a structured report with recommended career directions, AI impact ratings, skill-building guidance, and next actions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may ask for personal career background and preferences.

Mitigation: Users should provide only information needed for career planning, and optional profile persistence should occur only after an explicit request.

Risk: Salary ranges, job-demand trends, and company contact details may be stale or incomplete.

Mitigation: Users should verify salary data, hiring demand, and company contact information against current official or market sources before making career or financial decisions.

Risk: Optional report export, email, subscription, memory, or live-data integrations can create persistence or external sharing.

Mitigation: Those actions should remain opt-in and should not run unless the user explicitly asks for them in an environment that permits the action.

Risk: Insurance-company recommendations may influence financial decisions.

Mitigation: Recommendations should be treated as informational only; users should compare providers independently and avoid relying on the skill as financial advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career Assessment Framework](references/assessment.md)
- [AI Career Impact Reference](references/ai_career_impact.md)
- [Career Anchor Reference](references/career_anchor.md)
- [MBTI Career Reference](references/mbti.md)
- [Education Paths](references/education_paths.md)
- [Job Demand Trends](references/job_demand.md)
- [Industry Trends](references/industry_trends.md)
- [Salary Data Reference](references/salary_data.md)
- [Salary Database](references/salary_database.json)
- [Insurance Broker Company Data](references/insurance_broker_companies.json)
- [2026 Emerging Careers in China](references/emerging_industries/2026_careers.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown career planning report with structured recommendations and action items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include salary ranges, AI impact ratings, learning paths, optional insurance-company recommendations, and optional exported Markdown when explicitly requested.]

## Skill Version(s):

2.2.376 (source: server release evidence; artifact frontmatter lists 2.2.255)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
