from django.shortcuts import render, redirect, get_object_or_404
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


def page(request):
    return render(request, 'page.html')


def detalheProduto(request, id):
    print(id)
    produto = get_object_or_404(Produto, pk=id)
    return render(request, "detalhe_produto.html", {"produto": produto})


def cadastroProduto(request):
    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('preco')
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


def deletarProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()

    return redirect('adm_produto')


def atualizarProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        produto.nome = request.POST.get('nome', produto.nome)
        produto.descrição = request.POST.get('descrição', produto.descricao)

        # Converter os valores numéricos para evitar erro de tipo
        preco_novo = request.POST.get('preco', None)
        if preco_novo:
            try:
                produto.preço = float(preco_novo)
            except ValueError:
                pass  # Mantém o valor atual se a conversão falhar

        quantidade_nova = request.POST.get('quantidade_em_estoque', None)
        if quantidade_nova:
            try:
                produto.quantidade_estoque = int(quantidade_nova)
            except ValueError:
                pass  # Mantém o valor atual se a conversão falhar

        # Atualiza imagens se forem enviadas
        for i in range(1, 5):
            campo_imagem = f'imagem{i}'
            if campo_imagem in request.FILES:
                setattr(produto, campo_imagem, request.FILES[campo_imagem])

        produto.save()
        print(f"Imagem 1 salva como: {produto.imagem1}")

        produto.imagem1 = request.FILES.get('imagem1')
        produto.imagem2 = request.FILES.get('imagem2')
        produto.imagem3 = request.FILES.get('imagem3')
        produto.imagem4 = request.FILES.get('imagem4')

    return render(request, 'atualizar_produto.html', {'produto': produto})

