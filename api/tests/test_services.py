import pytest
import responses
from api.services.pokeapi import fetch_pokemon_list, fetch_pokemon_detail

BASE = "https://pokeapi.co/api/v2"

@responses.activate
def test_fetch_list_returns_json():
    url = f"{BASE}/pokemon"
    responses.add(
        responses.GET, url,
        json={"count":1, "results":[{"name":"p","url":f"{BASE}/pokemon/p/"}]},
        status=200
    )
    data = fetch_pokemon_list(offset=0, limit=1)
    assert data["count"] == 1

@responses.activate
def test_fetch_detail_error_raises():
    url = f"{BASE}/pokemon/p/"
    responses.add(responses.GET, url, status=404)
    with pytest.raises(Exception):
        fetch_pokemon_detail(url)
