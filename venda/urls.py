from django.urls import path
from venda import views
from .views import AdicionarAoCarrinho

urlpatterns = [
    path('', views.carrinho),
    path('api/adicionar/', AdicionarAoCarrinho.as_view(), name='adicionar_carrinho'),
]