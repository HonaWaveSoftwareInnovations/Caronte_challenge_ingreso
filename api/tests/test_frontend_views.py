import pytest
from django.test import Client

client = Client()

@pytest.mark.django_db
def test_index_renders_template(monkeypatch):
    monkeypatch.setattr(
        "api.services.pokeapi.fetch_pokemon_list",
        lambda offset, limit: {"count":1, "next":None, "previous":None,
                                "results":[{"name":"x","url":"u"}]}
    )
    monkeypatch.setattr(
        "api.services.pokeapi.fetch_pokemon_detail",
        lambda url: {"sprites":{"front_default":"img"}, "abilities":[]}
    )
    resp = client.get("/api/")
    assert resp.status_code == 200
    assert "Pokédex" in resp.content.decode()

@pytest.mark.django_db
def test_detail_view(monkeypatch):
    monkeypatch.setattr(
        "api.services.pokeapi.fetch_pokemon_detail",
        lambda url: {
            "name":"x",
            "sprites":{"front_default":"u"},
            "stats":[], "types":[],
            "abilities":[], "moves":[]
        }
    )
    resp = client.get("/api/pokemon/x/")
    assert resp.status_code == 200
    content = resp.content.decode()
    assert '<h1>' in content and 'X' in content
