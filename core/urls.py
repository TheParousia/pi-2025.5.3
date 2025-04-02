"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from info.views import sobreNos, desenvolvedores, contatos, faq
from produto.views import listaProdutos, cadastroProduto, detalheProduto
from usuario.views import cadastroCliente
from django.contrib import admin

# Rotas de exemplo de código
from exemplo.views import publico, logado, funcionario

urlpatterns = [
    # App produto
    path('', listaProdutos, name='lista_produtos'),
    path('produto/cadastro/', cadastroProduto, name='cadastro_produto'),
    path('produto/<int:id>', detalheProduto, name='detalhe_produto'),

    # App info
    path('info/sobre_nos/', sobreNos, name='sobre_nos'),
    path('info/dev/', desenvolvedores, name='dev'),
    path('info/contatos/', contatos, name='contatos'),
    path('info/faq/', faq, name='faq'),

    # App usuario
    path('cadastro/', cadastroCliente, name='cadastro_usuario'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # App venda
    path('carrinho/', carrinho, name='carrinho'),
    path('pagamento_cliente/', pagamentoCliente, name= 'pagamento_cliente'),

    # Teste
    path('exemplo/publico', publico, name='publico'),
    path('exemplo/logado/', logado, name='logado'),
    path('exemplo/funcionario/', funcionario, name='funcionario'),

]

urlpatterns += staticfiles_urlpatterns()
