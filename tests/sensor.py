from unittest.mock import patch

from fastapi import status
from fastapi.testclient import TestClient

from api_models.sensor import Write
from main import app

client = TestClient(app)


def test_create_item():
    response = client.post("/sensor/", json={"name": "Sensor1", "status": "active", "location": {}})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["detail"] == "Item successfully created."


def test_read_all_items():
    response = client.get("/sensor/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_read_item():
    item = Write(name="TestSensor", uid="1")
    with patch('main.sensors', new=[item]):
        response = client.get("/sensor/1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["uid"] == "1"


def test_read_item_not_found():
    response = client.get("/sensor/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_item():
    item = Write(name="TestSensor", uid="1")
    with patch('main.sensors', new=[item]):
        response = client.put("/sensor/1", json={"uid": "1", "name": "UpdatedSensor"})
        assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_item():
    item = Write(name="TestSensor", uid="1")
    with patch('main.sensors', new=[item]):
        response = client.delete("/sensor/1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == "Item successfully deleted."


def test_delete_item_not_found():
    response = client.delete("/sensor/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


