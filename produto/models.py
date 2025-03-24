from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length = 100, unique=True)
    
    imagem = models.ImageField(upload_to='static/imagem/produtos/', null=True, blank=True)

    descrição = models.TextField()
    preço = models.DecimalField(max_digits=15, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    
