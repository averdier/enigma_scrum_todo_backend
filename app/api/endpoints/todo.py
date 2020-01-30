# coding: utf-8

from flask import request, current_app
from flask_restplus import Namespace, Resource, abort
from werkzeug.exceptions import HTTPException
from ..serializers.todo import todo_model, todo_resource, todo_paginated_model
from ..parsers import pagniation_parser
from ...models import Todo


ns = Namespace('todo', description='Todo related operations.')


@ns.route('')
class TodoResource(Resource):

    @ns.marshal_with(todo_paginated_model)
    @ns.expect(pagniation_parser)
    def get(self):
        """Get todo list
        """
        owner = 'fixture'
        args = pagniation_parser.parse_args()

        limit = args['limit'] if args['limit'] is not None\
            else current_app.config['TODO_PER_PAGE']

        if limit <= 0:
            limit = current_app.config['TODO_PER_PAGE']

        key = None
        if args['key'] is not None:
            key = {
                'owner': {'S': owner},
                'created_at': {'N': args['key']}
            }

        try:
            iterator = Todo.query(
                owner,
                scan_index_forward=False,
                consistent_read=True,
                last_evaluated_key=key,
                limit=limit
            )

            result = {
                'todos': [todo for todo in iterator],
                'pagination': {
                    'current': args['key'],
                    'limit': limit,
                    'next': None
                }
            }

            last_key = iterator.last_evaluated_key
            if last_key is not None\
                    and last_key['created_at']['N'] != args['key']\
                    and len(result['todos']) > 0:
                last_item = result['todos'][len(result['todos']) - 1]
                if last_item.created_at == last_key['created_at']['N']:
                    result['pagination']['next'] = last_key['created_at']['N']

            return result

        except Exception as ex:
            current_app.logger.error(f'Unable to get todo list : {ex}')
            abort(400, 'Unable to get todo list, please try again later')

    @ns.marshal_with(todo_resource)
    @ns.expect(todo_model)
    def post(self):
        """Add todo
        """
        owner = 'fixture'
        payload = request.json

        todo = Todo(
            owner=owner,
            content=payload['content']
        )

        try:
            todo.save()

            return todo

        except Exception as ex:
            current_app.logger.error(f'Unable to create todo : {ex}')
            abort(400, 'Unable to create todo, please try again later')


@ns.route('/<todo_id>')
class TodoItemResource(Resource):

    @ns.expect(todo_model)
    @ns.marshal_with(todo_resource)
    def put(self, todo_id: str):
        """Update todo

        Arguments:
            todo_id {str} -- Todo unique ID
        """
        owner = 'fixture'
        payload = request.json

        try:
            query = [t for t in Todo.query(owner, Todo.uuid == todo_id)]
            if len(query) == 0:
                abort(404, 'Todo not found')

            if len(query) > 1:
                current_app.logger.info(
                    f'Too many todo for {owner} : {todo_id}'
                )

            todo = query[0]
            todo.content = payload['content']
            todo.save()

            return todo

        except HTTPException as ex:
            raise ex

        except Exception as ex:
            current_app.logger.error(f'Unable to patch todo : {ex}')
            abort(404, 'Unable to patch todo, please try again later')

    @ns.response(204, 'Todo successfully deleted')
    def delete(self, todo_id: str):
        """Delete todo by ID

        Arguments:
            todo_id {str} -- Todo unique ID
        """
        owner = 'fixture'

        try:
            query = [t for t in Todo.query(owner, Todo.uuid == todo_id)]
            if len(query) == 0:
                abort(404, 'Todo not found')

            with Todo.batch_write() as batch:
                for todo in query:
                    batch.delete(todo)

            return 'Todo successfully deleted', 204

        except HTTPException as ex:
            raise ex

        except Exception as ex:
            current_app.logger.error(f'Unable to delete todo : {ex}')
            abort(404, 'Unable to delete todo, please try again later')
