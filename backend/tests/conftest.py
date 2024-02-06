import os
import pytest
from app import app


@pytest.fixture(scope="module")
def test_client():
    """Creates a test client."""
    app.config.update(
        {
            "TESTING": True,
        }
    )

    with app.test_client() as testing_client:
        yield testing_client
