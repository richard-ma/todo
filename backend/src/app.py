from flask import Flask, jsonify
from flask_restful import Api

from src.models import db
from src.config import config_app
from src.api import create_api

def create_app():
    app = Flask(__name__)

    config_app(app)
    db.init_app(app)

    api = Api(app)
    create_api(api)

    return app
