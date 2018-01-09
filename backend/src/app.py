from flask import Flask

from src.models import db
from src.config import config_app

def create_app():
    app = Flask(__name__)

    config_app(app)
    db.init_app(app)

    @app.route('/')
    def index():
        return 'TODO is running'

    return app
