from django.db import models

class Cliente(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    celular = models.CharField(max_length=14)
    

    def __str__(self):
        return self.nome
    