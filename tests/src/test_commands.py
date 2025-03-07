from io import StringIO
from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from src.commands import create_ds, welcome

runner: CliRunner = CliRunner()


def test_welcome_message() -> None:
    """Tests if the welcome message is correctly printed."""
    output: StringIO = StringIO()

    with patch("sys.stdout", output):
        welcome()

    assert "Welcome to create_ds!" in output.getvalue()


@patch("src.commands.ProjectGenerator")
def test_create_ds(mock_generator: MagicMock) -> None:
    """Tests the create_ds function to ensure project generation is called correctly."""
    mock_instance: MagicMock = MagicMock()
    mock_generator.return_value = mock_instance

    create_ds("test_project")

    mock_generator.assert_called_once_with("test_project")
    mock_instance.generate_project.assert_called_once()
