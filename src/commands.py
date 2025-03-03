import typer
from rich import print
from rich.console import Console


def welcome() -> None:
    print("[bold red]Welcome[/bold red]")


app = typer.Typer(callback=welcome)
console = Console()


@app.command()
def main(name: str = "") -> None:
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
