from django.shortcuts import render
from .models import Produto
# Create your views here.
def listaProdutos(request):
    nome_produto = request.GET.get('nome_produto')
    valor_min = request.GET.get('valor_min')
    valor_max = request.GET.get('valor_max')
    ordem = request.GET.get('ordem')
    
    print("Produto pesquisado: ", nome_produto)
    
    produtos = Produto.objects.all()
    
    if nome_produto:
        produtos = Produto.objects.filter(nome__icontains=nome_produto)
    
    if valor_min and valor_max:
        produtos = Produto.objects.filter(preço__range=(valor_min, valor_max))

    if ordem:
        if ordem == '1':
            produtos = Produto.objects.all().order_by('nome')
        elif ordem == '2':
            produtos = Produto.objects.all().order_by('preço')
        elif ordem == '3':
            produtos = Produto.objects.all().order_by('-nome')
        elif ordem == '4':
            produtos = Produto.objects.all().order_by('-preço')
        #  Member.objects.all().order_by('firstname').values()

    return render(request, 'listagem_produto.html', {'produtos': produtos})
