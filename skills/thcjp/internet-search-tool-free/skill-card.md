## Description: <br>
A SearXNG-based multi-engine search aggregation skill that helps users route and run general, news, academic, and social searches through configured search engines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, students, and researchers use this skill to perform single-query web, news, academic, and social searches through a configured SearXNG instance. It is best suited for personal information retrieval, paper discovery, and collecting public community opinions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms may be sent to the configured SearXNG service and upstream search engines. <br>
Mitigation: Use a trusted self-hosted SearXNG instance for sensitive work and avoid entering secrets, private project names, or confidential queries. <br>
Risk: The artifact includes some examples for cache, export, and custom-engine behavior even though the free edition says those features are unsupported. <br>
Mitigation: Treat batch querying, export, custom-engine configuration, and search-result caching as unavailable unless the publisher clarifies support. <br>
Risk: The skill can ask the agent to run shell commands for SearXNG setup, health checks, and troubleshooting. <br>
Mitigation: Review commands before execution and run Docker, curl, and environment-variable changes only in an approved local environment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-query free edition; artifact describes a maximum of 10 results per query and no batch querying, export, custom engine configuration, or search-result cache.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
