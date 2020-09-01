import os

from flask import Flask
from flask_pymongo import PyMongo

from app.config import Config

mongo = PyMongo()


def create_app(configuration=Config):
    app = Flask(__name__)
    app.config.from_object(configuration)
    # mongo.init_app(app)

    from app.main.routes import main
    from app.data_structures.routes import ds

    app.register_blueprint(main)
    app.register_blueprint(ds)
    return app
