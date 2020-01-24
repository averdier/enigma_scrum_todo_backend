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
