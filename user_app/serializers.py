from rest_framework import serializers
from user_app.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf', 'nome', 'data_nascimento']
