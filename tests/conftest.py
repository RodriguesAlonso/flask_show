import pytest
from flask_show.app import create_app

@pytest.fixture(scope="module")
def app():
    """Instance of Main flask app"""
    return create_app()