import typer
import git
from rich.console import Console
from rich.table import Table
import re

app = typer.Typer(help="Run standards checks on the current repo.")
console = Console()

WORK_ID_PATTERN = re.compile(r"[A-Z]+-\d+")  # ej. FIN-123

@app.callback(invoke_without_command=True)
def check(ctx: typer.Context):
    """Validate Git conventions and branch naming."""
    if ctx.invoked_subcommand is None:
        run_all_checks()

def run_all_checks():
    try:
        repo = git.Repo(search_parent_directories=True)
    except git.InvalidGitRepositoryError:
        console.print("[red]Error:[/red] No se encontró un repositorio Git.")
        raise typer.Exit(code=1)

    table = Table(title="DevEx Standards Check", show_header=True)
    table.add_column("Check", style="bold")
    table.add_column("Status")
    table.add_column("Details")

    all_passed = True

    # Check 1: branch tiene Work ID
    branch_name = repo.active_branch.name
    has_work_id = bool(WORK_ID_PATTERN.search(branch_name))
    status = "[green]PASS[/green]" if has_work_id else "[red]FAIL[/red]"
    detail = branch_name if has_work_id else f"Branch '{branch_name}' no contiene Work ID (ej. FIN-123)"
    table.add_row("Work ID en branch", status, detail)
    if not has_work_id:
        all_passed = False

    # Check 2: hay commits sin staged changes sucias
    dirty = repo.is_dirty(untracked_files=False)
    status = "[green]PASS[/green]" if not dirty else "[yellow]WARN[/yellow]"
    detail = "Working tree limpio" if not dirty else "Hay cambios sin commitear"
    table.add_row("Working tree", status, detail)

    # Check 3: último commit message tiene Work ID
    if repo.head.is_valid():
        last_msg = repo.head.commit.message.strip()
        commit_has_id = bool(WORK_ID_PATTERN.search(last_msg))
        status = "[green]PASS[/green]" if commit_has_id else "[red]FAIL[/red]"
        detail = last_msg[:60] + "..." if len(last_msg) > 60 else last_msg
        table.add_row("Work ID en último commit", status, detail)
        if not commit_has_id:
            all_passed = False

    console.print(table)

    if not all_passed:
        console.print("\n[red]Algunos checks fallaron.[/red] Corrige antes de hacer push.")
        raise typer.Exit(code=1)
    else:
        console.print("\n[green]Todos los checks pasaron.[/green]")