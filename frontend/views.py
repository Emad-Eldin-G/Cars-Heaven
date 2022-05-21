from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "frontend/Layout.html")

def home(request):
    return render(request, "frontend/Home.html")

def blog(request):
    return render(request, "frontend/Blog.html")

def brands(request):
    return render(request, "frontend/Brands.html")
