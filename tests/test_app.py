from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_root_returns_hello_message():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert 'Hello World from Optimus!' in response.get_data(as_text=True)


def test_health_endpoint_returns_expected_payload():
    client = app.test_client()
    response = client.get('/health')

    assert response.status_code == 200
    assert response.get_json() == {
        'status': 'healthy',
        'message': 'Optimus Python app is running',
        'version': '1.0',
    }


def test_info_endpoint_returns_expected_payload():
    client = app.test_client()
    response = client.get('/info')

    assert response.status_code == 200
    assert response.get_json() == {
        'app': 'Optimus Python Hello World',
        'deployed_via': 'GitHub Actions',
        'aws_region': 'us-west-2',
        'account': '137360334857',
    }
