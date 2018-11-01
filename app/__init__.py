from flask import Flask,Blueprint

from app.api.db.db_con import create_tables


def create_app(config_name):
    create_tables()
    app=Flask(__name__)
    app.config["SECRET_KEY"] = 'joanN'
    from .api.v2 import version2 as v2
    app.register_blueprint(v2)

    return app
