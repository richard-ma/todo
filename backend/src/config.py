import os
import logging

# default configration
class DefaultConfig(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOGGING_LEVEL = logging.DEBUG
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    LOGGING_LOCATION = 'development.log'

class ProductionConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'
    LOGGING_LOCATION = 'production.log'
    LOGGING_LEVEL = logging.ERROR

class TestingConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://' # use memory for sqlite
    LOGGING_LOCATION = 'testing.log'
    TESTING = True

config = {
        "development": "src.config.DevelopmentConfig",
        "testing": "src.config.TestingConfig",
        "default": "src.config.BaseConfig",
}

def config_app(app):
    config_name = os.getenv('TODO_CONFIGURATION', 'development')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)

    #logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
