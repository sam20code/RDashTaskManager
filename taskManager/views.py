from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import Sprint
from taskManager.forms import SprintForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def credentials(request):
    return render(request,'taskManager/Credentials.html')

#user signup and login
@csrf_exempt
def userSignUp(request):
    if request.method == 'POST':
        username=request.POST['userName']
        email=request.POST['userEmail']
        password=request.POST['password']

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return render(request,'taskManager/Credentials.html')
    
@csrf_exempt
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
@csrf_exempt
def adminSignUp(request):
    if request.method == 'POST':
        username=request.POST['newAdminName']
        email=request.POST['newAdminEmail']
        password=request.POST['newAdminPassword']

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('taskManager/Credentials.html')
@csrf_exempt  
def adminLogin(request):
    if request.method == 'POST':
        username=request.POST['adminName']
        password=request.POST['adminPassword']

        myuser = authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            item_list = Sprint.objects.filter(sprintCreatedBy=request.user.username)
            context ={
                'item_list' : item_list,
            }
            return render(request,'taskManager/adminHomePage.html',context)
        
@csrf_exempt
def addSprint(request):
    form  = SprintForm(request.POST,request.FILES)
    if form.is_valid(): 
        form.save()
        item_list = Sprint.objects.filter(sprintCreatedBy=request.user.username)
        context ={
            'item_list' : item_list,
        }
        return render(request,'taskManager/adminHomePage.html',context)

    return render(request,'taskManager/AddSprint.html',{'form':form})
