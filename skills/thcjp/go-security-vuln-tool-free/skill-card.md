## Description: <br>
Go安全漏洞扫描免费版 helps individual Go developers scan Go modules with govulncheck, assess known dependency vulnerabilities, and identify suggested fixes before release, dependency updates, or CI integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to run govulncheck-oriented security checks on a single Go project, review affected modules and functions, and plan dependency updates before release or CI gating. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependency update examples can modify go.mod or go.sum and pull newer upstream code. <br>
Mitigation: Review and explicitly approve go get, go mod tidy, build, or test steps before running them. <br>
Risk: Vulnerability scan results and fix suggestions may still require human judgment, especially for not-called vulnerabilities or issues without fixed versions. <br>
Mitigation: Review govulncheck findings manually and prioritize called vulnerabilities before changing dependencies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/go-security-vuln-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash, YAML, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include govulncheck output summaries, dependency update commands, and CI snippets.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
