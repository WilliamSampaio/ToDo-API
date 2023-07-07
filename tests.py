from typing import List
from starlette.testclient import TestClient

from main import app, ItemModel

client = TestClient(app)


def test_main_status_code():
    response = client.get('/')
    assert response.status_code == 200


def test_main_json():
    response = client.get('/')
    assert response.json() == {'hello': 'world'}


def test_main_todo_list_type():
    response = client.get('/todo')
    assert isinstance(response.json(), List)


def test_main_todo_list_item():
    response = client.get('/todo')
    json = response.json()
    item = ItemModel(titulo='', descricao='', status='')
    if len(json) > 0:
        assert json[0].keys() == dict(item).keys()
    assert True
