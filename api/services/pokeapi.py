import requests
from django.conf import settings

BASE_URL = settings.POKEAPI_BASE_URL

def fetch_pokemon_list(offset=0, limit=20):
    """
    Devuelve el JSON de /pokemon?offset={offset}&limit={limit}
    """
    url = f"{BASE_URL}/pokemon"
    params = {'offset': offset, 'limit': limit}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def fetch_pokemon_detail(pokemon_url):
    """
    A partir de la URL completa del Pokémon, devuelve su JSON.
    """
    resp = requests.get(pokemon_url, timeout=10)
    resp.raise_for_status()
    return resp.json()
