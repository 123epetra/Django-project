from django.db import models

# Create your models here.
class Data (models.Model):
    genderz=[('M' , 'Male'),
            ("F", 'Female'),
            ("G" , "Gay"),
            ("B", 'Bisexual')]
    
    
    
    fname = models.CharField(max_length= 50)
    lname = models.CharField(max_length = 50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices = genderz)
    def __str__(self):
        return self.fname + ' ' + self.lname

