from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "Layout.html")

def home(request):
    return render(request, "Home.html")

def blog(request):
    return render(request, "Blog.html")

def brands(request):
    return render(request, "Brands.html")

def NewTest(request):
    return render(request, "New.html")

