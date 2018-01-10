from flask import jsonify
from flask_restful import Resource, reqparse, abort

from src.models import db
from src.models.task import Task

def create_api(api):
    def abort_if_task_doesnt_exist(task_id):
        counter = Task.query.filter_by(id=task_id).count()
        if counter == 0:
            abort(404, message="Task {} doesn't exist".format(task_id))

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('status', type=bool)

    class TaskResource(Resource):
        def get(self, task_id):
            abort_if_task_doesnt_exist(task_id)
            task = Task.query.filter_by(id=task_id).first()
            return jsonify(task.to_dict)

        def delete(self, task_id):
            abort_if_task_doesnt_exist(task_id)
            task = Task.query.filter_by(id=task_id).first()

            try:
                db.session.delete(task)
                db.session.commit()
            except exc.SQLAlchemyError:
                db.session.rollback()
                app.logger.error(self)

            return '', 204

        def post(self):
            args = parser.parse_args()
            task = Task()
            task.name = args['name']

            try:
                db.session.add(task)
                db.session.commit()
            except exc.SQLAlchemyError:
                db.session.rollback()
                app.logger.error(self)

            return '', 201

        def put(self, task_id):
            abort_if_task_doesnt_exist(task_id)
            args = parser.parse_args()
            task = Task.query.filter_by(id=task_id).first()
            task.status = args['status']

            try:
                db.session.commit()
            except exc.SQLAlchemyError:
                db.session.rollback()
                app.logger.error(self)

            return '', 201

    api.add_resource(TaskResource, '/task', '/task/<string:task_id>')

    class TaskListResource(Resource):
        def get(self, offset=0):
            task = Task.query.order_by(Task.id.desc()).slice(offset, offset).first()
            if task == None:
                abort(404, message='Task does not exist.')

            return jsonify(task.to_dict)

    api.add_resource(TaskListResource, '/tasks', '/tasks/<int:offset>')
