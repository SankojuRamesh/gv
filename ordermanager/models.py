from django.db import models
from django.contrib.auth import get_user_model
from productmanager.models import ProductModel

User = get_user_model()



# Create your models here.

class OrderModel(models.Model):
    orderid     = models.CharField(max_length=200)
    orderprice  =  models.DecimalField(max_digits=6, decimal_places=2)
    orderdate   = models.DateTimeField(auto_now_add=True)
    orderby     =  models.ForeignKey(User, on_delete=models.CASCADE)
    paymentid =  models.CharField(max_length=200, null=True, blank=True)
    paymentmethod =  models.CharField(max_length=200, null=True, blank=True)
    shippingid =  models.CharField(max_length=200, null=True, blank=True)
    


class OrderProductsModel(models.Model):
    orderid = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    productid = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING)
    productQuntity = models.IntegerField(null=True, blank=True)
    shipping_state =  models.CharField(max_length=50, choices=(
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('RETURNED', 'Returned'),  ),
        default='PENDING',
    )


class CartModel(models.Model):
    productid = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity =  models.IntegerField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    user  =  models.ForeignKey(User, on_delete=models.CASCADE)



class WishlistModel(models.Model):
    productid = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user  =  models.ForeignKey(User, on_delete=models.CASCADE)
