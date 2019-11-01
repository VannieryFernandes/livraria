from django.db import models


class Livro(models.Model):

    titulo =  models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    editora = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo