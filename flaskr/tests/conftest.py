import os
import tempfile

import pytest
from flaskr import colours

from flaskr import create_app
from flaskr.db import get_db
from flaskr.db import init_db

# read in SQL for populating test data
with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


@pytest.fixture
def db_app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({"TESTING": True, "DATABASE": db_path,
                     "FONT_OVERRIDE": True,
                      "MODES": {
                          'exclaim_1x11': [{'type': 'text', 'message': '!',
                                           'font': '1x11', 'background': colours.black}],
                          'exclaim_1x8': [{'type': 'text', 'message': '!',
                                          'font': '1x8', 'background': colours.black}],
                          'simple_multi': [{'type': 'text', 'message': 'x',
                                            'font': '1x8', 'background': colours.black}, {'type': 'text', 'message': 'z',
                                                                                          'font': '1x8', 'background': colours.black}],
                          'space_1x8': [{'type': 'text', 'message': ' ',
                                        'font': '1x8', 'background': colours.black}],
                      },
                      "FONTS": {
                          "1x11": {
                              "name": "1x8", "height": 11,
                              "characters": {
                                  "!": ["   oooo    "]
                              }
                          },
                          "1x8": {
                              "name": "1x8", "height": 8,
                              "characters": {
                                  "!": ["  oo    "],
                                  "x": ["oooooooo"],
                                  "z": ["  o o   "],
                              }
                          }
                      }})

    # create the database and load test data
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def db_client(db_app):
    """A test client for the app."""
    return db_app.test_client()
