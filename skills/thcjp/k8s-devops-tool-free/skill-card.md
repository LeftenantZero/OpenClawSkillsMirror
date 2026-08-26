## Description: <br>
K8s清单生成入门 helps developers generate and perform basic validation of Kubernetes YAML manifests for common resources such as Deployment, Service, ConfigMap, Secret, Ingress, Job/CronJob, PVC, and Namespace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and DevOps engineers use this skill to draft Kubernetes manifests for common workloads, generate app-stack YAML, and check manifests before applying them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Kubernetes Secrets or deployment manifests may contain sensitive or unsafe configuration. <br>
Mitigation: Review generated Secret and deployment files before use, and validate manifests with dry-run or equivalent checks before applying them. <br>
Risk: The skill requests exec/write authority and has broader routing language than its stated Kubernetes manifest purpose. <br>
Mitigation: Limit use to Kubernetes manifest generation and validation, and require explicit confirmation before executing commands or modifying project files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/k8s-devops-tool-free) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Kubernetes YAML snippets and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include generated manifest files, status messages, validation notes, and logs; generated Secrets and deployment files should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
