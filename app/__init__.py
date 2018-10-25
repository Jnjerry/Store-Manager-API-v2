from flask import Flask

from instance.config import app_config
db=Database()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(app_config[config_name])
    return app
