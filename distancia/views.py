from rest_framework import viewsets
from .models import Distancia
from .serializers import DistanciaSerializer

class DistanciaViewSet(viewsets.ModelViewSet):
    queryset = Distancia.objects.all()
    serializer_class = DistanciaSerializer