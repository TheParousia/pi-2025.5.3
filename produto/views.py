from django.shortcuts import render

# Create your views here.
def listagemProduto(request):
    
    return render(request, 'listagem_produto.html')