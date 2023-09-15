from django.shortcuts import render, HttpResponse
# Create your views here.
from categorymanager.models import CategoryModel, SubCategoryModel
from .models import WishlistModel, ProductModel, CartModel

# Create your views here.




def WishList_list(request):
    
    if request.method == "POST":
        productid  = ProductModel.objects.get(id=request.POST.get('pid'))
        # productid = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
        wishid = WishlistModel.objects.create(productid=productid, user=request.user)
        return HttpResponse( WishlistModel.objects.filter(user=request.user).count())

    else:     
        categories = CategoryModel.objects.all()
        wishlist = WishlistModel.objects.filter(user= request.user)
        return render(request,'frondend/wishlist.html', {"categories": categories, "wishlist":wishlist})

def Cart(request):  
    cartlist = CartModel.objects.filter(user= request.user)
    if request.GET.get("detail")  :
        return render(request,'frontend/cart_detail.html', {"cart": cartlist, "crtcount":cartlist.count()})

    return render(request,'frontend/cartlist.html', {"cart": cartlist, "crtcount":cartlist.count()})

def AddtoCart(request):  
    cartlist = CartModel.objects.filter(user= request.user)
    if request.method == "POST":
        product = ProductModel.objects.get(id=request.POST.get('pid'))
        total_price = float(product.price)*float(request.POST.get('quantity'))
        
        data = {
            "productid":product,
            "quantity":request.POST.get('quantity'),
            "total_price":total_price,
            "user":request.user 
        }
        
        CartModel.objects.create(**data)
    

    return HttpResponse("added")

def DeleteCart(request):
    cartid = request.
