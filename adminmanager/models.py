from django.db import models

# Create your models here.



class  BanerModel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    iamge = models.ImageField(upload_to='baner/')
    status = models.BooleanField(default=False)
