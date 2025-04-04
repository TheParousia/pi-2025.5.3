from django.shortcuts import render

# Create your views here.
def carrinho(request):
    
    return render(request,'carrinho.html')

def pagamentoCliente(request):
    
    return render(request,'pagamento_cliente.html')

