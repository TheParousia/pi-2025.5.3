from django.urls import path
from venda import views

urlpatterns = [
    path('carrinho/', views.carrinho),
]