from django.shortcuts import render
from .models import Produto

# Create your views here.

def cadastroProduto(request):
    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        descrição = request.POST.get('descrição')
        valor = request.POST.get('valor')
        quantidade_em_estoque = request.POST.get('quantidade_em_estoque')

        produto = Produto()
        produto.nome = nome
        produto.descrição = descrição
        produto.imagem = request.FILES.get('imagem')
        produto.preço = valor
        produto.quantidade_estoque = quantidade_em_estoque

        produto.save()
    return render(request,'form_produto.html')
    
