# api/views.py

from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response

import api.services.pokeapi as pokeapi
from .serializers import PokemonListSerializer, PokemonDetailSerializer


class PokemonViewSet(viewsets.ViewSet):
    """
    ViewSet para listar y recuperar Pokémon usando PokéAPI.
    """

    def list(self, request):
        # Soporta búsqueda exacta con param 'search'
        search_query = request.query_params.get('search')
        if search_query:
            url = f"{settings.POKEAPI_BASE_URL}/pokemon/{search_query.lower()}"
            try:
                detail = pokeapi.fetch_pokemon_detail(url)
                item = {
                    'name': detail['name'],
                    'url': url,
                    'sprite': detail['sprites']['front_default'],
                    'abilities_count': len(detail['abilities']),
                }
            except Exception:
                return Response({
                    'count': 0,
                    'next': None,
                    'previous': None,
                    'results': []
                }, status=status.HTTP_200_OK)

            serializer = PokemonListSerializer([item], many=True)
            return Response({
                'count': 1,
                'next': None,
                'previous': None,
                'results': serializer.data
            })

        # Paginación manual
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 10))
        offset = (page - 1) * page_size

        data = pokeapi.fetch_pokemon_list(offset=offset, limit=page_size)
        enriched = []
        for item in data['results']:
            detail = pokeapi.fetch_pokemon_detail(item['url'])
            enriched.append({
                'name': item['name'],
                'url': item['url'],
                'sprite': detail['sprites']['front_default'],
                'abilities_count': len(detail['abilities']),
            })

        serializer = PokemonListSerializer(enriched, many=True)
        return Response({
            'count': data['count'],
            'next': data['next'],
            'previous': data['previous'],
            'results': serializer.data
        })

    def retrieve(self, request, pk=None):
        url = f"{settings.POKEAPI_BASE_URL}/pokemon/{pk}"
        try:
            detail = pokeapi.fetch_pokemon_detail(url)
        except Exception:
            return Response(
                {'detail': 'Pokémon no encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PokemonDetailSerializer({'detail': detail})
        return Response(serializer.data)


# ------------------ VISTAS DE FRONTEND ------------------

def index(request):
    """
    Renderiza la lista paginada y buscable de Pokémon.
    """
    search = request.GET.get('search')
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 10))

    if search:
        try:
            detail = pokeapi.fetch_pokemon_detail(
                f"{settings.POKEAPI_BASE_URL}/pokemon/{search.lower()}"
            )
            pokemons = [{
                'name': detail['name'],
                'sprite': detail['sprites']['front_default'],
                'abilities_count': len(detail['abilities']),
            }]
            count = 1
            total_pages = 1
        except Exception:
            pokemons = []
            count = 0
            total_pages = 1
    else:
        offset = (page - 1) * page_size
        data = pokeapi.fetch_pokemon_list(offset=offset, limit=page_size)
        pokemons = []
        for item in data['results']:
            d = pokeapi.fetch_pokemon_detail(item['url'])
            pokemons.append({
                'name': item['name'],
                'sprite': d['sprites']['front_default'],
                'abilities_count': len(d['abilities']),
            })
        count = data['count']
        total_pages = (count + page_size - 1) // page_size

    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None

    return render(request, 'pokemon_list.html', {
        'pokemons': pokemons,
        'search': search or '',
        'page': page,
        'page_size': page_size,
        'total_pages': total_pages,
        'prev_page': prev_page,
        'next_page': next_page,
    })


def detail_view(request, name):
    """
    Renderiza el perfil completo de un Pokémon.
    """
    try:
        pokemon = pokeapi.fetch_pokemon_detail(
            f"{settings.POKEAPI_BASE_URL}/pokemon/{name.lower()}"
        )
    except Exception:
        return render(request, '404.html', status=404)

    return render(request, 'pokemon_detail.html', {
        'pokemon': pokemon
    })
