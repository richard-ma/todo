#!/usr/bin/env python

import os
import sys
import unittest

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app
from src.models import db
from src.models.task import Task

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('runserver', Server(host="0.0.0.0"))
manager.add_command('db', MigrateCommand)

def init_db():
    db.drop_all()
    db.create_all()

@manager.command
def exampleData():
    init_db()

    tasks = list()

    for idx in range(1, 100):
        task = Task()
        task.name = 'taskname{}'.format(idx)
        tasks.append(task)

    for task in tasks:
        db.session.add(task)
        db.session.commit()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        os.environ['TODO_CONFIGURATION'] = 'testing'
        tests = unittest.TestLoader().discover('tests', pattern='*_tests.py')
        unittest.TextTestRunner(verbosity=1).run(tests)
    else:
        manager.run()
