# coding: utf-8

from flask_restplus import Namespace, Resource, abort


ns = Namespace('todo', description='Todo related operations.')


@ns.route('')
class TodoResource(Resource):

    def get(self):
        """Get todo list
        """
        abort(418, 'Not implemented yet')

    def post(self):
        """Add todo
        """
        abort(418, 'Not implemented yet')


@ns.route('/<todo_id>')
class TodoItemResource(Resource):

    def delete(self, todo_id):
        """Delete todo by ID

        Arguments:
            todo_id {[type]} -- Todo unique ID
        """
        abort(418, 'Not implemented yet')
