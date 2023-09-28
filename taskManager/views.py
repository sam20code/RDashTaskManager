from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Create your views here.

def credentials(request):
    return render(request,'taskManager/Credentials.html')

#user signup and login
def userSignUp(request):
    if request.method == 'POST':
        username=request.POST['userName']
        email=request.POST['userEmail']
        password=request.POST['password']

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return render(request,'taskManager/Credentials.html')
    
def userLogin(request):
    if request.method == 'POST':
        username=request.POST['userName']
        password=request.POST['userPassword']

        myuser = authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            context ={
              
            }
            return render(request,'taskManager/Credentials.html',context)
        
#admin sign up and login  
def adminSignUp(request):
    if request.method == 'POST':
        username=request.POST['newAdminName']
        email=request.POST['newAdminEmail']
        password=request.POST['newAdminPassword']

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('taskManager/Credentials')
    
def adminLogin(request):
    if request.method == 'POST':
        username=request.POST['adminName']
        password=request.POST['adminPassword']

        myuser = authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            context ={
               
            }
            return render(request,'taskManager/Credentials.html',context)

