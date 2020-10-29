from flask import Flask, request, redirect, send_file
from werkzeug.utils import secure_filename

import boto3, botocore
import config
from utils import generateCode, allowed_file

s3 = boto3.client(
   "s3",
   aws_access_key_id=config.S3_KEY,
   aws_secret_access_key=config.S3_SECRET
)

print("banana", config.S3_BUCKET)

app = Flask(__name__)
app.config.from_object(config)

def upload_file_to_s3(file, bucket_name, acl="public-read"):

    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            generateCode(),
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type,
                "Metadata": {
                    "FileName": file.filename
                }
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e

    return "{}{}".format(app.config["S3_LOCATION"], file.filename)

def get_file_from_s3(code, bucket_name, acl="public-read"):

    try:

        obj = s3.get_object(
            Bucket=bucket_name,
            Key=code,
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e

    print(obj)

    return obj['Body'], obj['Metadata']['filename']

@app.route("/upload", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return "No user_file key in request.files"

    file = request.files["file"]

    if file.filename == "":
        return "Please select a file"

    print(file.filename)

    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output = upload_file_to_s3(file, app.config["S3_BUCKET"])
        return str(output)

    else:
        return redirect("/")

@app.route("/file/<code>", methods=["GET"])
def get_file(code):

    if code == "" or code == None:
        return "Please select a file"

    file, filename = get_file_from_s3(code, app.config['S3_BUCKET'])

    print(filename)

    return send_file(file, attachment_filename=filename, as_attachment=True)