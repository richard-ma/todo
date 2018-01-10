from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort

from src.models import db
from src.models.task import Task
from src.config import config_app

def create_app():
    app = Flask(__name__)

    config_app(app)
    db.init_app(app)

    api = Api(app)

    def abort_if_task_doesnt_exist(task_id):
        counter = Task.query.filter_by(id=task_id).count()
        if counter == 0:
            abort(404, message="Task {} doesn't exist".format(task_id))

    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('status')

    class TaskApi(Resource):
        def get(self, task_id):
            abort_if_task_doesnt_exist(task_id)
            task = Task.query.filter_by(id=task_id).first()
            return jsonify(task.as_dict())

        def delete(self, task_id):
            abort_if_task_doesnt_exist(task_id)
            task = Task.query.filter_by(id=task_id).first()
            db.session.delete(task)
            db.session.commit()
            return '', 204

        def put(self, task_id):
            args = parser.parse_args()
            task = Task()
            task.name = args['name']
            task.status = args['status']

            db.sessoin.add(task)
            db.session.commit()

            return jsonify(task.as_dict()), 201

    api.add_resource(TaskApi, '/task/<string:task_id>')

    return app
