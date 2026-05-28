# devex-cli
 
Developer Experience CLI — enforce Golden Path conventions across all engineering teams.
 
## Overview
 
`devex` is the developer-facing interface of the DevEx ecosystem. It runs on your local machine and ensures every branch, commit, and pull request follows the shared conventions required for consistent DORA metrics and SOC 2 auditability.
 
## Prerequisites
 
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) installed on your machine
## Installation
 
Install directly from the Git repository — no need to publish to PyPI:
 
```bash
uv tool install git+https://github.com/Rosten98/devex-cli
```
 
Verify the installation:
 
```bash
devex --help
```
 
## Updating
 
```bash
uv tool upgrade devex-cli
```
 
## Commands
 
### `devex check`
 
Validates that your current branch and latest commit follow Golden Path conventions.
 
```bash
devex check
```
 
Checks performed:
- Branch name contains a valid Work ID (e.g. `FIN-123`)
- Latest commit message contains a valid Work ID
- Working tree is clean
**Example output:**
```
PASS  Work ID found in branch: feat/FIN-123-add-payment-endpoint
PASS  Work ID in latest commit
PASS  Working tree clean
 
All checks passed.
```
 
---
 
### `devex branch create`
 
Creates a new branch following the Golden Path naming convention: `type/WORK-ID-description`.
 
```bash
devex branch create --id FIN-123 --desc "add-payment-endpoint" --type feat
```
 
**Options:**
 
| Option | Shorthand | Required | Description |
|--------|-----------|----------|-------------|
| `--id` | `-i` | Yes | Work ID, e.g. `FIN-123` |
| `--desc` | `-d` | Yes | Short description, e.g. `add-payment-endpoint` |
| `--type` | `-t` | No | Branch type: `feat`, `fix`, `chore`, `docs`, `refactor` (default: `feat`) |
 
**Example:**
```bash
devex branch create -i FIN-123 -d "add-payment-endpoint" -t feat
# Creates: feat/FIN-123-add-payment-endpoint
```
 
---
 
## Work ID Convention
 
Every branch, commit, and PR title must include a **Work ID** — a reference to the ticket in your project management tool.
 
Format: `[A-Z]+-[0-9]+`
 
Examples: `FIN-123`, `PROJ-9999`, `API-42`
 
This is the foundation of DORA metric traceability — it links every deployment back to a specific unit of work.
 
---
 
## Git Hooks (Pre-push)
 
The CLI manages git hooks for your repository. Once initialized, `devex check` runs automatically before every `git push`, blocking pushes that violate conventions.
 
To install the hooks in a repository:
 
```bash
cd your-service-repo
devex init
```
 
---
 
## Running Tests
 
```bash
uv run pytest tests/ -v
```
 
---
 
## Contributing
 
See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to propose changes or add new features to the CLI.# devex-cli
