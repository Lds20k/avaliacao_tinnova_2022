import os
import pytest
from application import create_app

@pytest.fixture()
def app():
    app = create_app(test=True)
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here
    os.remove('test.db')


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def create_vehicle():
    return {
        "nome": "carro1",
        "marca": "ford",
        "cor": "preta",
        "ano": "2002",
        "descricao": "Um carro",
        "vendido": True
    }

def test_success_create_vehicle(client):
    response = client.post("/veiculos", json=create_vehicle())
    assert response.status_code == 201

def test_fail_unprocessable_entity_create_vehicle(client):
    response = client.post("/veiculos", data={"invalid": "invalid"})
    assert response.status_code == 422

def test_fail_incorrect_body_create_vehicle(client):
    response = client.post("/veiculos", json={"invalid": "invalid"})
    assert response.status_code == 400

def test_success_create_vehicle(client):
    vehicle = create_vehicle()
    vehicle["marca"] = "invalid"

    response = client.post("/veiculos", json=vehicle)
    assert response.status_code == 400

def test_success_consult_vehicle(client):
    response = client.get("/veiculos/1")
    assert response.status_code == 200


def test_fail_not_foud_consult_vehicle(client):
    response = client.get("/veiculos/2")
    assert response.status_code == 404

def test_success_consult_vehicle(client):
    response = client.get("/veiculos")
    assert response.status_code == 200

def test_fail_invalid_brand_consult_vehicle(client):
    response = client.get("/veiculos", query_string={"marca": "invalid"})
    assert response.status_code == 400

def test_success_update_put_vehicle(client):
    vehicle = create_vehicle()
    vehicle["nome"] = "carro1"
    response = client.put("/veiculos/1", json=vehicle)
    assert response.status_code == 200

def test_fail_unprocessable_entity_create_vehicle(client):
    response = client.put("/veiculos/1", data={"invalid": "invalid"})
    assert response.status_code == 422

def test_success_update_patch_vehicle(client):
    vehicle = create_vehicle()
    vehicle["nome"] = "carro2"
    response = client.patch("/veiculos/1", json=vehicle)
    assert response.status_code == 200

def test_fail_incorrect_body_update_put_vehicle(client):
    vehicle = {}
    vehicle["invalid"] = "invalid"
    response = client.put("/veiculos/1", json=vehicle)
    assert response.status_code == 400

def test_fail_incorrect_body_update_patch_vehicle(client):
    vehicle = {}
    vehicle["invalid"] = "invalid"
    response = client.patch("/veiculos/1", json=vehicle)
    assert response.status_code == 400

def test_delete_vehicle(client):
    response = client.delete("/veiculos/1")
    assert response.status_code == 200