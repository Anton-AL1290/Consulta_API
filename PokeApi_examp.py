import requests

pokemon = input("Escribe el nombre de un Pokémon: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n--- Información del Pokémon ---")
    print(f"Nombre: {data['name'].capitalize()}")
    print(f"ID: {data['id']}")
    print(f"Altura: {data['height']}")
    print(f"Peso: {data['weight']}")

    print("Tipos:")
    for tipo in data["types"]:
        print(f"- {tipo['type']['name']}")

else:
    print("Pokémon no encontrado.")