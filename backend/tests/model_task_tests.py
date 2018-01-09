from flask_testing import TestCase

from src.models import db
from src.app import create_app
from src.models.task import Task

class ModelTaskTestCase(TestCase):
    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_task_CRUD(self):
        origin_task = Task()
        origin_task.name = 'origin task'
        origin_task.status = False

        # create
        db.session.add(origin_task)
        db.session.commit()

        # read
        tasks = Task.query.filter_by(name=origin_task.name)
        task = tasks.first()
        self.assertEqual(1, tasks.count())
        self.assertEqual(origin_task.status, task.status)

        # update
        task.status = True
        db.session.commit()
        tasks = Task.query.filter_by(name=origin_task.name)
        task = tasks.first()
        self.assertEqual(True, task.status)

        # delete
        db.session.delete(task)
        db.session.commit()

        tasks = Task.query.filter_by(name=task.name)
        self.assertEqual(0, tasks.count())
