import typer
import git
from rich.console import Console
import re

app = typer.Typer(help="Create branches following Golden Path conventions.")
console = Console()

VALID_TYPES = ["feat", "fix", "chore", "docs", "refactor"]

@app.command("create")
def create(
    work_id: str = typer.Option(..., "--id", "-i", help="Work ID, ej: FIN-123"),
    description: str = typer.Option(..., "--desc", "-d", help="Descripción corta, ej: add-payment-endpoint"),
    branch_type: str = typer.Option("feat", "--type", "-t", help=f"Tipo: {VALID_TYPES}"),
):
    """Create a branch following the naming convention: type/WORK-ID-description"""
    if branch_type not in VALID_TYPES:
        console.print(f"[red]Invalid type.[/red] Use one of: {VALID_TYPES}")
        raise typer.Exit(code=1)

    if not re.match(r"^[A-Z]+-\d+$", work_id):
        console.print("[red]Work ID inválido.[/red] Formato esperado: FIN-123")
        raise typer.Exit(code=1)

    branch_name = f"{branch_type}/{work_id}-{description}"

    try:
        repo = git.Repo(search_parent_directories=True)
        repo.git.checkout("-b", branch_name)
        console.print(f"[green]Branch creado:[/green] {branch_name}")
    except git.GitCommandError as e:
        console.print(f"[red]Error de Git:[/red] {e}")
        raise typer.Exit(code=1)