# api/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
    path('', include(router.urls)),
]
