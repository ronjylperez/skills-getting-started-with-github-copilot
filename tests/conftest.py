"""
Pytest configuration and fixtures for FastAPI test suite.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Provide a TestClient for testing FastAPI endpoints."""
    return TestClient(app)
