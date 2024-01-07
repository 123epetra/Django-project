from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    peoples = [
         {'name': 'chandra', 'age' : 20 },
         {'name': 'epetra', 'age' : 22 },
         {'name': 'hero', 'age' : 5 },
         {'name': 'anup', 'age' : 16 },
         {'name': 'ujjwal', 'age' : 10 },

    ]
    for people in peoples:
        print(people)

    

    return render(request, "home\index.html", context= {'peoples' : peoples, 'page':'Home'})
def contact(request):
    context = {'page' : 'contect'}
    return render(request, "home\contact.html", context) 
def about(request):
    context = {'page' : "about"}
    return render(request,"home/about.html", context)



# Create your views here.
