from flask import Flask
from flask.ext.bootstrap import Bootstrap, StaticCDN
from flask.ext.sqlalchemy import SQLAlchemy

from config import Configuration
from router import route, add_filters


def setup_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    return app


def setup_bootstrap(app):
    Bootstrap(app)
    app.extensions['bootstrap']['cdns']['bootstrap'] = StaticCDN()
    return app


def setup_database(app):
    db = SQLAlchemy(app)
    return db


def setup_routes(app):
    route(app)
    add_filters(app)
