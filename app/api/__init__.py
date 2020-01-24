# coding: utf-8

import os
from flask import Blueprint
from flask_restplus import Api


blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(
    blueprint,
    title='Scrum API backend',
    description='Swagger documentation for Enigma Scrum todo backend',
    doc='/' if os.getenv('APP_CONFIG') == 'dev' else None
)

from .endpoints.todo import ns as todo_namespace  # noqa E402

api.add_namespace(todo_namespace)
