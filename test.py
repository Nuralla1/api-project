from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_sum_numbers():
    response = client.get("/sum1n/{number}")
    assert response.status.code == 200
    assert response.json() = {"result":sum}

def test_fibo():
    response = client.get("/fibo")
    assert response.status_code == 200
    assert response.json() == {"result": n2}

def test_reverse():
    response = client.post("/reverse")
    assert response.status_code == 200
    assert response.json() == {"result": word[:: -1]}

def test_update_list():
    response = client.post("/list")
    assert response.status_code == 200
    assert response.json() == {"result": elements}

def test_show_list():
    response = client.post("/list")
    assert response.status_code == 200
    assert response.json() == {"result": elements}

def test_calculator():
    response = client.post("/calculator")
    assert response.status_code == 200
    assert response.json() == {"result": result}