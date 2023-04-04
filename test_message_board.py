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
                      "MODES": {
                          'fixed': [{'type': 'fixed',
                                    'repeat': ["11111111111", "22222222222", "33333333333"]}],
                          'exclaim_1x11': [{'type': 'text', 'message': '!',
                                           'font': '1x11', 'background': BLACK}],
                          'exclaim_1x8': [{'type': 'text', 'message': '!',
                                          'font': '1x8', 'background': BLACK}],
                          'simple_multi': [{'type': 'text', 'message': 'x',
                                            'font': '1x8', 'background': BLACK}, {'type': 'text', 'message': 'z',
                                                                                  'font': '1x8', 'background': BLACK}],
                          'space_1x8': [{'type': 'text', 'message': ' ',
                                        'font': '1x8', 'background': BLACK}],
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
                      }
                      })
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def initialise(client, mode):
    response = client.get(f"/init?mode={mode}")
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert len(response_data['id']) == 36
    return str(response_data['id'])


def test_state_invalid(client):
    response = client.get("/next")
    assert response.status_code == 422


def test_state_not_found(client):
    response = client.get("/next?id=db2d63b9-c1d5-4726-9977-3e3cecc3e745")
    assert response.status_code == 404


def test_mode_not_found(client):
    response = client.get(f"/init?mode={'non-existent-mode'}")
    assert response.status_code == 422


def test_mode_fixed(client):
    size = 2
    uuid = initialise(client, "fixed")
    assert (len(uuid) == 36)
    response = get_next_chunk(client, uuid, size)
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['chunks']) == 1
    assert len(parsed['chunks'][0]) == size
    assert parsed['chunks'][0] == ["11111111111", "22222222222"]
    size = 6
    response = get_next_chunk(client, uuid, size)
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['chunks']) == 1
    assert len(parsed['chunks'][0]) == size
    assert parsed['chunks'][0] == ["33333333333", "11111111111",
                                   "22222222222", "33333333333", "11111111111", "22222222222"]


def get_next_chunk(client, uuid, size=1):
    return client.get(f"/next?id={uuid}&chunk_size={size}")


def test_mode_1_1x11_font(client):
    uuid = initialise(client, "exclaim_1x11")
    response = get_next_chunk(client, uuid)
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['chunks']) == 1
    assert parsed['chunks'][0][0] == "00011110000"


def test_mode_2_1x8_font(client):
    uuid = initialise(client, "exclaim_1x8")
    response = get_next_chunk(client, uuid)
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['chunks']) == 1
    assert parsed['chunks'][0][0] == "00001100000"


def test_simple_multi(client):
    uuid = initialise(client, "simple_multi")
    response = get_next_chunk(client, uuid, 4)
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['chunks']) == 1
    assert len(parsed['chunks'][0]) == 4
    assert parsed['chunks'][0][0] == "00111111110"
    assert parsed['chunks'][0][1] == "0" * 11
    assert parsed['chunks'][0][2] == "00001010000"
    assert parsed['chunks'][0][3] == "0" * 11


def test_mode_3_1x8_font_missing_char(client):
    uuid = initialise(client, "space_1x8")
    response = get_next_chunk(client, uuid)
    assert response.status_code == 200
    parsed = json.loads(response.data)
    assert len(parsed['chunks']) == 1
    assert parsed['chunks'][0][0] == "0"*11


def test_info_endpoint_returns_status(client):
    response = client.get("/info")
    assert response.status_code == 200
    assert b"Running" in response.data


def test_get_uuid_returns_uuid(client):
    response = client.get("/uuid")
    assert response.status_code == 200
    assert len(response.data) == 36
