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
            produtos = Produto.objects.all().order_by('preço')
        elif ordem == '3':
            produtos = Produto.objects.all().order_by('-nome')
        elif ordem == '4':
            produtos = Produto.objects.all().order_by('-preço')
        #  Member.objects.all().order_by('firstname').values()

    return render(request, 'listagem_produto.html', {'produtos': produtos})

def page(request):
    return render(request,'page.html')

def detalheProduto(request, id):
    print(id)
    produto = get_object_or_404(Produto,pk = id)
    return render (request,"detalhe_produto.html", {"produto":produto})


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
        produto.imagem2 = request.FILES.get('imagem2')
        produto.imagem3 = request.FILES.get('imagem3')
        produto.imagem4 = request.FILES.get('imagem4')

        produto.save()
    return render(request,'form_produto.html')



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

    return render(request, 'adm_produto.html', {'produtos': produtos })

def deletarProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()

    return redirect('adm_produto')



def atualizarProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        descrição = request.POST.get('descrição')
        valor = request.POST.get('valor')
        quantidade_em_estoque = request.POST.get('quantidade_em_estoque')

        produto.nome = nome
        produto.descrição = descrição
        produto.preço = valor
        produto.quantidade_estoque = quantidade_em_estoque


        produto.imagem = request.FILES.get('imagem')
        produto.imagem2 = request.FILES.get('imagem2')
        produto.imagem3 = request.FILES.get('imagem3')
        produto.imagem4 = request.FILES.get('imagem4')

        produto.save()

    return render(request,'atualizar_produto.html', {'produto': produto})