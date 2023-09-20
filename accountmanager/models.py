from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.


# AbstractBaseUser
# BaseUserManager

class UserManager(auth_models.BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):

        "Creates and saves a new user"

        if not phone:
            raise ValueError(('Users must have an email address'))

        user = self.model(phone= phone, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password, name):

        "Creates and saves a new superuser"

        user = self.create_user(phone, password)
        user.name = name
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(auth_models.AbstractBaseUser, models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15,unique=True)
    dob = models.CharField(max_length=20, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile', default='', null=True, blank=True)
    # Mondatory things 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)  
    USERNAME_FIELD = 'phone'
    objects = UserManager()
    REQUIRED_FIELDS = ['name']
        
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
  






