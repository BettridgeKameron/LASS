"""
This is an example of how you could functional test parts of the backend together, such as API endpoints
"""

import pytest  # https://docs.pytest.org/en/8.0.x/

# Good resource to check out: https://testdriven.io/blog/flask-pytest/


def test_reverse_string(test_client):
    """Functional Test Example of checking the reverse_string endpoint"""
    test_string = "321CbA"
    # Make a POST request to the reverse_string endpoint
    response = test_client.post("/reverse_string", json={"string": test_string})
    # Assert the status code and the reversed string
    assert response.status_code == 200
    assert response.json == {"reversed_string": test_string[::-1]}


# TODO: Split test write prints into two separate tests


def test_generate_writeprint(test_client):
    """Functional Test Example of checking the writeprint endpoint"""
    # Make a POST request to the writeprint endpoint
    response = test_client.post(
        "/api/v1/authorship/writeprint", json={"text": "This is a test"}
    )
    # Assert the status code and the response
    assert response.status_code == 200
    assert response.json == {"text": "This is a test"}


def test_get_writeprint_results(test_client):
    """Functional Test Example of checking the writeprint endpoint"""
    # Make a POST request to the writeprint endpoint
    response = test_client.get("/api/v1/authorship/writeprint/1234")
    # Assert the status code and the response
    assert response.status_code == 200
    assert response.json == {"job_id": "1234"}


def test_rephrase(test_client):
    """Functional Test Example of checking the rephrase endpoint"""
    # Make a POST request to the rephrase endpoint
    response = test_client.post(
        "/api/v1/text/rephrase", json={"text": "This is a test"}
    )
    # Assert the status code and the response
    assert response.status_code == 200
    assert response.json == {"text": "This is a test"}


def test_obfuscate(test_client):
    """Functional Test Example of checking the obfuscate endpoint"""
    # Make a POST request to the obfuscate endpoint
    response = test_client.post(
        "/api/v1/text/obfuscate", json={"text": "This is a test"}
    )
    # Assert the status code and the response
    assert response.status_code == 200
    assert response.json == {"text": "This is a test"}


def test_sentiment_analysis(test_client):
    """Functional Test Example of checking the sentiment-analysis endpoint"""
    # Make a POST request to the sentiment-analysis endpoint
    response = test_client.post(
        "/api/v1/text/sentiment-analysis", json={"text": "This is a test"}
    )
    # Assert the status code and the response
    assert response.status_code == 200
    assert response.json == {"text": "This is a test"}


def test_predict_user_attributes(test_client):
    """Functional Test Example of checking the predict-user-attributes endpoint"""
    # Make a POST request to the predict-user-attributes endpoint
    response = test_client.post(
        "/api/v1/text/predict-user-attributes", json={"text": "This is a test"}
    )
    # Assert the status code and the response
    assert response.status_code == 200
    assert response.json == {"text": "This is a test"}


def test_health_endpoint(test_client):
    """Functional Test Example of checking the health endpoint"""
    # Make a GET request to the health endpoint
    response = test_client.get("/api/v1/health")
    # Assert the status code and the response
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
