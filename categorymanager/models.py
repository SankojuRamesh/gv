from django.db import models

# Create your models here.



class CategoryModel(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=1, null=True, blank=True)


    @property
    def sucat_list(self):
         
        return self.category.all()
    

     

class SubCategoryModel(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=1, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="category")

