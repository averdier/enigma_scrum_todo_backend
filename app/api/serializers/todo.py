# coding: utf-8

from flask_restplus import fields
from .import pagination_model, api


todo_model = api.model('Todo', {
    'content': fields.String(
        required=True,
        min_length=3,
        description='Content'
    )
})

todo_resource = api.inherit('Todo resource', todo_model, {
    'uuid': fields.String(required=True, description='Unique ID'),
    'created_at': fields.Float(required=True, description='Creation datetime')
})

todo_paginated_model = api.model('Todo paginated', {
    'todos': fields.List(
        fields.Nested(todo_resource),
        required=True,
        description='Todo list'
    ),
    'pagination': fields.Nested(
        pagination_model,
        required=True,
        description='Pagination'
    )
})
