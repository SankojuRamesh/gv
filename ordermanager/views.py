from django.shortcuts import render, HttpResponse
# Create your views here.
from categorymanager.models import CategoryModel, SubCategoryModel
from .models import WishlistModel, ProductModel, CartModel
from adminmanager.models import SettingsModel
from accountmanager.models import ShippmentModel

from django.shortcuts import render, redirect
from django.conf import settings
import razorpay


# Create your views here. 


def WishList_list(request):
    if not request.user.is_authenticated:
        return redirect('/userlogin/')
    
    if request.method == "POST":
        productid  = ProductModel.objects.get(id=request.POST.get('pid'))
        # productid = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
        wishid = WishlistModel.objects.filter(productid=request.POST.get('pid')).count()
        
        if  not wishid :
            wishid = WishlistModel.objects.create(productid=productid, user=request.user)
             
        return HttpResponse(WishlistModel.objects.filter(user= request.user).count())

    else:
        settingsdata = SettingsModel.objects.all().first()     
        categories = CategoryModel.objects.all()
        wishlist = WishlistModel.objects.filter(user= request.user)
        return render(request,'frontend/wishlist.html', {"categories": categories, "wishlist":wishlist, "settingsdata":settingsdata})



def WishlistCount(request):
    wishlist = WishlistModel.objects.filter(user= request.user).count()
    return HttpResponse(wishlist)

def delWishlist(request):
    wishlistid  = WishlistModel.objects.get(id=request.GET.get('wid')).delete()
    wishlist = WishlistModel.objects.filter(user= request.user).count()
    return HttpResponse(wishlist)

 
def Cart(request):
    settingsdata = SettingsModel.objects.all().first() 
         
    categories = CategoryModel.objects.all()
    wishlist = WishlistModel.objects.filter(user= request.user)
    if request.GET.get("detail")  :
        if not request.user.is_authenticated:
            return redirect('/userlogin/')  
        cartlist = CartModel.objects.filter(user= request.user)
        total= 0
        if cartlist:
            for cartAmount in cartlist:
                total = float(cartAmount.total_price)+float(total) 
        if not request.user.is_authenticated:
            return redirect('/userlogin/')  
        return render(request,'frontend/cart_detail.html', {"categories": categories, "wishlist":wishlist,"cart": cartlist,"total": total ,"crtcount":cartlist.count(), "settingsdata":settingsdata})

    cartlist = CartModel.objects.filter(user= request.user)
    total= 0
    if cartlist:
        for cartAmount in cartlist:
                total = float(cartAmount.total_price)+float(total)
    return render(request,'frontend/cartlist.html', {"cart": cartlist,"total": total , "crtcount":cartlist.count(), "settingsdata":settingsdata})

def AddtoCart(request):
    if not request.user.is_authenticated:
        return redirect('/userlogin/')   
    cartlist = CartModel.objects.filter(user= request.user) 
    if request.method == "POST":
        product = ProductModel.objects.get(id=request.POST.get('pid'))
        quantity=int(request.POST.get('quantity',1)) 
        total_price = float(product.price)*float(quantity)
        check_exist = CartModel.objects.filter(productid = request.POST.get('pid')).first()
         
        if check_exist:

            quntety = int(check_exist.quantity)+quantity
            check_exist.quantity= quntety
            check_exist.total_price = float(product.price)*float(quntety)
            check_exist.save()
        else:
            data = {
                "productid":product,
                "quantity":request.POST.get('quantity'),
                "total_price":total_price,
                "user":request.user 
            } 
            CartModel.objects.create(**data)
            return HttpResponse("added")
    

    return HttpResponse("added")
def updateCart(request):
    product = ProductModel.objects.get(id=request.POST.get('pid'))
    quantity=int(request.POST.get('quantity',1)) 
    total_price = float(product.price)*float(quantity)

 

def DeleteCart(request):
    cartid = request.GET.get('cartid', False)
    del_cart_quantity = request.GET.get('delquantity', False)    
    status = None
    if  del_cart_quantity and cartid:
        CartObj = CartModel.objects.get(pk=cartid)
        CartObj.quantity = del_cart_quantity
        CartObj.total_price = float(del_cart_quantity)*float(CartObj.productid.price)
        CartObj.save()
        status = True

        
    elif cartid:
        status = CartModel.objects.get(pk=cartid).delete()
        ...
    return HttpResponse(status)



def checkout(request):
    settingsdata = SettingsModel.objects.all().first()
    categories = CategoryModel.objects.all()
    wishlist_count  = WishlistModel.objects.filter(user=request.user).count()
    cartlist = CartModel.objects.filter(user= request.user)
    shipping_address= ShippmentModel.objects.filter(user= request.user) 
    total= 0
    if cartlist:
        for cartAmount in cartlist:
                total = float(cartAmount.total_price)+float(total)
    return render(request, 'frontend/checkout.html', {"categories": categories, "cartlist":cartlist,"total":total,  "wishlist_count":wishlist_count, "settingsdata":settingsdata,"shipping_address":shipping_address})


def orderdetails(request):
    orderid=request.GET.get("orderid")
    settingsdata = SettingsModel.objects.all().first()
    categories = CategoryModel.objects.all()
    wishlist_count  = WishlistModel.objects.filter(user=request.user).count()
    cartlist = CartModel.objects.filter(user= request.user)
    total= 0
    if cartlist:
        for cartAmount in cartlist:
                total = float(cartAmount.total_price)+float(total)
    return render(request, 'frontend/orderdetails.html', {"categories": categories, "cartlist":cartlist,"total":total,  "wishlist_count":wishlist_count, "settingsdata":settingsdata})