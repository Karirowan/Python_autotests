import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'b82ec80af040650ab79e5759de084e08'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create_pok = {
    "name": "Хороший",
    "photo_id": -1
}
response_create = requests.post(url=f'{URL}/v2/pokemons', headers = HEADER, json = body_create_pok)
response_json = response_create.json()
print(response_json)

message = response_create.json()['id']



body_rename = {
    "pokemon_id": message,
    "name": "Лучше",
    "photo_id": -1
}
response_rename = requests.put(url=f'{URL}/v2/pokemons', headers = HEADER, json = body_rename)
response_json = response_rename.json()
print(response_json)



body_add = {
    "pokemon_id": message
}
response_add = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_add)
response_json = response_add.json()
print(response_json)