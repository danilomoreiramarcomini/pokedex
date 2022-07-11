import requests


def get_informations():
    types_list = list()
    abilities_list = list()
    moves_list = list()
    search = str(input("Name or id: ")).lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{search}"
    pokemon_search = requests.get(url)
    pokemon_search = pokemon_search.json()

    for move_pokemon in pokemon_search["moves"]:
        moves_list.append(move_pokemon["move"]["name"])

    for type_pokemon in pokemon_search["types"]:
        types_list.append(type_pokemon["type"]["name"])

    for ability_pokemon in pokemon_search["abilities"]:
        abilities_list.append(ability_pokemon["ability"]["name"])

    name_pokemon = str(f"{pokemon_search['name'].title()}")
    id_pokemon = str(f"{pokemon_search['id']}")
    sprite_pokemon = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id_pokemon}.png"
    print(f"Name: {name_pokemon}\nID: {id_pokemon}")

    for element in types_list:
        print(f"Type: {str(element).title()}")

    for element in abilities_list:
        print(f"Ability: {str(element).title()}")

    for element in moves_list:
        print(f"Move: {str(element).title()}")


get_informations()
