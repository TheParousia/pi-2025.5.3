from django.shortcuts import render
from .models import Produto
# Create your views here.
def listaProdutos(request):
    produtos = Produto.objects.all()
    return render(request, 'listagem_produto.html', {'produtos': produtos})
