"""
Tests for the GET /activities endpoint.
"""

import pytest


def test_get_activities_returns_success(client):
    """Test that GET /activities returns status 200 and a dictionary."""
    # Arrange
    # No setup required beyond the client fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)


def test_get_activities_contains_all_fields(client):
    """Test that each activity has required fields."""
    # Arrange
    # No additional setup required beyond the client fixture

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for activity_name, activity_data in activities.items():
        assert isinstance(activity_name, str)
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)


def test_get_activities_has_default_activities(client):
    """Test that the default activities are present."""
    # Arrange
    expected_activities = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Soccer Team",
        "Basketball Club",
        "Art Studio",
        "Drama Club",
        "Math Olympiad",
        "Debate Team",
    ]

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for activity_name in expected_activities:
        assert activity_name in activities


def test_get_activities_participants_are_strings(client):
    """Test that all participant emails are strings."""
    response = client.get("/activities")
    activities = response.json()

    for activity_data in activities.values():
        for participant in activity_data["participants"]:
            assert isinstance(participant, str)
