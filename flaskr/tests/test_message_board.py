#!/usr/bin/env python3
import pytest
import json

from flaskr import create_app
import flaskr.colours as colours
from flaskr.bin_string_utils import discard_first_column, get_column_at, string_to_columns, columns_to_string, string_to_bin


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app({"TESTING": True,
                      "FONT_OVERRIDE": True,
                      "MODES": {
                          'fixed': [{'type': 'fixed',
                                     'repeat': [[3]*11, [128]*11, [3]*11]}],
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
    next_chunk = get_next_chunk(client, uuid, size)
    assert next_chunk['status_code'] == 200
    parsed = next_chunk['data']
    print(f'PARSED {parsed}')
    assert len(parsed) == 1
    assert len(parsed[0]) == size
    assert parsed[0] == [[3]*11, [128]*11]
    size = 6

    next_chunk = get_next_chunk(client, uuid, size)
    assert next_chunk['status_code'] == 200
    parsed = next_chunk['data']
    assert len(parsed) == 1
    assert len(parsed[0]) == size
    assert parsed[0] == [[3]*11, [3] *
                         11, [128]*11, [3]*11, [3]*11, [128]*11, ]


def get_next_chunk(client, uuid, size=1):
    response = client.get(f"/next?id={uuid}&chunk_size={size}")
    parsed = json.loads(response.data)
    data = parsed['chunks']
    chunks = []
    for chunk in data:
        chunks.append(string_to_columns(chunk))
    return {'status_code': response.status_code, 'data': chunks}


def test_columns_to_string():
    columns = []
    columns.append([1, 2, 3])
    c2s = columns_to_string(columns)
    assert c2s == 'AQID'
    assert string_to_columns(c2s, height=3) == columns
    columns = [[255, 128, 1], [111, 222, 123], [1, 2, 3]]
    c2s = columns_to_string(columns)
    assert c2s == '/4ABb957AQID'
    assert string_to_columns(c2s, height=3) == columns
    chunks_bin = string_to_bin(c2s)
    next_chunk = get_column_at(chunks_bin, 0, height=3)
    assert next_chunk == b"\xFF\x80\x01"
    next_chunk = get_column_at(chunks_bin, 1, height=3)
    assert next_chunk == b"\x6F\xDE\x7B"
    chunks_bin = discard_first_column(chunks_bin, height=3)
    assert len(chunks_bin) == 6
    assert get_column_at(chunks_bin, 0, height=3) == b"\x6F\xDE\x7B"


def test_mode_1_1x11_font(client):
    uuid = initialise(client, "exclaim_1x11")
    next_chunk = get_next_chunk(client, uuid)
    assert next_chunk['status_code'] == 200
    parsed = next_chunk['data']
    assert len(parsed) == 1
    assert parsed[0][0] == [colours.black] * \
        3 + [colours.blue]*4 + [colours.black] * 4


def test_mode_2_1x8_font(client):
    uuid = initialise(client, "exclaim_1x8")
    next_chunk = get_next_chunk(client, uuid)
    assert next_chunk['status_code'] == 200
    parsed = next_chunk['data']
    assert len(parsed) == 1
    assert parsed[0][0] == [colours.black] * \
        4 + [colours.blue]*2 + [colours.black] * 5


def test_simple_multi(client):
    uuid = initialise(client, "simple_multi")
    next_chunk = get_next_chunk(client, uuid, 4)
    assert next_chunk['status_code'] == 200
    parsed = next_chunk['data']
    assert len(parsed) == 1
    assert len(parsed[0]) == 4
    assert parsed[0][0] == [colours.black] * \
        2 + [colours.blue] * 8 + [colours.black] * 1
    assert parsed[0][1] == [0] * 11
    assert parsed[0][2] == [colours.black] * \
        4 + [colours.blue, colours.black, colours.blue] + [colours.black] * 4
    assert parsed[0][3] == [0] * 11


def test_mode_3_1x8_font_missing_char(client):
    uuid = initialise(client, "space_1x8")
    next_chunk = get_next_chunk(client, uuid)
    assert next_chunk['status_code'] == 200
    parsed = next_chunk['data']
    assert len(parsed) == 1
    assert parsed[0][0] == [0] * 11


def test_get_uuid_returns_uuid(client):
    response = client.get("/uuid")
    assert response.status_code == 200
    assert len(response.data) == 36
