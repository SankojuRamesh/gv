from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from productmanager.models import ProductModel
from categorymanager.models import CategoryModel, SubCategoryModel
from adminmanager.models import BanerModel
from django.shortcuts import redirect
from django.forms import ModelForm
# Create your views here. 

# @login_required(login_url='/login/')
def dashboard(request): 
    
    return render(request, 'backend/dashboard.html', {"title": "Dashboard",})
    
def category(request): 
    if request.method == "POST":  
        print(request.POST.get('title'))
        CategoryModel.objects.create(title= request.POST.get('title'), status=True)

    list_categories = CategoryModel.objects.all()

    return render(request, 'backend/category_list.html', {"title": "Categories List", "categories":list_categories})



def subcategoryById(request): 
    list_subcategories = SubCategoryModel.objects.filter(category=request.GET.get('cat') )  
    return render(request, 'backend/subcategory_options.html', {"title": "Sub Categories","subcategories":list_subcategories })
  

def subcategory(request):
    if request.method == "POST":  
         
        categoryobj = CategoryModel.objects.get(id=  request.POST.get('category')) 
        SubCategoryModel.objects.create(title= request.POST.get('title'), status=True, category = categoryobj) 
    list_subcategories = SubCategoryModel.objects.all()

    list_categories = CategoryModel.objects.all()
    return render(request, 'backend/subcategory_list.html', {"title": "Sub Categories","subcategories":list_subcategories,"categories":list_categories})
  


 
def products(request): 
    if request.method == "POST":
        
        data = {
                 "title":request.POST.get('title'), 
                'subcategory':SubCategoryModel.objects.get(id=  request.POST.get('subcategory')), 
                'description':request.POST.get('description'), 
                'price':request.POST.get('price'), 
                'coverImage': request.FILES['coverImage'],
                'Image1': request.FILES['image1'],
                'Image2': request.FILES['image2'],
                'Image3': request.FILES['image3'],
                'Image4': request.FILES['image4'],
            }
        print(data)
         
        ProductModel.objects.create(**data)
         

    all_products = ProductModel.objects.all()
    return render(request, 'backend/products_list.html', {"title": "Product List", "products":all_products})
    


def newproduct(request):
    list_categories = CategoryModel.objects.all()
    all_products = ProductModel.objects.all()
    return render(request, 'backend/newproduct.html', {"title": "Product List", "products":all_products, "list_categories":list_categories})


def settings(request):
    list_categories = CategoryModel.objects.all()
    all_products = ProductModel.objects.all()
    return render(request, 'backend/settings.html', {"title": "Settings"})



def homesettings(request):
     
    return render(request, 'backend/homesettings.html', {"title": "Home Settings"})
    





def baner(request):
     
    if request.method == "POST":        
        data = {
                 "title":request.POST.get('banername'), 
                'iamge': request.FILES['banerimage'], 
                
            } 
         
        BanerModel.objects.create(**data)
        
        return  redirect('/admin/homesettings/')
        
    
    baners = BanerModel.objects.all()
    return render(request, 'backend/banerimages.html', {"title": "Home Settings", "baners":baners})


def banerupdate(request):
    banerid = request.GET.get("banerid")
    status = request.GET.get("status")
    if banerid:
        BanerObj = BanerModel.objects.get(id=banerid)
        BanerObj.status = status
        BanerObj.save()
        return HttpResponse('updated')
def banerdelete(request):
    banerid = request.GET.get("banerid")
    BanerObj = BanerModel.objects.get(id=banerid).delete()
    return HttpResponse('deleted')