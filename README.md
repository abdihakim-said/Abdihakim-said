## Abdihakim Said

**Cloud & platform engineer · Founder, Human Layer AI Ltd (UK)**
AWS Certified Solutions Architect · Certified Kubernetes Administrator (CKA)

I help teams run secure, reliable and cost-efficient platforms on AWS and Azure. My work covers Terraform, Kubernetes and GitOps, DevSecOps pipelines, SRE practice, and adopting AI in operations *safely*.

I have 6 years in production infrastructure, most of it in regulated healthcare:

- **Luul Solutions**, Senior Cloud Platform Engineer (2022–present)
- **Moorfields Private Eye Hospital**, Cloud Engineer
- **Chelsea & Westminster Hospital NHS Foundation Trust**, System Administrator

---

### Reference builds

These are platforms I designed, deployed and debugged in my own cloud accounts, so you can read the code before we talk. They're not client systems. Each README has the architecture, the trade-offs I made, **the known limitations**, and what it costs to run.

| Project | What it shows | Status |
|---|---|---|
| [**Jenkins on AWS: golden-AMI factory**](https://github.com/abdihakim-said/jenkins-enterprise-platform) | Packer golden AMIs with Trivy/Inspector scanning, Terraform (11 modules), EFS-backed disposable controller, gated infra pipeline | Deployed in dev (~127 resources); real troubleshooting write-up |
| [**Robot Shop on Azure AKS: GitOps + DevSecOps**](https://github.com/abdihakim-said/robot-shop-azure-platform) | Layered Terraform, build-once/promote-by-Git, ArgoCD, Key Vault CSI, Trivy gate + SBOM, SLO alerting | Dev environment live at [hakimdevops.art](https://hakimdevops.art); engineering notes on 5 real incidents |
| [**AI-assisted IAM provisioning**](https://github.com/abdihakim-said/cloudmart-enterprise-iam-automation) | Bedrock (Claude) drafts IAM policies; permission boundaries, MFA enforcement; design for deterministic Access Analyzer gating | Prototype |
| [**HealthHub: serverless multi-cloud AI**](https://github.com/abdihakim-said/healthhub-enterprise-platform) | 7 Lambda services orchestrating Azure Speech, OpenAI and Google Vision; Terraform + Serverless | Prototype, sample data only |

---

### What I can help with

- AWS / Azure landing zones, Terraform module libraries, migrations
- Kubernetes platforms (EKS / AKS) with GitOps
- CI/CD security: scanning gates, SBOMs, OIDC instead of long-lived keys, least-privilege IAM
- SRE: SLOs, alerting, runbooks, incident reviews
- Cloud cost reviews (FinOps)
- Putting LLMs into ops workflows with guardrails that don't depend on the LLM

**Get in touch:** [LinkedIn](https://linkedin.com/in/said-devops) · [abdihakimsaid1@gmail.com](mailto:abdihakimsaid1@gmail.com)

<sub>AWS · Azure · GCP · Kubernetes · Terraform · Packer · ArgoCD · Helm · GitHub Actions · Jenkins · Python · Bash · Prometheus · Grafana</sub>
