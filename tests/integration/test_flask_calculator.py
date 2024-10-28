import pytest
from app import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_add_api(client):
    response = client.post('/add', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 15

def test_subtract_api(client):
    response = client.post('/subtract', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 5

def test_multiply_api(client):
    response = client.post('/multiply', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 50

def test_divide_api(client):
    response = client.post('/divide', json={'a': 10, 'b': 2})
    assert response.status_code == 200
    assert response.get_json()['result'] == 5

def test_divide_by_zero_api(client):
    response = client.post('/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400
    assert 'Cannot divide by zero!' in response.get_json()['error']
