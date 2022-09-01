from http.client import HTTPResponse
from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import *
# Create your views here.
def index(request):
    return render(request,"a.html")
def homes(request):
    k=Register.objects.filter(id=request.user.id).values_list()
    print(k)
    n=k[0][1]
    r=k[0][2]
    c=k[0][3]
    p=k[0][4]
    e=k[0][5]
    return render(request,"b.html",{"n":n,"r":r,"c":c,"p":p,"e":e})
def r(request):
    h=e()
    if request.method=="POST":
        name=request.POST["name"]
        roll=request.POST["roll"]
        college=request.POST["college"]
        password=request.POST["password"]
        email=request.POST['email']
        d=Register(name=name,roll=roll,password=password,college=college,email=email)
        d.save()
        b=User.objects.create_user(username=name,password=password)
        b.save()
        return redirect("accounts/login")
    return render(request,"c.html",{"e":h})