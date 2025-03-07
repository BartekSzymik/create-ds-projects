import os
from unittest.mock import MagicMock, patch

import pytest

from helpers.project_files import PROJECT_FILES
from helpers.project_structure import PROJECT_STRUCTURE
from helpers.pyproject_template import PYPROJECT_TEMPLATE
from src.main import ProjectGenerator


@pytest.fixture
def project_name() -> str:
    """Fixture to provide a sample project name."""
    return "test_project"


@pytest.fixture
def project_generator(tmp_path: pytest.TempPathFactory, project_name: str) -> ProjectGenerator:
    """Fixture to create a ProjectGenerator instance with a temporary path."""
    temp_dir = os.path.abspath(str(tmp_path))  # Ensure a string-based absolute path
    generator = ProjectGenerator(project_name)
    generator.project_path = os.path.join(temp_dir, project_name)  # Use os.path.join for compatibility
    return generator


def test_create_structure(project_generator: ProjectGenerator) -> None:
    """Test if the project directory structure is created correctly."""
    project_generator.create_structure()

    for folder in PROJECT_STRUCTURE:
        folder_path = os.path.join(project_generator.project_path, folder)
        assert os.path.isdir(folder_path), f"Directory {folder_path} was not created"
        assert os.path.isfile(os.path.join(folder_path, ".gitkeep")), ".gitkeep file is missing"


def test_create_files(project_generator: ProjectGenerator) -> None:
    """Test if project files are created correctly with expected content."""
    project_generator.create_files()

    for file, expected_content in PROJECT_FILES.items():
        file_path = os.path.join(project_generator.project_path, file)
        assert os.path.isfile(file_path), f"File {file_path} was not created"

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            assert content == expected_content, f"Content of {file_path} does not match expected"


@patch("subprocess.run")
def test_install_dependencies(mock_subprocess: MagicMock, project_generator: ProjectGenerator) -> None:
    """Test if dependencies are installed correctly by mocking `subprocess.run`."""
    requirements_content = "rich\npytest\n"
    requirements_path = os.path.join(project_generator.project_path, "requirements.txt")
    os.makedirs(project_generator.project_path, exist_ok=True)
    with open(requirements_path, "w", encoding="utf-8") as f:
        f.write(requirements_content)

    project_generator.install_dependencies()

    assert project_generator.dependencies == ["rich", "pytest"]
    mock_subprocess.assert_called_once_with(
        ["uv", "add", "rich", "pytest"], check=True, cwd=project_generator.project_path
    )


def test_create_pyproject_toml(project_generator: ProjectGenerator) -> None:
    """Test if the `pyproject.toml` file is created with the correct content."""
    project_generator.create_structure()

    project_generator.dependencies = ["rich", "pytest"]
    project_generator.create_pyproject_toml()

    pyproject_path = os.path.join(project_generator.project_path, "pyproject.toml")
    assert os.path.isfile(pyproject_path), "pyproject.toml file was not created"

    with open(pyproject_path, "r", encoding="utf-8") as f:
        content = f.read()
        expected_content = PYPROJECT_TEMPLATE.format(
            project_name=project_generator.project_name, dependencies=project_generator.dependencies
        )
        assert content == expected_content, "pyproject.toml content does not match expected"


@patch("subprocess.run")
def test_generate_project(mock_subprocess: MagicMock, project_generator: ProjectGenerator) -> None:
    """Test the full project generation process."""
    project_generator.generate_project()

    for folder in PROJECT_STRUCTURE:
        assert os.path.isdir(os.path.join(project_generator.project_path, folder)), (
            f"Directory {folder} was not created"
        )

    for file in PROJECT_FILES.keys():
        assert os.path.isfile(os.path.join(project_generator.project_path, file)), f"File {file} was not created"

    assert os.path.isfile(os.path.join(project_generator.project_path, "pyproject.toml")), (
        "pyproject.toml file was missing"
    )

    mock_subprocess.assert_called()
