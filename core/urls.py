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
from produto import views as vwproduto
from usuario import views as vwusuario

urlpatterns = [
    path('', vwproduto.listaProdutos),
    path('perfil/',vwusuario.perfilCliente, name= 'perfil_cliente'),
    path('cadastro/',vwusuario.cadastroCliente, name= 'cadastro_usuario'),
    path('produto/cadastro/', vwproduto.cadastroProduto),
    path('produto/<int:id>', vwproduto.detalheProduto),
    path('login/',vwusuario.login),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
