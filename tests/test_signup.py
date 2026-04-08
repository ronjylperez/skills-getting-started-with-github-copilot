"""
Tests for the POST /activities/{activity_name}/signup endpoint.
"""

import pytest


def test_signup_success(client):
    """Test successful signup of a student for an activity."""
    email = "newstudent@mergington.edu"
    activity_name = "Chess Club"

    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]
    assert activity_name in data["message"]


def test_signup_adds_participant_to_activity(client):
    """Test that signup actually adds the participant to the activity list."""
    email = "newstudent@mergington.edu"
    activity_name = "Programming Class"

    # Signup
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    assert response.status_code == 200

    # Verify participant was added
    response = client.get("/activities")
    activities = response.json()
    assert email in activities[activity_name]["participants"]


def test_signup_duplicate_email_returns_400(client):
    """Test that signing up the same email twice returns a 400 error."""
    email = "michael@mergington.edu"
    activity_name = "Chess Club"

    # First signup is already in the default data, so attempt to signup again
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "already signed up" in data["detail"].lower()


def test_signup_nonexistent_activity_returns_404(client):
    """Test that signing up for a nonexistent activity returns a 404 error."""
    email = "student@mergington.edu"
    activity_name = "Nonexistent Club"

    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()


def test_signup_multiple_different_activities(client):
    """Test that a student can sign up for multiple different activities."""
    email = "versatile@mergington.edu"
    activities = ["Chess Club", "Drama Club", "Math Olympiad"]

    for activity_name in activities:
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        assert response.status_code == 200

    # Verify all signups were recorded
    response = client.get("/activities")
    activities_data = response.json()
    for activity_name in activities:
        assert email in activities_data[activity_name]["participants"]
