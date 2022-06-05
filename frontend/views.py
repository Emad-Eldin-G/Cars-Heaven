from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate

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

def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = SignUpForm()

    return render(request, "registration/sign_up.html", {'form': form})