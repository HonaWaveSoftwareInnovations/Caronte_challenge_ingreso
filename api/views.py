from django.shortcuts import render
# api/views.py
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.services.pokeapi import fetch_pokemon_list, fetch_pokemon_detail
from .serializers import PokemonListSerializer, PokemonDetailSerializer

class PokemonViewSet(viewsets.ViewSet):
    """
    ViewSet para listar y recuperar Pokémon usando PokéAPI.
    """

    def list(self, request):
        # Paginación manual basada en query params page y page_size
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 10))
        offset = (page - 1) * page_size

        # Llamada al servicio
        data = fetch_pokemon_list(offset=offset, limit=page_size)

        # Construir resultados enriquecidos con sprite y count
        enriched = []
        for item in data['results']:
            detail = fetch_pokemon_detail(item['url'])
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
        # pk es el nombre o id, usamos el nombre 
        url = f"{settings.POKEAPI_BASE_URL}/pokemon/{pk}"
        try:
            detail = fetch_pokemon_detail(url)
        except Exception:
            return Response(
                {'detail': 'Pokémon no encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PokemonDetailSerializer({'detail': detail})
        return Response(serializer.data)

# Create your views here.
