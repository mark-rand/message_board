from flaskr.db import get_db
import sqlite3
import pytest


def test_get_close_db(db_app):
    with db_app.app_context():
        db = get_db()
        assert db is get_db()
        modes = db.execute(
                "SELECT name, json"
                " FROM mode"
            ).fetchall()
    assert modes[0]['name'] == 'test'
    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute("SELECT 1")

    assert "closed" in str(e.value)
