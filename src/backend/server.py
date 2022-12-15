#!/usr/bin/env python3
import os
import sys
import logging
from flask import Flask
from flask_restful import Api
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)

    try:
        _initialize_db(app)
    except Exception as e:
        logging.error('Database initialization failed: %s', e)
        sys.exit(1)

    # Setup CORS
    CORS(app)

    # Register api resources
    list_of_resource_and_endpoints = _register_api_resources(app)

    @app.route('/')
    def home():
        anchors = [
            f'<a href="{app_root}{ep}">{ep}</a>' for _, ep
            in list_of_resource_and_endpoints
        ]
        return '<br>'.join(anchors)

    return app


def _initialize_db(app):
    from backend.models.database import db   # pylint: disable=import-error
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()


def _register_api_resources(app):
    from backend.resources import TopicResource  # pylint: disable=import-error
    from backend.resources import NumericEntryResource  # pylint: disable=import-error

    api = Api(app)

    list_of_resources = [
        TopicResource,
        NumericEntryResource,
    ]

    list_of_resource_and_endpoints = [
        (res, '/api/v1/%s' % res.__name__.replace("Resource", "").lower()) for
        res in list_of_resources
    ]

    for res, ep in list_of_resource_and_endpoints:
        api.add_resource(res, ep)

    return list_of_resource_and_endpoints


if __name__ == '__main__':
    logging.info('Starting server...')

    config = {}
    config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'

    app_scheme = os.getenv('APP_SCHEME', 'http')
    app_host = os.getenv('APP_HOST', '127.0.0.1')
    app_port = os.getenv('APP_PORT', '8000')
    app_root = '%s://%s:%s' % (app_scheme, app_host, app_port)

    flask_app = create_app(config)
    flask_app.run(host=os.getenv('APP_HOST', app_host),
                  port=os.getenv('APP_PORT', app_port))
