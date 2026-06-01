"""
Tests for the Churn Prediction API.

Run with:
    pytest tests/ -v
    pytest tests/ -v --cov=app --cov=main --cov-report=term-missing
"""

import pytest
from app.model_utils import predict_churn
from litestar.testing import TestClient
from main import app
# ---------------------------------------------------------------------------
# Function Tests
# ---------------------------------------------------------------------------


# TODO 1: Write a test that calls predict_churn() directly with sample features
#         and asserts the result is 0 or 1
#         Hint: import predict_churn from app.model_utils
def test_predict_churn(
    sample=[
        619,
        "France",
        "Female",
        42,
        2,
        0.0,
        1,
        1,
        1,
        101348.88,
    ],
):
    assert predict_churn(sample) == 0 or predict_churn(sample) == 1


# TODO 2 (bonus): Write another function test with a `with pytest.raises(...):`
def test_predict_churn_invalid_input():
    with pytest.raises(ValueError):
        predict_churn("invalid input")


# ---------------------------------------------------------------------------
# Endpoint Tests
# ---------------------------------------------------------------------------


# TODO 3: Write a test that POSTs to /predict with valid JSON
#         and checks the status code and response body
#         Hint: Litestar POST returns 201, not 200
#         Hint: use `with TestClient(app=app) as client:`
def test_predict_endpoint():
    with TestClient(app=app) as client:
        response = client.post(
            "/predict",
            json={
                "CreditScore": 619,
                "Geography": "France",
                "Gender": "Female",
                "Age": 42,
                "Tenure": 2,
                "Balance": 0.0,
                "NumOfProducts": 1,
                "HasCrCard": 1,
                "IsActiveMember": 1,
                "EstimatedSalary": 101348.88,
            },
        )
        assert response.status_code == 201
        assert "prediction" in response.json()


# TODO 4: Write a test for GET /health
def test_health_endpoint():
    with TestClient(app=app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


# TODO 5: Write a test for GET /
def test_home_endpoint():
    with TestClient(app=app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert "Welcome" in response.json().get("message", "")


# TODO 6 (bonus): Test that invalid input returns status 400
def test_predict_endpoint_invalid_input():
    with TestClient(app=app) as client:
        response = client.post(
            "/predict",
            json={
                "CreditScore": "ay7aga",
                "Geography": "France",
                "Gender": "Female",
                "Age": 42,
                "Tenure": 2,
                "Balance": 0.0,
                "NumOfProducts": 1,
                "HasCrCard": 1,
                "IsActiveMember": 1,
                "EstimatedSalary": 101348.88,
            },
        )
        assert response.status_code == 400
