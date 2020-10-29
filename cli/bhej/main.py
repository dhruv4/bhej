from bhej.config import API_URL
import requests
import magic
import typer

app = typer.Typer()
url = API_URL

@app.command()
def up(filename: str):
    try: 
        mime = magic.Magic(mime=True)
        files = {'upload_file': (filename, open(filename, 'rb'), mime.from_file(filename))}
    except FileNotFoundError as err:
        typer.echo(f"No such file: '{filename}'. Aborting.")
        return
    except Exception as err:
        typer.echo(f"Unexpected Error: {str(err)}")
        raise(err)
    
    typer.echo(f"Uploading {filename}")

    req = requests.post(url + '/upload', files=files)
    if (req.text == "Missing upload_file"): 
        typer.echo(f"Error with file upload.")

    return req.text
    

@app.command()
def down(filecode: str):
    typer.echo(f"Downloading {filecode}")
    

if __name__ == "__main__":
    app()
