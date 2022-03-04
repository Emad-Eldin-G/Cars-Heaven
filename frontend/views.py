from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "frontend/Layout.html")

def home(request):
    return render(request, "frontend/Home.html")

def New(request):
    return render(request, "frontend/New.html")

def Car(request, pk):
    return render(request, "frontend/Specific.html")

def Brands(request):
    return render(request, "frontend/Brands.html")
