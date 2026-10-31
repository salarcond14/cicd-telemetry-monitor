# CI/CD Telemetry & Performance Monitor

An automated DevOps telemetry tool built with Python and GitHub REST API to monitor, aggregate, and visualize build performance metrics across GitHub Actions workflows.

---

## Key Features

* **Automated CI/CD Execution:** Configured continuous integration workflows via `.github/workflows/ci.yml`.
* **REST API Integration:** Consumes GitHub's REST API using Python (`requests`) with secure token authentication.
* **Build Observability:** Calculates real-time failure rates, success percentages, build frequency, and execution logs.
* **Automated Reporting:** Generates structured Markdown (`ci_report.md`) performance summaries automatically.

---

## Tech Stack & Concepts

* **Languages:** Python 3, YAML
* **DevOps & Infrastructure:** GitHub Actions, CI/CD Pipelines, Build Automation
* **Concepts:** Observability, Telemetry, REST APIs, JSON Parsing, Version Control (Git)

---

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/salarcond14/cicd-telemetry-monitor.git](https://github.com/salarcond14/cicd-telemetry-monitor.git)
   cd cicd-telemetry-monitor
