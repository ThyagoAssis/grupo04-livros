from django.db import models

# Create your models here.
class Livros (models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    editora = models.CharField(max_length=30, null=False, blank=False)
    autor = models.CharField(max_length=30, null=False, blank=False)
    imagem = models.CharField(max_length=255, null=False, blank=False)
    publicado_em = models.DateField()