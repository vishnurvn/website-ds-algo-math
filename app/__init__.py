import os

from flask import Flask
from flask_pymongo import PyMongo

from app.config import Config

mongo = PyMongo()
application = Flask(__name__)


def create_app(configuration=Config):
    application.config.from_object(configuration)
    # mongo.init_app(app)

    from app.main.routes import main
    from app.data_structures.routes import ds

    application.register_blueprint(main)
    application.register_blueprint(ds)
    return application
