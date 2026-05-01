from django.db import models
from django.contrib.auth.models import AbstractBaseUser  , PermissionsMixin 
from user.managers import CustomUserManager

class CustomUser(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15 , blank=True  , null=True)

    objects = CustomUserManager()
    REQUIRED_FIELDS = ["phone_number"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

class UserConfirm(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user}"   