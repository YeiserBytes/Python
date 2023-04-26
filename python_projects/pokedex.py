from rich import print
import requests
import json


def get_pokemon(pokemon) -> dict:
    url = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}/')
    data = url.json()
    return data


def show_stats(pokemon) -> None:
    data = get_pokemon(pokemon)
    print('\nInformación del pokemon \n')
    print(f'Image: {data["sprites"]["front_default"]}')
    print(f'Name: [bold white]{data["name"]}[/bold white]')
    print(f'ID: Nº[bold white]{data["id"]}[/bold white]')
    print(f'Type: {data["types"][0]["type"]["name"]}')
    print(f'HP: {data["stats"][0]["base_stat"]}')
    print(f'Attack: {data["stats"][1]["base_stat"]}')
    print(f'Defense: {data["stats"][2]["base_stat"]}')
    print(f'Special Attack: {data["stats"][3]["base_stat"]}')
    print(f'Special Defense: {data["stats"][4]["base_stat"]}')
    print(f'Speed: {data["stats"][5]["base_stat"]}')
    print(f'Height: {data["height"]}')
    print(f'Weight: {data["weight"]}')


pokemon = input('Escribe el nombre del pokemon o el ID: ')
show_stats(pokemon)
