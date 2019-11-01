from .models import Estoque
from .serializers import EstoqueSerializer
from rest_framework import viewsets


class EstoqueViewSet(viewsets.ModelViewSet):

 
    serializer_class = EstoqueSerializer
    queryset = Estoque.objects.all()