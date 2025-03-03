import typer
from rich import print
from rich.console import Console

from src.main import create_project_structure


def welcome() -> None:
    print("[bold red]Welcome[/bold red]")


app = typer.Typer(callback=welcome)
console = Console()


@app.command()
def main(name: str = "") -> None:
    print(f"Hello {name}")


@app.command()
def create_ds(project_name: str) -> None:
    """Creates a DS project structure and installs the most essential dependencies."""
    create_project_structure(project_name)


if __name__ == "__main__":
    app()
