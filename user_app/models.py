from django.db import models

class Usuario(models.Model):
    cpf = models.IntegerField(primary_key=True)
    nome = models.TextField()
    data_nascimento = models.DateField()
