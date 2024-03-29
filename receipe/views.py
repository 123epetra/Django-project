from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.db.models import Q,  Sum
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .utils import *
from django.contrib.auth import get_user_model
User = get_user_model()



@login_required(login_url='login')
def hello(request):
    if request.method == 'POST':
        data = request.POST
        receipe_name = request.POST.get('recipeName')
        receipe_description = request.POST.get('recipeDescription')
        receipe_image = request.FILES.get('recipeImage')

        print(data)
        receipe.objects.create(receipe_name = receipe_name, receipe_description=receipe_description, receipe_image=receipe_image )
        return redirect('receipe')
 

    image_receipe = receipe.objects.all()
    if request.GET.get('search'):
        data = request.GET.get('search')
        image_receipe = receipe.objects.filter(
            Q(receipe_name__icontains=data) |
            Q(receipe_description__icontains = data)
        )
    # image_receipe = [ image_receipe.receipe_image for image_receipe in Receipe ]
    context = {'image_receipe' : image_receipe}

    
    
    

    
    
    return render (request, 'receipe.html',context)
@login_required(login_url='login')
def delete(request, id):
    instance = receipe.objects.get(id = id )
    instance.delete()
    return redirect('receipe')
@login_required(login_url='login')
def update(request, id):
    queryset = receipe.objects.get(id = id) 
    if request.method == 'POST':
        data = request.POST

        receipe_name = data.get('recipeName')
        
        receipe_description = request.POST.get('recipeDescription')
        receipe_image = request.FILES.get('recipeImage')
        
        queryset.receipe_name = receipe_name
        
        queryset.receipe_description = receipe_description
         
        
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('receipe')
      
        
    context = {'image_receipe': queryset}
    return render (request,'update.html', context)

def login_page(request):
    if request.method == 'POST':
        user_name = request.POST.get("username")
        pass_word = request.POST.get("password")

        user = authenticate(request , username = user_name, password = pass_word)
        if user is None:
            messages.info(request, 'username of password incorrect please try again')

        else:
            print('user is here now ')
            login(request, user)
            
            return redirect('/receipe/')
    return render (request, 'login.html')
def logout_page(request):
    logout(request)
    return redirect('/login/')
            
        

        

def send_email(request):
    send_email_to_client()
    return redirect('/')


def register(request):
    if request.method == "POST":
            
        FirstName= request.POST.get('First_Name')
        LastName = request.POST.get('Last_Name')
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username already exists")
            return redirect ('/register/')
            
        user = User.objects.create(
            first_name=FirstName,
            last_name = LastName,
            username= username,
            
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        
    print("hey this is register")

    
    return render (request, 'register.html')

def get_students(request):
    queryset = Student.objects.all()
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(Q(student_name__icontains=search) | Q(abc__department__icontains= search) | Q(student_email__icontains = search))
        

   
    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    

    return render (request, 'students.html ', {'queryset' : page_obj} )

def marks_page(request, student_id):
    queryset = marks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks=Sum('marks'))
    
    

    return render (request, 'markshit.html', {'queryset' : queryset, 'total' : total_marks})



        
# def search(request):
#     data = request.GET.get('search','')
#     print(data)
#     print('eyyh hhhhhhhhhhhhhhhhhhhhhhhhhhhh')
        

        


    

# Create your views here.
