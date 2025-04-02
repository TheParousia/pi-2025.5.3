from django.shortcuts import render, get_object_or_404
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
            produtos = Produto.objects.all().order_by('preco')
        elif ordem == '3':
            produtos = Produto.objects.all().order_by('-nome')
        elif ordem == '4':
            produtos = Produto.objects.all().order_by('-preco')
        #  Member.objects.all().order_by('firstname').values()

    return render(request, 'listagem_produto.html', {'produtos': produtos})

def detalheProduto(request, id):
    print(id)
    produto = get_object_or_404(Produto,pk = id)
    return render (request,"detalhe_produto.html", {"produto":produto})

def cadastroProduto(request):
    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        quantidade_em_estoque = request.POST.get('quantidade_em_estoque')

        produto = Produto()
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = valor
        produto.quantidade_estoque = quantidade_em_estoque
        produto.imagem = request.FILES.get('imagem')
        produto.imagem2 = request.FILES.get('imagem2')
        produto.imagem3 = request.FILES.get('imagem3')
        produto.imagem4 = request.FILES.get('imagem4')

        produto.save()
    return render(request,'form_produto.html')
