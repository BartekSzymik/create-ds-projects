import typer
from rich import print
from rich.console import Console

from src.main import ProjectGenerator


def welcome() -> None:
    """Display a welcome message when the application starts.

    This function is used as a callback for the Typer application.
    It prints a styled welcome message to the console using `rich.print`.
    """
    print("[bold red]Welcome to create_ds![/bold red]")


app = typer.Typer(callback=welcome)
console = Console()


@app.command()
def create_ds(project_name: str) -> None:
    """Create a Data Science project structure and install basic dependencies.

    This function initializes a `ProjectGenerator` instance with the given project name
    and generates the project structure. It provides feedback to the user using `rich.console.Console`.
    """
    console.print(f"[green]📂 Creating project: {project_name}[/green]")
    generator = ProjectGenerator(project_name)
    generator.generate_project()
    console.print(f"[bold green]✅ Project {project_name} has been generated successfully![/bold green]")


if __name__ == "__main__":
    app()
