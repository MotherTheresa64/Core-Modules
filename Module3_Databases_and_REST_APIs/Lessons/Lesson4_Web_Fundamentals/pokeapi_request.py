import requests

# Make a GET request to PokeAPI for Pikachu
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

if response.status_code == 200:
    data = response.json()
    name = data['name']
    height = data['height']
    abilities = [a['ability']['name'] for a in data['abilities']]
    print(f"Name: {name}, Height: {height}, Abilities: {abilities}")
else:
    print(f"Error: {response.status_code}")
