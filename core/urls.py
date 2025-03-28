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
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from produto import vwproduto
from usuario import vwusuario
from info import vwinfo

urlpatterns = [
    #Página de exemplo de como se usar o template master base.html
    path('page/', views.page),

    path('', vwproduto.listaProdutos),
    path('produto/cadastro/', vwproduto.cadastroProduto),
    path('produto/<int:id>', vwproduto.detalheProduto),
  
    path('carrinho/', include('venda.urls')),
  
    path('sobre_nos/',vwinfo.sobreNos, name='sobre_nos'),
    path('dev/',vwinfo.desenvolvedores, name='dev'),
    path('contatos/',vwinfo.contatos, name='contatos'),

    path('login/',vwusuario.login),
    path('cadastro/',vwusuario.cadastroCliente, name= 'cadastro_usuario'),  
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
