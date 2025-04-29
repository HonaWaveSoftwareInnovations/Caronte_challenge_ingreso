import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_api_list_pagination(monkeypatch):
    monkeypatch.setattr(
        "api.services.pokeapi.fetch_pokemon_list",
        lambda offset, limit: {
            "count":2, "next":None, "previous":None,
            "results":[{"name":"a","url":"u"},{"name":"b","url":"v"}]
        }
    )
    monkeypatch.setattr(
        "api.services.pokeapi.fetch_pokemon_detail",
        lambda url: {"sprites":{"front_default":"s"}, "abilities":[1,2]}
    )
    resp = client.get("/api/pokemon/?page=1&page_size=2")
    assert resp.status_code == 200
    body = resp.json()
    assert body["count"] == 2
    assert len(body["results"]) == 2

@pytest.mark.django_db
def test_api_search_not_found(monkeypatch):
    monkeypatch.setattr(
        "api.services.pokeapi.fetch_pokemon_detail",
        lambda url: (_ for _ in ()).throw(Exception())
    )
    resp = client.get("/api/pokemon/?search=none")
    assert resp.status_code == 200
    assert resp.json()["count"] == 0
