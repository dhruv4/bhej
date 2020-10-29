import config 
import requests
import typer

app = typer.Typer()
url = config.API_URL

@app.command()
def up(filename: str):
    try: 
        files = {'upload_file': open(filename, 'rb')}
    except FileNotFoundError as err:
        typer.echo(f"No such file: '{filename}'. Aborting.")
        return
    except Exception as err:
        typer.echo(f"Unexpected Error: {str(err)}")
        raise(err)
    
    typer.echo(f"Uploading {filename}")

    req = requests.post(url + '/upload', files=files)
    return req.text
    

@app.command()
def down(filecode: str):
    typer.echo(f"Downloading {filecode}")


if __name__ == "__main__":
    app()
