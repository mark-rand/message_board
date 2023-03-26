#!/usr/bin/env python3
import os

import pytest
import json

from flaskr import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app({"TESTING": True, "STATES": [
                     {'type': 'text', 'text': 'This is a test'}]})
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_get_next_no_data(client):
    response = client.get("/")
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert parsed['cols'] == [11111111111,22222222222,33333333333]
    assert parsed['message'] == [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]

def test_info_endpoint_returns_status(client):
    response = client.get("/info")
    assert response.status_code == 200
    assert b"Running" in response.data