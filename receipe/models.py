from django.db import models
from django.contrib.auth.models import User


class receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank = True)

    receipe_name = models.CharField(max_length = 100)
    receipe_description = models.CharField(max_length = 500)
    receipe_image =  models.ImageField(upload_to= "receipe_image")


    




# Create your models here.
