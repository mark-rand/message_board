import json
from flaskr.db import get_db


def test_modes(db_client, db_app):
    with db_app.app_context():
        get_db().execute('DELETE FROM mode')
        response = db_client.get("/modes")
        assert response.status_code == 200
        assert json.loads(response.data) == []
        new_mode = json.dumps({'hello': 'world'})
        response = db_client.post("/modes/new_mode", json=new_mode)
        assert response.status_code == 201
        response = db_client.get("/modes")
        assert response.status_code == 200
        assert json.loads(response.data) == ['new_mode']
        response = db_client.get("/modes/new_mode")
        assert response.status_code == 200
        assert json.loads(response.data) == new_mode
        response = db_client.post("/modes/new_mode", json=new_mode)
        updated_mode = json.dumps({'new': 'world'})
        response = db_client.put("/modes/new_mode", json=updated_mode)
        assert response.status_code == 201
        response = db_client.get("/modes/new_mode")
        assert response.status_code == 200
        assert json.loads(response.data) == updated_mode


def test_update_non_existent(db_client):
    json_data = json.dumps({'hello': 'world'})
    response = db_client.put("/modes/non_existent", json=json_data)
    assert response.status_code == 404


def test_get_non_existent(db_client):
    response = db_client.get("/modes/non_existent")
    assert response.status_code == 404


def test_invalid_json(db_client):
    response = db_client.post("/modes/hello", data="meh{}")
    assert response.status_code == 400
