from django.db import models
from livros.models import Livro

class Estoque(models.Model):
    quantidade = models.IntegerField()
    livro = models.OneToOneField(Livro,on_delete=models.CASCADE)