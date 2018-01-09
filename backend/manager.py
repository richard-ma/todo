#!/usr/bin/env python

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app
from src.models import db

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('runserver', Server(host="0.0.0.0"))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
