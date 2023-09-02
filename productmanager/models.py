from django.db import models
from categorymanager.models import SubCategoryModel

# Create your models here.
class ProductModel(models.Model):
    subcategory = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description  = models.TextField()
    price  = models.DecimalField(max_digits=6, decimal_places=2)
    property = models.CharField(max_length=50, blank=False)
    coverImage = models.ImageField(upload_to='products')
    Image1 = models.ImageField(upload_to='products', null=True, blank=True)
    Image2 = models.ImageField(upload_to='products', null=True, blank=True)
    Image3 = models.ImageField(upload_to='products', null=True, blank=True)
    Image4 = models.ImageField(upload_to='products', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)



    def __str__(self):
        return self.title
    
