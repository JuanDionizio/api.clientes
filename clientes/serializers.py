from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        validators = ()
        
    def validate(self, data):
        print('teste')
        if not nome_valido(data['nome']):
            raise serializers.ValidationError ({'nome':" Inclua apenas letras nesse campo "})  
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError ({'cpf': "O CPF deve valido"})
        if not rg_valido(data['rg']): 
            raise serializers.ValidationError ({'rg':"O RG deve ter 9 digitos!"})
        if not celular_valido(data ['celular']):
            raise serializers.ValidationError ({'celular':"O celular deve seguir o padrao 00 9000-0000 , respeitadndo os espaçoes e separações ."})      
        return data