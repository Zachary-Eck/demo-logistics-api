from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_create_truck():
    response = client.post("/trucks", json={"driver_name":"Alice","capacity":10})
    assert response.status_code == 200
    data = response.json()
    assert data["driver_name"] == "Alice"
    assert "id" in data

def test_list_trucks():
    response = client.get("/trucks")
    assert response.status_code == 200
    data = response.json()
    assert "trucks" in data
    assert isinstance(data["trucks"], list)