from django.shortcuts import render

# Create your views here.
def login(request):   
    if request.method == "POST":
        login = request.POST.get("login")
        senha = request.POST.get("senha")

        

    return render(request,'login.html')