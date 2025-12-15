import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    body = response.json()
    assert body["id"] == 1
    assert "email" in body
    assert "username" in body


def test_create_post():
    payload = {
        "title": "Automation Test",
        "body": "Testing API with pytest and requests",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    body = response.json()
    assert body["title"] == payload["title"]
    assert body["userId"] == 1
    assert "id" in body


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
