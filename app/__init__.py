# coding: utf-8

from flask import Flask
from flask_cors import CORS
from config import config


def create_app(config_name: str = 'default') -> Flask:
    """Create Flask app

    Keyword Arguments:
        config_name {str} -- Configuration to use (default: {'default'})

    Returns:
        Flask -- Configured Flask app
    """
    app = Flask(__name__)
    CORS(app)

    target_config = config.get(config_name, config['default'])
    app.config.from_object(target_config)
    target_config.init_app(app)

    from .api import blueprint as api_blueprint

    app.register_blueprint(api_blueprint)

    return app
