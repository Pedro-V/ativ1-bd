from django.db import models

class Usuario(models.Model):
    """
    Um usuário cadastrado.
    """
    cpf = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=80)
    data_nascimento = models.DateField()
