from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_create_job():
    response = client.post("/jobs/", json={"load_type":"Sand", "destination":"Example Co"})
    assert response.status_code == 200