import pytest
from app import app

def test_index_route(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>' in response.data  # Check if HTML content exists

def test_cart_route(client):
    """Test the cart route"""
    response = client.get('/cart')
    assert response.status_code == 200

def test_success_route(client):
    """Test the success route"""
    response = client.get('/success')
    assert response.status_code == 200

def test_app_instance():
    """Test if app instance is created properly"""
    assert app is not None
    assert app.config is not None