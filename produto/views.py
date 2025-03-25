from django.shortcuts import render, get_object_or_404
from .models import Produto

# Create your views here.
def detalheProduto(request, id):
    print(id)
    produto = get_object_or_404(Produto,pk = id)
    return render (request,"detalhe_produto.html", {"produto":produto})