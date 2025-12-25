"""
Tests for token-related endpoints.

These tests verify:
- Tokens can be added
- Tokens can be consumed
- Errors are handled correctly
"""

def test_add_tokens(client):
    # Create a user first
    response = client.post("/users", json={"email": "pytest@example.com"})
    user = response.json()
    user_id = user["id"]

    # Add tokens
    response = client.post(
        f"/tokens/add/{user_id}/5",
        params={"reason": "test"}
    )

    assert response.status_code == 200
    assert response.json()["tokens"] == 5


def test_consume_tokens(client):
    response = client.post("/users", json={"email": "consume@example.com"})
    user = response.json()
    user_id = user["id"]

    client.post(f"/tokens/add/{user_id}/3", params={"reason": "setup"})

    response = client.post(
        f"/tokens/consume/{user_id}/2",
        params={"reason": "usage"}
    )

    assert response.status_code == 200
    assert response.json()["tokens"] == 1


def test_consume_too_many_tokens(client):
    response = client.post("/users", json={"email": "fail@example.com"})
    user_id = response.json()["id"]

    response = client.post(
        f"/tokens/consume/{user_id}/1",
        params={"reason": "fail"}
    )

    assert response.status_code == 400
