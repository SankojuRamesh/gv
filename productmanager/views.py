from django.shortcuts import render, HttpResponse

# Create your views here.
from categorymanager.models import CategoryModel, SubCategoryModel
from .models import ProductModel
from ordermanager.models import WishlistModel, OrderModel
from adminmanager.models import BanerModel



def home(request):
    categories = CategoryModel.objects.all()
    banerimaes = BanerModel.objects.filter(status=1)

    return render(request, 'frontend/home.html', {"categories": categories, "banerimages":banerimaes})


def products(request):
    categories = CategoryModel.objects.all()
    wishlist_count= 0
    try:
        wishlist_count  = WishlistModel.objects.filter(user=request.user).count()
    except:
        wishlist_count=0
    subid = request.GET.get('sub')
    products = ProductModel.objects.all() 
    if subid:
        products = ProductModel.objects.filter(subcategory=subid)  
    return render(request, 'frontend/all_products.html', {"categories": categories, "products":products, "wishlist_count":wishlist_count})

def product_detail(request):
    categories = CategoryModel.objects.all()
    wishlist_count  = WishlistModel.objects.filter(user=request.user).count()

    pid = request.GET.get('id')
    product = {}
    if pid:
        product = ProductModel.objects.get(id=pid)  

    return render(request, 'frontend/productDetails.html', {"categories": categories,"product":product, "wishlist_count":wishlist_count})



