from django.shortcuts import render, HttpResponse

# Create your views here.
from categorymanager.models import CategoryModel, SubCategoryModel
from .models import ProductModel



def home(request):
    categories = CategoryModel.objects.all()

    return render(request, 'frontend/home.html', {"categories": categories})


def products(request):
    categories = CategoryModel.objects.all()
    subid = request.GET.get('sub')
    products= {}
    if subid:
        products = ProductModel.objects.filter(subcategory=subid)
    

   

    return render(request, 'frontend/all_products.html', {"categories": categories, "products":products})

