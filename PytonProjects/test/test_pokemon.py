import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'b82ec80af040650ab79e5759de084e08'
HEADER = {'Content-Type' : 'application/json'}
TRAINER_ID = 13864

def test_status_code():
    response = requests.get(url=f'{URL}/v2/trainers')
    assert response.status_code == 200

def test_has_id():
    response_has_id = requests.get(url=f'{URL}/v2/trainers', params={'trainer_id':TRAINER_ID})
    assert response_has_id.json()["data"][0]["trainer_name"] == 'Karina'
