"""
Tests for the DELETE /activities/{activity_name}/participants/{email} endpoint.
"""

import pytest


def test_unregister_success(client):
    """Test successful unregistration of a student from an activity."""
    # Arrange
    email = "michael@mergington.edu"
    activity_name = "Chess Club"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]
    assert activity_name in data["message"]


def test_unregister_removes_participant_from_activity(client):
    """Test that unregister actually removes the participant from the activity list."""
    # Arrange
    email = "temporary@mergington.edu"
    activity_name = "Basketball Club"

    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    assert response.status_code == 200

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )
    assert response.status_code == 200

    # Assert
    response = client.get("/activities")
    activities = response.json()
    assert email not in activities[activity_name]["participants"]


def test_unregister_nonexistent_activity_returns_404(client):
    """Test that unregistering from a nonexistent activity returns a 404 error."""
    # Arrange
    email = "student@mergington.edu"
    activity_name = "Nonexistent Club"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()


def test_unregister_not_enrolled_student_returns_404(client):
    """Test that unregistering a student not enrolled in activity returns a 404 error."""
    # Arrange
    email = "notenrolled@mergington.edu"
    activity_name = "Chess Club"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not signed up" in data["detail"].lower()


def test_unregister_and_signup_again(client):
    """Test that a student can unregister and then sign up again."""
    # Arrange
    email = "versatile@mergington.edu"
    activity_name = "Soccer Team"

    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    assert response.status_code == 200

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )
    assert response.status_code == 200

    # Assert initial unregister
    response = client.get("/activities")
    activities = response.json()
    assert email not in activities[activity_name]["participants"]

    # Act again: sign up again
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    assert response.status_code == 200

    # Assert signup again
    response = client.get("/activities")
    activities = response.json()
    assert email in activities[activity_name]["participants"]
