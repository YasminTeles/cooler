from fastapi.testclient import TestClient

from cooler.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': "I'm working!"}


def test_add_register():
    register = {
        'type_beverage': "non-alcoholic",
        'amount': 5,
        'movement': "entry"
    }
    response = client.post("/history/register", json=register)
    assert response.status_code == 201
    assert response.json().get("id")
