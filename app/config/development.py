from os import getenv
from app.config.base import Config
class Config(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' if getenv('LOCAL_DATABASE_URL') == None else getenv('LOCAL_DATABASE_URL')