from flask import Flask
from flask_show.ext import site

def create_app():  # Factory principal

    app = Flask(__name__)
    site.init_app(app)

    return app
