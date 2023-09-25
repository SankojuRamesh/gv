from django.db import models
from django.contrib.auth import get_user_model
from productmanager.models import ProductModel
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus



User = get_user_model()



# Create your models here.

class OrderModel(models.Model):
    orderid     = models.CharField(max_length=200, null=True, blank=True)
    orderquentity     = models.IntegerField(default=0)
    orderprice  =  models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    orderdate   = models.DateTimeField(auto_now_add=True)
    orderby     =  models.ForeignKey(User, on_delete=models.CASCADE)
    paymentid =  models.CharField(max_length=200, null=True, blank=True)
    paymentmethod =  models.CharField(max_length=200, null=True, blank=True)
    shippingid =  models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = models.CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
         
        return f"{self.id}-{self.name}-{self.status}"
    

    @property
    def shippingDetails(self):
        
        data = self.orderproduct.all().filter(orderid=self)
        if data:
            if data.first().shipping_state == 'SHIPPED':
                return "Dispatched"

            return data.first().shipping_state
            
        return "PENDING"


class OrderProductsModel(models.Model):
    orderid = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='orderproduct')
    productid = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING)
    productQuntity = models.IntegerField(null=True, blank=True)
    shipping_state =  models.CharField(max_length=50, choices=(
        ('SHIPPED', 'Dispatched'),
        ('DELIVERED', 'Delivered'),
        ('RETURNED', 'Returned'), 
         ('CANCELED', 'Canceled'),  ),
        default='PENDING',
    )



class CartModel(models.Model):
    productid = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity =  models.IntegerField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    user  =  models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def subtotal(self):
        if self.quantity:             
            return float(self.quantity) * float(self.productid.price)
        return 0
    
class WishlistModel(models.Model):
    productid = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user  =  models.ForeignKey(User, on_delete=models.CASCADE)



# views.py

