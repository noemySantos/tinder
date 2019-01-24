from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo =  models.CharField(max_length=50)
    cidade =  models.CharField(max_length=50)
    signo =  models.CharField(max_length=50)
    Gosto_musical =  models.CharField(max_length=50)
