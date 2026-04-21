from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat():
    res = client.post("/api/chat", json={"message": "hello"})
    assert res.status_code == 200
    assert "Xin chào" in res.json()["response"]
