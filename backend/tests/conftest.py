"""
Global test configuration.

This file provides fixtures that can be reused
across all test files.
"""

import sys
from pathlib import Path

# Add parent directory to path so app module can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

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
