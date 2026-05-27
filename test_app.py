import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the main route"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello World from Optimus!' in rv.data
    assert b'Version:' in rv.data

def test_health_check(client):
    """Test health check endpoint"""
    rv = client.get('/health')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['status'] == 'healthy'
    assert data['message'] == 'Optimus Python app is running'
    assert 'version' in data

def test_info_endpoint(client):
    """Test info endpoint"""
    rv = client.get('/info')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['app'] == 'Optimus Python Hello World'
    assert data['deployed_via'] == 'GitHub Actions'
    assert data['aws_region'] == 'us-west-2'
    assert data['account'] == '137360334857'