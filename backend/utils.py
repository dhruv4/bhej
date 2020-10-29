from random import choices
from string import ascii_uppercase, digits
from config import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def generateCode():
    return ''.join(choices(ascii_uppercase + digits, k=6))