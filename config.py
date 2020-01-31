# coding: utf-8

import os
import secrets
from flask import Flask


class Config:
    """Base configuration
    """
    ADMINS = os.getenv('ADMINS', 'arthur.verdier@enigma-school.com')

    ENV = os.getenv('ENV', 'development')
    SECRET_KEY = os.getenv('APP_SECRET', secrets.token_urlsafe(16))
    NAME = os.getenv('APP_NAME', 'enigma_scrum_backend')

    PROVIDER_REGION = os.getenv('PROVIDER_REGION', 'eu-central-1')
    TODO_TABLE = os.getenv('TODO_TABLE', 'todo-table-dev')
    TODO_PER_PAGE = int(os.getenv('TODO_PER_PAGE', '35'))

    AUTH_POOL = os.getenv('AUTH_POOL', 'eu-central-1_3jLXINTS3')

    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = True
    JSON_SORT_KEYS = False

    @staticmethod
    def init_app(flask_app: Flask):
        """Initialize flask application

        Arguments:
            flask_app {Flask} -- Application to initialize
        """
        pass


class DevelopmentConfig(Config):
    """Development configuration
    """
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration
    """
    ENV = 'production'
    DEBUG = False


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}
