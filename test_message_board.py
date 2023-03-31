#!/usr/bin/env python3
import os

import pytest
import json

from flaskr import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app({"TESTING": True,
                      "STATES": [
                          {'type': 'fixed',
                           'cols': [11111111111, 22222222222, 33333333333],
                           'message': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]},
                          {'type': 'text', 'message': '!', 'font': '1x11'},
                          {'type': 'text', 'message': '!', 'font': '1x8'},
                      ],
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
                                  "!": ["  oo    "]
                              }
                          }
                      }
                      })
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_get_next_state_0(client):
    response = client.get("/")
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert parsed['cols'] == [11111111111, 22222222222, 33333333333]
    assert parsed['message'] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                                 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]


def test_state_1_1x11_font(client):
    response = client.get("/?state=1")
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['cols']) == 1
    assert parsed['cols'][0] == "00011110000"
    assert parsed['message'] == [1]

def test_state_2_1x8_font(client):
    response = client.get("/?state=2")
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['cols']) == 1
    assert parsed['cols'][0] == "00011000000"
    assert parsed['message'] == [1]


def test_not_found(client):
    response = client.get('/?state=100')
    assert response.status_code == 200


def test_info_endpoint_returns_status(client):
    response = client.get("/info")
    assert response.status_code == 200
    assert b"Running" in response.data
