import typer

app = typer.Typer()

@app.command()
def up(filename: str):
    typer.echo(f"Uploading {filename}")

@app.command()
def down(filecode: str):
    typer.echo(f"Downloading {filecode}")


if __name__ == "__main__":
    app()
