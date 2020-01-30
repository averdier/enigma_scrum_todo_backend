# coding: utf-8

from flask_restplus import reqparse


pagniation_parser = reqparse.RequestParser()
pagniation_parser.add_argument('key', help='Start key')
pagniation_parser.add_argument('limit', type=int, help='Items per parge')
