#PrimerParcial
import requests

# Endpoint de la PokéAPI
url = "https://pokeapi.co/api/v2/pokemon?limit=20"

# Petición GET
response = requests.get(url)

# Validación del estado
if response.status_code == 200:
    data = response.json()
    pokemones = data["results"]

    # Recorrer la lista de pokemones
    for pokemon in pokemones:
        nombre = pokemon["name"]

        # Condición especial: empieza con "b" o "B"
        if nombre.lower().startswith("b"):
            print(f"[ESPECIAL] {nombre}")
        else:
            print(f"Nombre: {nombre}")

else:
    print("Error: No se pudo conectar a la API.")
    print(f"Código de estado: {response.status_code}")