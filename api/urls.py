# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, detail_view, PokemonViewSet

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
    # Ruta de la lista HTML con buscador
    path('', index, name='home'),
    # Ruta del perfil HTML de cada Pokémon
    path('pokemon/<str:name>/', detail_view, name='detail'),
    # Rutas de la API REST (list, retrieve)
    path('', include(router.urls)),
]
