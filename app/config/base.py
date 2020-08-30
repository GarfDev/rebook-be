from dotenv import load_dotenv
from os import getenv

load_dotenv()

##
# This is base config, other configs will extends from this
##


class Config(object):
    SECRET_KEY = 'do-i-really-need-this-yeah-you-do'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_SECRET = SECRET_KEY
