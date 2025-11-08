import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Welcome to CI/CD with Flask!"

def test_square(client):
    response = client.get("/square/4")
    assert response.status_code == 200
    assert response.json["square"] == 16
