import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
S3_SECRET = os.getenv("S3_SECRET_ACCESS_KEY")
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

ALLOWED_EXTENSIONS = set(['txt', 'json', 'csv', 'env'])

SECRET_KEY = os.urandom(32)
DEBUG = True
PORT = 5000