from django.contrib import admin

from .models import Data



# Register your models here.

class DataAdmin(admin.ModelAdmin):
  list_display = ("id", "lname", "fname", "age", "gender")
  
admin.site.register(Data, DataAdmin)



# Register your models here.