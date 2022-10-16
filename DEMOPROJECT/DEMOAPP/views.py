from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return render(request,'DEMOAPP/hi.html')

def about(request):
    return render(request,'DEMOAPP/about.html')

def login(request):
    return render(request,'DEMOAPP/login.html')

def newuser(request):
    return render(request,'DEMOAPP/newuser.html')
def contact(request):
    return render(request,'DEMOAPP/contact.html')










