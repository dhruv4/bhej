import cgi
import config 
import requests
import magic
import typer
import os

app = typer.Typer()
url = config.API_URL

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
def down(filecode: str, dest: str = '.'):
    # TODO: Add an option to change the file name? 

    if not os.path.exists(dest):
        typer.echo(f"No such location: {dest}. Aborting.")
        return

    if not os.path.isdir(dest):
        typer.echo(f"{dest} is not a directory. Aborting.")
        # TODO: Add a prompt to ask whether you'd like to create the dir.
        return

    dest = os.path.join(dest, '') # Adds trailing slash if missing.

    typer.echo(f"Downloading {filecode}")
    req = requests.get(url + '/file/'+ filecode)
    _, params = cgi.parse_header(req.headers['Content-Disposition'])

    open(dest + params['filename'], 'wb').write(req.content)
    typer.echo("Done!")

if __name__ == "__main__":
    app()
