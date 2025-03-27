from django.shortcuts import render
from .models import FeedBack

# Create your views here.
def feedback(request):
    if request.mother == 'POST':
        print('Dados recebidos com sucesso!')
        comentario = request.POST.get('comentario')

        comentarios = FeedBack()
        comentarios.comentario = comentario

        comentarios.save()
    return render(request, 'sobre_nos.html')

def sobreNos(request):
    return render(request, 'sobre_nos.html')


def desenvolvedores(request):
    return render(request, 'desenvolvedores.html')

def contatos(request):
    return render(request, 'contatos.html')

