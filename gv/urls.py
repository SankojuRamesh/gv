"""gv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from productmanager import views as pviews
from ordermanager import views as orderViews
from ordermanager import payment
from accountmanager import views as accountViews


urlpatterns = [
    path('superadmin/', admin.site.urls),
     path('logout/', accountViews.logoutview),
      path('userlogin/', accountViews.userloginview),
    path('account/', accountViews.account), 
    path('register/', accountViews.register),
    path('admin/', include('adminmanager.urls')),
    
    path('',  pviews.home),
    path('products/',  pviews.products),
    path('product/',  pviews.product_detail),
    path('wishlist/',  orderViews.WishList_list),
    path('Wishlistcount/',  orderViews.WishlistCount),
    path('delWishlist/',  orderViews.delWishlist),
    path('cart/',  orderViews.Cart),
    path('addtocart/',  orderViews.AddtoCart), 
    path('updatecart/',  orderViews.updateCart),
    path('deletecart/',  orderViews.DeleteCart),
    path('checkout/',  orderViews.checkout),
    path("payment/", payment.order_payment, name="payment"),
    path("callback/", payment.callback, name="callback"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
