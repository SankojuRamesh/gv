from django.shortcuts import render, HttpResponse

# Create your views here.
from categorymanager.models import CategoryModel, SubCategoryModel
from .models import ProductModel
from ordermanager.models import WishlistModel, OrderModel
from adminmanager.models import BanerModel, SettingsModel
 



def home(request):
    settingsdata = SettingsModel.objects.all().first()
    categories = CategoryModel.objects.all()
    banerimaes = BanerModel.objects.filter(status=1)
    pproducts = ProductModel.objects.all()[:16]
    best_sells = ProductModel.objects.filter(sell_state= 'BEST')
    return render(request, 'frontend/home.html', {"categories": categories, "banerimages":banerimaes, "settingsdata":settingsdata, "pproducts":pproducts, "best_sells":best_sells})


def aboutus(request):
    settingsdata = SettingsModel.objects.all().first()
    categories = CategoryModel.objects.all()
    banerimaes = BanerModel.objects.filter(status=1)
    pproducts = ProductModel.objects.all()[:16]
    best_sells = ProductModel.objects.filter(sell_state= 'BEST')
    return render(request, 'frontend/aboutus.html', {"categories": categories, "banerimages":banerimaes, "settingsdata":settingsdata, "pproducts":pproducts, "best_sells":best_sells})


def products(request):
    settingsdata = SettingsModel.objects.all().first()
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
    return render(request, 'frontend/all_products.html', {"categories": categories, "products":products, "wishlist_count":wishlist_count, "settingsdata":settingsdata})

def product_detail(request):
    settingsdata = SettingsModel.objects.all().first()
    categories = CategoryModel.objects.all()
    wishlist_count  = WishlistModel.objects.filter(user=request.user).count()

    pid = request.GET.get('id')
    product = {}
    
    if pid:
        product = ProductModel.objects.get(id=pid) 
        Relatedproducts = ProductModel.objects.filter(subcategory=product.subcategory).order_by('-id')[0:15]

    return render(request, 'frontend/productDetails.html', {"categories": categories,"product":product, "wishlist_count":wishlist_count, "settingsdata":settingsdata,"Relatedproducts":Relatedproducts})





