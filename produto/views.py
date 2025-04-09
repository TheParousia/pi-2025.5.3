from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from decimal import Decimal, InvalidOperation
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Produto

# Create your views here.
def verificar_grupo(usuario):
    return usuario.groups.filter(name='funcionario').exists()


def listaProdutos(request):
    nome_produto = request.GET.get('nome_produto')
    valor_min = request.GET.get('valor_min', '')
    valor_max = request.GET.get('valor_max', '')
    ordem = request.GET.get('ordem', '')

    # Começa com queryset base
    produtos = Produto.objects.all()

    # Aplica filtro de nome
    if nome_produto:
        produtos = produtos.filter(nome__icontains=nome_produto)

    # Aplica filtro de preço
    if valor_min and valor_max:
        try:
            min_val = float(valor_min)
            max_val = float(valor_max)
            produtos = produtos.filter(preco__range=(min_val, max_val))
        except ValueError:
            # Ignora valores inválidos
            pass

    # Aplica ordenação
    if ordem:
        if ordem == '1':  # Nome ascendente
            produtos = produtos.order_by('nome')
        elif ordem == '2':  # Preço ascendente
            produtos = produtos.order_by('preco')
        elif ordem == '3':  # Nome descendente
            produtos = produtos.order_by('-nome')
        elif ordem == '4':  # Preço descendente
            produtos = produtos.order_by('-preco')

    return render(request, 'listagem_produto.html', {'produtos': produtos})


def page(request):
    return render(request, 'page.html')


def detalheProduto(request, id):
    print(id)
    produto = get_object_or_404(Produto, pk=id)
    return render(request, "detalhe_produto.html", {"produto": produto})


@user_passes_test(verificar_grupo)
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

        produto.imagem1 = request.FILES.get('imagem1')
        produto.imagem2 = request.FILES.get('imagem2')
        produto.imagem3 = request.FILES.get('imagem3')
        produto.imagem4 = request.FILES.get('imagem4')

        produto.save()
    return render(request, 'form_produto.html')


# Controle de Estoque
@user_passes_test(verificar_grupo)
def controleEstoque(request):
    produtos = Produto.objects.all()

    if request.method == 'POST':
        print("Dados atualizados com sucesso")

        productName = request.POST.get('nome')
        productPrice = request.POST.get('price')
        productQtd = request.POST.get('qtd')

        adm = controleEstoque()
        adm.nome = productName
        adm.preco = productPrice
        adm.quantidade = productQtd

        adm.save()

    return render(request, 'adm_produto.html', {'produtos': produtos})

# Adm produto
@user_passes_test(verificar_grupo)
def admProduto(request):
    produtos = Produto.objects.all()
    return render(request, 'adm_produto.html', {'produtos': produtos})

@user_passes_test(verificar_grupo)
def deletarProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()

    return redirect('adm_produto')


# atualizar produto (tela de atualização dos dados do produto)

@user_passes_test(verificar_grupo)
def atualizarProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        produto.nome = request.POST.get("nome") or produto.nome
        produto.descricao = request.POST.get("descricao") or produto.descricao

        # Converter os valores numéricos para evitar erro de tipo
        preco = request.POST.get('preco')
        if preco:
            try:
                preco = preco.replace(',','.')
                produto.preco = Decimal(preco)
            except InvalidOperation:
                return HttpResponse("Erro: O preço deve ser um número válido.", status=400)
        
        
        # Atualiza a quantidade
        quantidade= request.POST.get('quantidade_estoque')
        if quantidade:
            try:
                produto.quantidade_estoque = int(quantidade)
            except ValueError:
                return HttpResponse("Erro: A quantidade deve ser um número inteiro.", status=400)

        # Atualiza as imagens se forem enviadas
        if 'imagem1' in request.FILES:
            produto.imagem1 = request.FILES['imagem1']
        if 'imagem2' in request.FILES:
            produto.imagem2 = request.FILES['imagem2']
        if 'imagem3' in request.FILES:
            produto.imagem3 = request.FILES['imagem3']
        if 'imagem4' in request.FILES:
            produto.imagem4 = request.FILES['imagem4']
        produto.save()

    return render(request, 'atualizar_produto.html', {'produto': produto})

