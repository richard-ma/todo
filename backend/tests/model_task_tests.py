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

    def test_task(self):
        return True
