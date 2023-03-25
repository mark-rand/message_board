#!/usr/bin/env python3
import os

import pytest
import json

from flaskr import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app({"TESTING": True})
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_get_next_no_data(client):
    response = client.get("/")
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert parsed['hello'] == 'world'
