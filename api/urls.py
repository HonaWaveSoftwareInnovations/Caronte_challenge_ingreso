from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index,detail_view, PokemonViewSet

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
    path(index, name='api-home'),

    path('pokemon/<str:name>/', detail_view, name='detail'),
    path('', include(router.urls)),
]
