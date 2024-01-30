from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *

class CreateUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length = 100, unique = True)
    user_bio = models.CharField(max_length = 100)
    user_profile_image = models.ImageField(upload_to = 'profile')
    email= models.EmailField(unique = True, blank = True, null= True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

# Create your models here.
