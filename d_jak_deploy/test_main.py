
from fastapi.testclient import TestClient
import pytest
from main import app


client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}


# def test_method():
#     response = client.get('/method')
#     assert response.status_code == 200

# @pytest.mark.parametrize("name", ['Zenek', 'Marek', 'Alojzy Niezdąży'])
# def test_hello_name(name):
#     response = client.get(f'/hello/{name}')
#     assert response.status_code == 200
#     assert response.json() == {"msg": f"Hello {name}"}

def test_counter():
    response = client.get('/counter')
    assert response.status_code == 200
    
# def test_receive_something():
#     response = client.post("/dej/mi/coś", json={'first_key': 'some_value'})
#     assert response.json() == {"received": {'first_Key': 'some_value'},
#                              "constant_data": "python jest super"}

def test_receive_something():
    response = client.post("/patient", json={'name': 'some_value', 'surename': 'some_value'})
    assert response.status_code == 200
    assert response.json() == {"id": 0 ,"patient": {'name': 'some_value', 'surename': 'some_value'}}


def test_methods():
    response = client.get('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}

    response = client.post('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "POST"}
    
    response = client.delete('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "DELETE"}

    response = client.put('/method')
    assert response.status_code == 200
    assert response.json() == {"method": "PUT"}

