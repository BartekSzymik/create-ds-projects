from typing import Set

from helpers.project_files import PROJECT_FILES
from helpers.pyproject_template import PYPROJECT_TEMPLATE


def test_project_files_keys() -> None:
    """Checks if PROJECT_FILES contains all required files."""
    expected_files: Set[str] = {
        "README.md",
        "requirements.txt",
        "environment.yml",
        ".gitignore",
        "reports/final_report.md",
    }
    assert expected_files.issubset(PROJECT_FILES.keys()), "Missing required files in PROJECT_FILES"


def test_readme_content() -> None:
    """Checks if README.md has the correct content."""
    expected_content: str = "# Automatically generated project\n\nProject description..."
    assert PROJECT_FILES["README.md"] == expected_content, "Incorrect content in README.md"


def test_requirements_content() -> None:
    """Checks if `requirements.txt` contains the required dependencies."""
    requirements: str = PROJECT_FILES["requirements.txt"]

    assert "typer" in requirements, "Missing `typer` in requirements.txt"
    assert "pandas" in requirements, "Missing `pandas` in requirements.txt"
    assert "numpy" in requirements, "Missing `numpy` in requirements.txt"
    assert "matplotlib" in requirements, "Missing `matplotlib` in requirements.txt"
    assert "scikit-learn" in requirements, "Missing `scikit-learn` in requirements.txt"


def test_environment_file() -> None:
    """Checks the correctness of the `environment.yml` file."""
    environment_content: str = PROJECT_FILES["environment.yml"]

    assert "python=3.13" in environment_content, "Incorrect Python version in environment.yml"
    assert "pandas" in environment_content, "Missing `pandas` in environment.yml"
    assert "numpy" in environment_content, "Missing `numpy` in environment.yml"
    assert "matplotlib" in environment_content, "Missing `matplotlib` in environment.yml"
    assert "scikit-learn" in environment_content, "Missing `scikit-learn` in environment.yml"


def test_pyproject_template() -> None:
    """Checks if PYPROJECT_TEMPLATE correctly generates `pyproject.toml`."""
    project_name: str = "test_project"
    dependencies: list[str] = ["typer", "pandas", "numpy"]

    expected_output: str = f"""[project]
name = "{project_name}"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = {dependencies}
"""

    generated_output: str = PYPROJECT_TEMPLATE.format(project_name=project_name, dependencies=dependencies)
    assert generated_output.strip() == expected_output.strip(), "Incorrect content in `pyproject.toml`"
