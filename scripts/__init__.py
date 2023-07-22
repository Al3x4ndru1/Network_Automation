from flask import Flask
from .Server import server

def create_app():
    app = Flask(__name__)
    app.register_blueprint(server,url_prefix='/')

    return app