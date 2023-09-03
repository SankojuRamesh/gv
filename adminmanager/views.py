from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required(login_url='/login/')
def dashboard(request):
     

    return render(request, 'backend/dashboard.html', {"title": "Product List"})
    return HttpResponse("admin dashboard")
