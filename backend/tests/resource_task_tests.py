from json import loads

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

    def test_task_get(self):
        response = self.client.get('/task/{}'.format(self.task.id))

        self.assertEqual(200, response.status_code)
        self.assertEqual(jsonify(self.task.to_dict).json, response.json)

    def test_task_delete(self):
        response = self.client.delete('/task/{}'.format(self.task.id))

        self.assertEqual(204, response.status_code)

    def test_task_post(self):
        response = self.client.post('/task', data={'name': 'testname'})

        self.assertEqual(201, response.status_code)

    def test_task_put(self):
        response = self.client.put(
                '/task/{}'.format(self.task.id),
                data={'status': True},
        )

        self.assertEqual(201, response.status_code)
