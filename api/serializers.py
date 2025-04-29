# api/serializers.py
from rest_framework import serializers

class PokemonListSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.URLField()
    sprite = serializers.URLField(allow_null=True)
    abilities_count = serializers.IntegerField()

class PokemonDetailSerializer(serializers.Serializer):
    # Para exponer todo el JSON crudo:
    raw = serializers.JSONField(source='detail')
