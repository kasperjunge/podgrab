import pytest
from typer.testing import CliRunner
from podgrab import app

runner = CliRunner()

def test_empty_podcast_name():
    result = runner.invoke(app, ["download", "", "Episode Title"])
    assert result.exit_code != 0
    assert "Podcast name cannot be empty" in result.stdout

def test_empty_episode_title():
    result = runner.invoke(app, ["download", "Podcast Name", ""])
    assert result.exit_code != 0
    assert "Episode title cannot be empty" in result.stdout

def test_invalid_output_path(tmp_path):
    invalid_path = tmp_path / "non_existent_dir"
    result = runner.invoke(app, ["download", "Podcast Name", "Episode Title", "--output", str(invalid_path)])
    assert result.exit_code != 0
    assert "is not a valid directory" in result.stdout
