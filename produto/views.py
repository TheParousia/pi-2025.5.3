from django.shortcuts import render

# Create your views here.
def detalheProduto(request):
    return render (request,"detalhe_produto.html")