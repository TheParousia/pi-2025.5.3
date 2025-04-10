from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required


def verificar_grupo(usuario):
    return usuario.groups.filter(name='funcionario').exists()


def publico(request):
    return render(request, 'publico.html')


@login_required()
def logado(request):
    return render(request, 'logado.html')


@user_passes_test(verificar_grupo)
def funcionario(request):
    return render(request, 'funcionario.html')
