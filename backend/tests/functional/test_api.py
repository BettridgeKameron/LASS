"""
This is an example of how you could functional test parts of the backend together, such as API endpoints
"""

import pytest  # https://docs.pytest.org/en/8.0.x/

# Good resource to check out: https://testdriven.io/blog/flask-pytest/


def test_rev_str():
    """Example of importing a function to do a unit test"""
    from app import rev_str

    assert rev_str("hello") == "olleh", "Should reverse a normal string"
    assert rev_str("") == "", "Should handle empty string"
    assert rev_str("12345") == "54321", "Should reverse numeric strings"
    assert (
        rev_str("hello, hi!") == "!ih ,olleh"
    ), "Should reverse strings with punctuation and spaces"


def test_reverse_string(test_client):
    """Functional Test Example of checking the reverse_string endpoint"""
    test_string = "321CbA"
    # Make a POST request to the reverse_string endpoint
    response = test_client.post("/reverse_string", json={"string": test_string})
    # Assert the status code and the reversed string
    assert response.status_code == 200
    assert response.json == {"reversed_string": test_string[::-1]}
