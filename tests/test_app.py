import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Book service is alive!"}

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data.decode() == "OK"

def test_ready(client):
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.data.decode() == "READY"
