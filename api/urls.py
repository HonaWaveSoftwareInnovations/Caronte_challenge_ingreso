# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, detail_view, PokemonViewSet

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
-   path('pokemon/<str:name>/', detail_view, name='detail'),
-   path('', include(router.urls)),
+   # Lista HTML + buscador disponible en /api/
+   path('', index, name='api-home'),
+   # Detalle HTML de cada Pokémon en /api/pokemon/<name>/
+   path('pokemon/<str:name>/', detail_view, name='detail'),
+   # Endpoints JSON de la API REST
+   path('', include(router.urls)),
]
