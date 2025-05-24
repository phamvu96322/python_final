from app import app
import pytest

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>' in response.data  # Check if HTML content exists

def test_cart_route(client):
    response = client.get('/cart')
    assert response.status_code == 200

def test_success_route(client):
    response = client.get('/success')
    assert response.status_code == 200

def test_app_instance():
    assert app is not None
    assert app.config is not None
