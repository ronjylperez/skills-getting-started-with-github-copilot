"""
Pytest configuration and fixtures for FastAPI test suite.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


# Initial activities data for resetting between tests
INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Team training and matches for the school soccer team",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 18,
        "participants": ["nina@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice drills, scrimmages, and basketball conditioning",
        "schedule": "Wednesdays and Fridays, 5:00 PM - 6:30 PM",
        "max_participants": 16,
        "participants": ["sebastian@mergington.edu"]
    },
    "Art Studio": {
        "description": "Painting, drawing, and sculpture projects for creative students",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["ava@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting, set design, and rehearsal time for school performances",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["liam@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Challenging math problems and competition preparation",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["sophia@mergington.edu"]
    },
    "Debate Team": {
        "description": "Speech practice, argument strategy, and debate tournaments",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["ethan@mergington.edu"]
    }
}


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the activities dictionary to initial state before each test."""
    activities.clear()
    activities.update(INITIAL_ACTIVITIES)


@pytest.fixture
def client():
    """Provide a TestClient for testing FastAPI endpoints."""
    return TestClient(app)
