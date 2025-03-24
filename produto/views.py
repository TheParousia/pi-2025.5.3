from django.shortcuts import render

# Create your views here.
def listaProdutos(request):
    produtos = Produto.objects.all()
    return render(request, 'listagem_produto.html', {'produtos': produtos})

def listagemProduto(request):
    
    return render(request, 'listagem_produto.html')