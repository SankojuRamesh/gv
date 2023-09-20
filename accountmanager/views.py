from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
User = get_user_model()

def logoutview(request):
    logout(request)
    return redirect('/')
 
def userloginlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user=authenticate(username=username,password=pwd)
        
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("/")
    return render(request, 'frontend/login.html')
    


def account(request):
    return render(request, 'frontend/account.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user = User.objects.create_end_user(name=name,
                                 phone= username,
                                 password=pwd)
        return redirect("/")
        
    return render(request, 'frontend/register.html')
