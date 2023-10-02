from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from adminmanager.models import SettingsModel
from .models import ShippmentModel
from ordermanager.models import  OrderModel
from categorymanager.models import CategoryModel
User = get_user_model()

def logoutview(request):
    logout(request)
    return redirect('/')
 
def userloginview(request):
    settingsdata = SettingsModel.objects.all().first()
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user=authenticate(username=username,password=pwd)
        
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("/")
    return render(request, 'frontend/login.html', {"settingsdata":settingsdata})
    


def account(request):
    settingsdata = SettingsModel.objects.all().first()
    shipment= ShippmentModel.objects.filter(user= request.user) 
     
    categories = CategoryModel.objects.all()
    
     
    
    orders = OrderModel.objects.filter(orderby=request.user)
   
    if  request.method == "POST":
               
        data =  {'Fullname': request.POST.get('Fullname'), 
        'Mobilenumber':  request.POST.get('Mobilenumber'), 
        'Pincode':  request.POST.get('Pincode'), 
        'Flat_House_no_Building_Apartment':  request.POST.get('Flat_House_no_Building_Apartment'), 
        'Area_Street_Sector_Village':   request.POST.get('Area_Street_Sector_Village'),
        'Landmark':   request.POST.get('Landmark'),
        'Town_City':  request.POST.get('Town_City'),
        'user':request.user}
        if not shipment:
            data['status'] =  1
        else:
            data['status'] =  0
        
        
         
        ShippmentModel.objects.create(**data)
        

    return render(request, 'frontend/account.html', {"categories": categories,   "settingsdata":settingsdata,"settingsdata":settingsdata, "shipment" : shipment, "orders":orders})

def profileupdate(request):
    if  request.method == "POST":
        print(request.POST)
        user = User.objects.filter(id=request.user.id).first()
        user.name= request.POST.get('name')
        user.phone= request.POST.get('phone')
        user.email= request.POST.get('email')
        user.save()

    return redirect('/account/')

def register(request):
    settingsdata = SettingsModel.objects.all().first()
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user = User.objects.create_end_user(name=name,
                                 phone= username,
                                 password=pwd)
        return redirect("/userlogin/")
        
    return render(request, 'frontend/register.html', {"settingsdata":settingsdata})
