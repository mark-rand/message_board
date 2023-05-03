import pytest
import json
from flaskr import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app({"TESTING": True,
                      })
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_info_endpoint_returns_status(client):
    response = client.get("/info")
    assert response.status_code == 200
    parsed_response = json.loads(response.data)
    assert parsed_response['running']
    assert parsed_response['test_mode']
    assert parsed_response['font_count'] > 3
