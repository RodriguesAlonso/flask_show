from flask import Flask
from flask_show.ext import site
from flask_show.ext import toolbar
from flask_show.ext import config

def create_app():  # Factory principal

    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
