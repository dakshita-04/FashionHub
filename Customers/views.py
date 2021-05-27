from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from datetime import datetime

def Login(request):
    if 'login' in request.POST:
        un=request.POST['un']
        pwd=request.POST['pwd']
        check=authenticate(username=un,password=pwd)
        if check:
            login(request,check)
            return redirect('home')
        else:
            return HttpResponse("username password not match")    

def Logout(request):
    logout(request)
    return redirect('home')

def Signup(request):
    print("inside signup")
    errorUN=False
    errorPWD=False
    if 'signup' in request.POST:
        print('inside if 1 ')
        n=request.POST['Name']
        un=request.POST['username']   
        e=request.POST['email']
        m=request.POST['mob']
        pwd1=request.POST['password1']
        pwd2=request.POST['password2']
        
        check=User.objects.filter(username=un).first()
        if check:
            print("error un")
            errorUN=True
        elif pwd1 != pwd2:
            print("ped")
            errorPWD=True
        else:
            print("working")
            User.objects.create_user(username=un,password=pwd1,first_name=n,email=e)
            auth=authenticate(username=un,password=pwd1)   
            login(request,auth) 
            UserProfile.objects.create(user=request.user,mobile=m,last_login=datetime.now())
            return redirect('home')
        
    print('outside if')
    return HttpResponse('Not Working')
