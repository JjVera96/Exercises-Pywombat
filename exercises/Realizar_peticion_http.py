import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/1/').json()
print('El nombre del pokemon es:', response['name'])