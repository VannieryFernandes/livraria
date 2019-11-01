from .models import Estoque
from livros.models import Livro
from rest_framework import serializers
from livros.serializers import LivroSerializer


class EstoqueSerializer(serializers.ModelSerializer):
    
    livro = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.all())

    
    class Meta:

        model = Estoque
        fields = ['id','quantidade', 'livro']
        