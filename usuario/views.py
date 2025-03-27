from django.shortcuts import render

# Create your views here.
def login(request):   
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        

    return render(request,'login.html')
