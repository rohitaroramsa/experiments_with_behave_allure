import pytest
from flask import Flask

# Create a test client
@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True

    @app.route('/name')
    def hello():
        return 'Hello, World!'

    with app.test_client() as client:
        yield client

# Test the hello endpoint
def test_hello(client):
    response = client.get('/name')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'
