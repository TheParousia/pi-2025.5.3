from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venda(models.Model):
    dataHora = models.DateTimeField(auto_now_add=True)
    valorTotal = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, null=True, blank=True)

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey('produto.Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valorUnitario = models.DecimalField(max_digits=15, decimal_places=2)