# coding: utf-8

from flask_restplus import fields
from .. import api

pagination_model = api.model('Pagination', {
    'current': fields.String(required=True, description='Current key'),
    'limit': fields.Integer(required=True, description='Items per page'),
    'next': fields.String(required=True, description='Next key')
})
