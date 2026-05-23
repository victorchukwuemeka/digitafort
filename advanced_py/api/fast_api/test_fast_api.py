"""Tests for the FastAPI course examples."""
from fastapi.testclient import TestClient
from fast_api_examples import app

client = TestClient(app)


def test_read_root():
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert "message" in data
    assert "docs" in data


def test_health_check():
    resp = client.get("/health/")
    assert resp.status_code == 200
    assert resp.json()["status"] == "healthy"


def test_create_and_get_item():
    resp = client.post("/items/", json={"name": "Laptop", "price": 999.99})
    assert resp.status_code == 201
    item_id = resp.json()["id"]

    resp = client.get(f"/items/{item_id}")
    assert resp.status_code == 200
    assert resp.json()["name"] == "Laptop"


def test_get_item_not_found():
    resp = client.get("/items/99999")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Item not found"


def test_list_items():
    resp = client.get("/items/")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_update_item():
    client.post("/items/", json={"name": "Phone", "price": 499.99})
    resp = client.put("/items/1", json={"name": "Phone Pro", "price": 699.99})
    assert resp.status_code == 200
    assert resp.json()["name"] == "Phone Pro"


def test_patch_item():
    resp = client.patch("/items/1", json={"price": 599.99})
    assert resp.status_code == 200


def test_delete_item():
    client.post("/items/", json={"name": "Temp", "price": 10.0})
    resp = client.delete("/items/1")
    assert resp.status_code == 204


def test_create_user():
    resp = client.post("/users/", json={
        "username": "johndoe",
        "email": "john@example.com",
        "age": 30,
    })
    assert resp.status_code == 201
    data = resp.json()
    assert data["username"] == "johndoe"
    assert "email" not in data  # filtered by response model


def test_custom_response():
    resp = client.get("/custom-response/")
    assert resp.status_code == 201
    assert resp.headers["x-custom-header"] == "custom-value"
