import pytest
from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_redirect(client):
    response = client.get("/home")
    assert response.status_code == 302
    assert response.location == "/"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Index</title>" in response.data


def test_trap(client):
    response = client.get("/trap")
    assert response.status_code == 200
    assert b"<title>You were warned...</title>" in response.data


def test_login(client):
    response = client.get("/magic")
    assert response.status_code == 200
    assert b"<title>Magic</title>" in response.data


def test_invalid_url(client):
    response = client.post("/dashboard")
    assert response.status_code == 405
