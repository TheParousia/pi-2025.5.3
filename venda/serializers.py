from rest_framework import serializers
from .models import ItemVenda

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = ['id', 'venda', 'produto', 'quantidade', 'valorUnitario']