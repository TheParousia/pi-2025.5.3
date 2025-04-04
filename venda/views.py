from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from produto.models import Produto
from .models import Venda, ItemVenda
from .serializers import CarrinhoSerializer

# Create your views here.
def carrinho(request):
    
    return render(request,'carrinho.html')

def pagamentoCliente(request):
    
    return render(request,'pagamento_cliente.html')


class AdicionarAoCarrinho(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Obtendo dados da requisição
        produto_id = request.data.get('produto_id')
        quantidade = request.data.get('quantidade', 1)

        try:
            # Verificando se o produto existe
            produto = Produto.objects.get(id=produto_id)
            
            # Verificando estoque
            if produto.quantidade_estoque < quantidade:
                return Response({
                    'erro': 'Quantidade solicitada maior que o estoque disponível'
                }, status=400)

            vendaAtual, created = Venda.objects.get_or_create(
                usuario=request.user,
                status='CARRINHO',
            )

            # Criando ou atualizando item no carrinho
            carrinho_item, created = ItemVenda.objects.get_or_create(
                venda=vendaAtual,
                produto=produto,
                quantidade=quantidade,
                valorUnitario=produto.preco,
            )

            if not created:
                carrinho_item.quantidade += quantidade
                carrinho_item.save()

            serializer = CarrinhoSerializer(carrinho_item)
            return Response(serializer.data)

        except Produto.DoesNotExist:
            return Response({
                'erro': 'Produto não encontrado'
            }, status=404)
        except Exception as e:
            return Response({
                'erro': str(e)
            }, status=500)
        
