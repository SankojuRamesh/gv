from django.db import models
from productmanager.models import ProductModel

# Create your models here.



class  BanerModel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    iamge = models.ImageField(upload_to='baner/')
    status = models.BooleanField(default=False)


class  SettingsModel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='sitelogo/')
    address = models.TextField( blank=True, null=True)
    status = models.BooleanField(default=True)


