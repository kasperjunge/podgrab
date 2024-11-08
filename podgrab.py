import os
import sys
import typer
import requests
import json


app = typer.Typer()

@app.command()
def download(
    podcast_name: str = typer.Argument(..., help="Name of the podcast"),
    episode_title: str = typer.Argument(..., help="Title of the episode"),
    output_path: str = typer.Option(
        '.', '--output', '-o', help="Output directory for the downloaded file"
    )
):
    """
    Download a podcast episode by specifying the podcast name and episode title.
    """
    try:
        # Trim whitespace
        podcast_name = podcast_name.strip()
        episode_title = episode_title.strip()

        # Validate podcast name
        if not podcast_name:
            typer.echo("Error: Podcast name cannot be empty.")
            sys.exit(1)

        # Validate episode title
        if not episode_title:
            typer.echo("Error: Episode title cannot be empty.")
            sys.exit(1)

        # Validate output path
        if not os.path.isdir(output_path):
            typer.echo(f"Error: The output path '{output_path}' is not a valid directory.")
            sys.exit(1)

        if not os.access(output_path, os.W_OK):
            typer.echo(f"Error: The output path '{output_path}' is not writable.")
            sys.exit(1)

        # Placeholder for file name
        file_name = "episode_audio.mp3"
        full_file_path = os.path.join(output_path, file_name)

        # Continue with processing...
        typer.echo(f"Podcast Name: {podcast_name}")
        typer.echo(f"Episode Title: {episode_title}")
        typer.echo(f"Full File Path: {full_file_path}")

    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")
        sys.exit(1)


@app.command()
def transcribe(file_path: str):
    typer.echo(f"File Path: {file_path}")
    
if __name__ == "__main__":
    app()
