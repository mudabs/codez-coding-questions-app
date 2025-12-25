"""
Global test configuration.

This file provides fixtures that can be reused
across all test files.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """
    Provides a TestClient instance for making
    HTTP requests to the FastAPI app.
    """
    return TestClient(app)
