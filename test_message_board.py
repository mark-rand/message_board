#!/usr/bin/env python3
import os

import pytest
import json

from flaskr import create_app
from flaskr.colours import *


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app({"TESTING": True,
                      "STATES": [
                          {'type': 'fixed',
                           'cols': [11111111111, 22222222222, 33333333333],
                           'message': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]},
                          {'type': 'text', 'message': '!',
                              'font': '1x11', 'background': BLACK},
                          {'type': 'text', 'message': '!',
                              'font': '1x8', 'background': BLACK},
                          {'type': 'text', 'message': ' ',
                              'font': '1x8', 'background': BLACK},
                          {'type': 'ober'},
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
    assert len(parsed['cols']) == 2
    assert parsed['cols'][0] == "00011110000"
    assert parsed['message'] == [1]


def test_state_2_1x8_font(client):
    response = client.get("/?state=2")
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['cols']) == 2
    assert parsed['cols'][0] == "00001100000"
    assert parsed['message'] == [1]


def test_state_3_1x8_font_missing_char(client):
    response = client.get("/?state=3")
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['cols']) == 4
    assert parsed['cols'][0] == "0" * 11
    assert parsed['message'] == [1]

def test_odd_blue_even_red(client):
    response = client.get("/?state=4")
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['cols']) == 110


def test_not_found(client):
    response = client.get('/?state=100')
    assert response.status_code == 200


def test_info_endpoint_returns_status(client):
    response = client.get("/info")
    assert response.status_code == 200
    assert b"Running" in response.data

def test_get_uuid_returns_uuid(client):
    response = client.get("/uuid")
    assert response.status_code == 200
    assert len(response.data) == 36
