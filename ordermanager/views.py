from django.shortcuts import render
# Create your views here.
from categorymanager.models import CategoryModel, SubCategoryModel
from .models import WishlistModel, ProductModel, CartModel

# Create your views here.




def WishList_list(request):
    categories = CategoryModel.objects.all()
    wishlist = WishlistModel.objects.all()
    return render(request,'frondend/wishlist.html', {"categories": categories, "wishlist":wishlist})


