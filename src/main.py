import os
import subprocess
from typing import Dict, List

from rich.console import Console

from helpers.project_files import PROJECT_FILES
from helpers.project_structure import PROJECT_STRUCTURE
from helpers.pyproject_template import PYPROJECT_TEMPLATE

console = Console()


class ProjectGenerator:
    """A class for generating a project structure and installing dependencies."""

    def __init__(self, project_name: str) -> None:
        """Initializes the ProjectGenerator with the given project name.

        Args:
            project_name (str): The name of the project to be generated.
        """
        self.project_name: str = project_name
        self.project_path: str = os.path.join(os.getcwd(), project_name)  # Use os.path.join for compatibility
        self.structure: List[str] = PROJECT_STRUCTURE
        self.files: Dict[str, str] = PROJECT_FILES
        self.dependencies: List[str] = []  # List of dependencies to be installed

    def create_structure(self) -> None:
        """Creates the project directory structure and adds `.gitkeep` files to empty directories.

        This ensures that empty directories are tracked in version control.
        """
        console.print("[blue]📂 Creating project directory structure...[/blue]")
        for folder in self.structure:
            folder_path: str = os.path.join(self.project_path, folder)
            os.makedirs(folder_path, exist_ok=True)  # Create directories
            with open(os.path.join(folder_path, ".gitkeep"), "w") as f:
                f.write("")  # Create an empty .gitkeep file
        console.print("[green]✅ Project directory structure created![/green]")

    def create_files(self) -> None:
        """Creates essential project files.

        Reads the predefined file templates and writes them to the appropriate
        locations within the project structure.
        """
        console.print("[blue]📝 Generating configuration files...[/blue]")
        for file, content in self.files.items():
            file_path: str = os.path.join(self.project_path, file)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directories exist
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)  # Write content to the file
        console.print("[green]✅ Configuration files created![/green]")

    def install_dependencies(self) -> None:
        """Installs dependencies using the `uv add` command.

        Reads dependencies from `requirements.txt` and installs them.
        """
        console.print("[blue]📦 Installing dependencies...[/blue]")
        requirements_path: str = os.path.join(self.project_path, "requirements.txt")
        with open(requirements_path, "r", encoding="utf-8") as f:
            self.dependencies = [line.strip() for line in f.readlines() if line.strip()]

        if self.dependencies:
            uv_command: List[str] = ["uv", "add"] + self.dependencies
            subprocess.run(uv_command, check=True, cwd=self.project_path)
            console.print("[green]✅ Dependencies installed successfully![/green]")

    def create_pyproject_toml(self) -> None:
        """Generates a `pyproject.toml` file using the predefined template.

        The template is formatted with the project name and dependencies.
        """
        console.print("[blue]📜 Generating pyproject.toml...[/blue]")
        pyproject_content: str = PYPROJECT_TEMPLATE.format(
            project_name=self.project_name, dependencies=self.dependencies
        )
        pyproject_path: str = os.path.join(self.project_path, "pyproject.toml")
        with open(pyproject_path, "w", encoding="utf-8") as f:
            f.write(pyproject_content)  # Write content to the file
        console.print("[green]✅ pyproject.toml file created![/green]")

    def generate_project(self) -> None:
        """Generates the entire project.

        This includes:
        - Creating the project directory structure
        - Creating necessary project files
        - Installing dependencies
        - Generating the `pyproject.toml` file
        """
        console.print(f"[bold cyan]🚀 Generating project '{self.project_name}'...[/bold cyan]")
        self.create_structure()
        self.create_files()
        self.install_dependencies()
        self.create_pyproject_toml()
        console.print(f"[bold green]🎉 Project '{self.project_name}' has been successfully generated![/bold green]")
