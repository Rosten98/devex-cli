# Contributing to devex-cli
 
Thank you for investing time in improving the Developer Experience for all engineering teams. This guide explains how to propose and contribute changes to the CLI following our Inner-Source model.
 
---
 
## Inner-Source Model
 
The DevEx platform team owns and maintains this repository, but **any engineering team can contribute**. We treat contributions from internal teams the same way open-source projects treat external contributors — through pull requests, code review, and discussion.
 
The platform team's role is to **review and guide**, not to implement features on behalf of other teams.
 
---
 
## Before You Start
 
### Check existing issues and discussions
 
Before opening a PR, check whether there is already an issue or discussion about your proposal. If not, **open an issue first** to describe the problem or feature. This avoids wasted effort and lets the platform team give early feedback on direction.
 
### Work ID requirement
 
Every branch, commit, and PR title must include a Work ID referencing your team's ticket. This is enforced by the CLI itself — use `devex branch create` to get started:
 
```bash
devex branch create --id YOUR-123 --desc "your-feature-description" --type feat
```
 
---
 
## Development Setup
 
### Prerequisites
 
- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
### Install dependencies
 
```bash
git clone https://github.com/your-org/devex-cli
cd devex-cli
uv sync
uv pip install -e .
```
 
### Verify your setup
 
```bash
devex --help
uv run pytest tests/ -v
```
 
---
 
## Project Structure
 
```
devex-cli/
├── src/devex/
│   ├── main.py          ← CLI entrypoint, command registration
│   └── commands/
│       ├── check.py     ← devex check command
│       └── branch.py    ← devex branch commands
└── tests/
    └── test_check.py    ← pytest test suite
```
 
---
 
## Making Changes
 
### Adding a new command
 
**Step 1:** Create a new file in `src/devex/commands/`:
 
```python
# src/devex/commands/my_command.py
import typer
from rich.console import Console
 
app = typer.Typer(help="Description of your command group.")
console = Console()
 
@app.command("run")
def run():
    """What this command does."""
    console.print("[green]Running...[/green]")
```
 
**Step 2:** Register it in `src/devex/main.py`:
 
```python
from devex.commands import my_command
 
app.add_typer(my_command.app, name="my-command")
```
 
**Step 3:** Add tests in `tests/`:
 
```python
# tests/test_my_command.py
from typer.testing import CliRunner
from devex.main import app
 
runner = CliRunner()
 
def test_my_command_runs():
    result = runner.invoke(app, ["my-command", "run"])
    assert result.exit_code == 0
```
 
### Modifying an existing command
 
- Keep backwards compatibility — do not remove or rename existing options
- If a breaking change is necessary, discuss it in the issue before implementing
- Update the relevant test file
---
 
## Testing Requirements
 
Every PR must include at least one test for the new or modified behavior. We use `pytest`.
 
```bash
# Run all tests
uv run pytest tests/ -v
 
# Run a specific test file
uv run pytest tests/test_check.py -v
```
 
Tests must pass locally before opening a PR. The CI pipeline will also run them automatically.
 
---
 
## Pull Request Process
 
1. **Branch** — create a branch using `devex branch create` with your Work ID
2. **Commit** — include the Work ID in every commit message: `feat(check): add linting step FIN-123`
3. **PR title** — must include the Work ID: `feat: add linting step to devex check [FIN-123]`
4. **PR description** — fill in the template provided when opening the PR
5. **Two reviewers** — at least two approvals are required before merging (enforced by GitHub branch protection)
6. **Merge** — squash merge into `main`
---
 
## Commit Message Convention
 
```
type(scope): short description WORK-ID
 
Examples:
feat(branch): add --draft flag for draft PRs FIN-456
fix(check): handle repos with no commits FIN-789
chore(deps): upgrade typer to 0.13 FIN-101
```
 
Types: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`
 
---
 
## What the Platform Team Reviews
 
- **Correctness** — does the change work as described?
- **Conventions** — does it follow the project's code style and patterns?
- **Tests** — is the behavior covered by tests?
- **Backwards compatibility** — does it break existing users?
- **Documentation** — is the README updated if needed?
---
 
## Questions
 
Open a GitHub Discussion or reach out to the DevEx platform team directly.