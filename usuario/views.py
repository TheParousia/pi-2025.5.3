from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def verificar_grupo(usuario):
    return usuario.groups.filter(name='funcionario').exists()

def login(request):   
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

    return render(request,'login.html')

def perfilCliente(request):
    return render(request,'perfil_cliente.html')

def home(request):
    return render(request,'home.html')

@login_required
def privado(request):
    return render(request,'privado.html')

@user_passes_test(verificar_grupo)
def funcionario(request):
    return render(request,'funcionario.html')

def cadastroCliente(request):
    
    if request.method == 'POST':
        # Create user and save to the database
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        nomeDeUsuario = email
        senha = request.POST.get('senha')

        usuario = User.objects.create_user(
            nomeDeUsuario, email, senha
        )

        # Update fields and then save again
        usuario.first_name = nome
        usuario.last_name = sobrenome
        usuario.save()

        return redirect('lista_produtos')
    
    return render(request,'form_cliente.html')
