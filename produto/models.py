from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length = 100, unique=True)
    quantidade_estoque = models.IntegerField()
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=15, decimal_places=2)

    imagem1 = models.ImageField(upload_to='static/imagem/produtos/', null=True, blank=True)
    imagem2 = models.ImageField(upload_to='static/imagem/produtos/', null=True, blank=True)
    imagem3 = models.ImageField(upload_to='static/imagem/produtos/', null=True, blank=True)
    imagem4 = models.ImageField(upload_to='static/imagem/produtos/', null=True, blank=True)

class Estoque(models.Model):
    productName = models.CharField(max_length=255)
    productPrice = models.DecimalField (max_digits=10, decimal_places=2)
    productQtd = models.IntegerField()
