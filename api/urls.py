# api/urls.py
from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        return Response({"message": "¡DRF funcionando!"})

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
]
