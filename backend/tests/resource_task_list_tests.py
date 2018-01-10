from flask import jsonify
from flask_testing import TestCase

from src.models import db
from src.app import create_app
from src.models.task import Task

class TaskResourceTestCase(TestCase):
    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all()

        # example task
        t = Task()
        t.name = 'test added task'

        db.session.add(t)
        db.session.commit()

        self.task = Task.query.filter_by(name=t.name).first()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_task_list_with_none_argument(self):
        response = self.client.get('/tasks')

        self.assertEqual(200, response.status_code)

    def test_task_list_with_bounded_offset(self):
        response = self.client.get('/tasks/0')

        self.assertEqual(200, response.status_code)

    def test_task_list_with_unbounded_offset(self):
        response = self.client.get('/tasks/10000')

        self.assertEqual(404, response.status_code)
