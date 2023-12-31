from django.db import models
from categorymanager.models import SubCategoryModel

# Create your models here.
class ProductModel(models.Model):
    subcategory = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description  = models.TextField()
    price  = models.DecimalField(max_digits=6, decimal_places=2)
    prouct_property = models.CharField(max_length=50, blank=False)
    coverImage = models.ImageField(upload_to='products/')
    Image1 = models.ImageField(upload_to='products', null=True, blank=True)
    Image2 = models.ImageField(upload_to='products', null=True, blank=True)
    Image3 = models.ImageField(upload_to='products', null=True, blank=True)
    Image4 = models.ImageField(upload_to='products', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
     
    sells_type =( ("BEST", "BEST"), ("DEALS", "DEALS"), ("ALL", "ALL")) 
    sell_state =    models.CharField(max_length=9, choices=sells_type,  default="ALL")   
    def __str__(self):
        return self.title


    @property
    def oldPrice(self):
        return (self.price*10)/100+self.price


    @property
    def ActiveState(self):
        if self.is_published:
            return "Active"
        else:
            return "In Active"
    
