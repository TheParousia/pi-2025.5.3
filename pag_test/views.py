from django.shortcuts import render

# Create your views here.


def viewTeste(request):
    return render(request, 'teste.html')
