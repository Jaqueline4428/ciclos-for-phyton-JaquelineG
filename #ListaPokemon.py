#ListaPokemon
import requests

# URL de la API pública de Pokémon
url = "https://pokeapi.co/api/v2/pokemon"

# Realizar la petición GET
response = requests.get(url)
data = response.json()

# Obtener la lista de Pokémon (por defecto 20)
pokemon_list = data["results"]

# Mostrar solo el nombre de cada Pokémon
for pokemon in pokemon_list:
    print(pokemon["name"])