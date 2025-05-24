import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"success" in response.data or b"<html" in response.data  # tùy nội dung HTML

def test_add_to_cart(client):
    response = client.get("/add-to-cart/1", follow_redirects=True)
    assert response.status_code == 200
    assert b"cart" in response.data or b"<html" in response.data

def test_cart(client):
    response = client.get("/cart")
    assert response.status_code == 200

def test_checkout(client):
    response = client.get("/success")
    assert response.status_code == 200
