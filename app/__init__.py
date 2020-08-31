from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.main.routes import main
    from app.data_structures.routes import ds

    app.register_blueprint(main)
    app.register_blueprint(ds)
    return app
