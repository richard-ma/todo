from flask import Flask

from src.config import config_app

def create_app():
    app = Flask(__name__)

    config_app(app)

    @app.route('/')
    def index():
        return 'TODO is running'

    return app
