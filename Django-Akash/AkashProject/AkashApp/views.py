from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def AkashApp(request):
    return HttpResponse("<h1>I am Akash<h1>")

def AkashApp2(request):
    return HttpResponse("<h1>I am Akash2<h1>")

def AkashApp3(request):
    return render(request,"akash.html")


  