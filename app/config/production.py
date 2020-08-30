from os import getenv
from app.config.base import Config

class Config(Config):
    DEBUG = False
    DEVELOPMENT = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' if getenv('DATABASE_URL') == None else getenv('DATABASE_URL')
