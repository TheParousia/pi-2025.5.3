from django.shortcuts import render

# Create your views here.

def cadastroProduto(request):
    return render(request,'form_produto.html')