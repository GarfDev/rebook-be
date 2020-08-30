# all flask apps must create an application instance. The web server passes all requests to this object using a protocol called WSGI.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
#################################
# So I still want to access bellow variable in other place
# but when I put them on initialize_app function because that
# make them accessable only inside that function, so a solution is
# `Hoisting` them here and initialize them later when the function run
#################################
db = SQLAlchemy()
api = Api()
bcrypt = Bcrypt()
migrate = Migrate()

def initialize_app(config_type):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(f'app.config.{config_type}.Config')

    # Initialize ORM (Object Relationship Mapping)
    db.init_app(app)
    # Initialize CORS
    CORS(app)
    # Initialize RESTful (We can still archive RESTful by Flask natively)
    api.init_app(app)
    # Intiialize Bcrypt (An library for encrypting and descripting user data, it use our SECRECT_KEY as Salt)
    bcrypt.init_app(app)
    # Initialize Migrate for Database (This will auto commit changes of our model onto current database)
    migrate.init_app(app, db)
    # Return the Application with Execution Context
    with app.app_context():
        ## Import Model Context ###################
        # I'm but this after db.init_app cause we need db initialized before
        # initialize db models. initialize_models function not return anything, it
        # just import context of all model in models folder.
        ###########################################
        from .model import initialize_models
        initialize_models()
        ## Import Application Resources ###########
        # Same with model, resources should be initialize after model. In this
        # project I gonna use namespace for resource `Routing`. There still other
        # way to archive this, like Blueprint.
        ###########################################
        from .resources.hello import hello

        api.add_namespace(hello)

        return app
