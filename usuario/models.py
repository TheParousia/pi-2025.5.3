from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    dataDeNascimento = models.DateField()

class Endereco(models.Model):
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    uf = models.CharField(max_length=2)
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    numeroDaCasa = models.IntegerField()
    logradouro = models.CharField(max_length=100)
    pontoReferencia = models.CharField(max_length=100)
