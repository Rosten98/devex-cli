import typer
from devex.commands import check, branch

app = typer.Typer(
    name="devex",
    help="Developer Experience CLI — enforce Golden Path conventions.",
    no_args_is_help=True,
)

app.add_typer(check.app, name="check")
app.add_typer(branch.app, name="branch")

if __name__ == "__main__":
    app()